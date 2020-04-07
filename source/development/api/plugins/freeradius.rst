Freeradius
~~~~~~~~~~

.. csv-table:: Resources (AvpairController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","avpair","addAvpair",""
    "``POST``","freeradius","avpair","delAvpair","$uuid"
    "``GET``","freeradius","avpair","getAvpair","$uuid=null"
    "``*``","freeradius","avpair","searchAvpair",""
    "``POST``","freeradius","avpair","setAvpair","$uuid"
    "``POST``","freeradius","avpair","toggleAvpair","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Avpair.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Avpair.xml>`__"

.. csv-table:: Resources (ClientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","client","addClient",""
    "``POST``","freeradius","client","delClient","$uuid"
    "``GET``","freeradius","client","get",""
    "``GET``","freeradius","client","getClient","$uuid=null"
    "``GET``","freeradius","client","searchClient",""
    "``POST``","freeradius","client","set",""
    "``POST``","freeradius","client","setClient","$uuid"
    "``GET``","freeradius","client","toggleClient","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Client.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Client.xml>`__"

.. csv-table:: Resources (DhcpController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","dhcp","addDhcp",""
    "``POST``","freeradius","dhcp","delDhcp","$uuid"
    "``GET``","freeradius","dhcp","getDhcp","$uuid=null"
    "``*``","freeradius","dhcp","searchDhcp",""
    "``POST``","freeradius","dhcp","setDhcp","$uuid"
    "``POST``","freeradius","dhcp","toggleDhcp","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Dhcp.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Dhcp.xml>`__"

.. csv-table:: Resources (EapController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","freeradius","eap","get",""
    "``POST``","freeradius","eap","set",""

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","freeradius","general","get",""
    "``POST``","freeradius","general","set",""

.. csv-table:: Resources (LeaseController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","lease","addLease",""
    "``POST``","freeradius","lease","delLease","$uuid"
    "``GET``","freeradius","lease","getLease","$uuid=null"
    "``*``","freeradius","lease","searchLease",""
    "``POST``","freeradius","lease","setLease","$uuid"
    "``POST``","freeradius","lease","toggleLease","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Lease.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Lease.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","service","reconfigure",""
    "``POST``","freeradius","service","restart",""
    "``POST``","freeradius","service","start",""
    "``GET``","freeradius","service","status",""
    "``POST``","freeradius","service","stop",""

.. csv-table:: Resources (UserController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","user","addUser",""
    "``POST``","freeradius","user","delUser","$uuid"
    "``GET``","freeradius","user","get",""
    "``GET``","freeradius","user","getUser","$uuid=null"
    "``GET``","freeradius","user","searchUser",""
    "``POST``","freeradius","user","set",""
    "``POST``","freeradius","user","setUser","$uuid"
    "``GET``","freeradius","user","toggleUser","$uuid"

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/User.xml>`__"
