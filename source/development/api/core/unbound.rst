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

    "``<<uses>>``", "", "", "", "*model* `Dnsbl.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unboundplus/Dnsbl.xml>`__"
