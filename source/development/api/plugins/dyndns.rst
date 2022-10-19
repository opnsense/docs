Dyndns
~~~~~~

.. csv-table:: Resources (AccountsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dyndns","accounts","addItem",""
    "``POST``","dyndns","accounts","delItem","$uuid"
    "``GET``","dyndns","accounts","get",""
    "``GET``","dyndns","accounts","getItem","$uuid=null"
    "``*``","dyndns","accounts","searchItem",""
    "``POST``","dyndns","accounts","set",""
    "``POST``","dyndns","accounts","setItem","$uuid"
    "``POST``","dyndns","accounts","toggleItem","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `DynDNS.xml <https://github.com/opnsense/plugins/blob/master/dns/ddclient/src/opnsense/mvc/app/models/OPNsense/DynDNS/DynDNS.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dyndns","service","reconfigure",""
    "``POST``","dyndns","service","restart",""
    "``POST``","dyndns","service","start",""
    "``GET``","dyndns","service","status",""
    "``POST``","dyndns","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `DynDNS.xml <https://github.com/opnsense/plugins/blob/master/dns/ddclient/src/opnsense/mvc/app/models/OPNsense/DynDNS/DynDNS.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dyndns","settings","get",""
    "``GET``","dyndns","settings","get",""
    "``POST``","dyndns","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `DynDNS.xml <https://github.com/opnsense/plugins/blob/master/dns/ddclient/src/opnsense/mvc/app/models/OPNsense/DynDNS/DynDNS.xml>`__"
