Zabbixproxy
~~~~~~~~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","zabbixproxy","general","get",""
    "``POST``","zabbixproxy","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/zabbix-proxy/src/opnsense/mvc/app/models/OPNsense/Zabbixproxy/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","zabbixproxy","service","reconfigure",""
    "``POST``","zabbixproxy","service","restart",""
    "``POST``","zabbixproxy","service","start",""
    "``GET``","zabbixproxy","service","status",""
    "``POST``","zabbixproxy","service","stop",""
