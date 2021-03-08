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

.. csv-table:: Service (DnsblController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","unbound","dnsbl","get",""
    "``GET``","unbound","dnsbl","set",""

    "``<<uses>>``", "", "", "", "*model* `Dnsbl.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unboundplus/Dnsbl.xml>`__"

.. csv-table:: Service (MiscellaneousController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","unbound","miscellaneous","get",""
    "``GET``","unbound","miscellaneous","set",""

    "``<<uses>>``", "", "", "", "*model* `Miscellaneous.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unboundplus/Miscellaneous.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","unbound","service","dnsbl",""
    "``GET``","unbound","service","reconfigure",""
    "``GET``","unbound","service","restart",""
    "``GET``","unbound","service","start",""
    "``GET``","unbound","service","status",""
    "``GET``","unbound","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Dnsbl.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unboundplus/Dnsbl.xml>`__"
