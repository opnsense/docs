import os
import re

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
    def __init__(self, filename):
        self._filename = filename
        self.base_filename = os.path.basename(filename)
        self.controller = re.sub('(?<!^)(?=[A-Z])', '_', self.base_filename.split('Controller.php')[0]).lower()
        self.module_name = filename.replace('\\', '/').split('/')[-3].lower()
        self._data = open(filename).read()

    def _get_model_filename(self):
        m = re.findall(r"\sprotected\sstatic\s\$internalModelClass\s=\s['|\"]([\w|\\]*)['|\"];", self._data)
        if len(m) == 0:
            m = re.findall(r"\sprotected\sstatic\s\$internalServiceClass\s=\s['|\"]([\w|\\]*)['|\"];", self._data)

        if len(m) > 0:
            app_location = "/".join(self._filename.split('/')[:-5])
            model_xml = "%s/models/%s.xml" % (app_location, m[0].replace("\\", "/"))
            if os.path.isfile(model_xml):
                return  model_xml.replace('//', '/')

    def _parse_action_content(self, code_block):
        record = {}
        boilerplates = {
            'get': {'pattern': '$this->getBase', 'method': 'GET'},
            'del': {'pattern': '$this->delBase', 'method': 'POST'},
            'add': {'pattern': '$this->addBase', 'method': 'POST'},
            'set': {'pattern': '$this->setBase', 'method': 'POST'},
            'toggle': {'pattern': '$this->toggleBase', 'method': 'POST'},
            'search': {'pattern': '$this->searchBase', 'method': 'GET,POST'},
        }
        for action, boilerplate in boilerplates.items():
            pos = code_block.find(boilerplate['pattern'])
            if pos > -1:
                record['method'] = boilerplate['method']

        if 'method' not in record:
            methods = []
            if code_block.find('request->isPost(') > -1:
                methods.append('POST')
            if code_block.find('request->isGet(') > -1:
                methods.append('GET')
            if len(methods) > 1:
                record['method'] = ','.join(methods)

        return record


    def parse_api_php(self):
        data = self._data
        m = re.findall(r"\n([\w]*).*class.*Controller.*extends\s([\w|\\]*)", data)
        base_class = m[0][1].split('\\')[-1] if len(m) > 0 else None
        is_abstract = len(m) > 0 and m[0][0] == 'abstract'

        model_filename = self._get_model_filename()

        function_callouts = re.findall(r"(\n\s+(private|public|protected)\s+function\s+(\w+)\((.*)\))", data)
        result = list()
        this_commands = []
        for idx, function in enumerate(function_callouts):
            begin_marker = data.find(function_callouts[idx][0])
            if idx+1 < len(function_callouts):
                end_marker = data.find(function_callouts[idx+1][0])
            else:
                end_marker = -1
            code_block = data[begin_marker+len(function[0]):end_marker]
            if function[2].endswith('Action'):
                cmd = "".join("_" + c.lower() if c.isupper() else c for c in function[2][:-6])
                this_commands.append(cmd)
                record = {
                    'method': 'GET',
                    'module': self.module_name,
                    'controller': self.controller,
                    'is_abstract': is_abstract,
                    'base_class': base_class,
                    'command': cmd,
                    'parameters': function[3].replace(' ', '').replace('"', '""'),
                    'filename': self.base_filename,
                    'model_filename': model_filename
                }
                if is_abstract:
                    record['type'] = 'Abstract [non-callable]'
                elif self.controller.find('service') > -1:
                    record['type'] = 'Service'
                else:
                    record['type'] = 'Resources'
                record.update(self._parse_action_content(code_block))
                # find most likely method (default => GET)
                result.append(record)
        if base_class in DEFAULT_BASE_METHODS:
            for item in DEFAULT_BASE_METHODS[base_class]:
                if item not in this_commands:
                    result.append({
                        'type': 'Service',
                        'method': item['method'],
                        'module': self.module_name,
                        'controller': self.controller,
                        'is_abstract': False,
                        'base_class': base_class,
                        'command': item['command'],
                        'parameters': item['parameters'],
                        'filename': self.base_filename,
                        'model_filename': model_filename
                    })

        return sorted(result, key=lambda i: i['command'])