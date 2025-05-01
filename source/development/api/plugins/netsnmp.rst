Netsnmp
~~~~~~~

.. csv-table:: Resources (GeneralController.php)
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

.. csv-table:: Resources (UserController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","netsnmp","user","add_user",""
    "``POST``","netsnmp","user","del_user","$uuid"
    "``GET``","netsnmp","user","get",""
    "``GET``","netsnmp","user","get_user","$uuid=null"
    "``POST,GET``","netsnmp","user","search_user",""
    "``POST``","netsnmp","user","set",""
    "``POST``","netsnmp","user","set_user","$uuid"
    "``POST``","netsnmp","user","toggle_user","$uuid"

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/net-snmp/src/opnsense/mvc/app/models/OPNsense/Netsnmp/User.xml>`__"
