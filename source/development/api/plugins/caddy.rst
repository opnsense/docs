Caddy
~~~~~

.. csv-table:: Resources (DiagnosticsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","caddy","diagnostics","caddyfile",""
    "``GET``","caddy","diagnostics","config",""
    "``GET``","caddy","diagnostics","get",""
    "``POST``","caddy","diagnostics","set",""

    "``<<uses>>``", "", "", "", "*model* `Caddy.xml <https://github.com/opnsense/plugins/blob/master/www/caddy/src/opnsense/mvc/app/models/OPNsense/Caddy/Caddy.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","caddy","general","get",""
    "``POST``","caddy","general","set",""

    "``<<uses>>``", "", "", "", "*model* `Caddy.xml <https://github.com/opnsense/plugins/blob/master/www/caddy/src/opnsense/mvc/app/models/OPNsense/Caddy/Caddy.xml>`__"

.. csv-table:: Resources (ReverseProxyController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","caddy","reverse_proxy","add_access_list",""
    "``POST``","caddy","reverse_proxy","add_basic_auth",""
    "``POST``","caddy","reverse_proxy","add_handle",""
    "``POST``","caddy","reverse_proxy","add_header",""
    "``POST``","caddy","reverse_proxy","add_layer4",""
    "``POST``","caddy","reverse_proxy","add_layer4_openvpn",""
    "``POST``","caddy","reverse_proxy","add_reverse_proxy",""
    "``POST``","caddy","reverse_proxy","add_subdomain",""
    "``POST``","caddy","reverse_proxy","del_access_list","$uuid"
    "``POST``","caddy","reverse_proxy","del_basic_auth","$uuid"
    "``POST``","caddy","reverse_proxy","del_handle","$uuid"
    "``POST``","caddy","reverse_proxy","del_header","$uuid"
    "``POST``","caddy","reverse_proxy","del_layer4","$uuid"
    "``POST``","caddy","reverse_proxy","del_layer4_openvpn","$uuid"
    "``POST``","caddy","reverse_proxy","del_reverse_proxy","$uuid"
    "``POST``","caddy","reverse_proxy","del_subdomain","$uuid"
    "``GET``","caddy","reverse_proxy","get",""
    "``GET``","caddy","reverse_proxy","get_access_list","$uuid=null"
    "``GET``","caddy","reverse_proxy","get_all_reverse_domains",""
    "``GET``","caddy","reverse_proxy","get_basic_auth","$uuid=null"
    "``GET``","caddy","reverse_proxy","get_handle","$uuid=null"
    "``GET``","caddy","reverse_proxy","get_header","$uuid=null"
    "``GET``","caddy","reverse_proxy","get_layer4","$uuid=null"
    "``GET``","caddy","reverse_proxy","get_layer4_openvpn","$uuid=null"
    "``GET``","caddy","reverse_proxy","get_reverse_proxy","$uuid=null"
    "``GET``","caddy","reverse_proxy","get_subdomain","$uuid=null"
    "``*``","caddy","reverse_proxy","search_access_list",""
    "``*``","caddy","reverse_proxy","search_basic_auth",""
    "``*``","caddy","reverse_proxy","search_handle",""
    "``*``","caddy","reverse_proxy","search_header",""
    "``*``","caddy","reverse_proxy","search_layer4",""
    "``*``","caddy","reverse_proxy","search_layer4_openvpn",""
    "``*``","caddy","reverse_proxy","search_reverse_proxy",""
    "``*``","caddy","reverse_proxy","search_subdomain",""
    "``POST``","caddy","reverse_proxy","set",""
    "``POST``","caddy","reverse_proxy","set_access_list","$uuid"
    "``POST``","caddy","reverse_proxy","set_basic_auth","$uuid"
    "``POST``","caddy","reverse_proxy","set_handle","$uuid"
    "``POST``","caddy","reverse_proxy","set_header","$uuid"
    "``POST``","caddy","reverse_proxy","set_layer4","$uuid"
    "``POST``","caddy","reverse_proxy","set_layer4_openvpn","$uuid"
    "``POST``","caddy","reverse_proxy","set_reverse_proxy","$uuid"
    "``POST``","caddy","reverse_proxy","set_subdomain","$uuid"
    "``POST``","caddy","reverse_proxy","toggle_handle","$uuid,$enabled=null"
    "``POST``","caddy","reverse_proxy","toggle_layer4","$uuid,$enabled=null"
    "``POST``","caddy","reverse_proxy","toggle_layer4_openvpn","$uuid,$enabled=null"
    "``POST``","caddy","reverse_proxy","toggle_reverse_proxy","$uuid,$enabled=null"
    "``POST``","caddy","reverse_proxy","toggle_subdomain","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Caddy.xml <https://github.com/opnsense/plugins/blob/master/www/caddy/src/opnsense/mvc/app/models/OPNsense/Caddy/Caddy.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","caddy","service","reconfigure",""
    "``POST``","caddy","service","restart",""
    "``POST``","caddy","service","start",""
    "``GET``","caddy","service","status",""
    "``POST``","caddy","service","stop",""
    "``GET``","caddy","service","validate",""

    "``<<uses>>``", "", "", "", "*model* `Caddy.xml <https://github.com/opnsense/plugins/blob/master/www/caddy/src/opnsense/mvc/app/models/OPNsense/Caddy/Caddy.xml>`__"
