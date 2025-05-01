Zabbixagent
~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","zabbixagent","service","reconfigure",""
    "``POST``","zabbixagent","service","restart",""
    "``POST``","zabbixagent","service","start",""
    "``GET``","zabbixagent","service","status",""
    "``POST``","zabbixagent","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","zabbixagent","settings","add_alias",""
    "``POST``","zabbixagent","settings","add_userparameter",""
    "``POST``","zabbixagent","settings","del_alias","$uuid"
    "``POST``","zabbixagent","settings","del_userparameter","$uuid"
    "``GET``","zabbixagent","settings","get",""
    "``GET``","zabbixagent","settings","get_alias","$uuid=null"
    "``GET``","zabbixagent","settings","get_userparameter","$uuid=null"
    "``GET,POST``","zabbixagent","settings","search_aliases",""
    "``GET,POST``","zabbixagent","settings","search_userparameters",""
    "``POST``","zabbixagent","settings","set",""
    "``POST``","zabbixagent","settings","set_alias","$uuid"
    "``POST``","zabbixagent","settings","set_userparameter","$uuid"
    "``POST``","zabbixagent","settings","toggle_alias","$uuid"
    "``POST``","zabbixagent","settings","toggle_userparameter","$uuid"

    "``<<uses>>``", "", "", "", "*model* `ZabbixAgent.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/zabbix-agent/src/opnsense/mvc/app/models/OPNsense/ZabbixAgent/ZabbixAgent.xml>`__"
