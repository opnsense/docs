Caddy
~~~~~

.. csv-table:: Resources (DiagnosticsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","caddy","diagnostics","caddyfile",""
    "``GET``","caddy","diagnostics","certificate",""
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

    "``POST``","caddy","reverse_proxy","addAccessList",""
    "``POST``","caddy","reverse_proxy","addBasicAuth",""
    "``POST``","caddy","reverse_proxy","addHandle",""
    "``POST``","caddy","reverse_proxy","addHeader",""
    "``POST``","caddy","reverse_proxy","addReverseProxy",""
    "``POST``","caddy","reverse_proxy","addSubdomain",""
    "``POST``","caddy","reverse_proxy","delAccessList","$uuid"
    "``POST``","caddy","reverse_proxy","delBasicAuth","$uuid"
    "``POST``","caddy","reverse_proxy","delHandle","$uuid"
    "``POST``","caddy","reverse_proxy","delHeader","$uuid"
    "``POST``","caddy","reverse_proxy","delReverseProxy","$uuid"
    "``POST``","caddy","reverse_proxy","delSubdomain","$uuid"
    "``GET``","caddy","reverse_proxy","get",""
    "``GET``","caddy","reverse_proxy","getAccessList","$uuid=null"
    "``GET``","caddy","reverse_proxy","getAllReverseDomains",""
    "``GET``","caddy","reverse_proxy","getBasicAuth","$uuid=null"
    "``GET``","caddy","reverse_proxy","getHandle","$uuid=null"
    "``GET``","caddy","reverse_proxy","getHeader","$uuid=null"
    "``GET``","caddy","reverse_proxy","getReverseProxy","$uuid=null"
    "``GET``","caddy","reverse_proxy","getSubdomain","$uuid=null"
    "``*``","caddy","reverse_proxy","searchAccessList",""
    "``*``","caddy","reverse_proxy","searchBasicAuth",""
    "``GET``","caddy","reverse_proxy","searchHandle",""
    "``*``","caddy","reverse_proxy","searchHeader",""
    "``GET``","caddy","reverse_proxy","searchReverseProxy",""
    "``GET``","caddy","reverse_proxy","searchSubdomain",""
    "``POST``","caddy","reverse_proxy","set",""
    "``POST``","caddy","reverse_proxy","setAccessList","$uuid"
    "``POST``","caddy","reverse_proxy","setBasicAuth","$uuid"
    "``POST``","caddy","reverse_proxy","setHandle","$uuid"
    "``POST``","caddy","reverse_proxy","setHeader","$uuid"
    "``POST``","caddy","reverse_proxy","setReverseProxy","$uuid"
    "``POST``","caddy","reverse_proxy","setSubdomain","$uuid"
    "``POST``","caddy","reverse_proxy","toggleHandle","$uuid,$enabled=null"
    "``POST``","caddy","reverse_proxy","toggleReverseProxy","$uuid,$enabled=null"
    "``POST``","caddy","reverse_proxy","toggleSubdomain","$uuid,$enabled=null"

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
