import os
import re
from typing import List, Literal, NotRequired, TypedDict
from lib.phply.phpast import Class, MethodCall, Constant, UnaryOp
from lib.phply.phplex import lexer
from lib.phply.phpparse import make_parser


HttpMethod = Literal["GET", "POST", "GET,POST"]
ControllerType = Literal["Abstract [non-callable]", "Service", "Resources"]

class ApiAction(TypedDict):
    command: str
    parameters: str
    method: HttpMethod
    model_path: NotRequired[str]

class ApiController(TypedDict):
    actions: List[ApiAction]
    type: ControllerType
    module: str
    controller: str
    is_abstract: bool
    base_class: str | None
    filename: str
    model_filename: str | None


DEFAULT_BASE_METHODS = {
    "ApiMutableModelControllerBase": [{
        "command": "set",
        "parameters": "",
        "method": "POST"
    }, {
        "command": "get",
        "parameters": "",
        "method": "GET"
    }],
    "ApiMutableServiceControllerBase": [{
        "command": "status",
        "parameters": "",
        "method": "GET"
    }, {
        "command": "start",
        "parameters": "",
        "method": "POST"
    }, {
        "command": "stop",
        "parameters": "",
        "method": "POST"
    }, {
        "command": "restart",
        "parameters": "",
        "method": "POST"
    }, {
        "command": "reconfigure",
        "parameters": "",
        "method": "POST"
    }]
}


class ApiParser:
    def __init__(self, filename, debug=False):
        self._debug = debug
        self._filename = filename
        self.base_filename = os.path.basename(filename)
        self.controller = re.sub('(?<!^)(?=[A-Z])', '_', self.base_filename.split('Controller.php')[0]).lower()
        self.module_name = filename.replace('\\', '/').split('/')[-3].lower()

        self.model_filename = None
        self.is_abstract = False
        self.base_class = None
        self.api_commands = {}
        self._data = open(filename).read()

    def _parse_class_variables(self, node):
        if node.nodes[-1].name == '$internalModelClass':
            class_name = node.nodes[-1].initial
            app_location = "/".join(self._filename.split('/')[:-5])
            model_xml = "%s/models/%s.xml" % (app_location, class_name.replace("\\", "/"))
            if os.path.isfile(model_xml):
                self.model_filename = model_xml.replace('//', '/')

    def _extract_ops(self, root):
        """ Rercursively dive into offered root node, used to extracts details from within methods
        """
        for node in root:
            for value in node.__dict__.values():
                if isinstance(value, list):
                    yield from self._extract_ops(value)
                elif hasattr(value, '__dict__'):
                    yield from self._extract_ops([value])
                else:
                    yield node

    def _parse_method(self, node):
        """ Extract action methods to api endpoints
        """
        if node.name.endswith('Action'):
            cmd = "".join("_" + c.lower() if c.isupper() else c for c in node.name[:-6])
            record = {'command': cmd}
            params = []
            for p in node.params:
                default = default = p.default
                if isinstance(p.default, UnaryOp):
                    default = '%s%s' % (p.default.op, p.default.expr)
                elif isinstance(p.default, Constant):
                    default = p.default.name
                elif p.default == '':
                    default = "''"
                params.append('%s=%s' % (p.name, default) if default is not None else p.name)

            record['parameters'] = ','.join(params)

            self.api_commands[cmd] = record
            detected_methods = set()
            for item in self._extract_ops(node.nodes):
                if isinstance(item, MethodCall):
                    if item.name == 'isPost':
                        detected_methods.add('POST')
                    elif item.name == 'isGet':
                        detected_methods.add('GET')
                    elif item.name in ('addBase', 'setBase'):
                        record['model_path'] = item.params[1].node
                        detected_methods.add('POST')
                    elif item.name in ('delBase', 'toggleBase', 'searchBase'):
                        record['model_path'] = item.params[0].node
                        detected_methods.add('POST')
                        if item.name == 'searchBase':
                            detected_methods.add('GET')
                    elif item.name in ('setAction'):
                        detected_methods.add('POST')

            default_method = 'POST' if cmd == 'set' else 'GET'
            record['method'] = ','.join(sorted(detected_methods)) if detected_methods else default_method

    def _p_error(self, p):
        """ error handler, ignore unexpected tokens
        """
        if p:
            if self._debug:
                print("ignoring token %s at line %s" % (p.value, p.lexer.lineno))
            self.parser.errok()

    def parse_api_php(self) -> ApiController:
        """ collect api endpoints
        """
        self.api_commands = {}
        self.parser = make_parser()
        self.parser.errorfunc = self._p_error

        for root in self.parser.parse(self._data, lexer=lexer.clone(), tracking=True):
            if type(root) is Class:
                self.is_abstract = root.type == 'abstract'
                self.base_class = root.extends
                for node in root.nodes:
                    tmp = "".join("_" + c.lower() if c.isupper() else c for c in type(node).__name__)
                    node_method =  '_parse%s' % tmp
                    if hasattr(self, node_method):
                        getattr(self, node_method)(node)

        # stick base class defaults to the list when not yet defined
        if self.base_class in DEFAULT_BASE_METHODS:
            for item in DEFAULT_BASE_METHODS[self.base_class]:
                if item['command'] not in self.api_commands:
                    self.api_commands[item['command']] = {
                        'method': item['method'],
                        'command': item['command'],
                        'parameters': item['parameters']
                    }

        if self.is_abstract:
            controller_type = 'Abstract [non-callable]'
        elif self.controller.find('service') > -1:
            controller_type = 'Service'
        else:
            controller_type = 'Resources'

        return {
            'actions': sorted(self.api_commands.values(), key=lambda i: i['command']),
            'type': controller_type,
            'module': self.module_name,
            'controller': self.controller,
            'is_abstract': self.is_abstract,
            'base_class': self.base_class,
            'filename': self.base_filename,
            'model_filename': self.model_filename
        }
