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

.. csv-table:: Resources (OverviewController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","unbound","overview","Rolling","$timeperiod,$clients=false"
    "``GET``","unbound","overview","isBlockListEnabled",""
    "``GET``","unbound","overview","isEnabled",""
    "``GET``","unbound","overview","searchQueries",""
    "``GET``","unbound","overview","totals","$maximum"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","unbound","service","dnsbl",""
    "``POST``","unbound","service","reconfigure",""
    "``GET``","unbound","service","reconfigureGeneral",""
    "``POST``","unbound","service","restart",""
    "``POST``","unbound","service","start",""
    "``GET``","unbound","service","status",""
    "``POST``","unbound","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Unbound.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","unbound","settings","addAcl",""
    "``POST``","unbound","settings","addDomainOverride",""
    "``POST``","unbound","settings","addForward",""
    "``POST``","unbound","settings","addHostAlias",""
    "``POST``","unbound","settings","addHostOverride",""
    "``POST``","unbound","settings","delAcl","$uuid"
    "``POST``","unbound","settings","delDomainOverride","$uuid"
    "``POST``","unbound","settings","delForward","$uuid"
    "``POST``","unbound","settings","delHostAlias","$uuid"
    "``POST``","unbound","settings","delHostOverride","$uuid"
    "``GET``","unbound","settings","get",""
    "``GET``","unbound","settings","getAcl","$uuid=null"
    "``GET``","unbound","settings","getDomainOverride","$uuid=null"
    "``GET``","unbound","settings","getForward","$uuid=null"
    "``GET``","unbound","settings","getHostAlias","$uuid=null"
    "``GET``","unbound","settings","getHostOverride","$uuid=null"
    "``GET``","unbound","settings","getNameservers",""
    "``*``","unbound","settings","searchAcl",""
    "``*``","unbound","settings","searchDomainOverride",""
    "``*``","unbound","settings","searchForward",""
    "``*``","unbound","settings","searchHostAlias",""
    "``*``","unbound","settings","searchHostOverride",""
    "``POST``","unbound","settings","set",""
    "``POST``","unbound","settings","setAcl","$uuid"
    "``POST``","unbound","settings","setDomainOverride","$uuid"
    "``POST``","unbound","settings","setForward","$uuid"
    "``POST``","unbound","settings","setHostAlias","$uuid"
    "``POST``","unbound","settings","setHostOverride","$uuid"
    "``POST``","unbound","settings","toggleAcl","$uuid,$enabled=null"
    "``POST``","unbound","settings","toggleDomainOverride","$uuid,$enabled=null"
    "``POST``","unbound","settings","toggleForward","$uuid,$enabled=null"
    "``POST``","unbound","settings","toggleHostAlias","$uuid,$enabled=null"
    "``POST``","unbound","settings","toggleHostOverride","$uuid,$enabled=null"
    "``POST``","unbound","settings","updateBlocklist",""

    "``<<uses>>``", "", "", "", "*model* `Unbound.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml>`__"
