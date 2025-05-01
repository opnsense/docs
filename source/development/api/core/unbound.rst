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

    "``GET``","unbound","overview","_rolling","$timeperiod,$clients=0"
    "``GET``","unbound","overview","is_block_list_enabled",""
    "``GET``","unbound","overview","is_enabled",""
    "``GET``","unbound","overview","search_queries",""
    "``GET``","unbound","overview","totals","$maximum"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","unbound","service","dnsbl",""
    "``POST``","unbound","service","reconfigure",""
    "``GET``","unbound","service","reconfigure_general",""
    "``POST``","unbound","service","restart",""
    "``POST``","unbound","service","start",""
    "``GET``","unbound","service","status",""
    "``POST``","unbound","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","unbound","settings","add_acl",""
    "``POST``","unbound","settings","add_forward",""
    "``POST``","unbound","settings","add_host_alias",""
    "``POST``","unbound","settings","add_host_override",""
    "``POST``","unbound","settings","del_acl","$uuid"
    "``POST``","unbound","settings","del_forward","$uuid"
    "``POST``","unbound","settings","del_host_alias","$uuid"
    "``POST``","unbound","settings","del_host_override","$uuid"
    "``GET``","unbound","settings","get",""
    "``GET``","unbound","settings","get_acl","$uuid=null"
    "``GET``","unbound","settings","get_forward","$uuid=null"
    "``GET``","unbound","settings","get_host_alias","$uuid=null"
    "``GET``","unbound","settings","get_host_override","$uuid=null"
    "``GET``","unbound","settings","get_nameservers",""
    "``GET,POST``","unbound","settings","search_acl",""
    "``GET,POST``","unbound","settings","search_forward",""
    "``GET,POST``","unbound","settings","search_host_alias",""
    "``GET,POST``","unbound","settings","search_host_override",""
    "``POST``","unbound","settings","set",""
    "``POST``","unbound","settings","set_acl","$uuid"
    "``POST``","unbound","settings","set_forward","$uuid"
    "``POST``","unbound","settings","set_host_alias","$uuid"
    "``POST``","unbound","settings","set_host_override","$uuid"
    "``POST``","unbound","settings","toggle_acl","$uuid,$enabled=null"
    "``POST``","unbound","settings","toggle_forward","$uuid,$enabled=null"
    "``POST``","unbound","settings","toggle_host_alias","$uuid,$enabled=null"
    "``POST``","unbound","settings","toggle_host_override","$uuid,$enabled=null"
    "``POST``","unbound","settings","update_blocklist",""

    "``<<uses>>``", "", "", "", "*model* `Unbound.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Unbound/Unbound.xml>`__"
