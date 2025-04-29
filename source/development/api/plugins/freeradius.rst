Freeradius
~~~~~~~~~~

.. csv-table:: Resources (AvpairController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","avpair","add_avpair",""
    "``POST``","freeradius","avpair","del_avpair","$uuid"
    "``GET``","freeradius","avpair","get",""
    "``GET``","freeradius","avpair","get_avpair","$uuid=null"
    "``*``","freeradius","avpair","search_avpair",""
    "``POST``","freeradius","avpair","set",""
    "``POST``","freeradius","avpair","set_avpair","$uuid"
    "``POST``","freeradius","avpair","toggle_avpair","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Avpair.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Avpair.xml>`__"

.. csv-table:: Resources (ClientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","client","add_client",""
    "``POST``","freeradius","client","del_client","$uuid"
    "``GET``","freeradius","client","get",""
    "``GET``","freeradius","client","get",""
    "``GET``","freeradius","client","get_client","$uuid=null"
    "``GET``","freeradius","client","search_client",""
    "``POST``","freeradius","client","set",""
    "``POST``","freeradius","client","set",""
    "``POST``","freeradius","client","set_client","$uuid"
    "``GET``","freeradius","client","toggle_client","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Client.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Client.xml>`__"

.. csv-table:: Resources (DhcpController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","dhcp","add_dhcp",""
    "``POST``","freeradius","dhcp","del_dhcp","$uuid"
    "``GET``","freeradius","dhcp","get",""
    "``GET``","freeradius","dhcp","get_dhcp","$uuid=null"
    "``*``","freeradius","dhcp","search_dhcp",""
    "``POST``","freeradius","dhcp","set",""
    "``POST``","freeradius","dhcp","set_dhcp","$uuid"
    "``POST``","freeradius","dhcp","toggle_dhcp","$uuid"

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

.. csv-table:: Service (LdapController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","freeradius","ldap","get",""
    "``POST``","freeradius","ldap","set",""

    "``<<uses>>``", "", "", "", "*model* `Ldap.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Ldap.xml>`__"

.. csv-table:: Resources (LeaseController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","lease","add_lease",""
    "``POST``","freeradius","lease","del_lease","$uuid"
    "``GET``","freeradius","lease","get",""
    "``GET``","freeradius","lease","get_lease","$uuid=null"
    "``*``","freeradius","lease","search_lease",""
    "``POST``","freeradius","lease","set",""
    "``POST``","freeradius","lease","set_lease","$uuid"
    "``POST``","freeradius","lease","toggle_lease","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Lease.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Lease.xml>`__"

.. csv-table:: Resources (ProxyController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","freeradius","proxy","add_homeserver",""
    "``POST``","freeradius","proxy","add_homeserverpool",""
    "``POST``","freeradius","proxy","add_realm",""
    "``POST``","freeradius","proxy","del_homeserver","$uuid"
    "``POST``","freeradius","proxy","del_homeserverpool","$uuid"
    "``POST``","freeradius","proxy","del_realm","$uuid"
    "``GET``","freeradius","proxy","get",""
    "``GET``","freeradius","proxy","get",""
    "``GET``","freeradius","proxy","get_homeserver","$uuid=null"
    "``GET``","freeradius","proxy","get_homeserverpool","$uuid=null"
    "``GET``","freeradius","proxy","get_realm","$uuid=null"
    "``GET``","freeradius","proxy","search_homeserver",""
    "``GET``","freeradius","proxy","search_homeserverpool",""
    "``GET``","freeradius","proxy","search_realm",""
    "``POST``","freeradius","proxy","set",""
    "``POST``","freeradius","proxy","set",""
    "``POST``","freeradius","proxy","set_homeserver","$uuid"
    "``POST``","freeradius","proxy","set_homeserverpool","$uuid"
    "``POST``","freeradius","proxy","set_realm","$uuid"
    "``GET``","freeradius","proxy","toggle_homeserver","$uuid"
    "``GET``","freeradius","proxy","toggle_homeserverpool","$uuid"
    "``GET``","freeradius","proxy","toggle_realm","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Proxy.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/Proxy.xml>`__"

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

    "``POST``","freeradius","user","add_user",""
    "``POST``","freeradius","user","del_user","$uuid"
    "``GET``","freeradius","user","get",""
    "``GET``","freeradius","user","get",""
    "``GET``","freeradius","user","get_user","$uuid=null"
    "``GET``","freeradius","user","search_user",""
    "``POST``","freeradius","user","set",""
    "``POST``","freeradius","user","set",""
    "``POST``","freeradius","user","set_user","$uuid"
    "``GET``","freeradius","user","toggle_user","$uuid"

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/plugins/blob/master/net/freeradius/src/opnsense/mvc/app/models/OPNsense/Freeradius/User.xml>`__"
