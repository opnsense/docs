Netsnmp
~~~~~~~

.. csv-table:: Resources (UserController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","netsnmp","user","addUser",""
    "``POST``","netsnmp","user","delUser","$uuid"
    "``GET``","netsnmp","user","getUser","$uuid=null"
    "``*``","netsnmp","user","searchUser",""
    "``POST``","netsnmp","user","setUser","$uuid"
    "``POST``","netsnmp","user","toggleUser","$uuid"

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/net-snmp/src/opnsense/mvc/app/models/OPNsense/Netsnmp/User.xml>`__"
