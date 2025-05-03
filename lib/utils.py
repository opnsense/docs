import os
from . import ApiParser

EXCLUDE_CONTROLLERS = ['Core/Api/FirmwareController.php']

def collect_api_modules(source: str, debug: bool = False) -> dict[str, list[dict]]:
    # collect all endpoints
    all_modules = dict()
    for root, dirs, files in os.walk(source):
        for fname in sorted(files):
            filename = os.path.join(root, fname)
            skip = False
            for to_exclude in EXCLUDE_CONTROLLERS:
                if filename.endswith(to_exclude):
                    skip = True
                    break
            if not skip and filename.lower().endswith('controller.php') and filename.find('mvc/app/controllers') > -1 \
                    and root.endswith('Api'):
                payload = ApiParser(filename, debug).parse_api_php()
                if len(payload) > 0:
                    if payload['module'] not in all_modules:
                        all_modules[payload['module']] = list()
                    all_modules[payload['module']].append(payload)

    return all_modules
