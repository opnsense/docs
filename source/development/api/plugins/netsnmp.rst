Netsnmp
~~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","netsnmp","general","get",""
    "``POST``","netsnmp","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/net-snmp/src/opnsense/mvc/app/models/OPNsense/Netsnmp/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","netsnmp","service","reconfigure",""
    "``POST``","netsnmp","service","restart",""
    "``POST``","netsnmp","service","start",""
    "``GET``","netsnmp","service","status",""
    "``POST``","netsnmp","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/net-snmp/src/opnsense/mvc/app/models/OPNsense/Netsnmp/General.xml>`__"

.. csv-table:: Resources (UserController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","netsnmp","user","addUser",""
    "``POST``","netsnmp","user","delUser","$uuid"
    "``GET``","netsnmp","user","get",""
    "``GET``","netsnmp","user","getUser","$uuid=null"
    "``*``","netsnmp","user","searchUser",""
    "``POST``","netsnmp","user","set",""
    "``POST``","netsnmp","user","setUser","$uuid"
    "``POST``","netsnmp","user","toggleUser","$uuid"

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/net-snmp/src/opnsense/mvc/app/models/OPNsense/Netsnmp/User.xml>`__"
