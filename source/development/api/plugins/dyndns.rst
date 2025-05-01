Dyndns
~~~~~~

.. csv-table:: Resources (AccountsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dyndns","accounts","add_item",""
    "``POST``","dyndns","accounts","del_item","$uuid"
    "``GET``","dyndns","accounts","get",""
    "``GET``","dyndns","accounts","get_item","$uuid=null"
    "``GET,POST``","dyndns","accounts","search_item",""
    "``POST``","dyndns","accounts","set",""
    "``POST``","dyndns","accounts","set_item","$uuid"
    "``POST``","dyndns","accounts","toggle_item","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `DynDNS.xml <https://github.com/opnsense/plugins/blob/master/dns/ddclient/src/opnsense/mvc/app/models/OPNsense/DynDNS/DynDNS.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dyndns","service","reconfigure",""
    "``POST``","dyndns","service","restart",""
    "``POST``","dyndns","service","start",""
    "``GET``","dyndns","service","status",""
    "``POST``","dyndns","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dyndns","settings","get",""
    "``POST``","dyndns","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `DynDNS.xml <https://github.com/opnsense/plugins/blob/master/dns/ddclient/src/opnsense/mvc/app/models/OPNsense/DynDNS/DynDNS.xml>`__"
