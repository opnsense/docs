Kea
~~~

.. csv-table:: Resources (CtrlAgentController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","kea","ctrl_agent","get",""
    "``POST``","kea","ctrl_agent","set",""

    "``<<uses>>``", "", "", "", "*model* `KeaCtrlAgent.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Kea/KeaCtrlAgent.xml>`__"

.. csv-table:: Resources (Dhcpv4Controller.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","kea","dhcpv4","add_peer",""
    "``POST``","kea","dhcpv4","add_reservation",""
    "``POST``","kea","dhcpv4","add_subnet",""
    "``POST``","kea","dhcpv4","del_peer","$uuid"
    "``POST``","kea","dhcpv4","del_reservation","$uuid"
    "``POST``","kea","dhcpv4","del_subnet","$uuid"
    "``GET``","kea","dhcpv4","download_reservations",""
    "``GET``","kea","dhcpv4","get",""
    "``GET``","kea","dhcpv4","get_peer","$uuid=null"
    "``GET``","kea","dhcpv4","get_reservation","$uuid=null"
    "``GET``","kea","dhcpv4","get_subnet","$uuid=null"
    "``GET,POST``","kea","dhcpv4","search_peer",""
    "``GET,POST``","kea","dhcpv4","search_reservation",""
    "``GET,POST``","kea","dhcpv4","search_subnet",""
    "``POST``","kea","dhcpv4","set",""
    "``POST``","kea","dhcpv4","set_peer","$uuid"
    "``POST``","kea","dhcpv4","set_reservation","$uuid"
    "``POST``","kea","dhcpv4","set_subnet","$uuid"
    "``POST``","kea","dhcpv4","upload_reservations",""

    "``<<uses>>``", "", "", "", "*model* `KeaDhcpv4.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Kea/KeaDhcpv4.xml>`__"

.. csv-table:: Resources (Leases4Controller.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","kea","leases4","search",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","kea","service","reconfigure",""
    "``POST``","kea","service","restart",""
    "``POST``","kea","service","start",""
    "``GET``","kea","service","status",""
    "``POST``","kea","service","stop",""
