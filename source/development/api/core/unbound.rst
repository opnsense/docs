Unbound
~~~~~~~

.. csv-table:: Resources (DiagnosticsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","unbound","diagnostics","dumpcache",""
    "``GET``","unbound","diagnostics","dumpinfra",""
    "``GET``","unbound","diagnostics","listinsecure",""
    "``GET``","unbound","diagnostics","listlocaldata",""
    "``GET``","unbound","diagnostics","listlocalzones",""
    "``GET``","unbound","diagnostics","stats",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","unbound","service","dnsbl",""
    "``GET``","unbound","service","reconfigure",""
    "``GET``","unbound","service","restart",""
    "``GET``","unbound","service","start",""
    "``GET``","unbound","service","status",""
    "``GET``","unbound","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Unbound.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","unbound","settings","addDot",""
    "``POST``","unbound","settings","delDot","$uuid"
    "``GET``","unbound","settings","get",""
    "``GET``","unbound","settings","getDot","$uuid=null"
    "``*``","unbound","settings","searchDot",""
    "``GET``","unbound","settings","set",""
    "``POST``","unbound","settings","setDot","$uuid"
    "``POST``","unbound","settings","toggleDot","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Unbound.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml>`__"
