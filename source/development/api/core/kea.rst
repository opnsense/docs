Kea
~~~

.. csv-table:: Resources (CtrlAgentController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","kea","ctrl_agent","get",""
    "``GET``","kea","ctrl_agent","get",""
    "``POST``","kea","ctrl_agent","set",""

    "``<<uses>>``", "", "", "", "*model* `KeaCtrlAgent.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Kea/KeaCtrlAgent.xml>`__"

.. csv-table:: Resources (Dhcpv4Controller.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","kea","dhcpv4","addPeer",""
    "``POST``","kea","dhcpv4","addReservation",""
    "``POST``","kea","dhcpv4","addSubnet",""
    "``POST``","kea","dhcpv4","delPeer","$uuid"
    "``POST``","kea","dhcpv4","delReservation","$uuid"
    "``POST``","kea","dhcpv4","delSubnet","$uuid"
    "``GET``","kea","dhcpv4","get",""
    "``GET``","kea","dhcpv4","get",""
    "``GET``","kea","dhcpv4","getPeer","$uuid=null"
    "``GET``","kea","dhcpv4","getReservation","$uuid=null"
    "``GET``","kea","dhcpv4","getSubnet","$uuid=null"
    "``*``","kea","dhcpv4","searchPeer",""
    "``*``","kea","dhcpv4","searchReservation",""
    "``*``","kea","dhcpv4","searchSubnet",""
    "``POST``","kea","dhcpv4","set",""
    "``POST``","kea","dhcpv4","setPeer","$uuid"
    "``POST``","kea","dhcpv4","setReservation","$uuid"
    "``POST``","kea","dhcpv4","setSubnet","$uuid"

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

    "``<<uses>>``", "", "", "", "*model* `KeaDhcpv4.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Kea/KeaDhcpv4.xml>`__"
