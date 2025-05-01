Quagga
~~~~~~

.. csv-table:: Resources (BfdController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","bfd","add_neighbor",""
    "``POST``","quagga","bfd","del_neighbor","$uuid"
    "``GET``","quagga","bfd","get",""
    "``GET``","quagga","bfd","get_neighbor","$uuid=null"
    "``POST,GET``","quagga","bfd","search_neighbor",""
    "``POST``","quagga","bfd","set",""
    "``POST``","quagga","bfd","set_neighbor","$uuid"
    "``POST``","quagga","bfd","toggle_neighbor","$uuid"

    "``<<uses>>``", "", "", "", "*model* `BFD.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/BFD.xml>`__"

.. csv-table:: Resources (BgpController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","bgp","add_aspath",""
    "``POST``","quagga","bgp","add_communitylist",""
    "``POST``","quagga","bgp","add_neighbor",""
    "``POST``","quagga","bgp","add_peergroup",""
    "``POST``","quagga","bgp","add_prefixlist",""
    "``POST``","quagga","bgp","add_redistribution",""
    "``POST``","quagga","bgp","add_routemap",""
    "``POST``","quagga","bgp","del_aspath","$uuid"
    "``POST``","quagga","bgp","del_communitylist","$uuid"
    "``POST``","quagga","bgp","del_neighbor","$uuid"
    "``POST``","quagga","bgp","del_peergroup","$uuid"
    "``POST``","quagga","bgp","del_prefixlist","$uuid"
    "``POST``","quagga","bgp","del_redistribution","$uuid"
    "``POST``","quagga","bgp","del_routemap","$uuid"
    "``GET``","quagga","bgp","get",""
    "``GET``","quagga","bgp","get_aspath","$uuid=null"
    "``GET``","quagga","bgp","get_communitylist","$uuid=null"
    "``GET``","quagga","bgp","get_neighbor","$uuid=null"
    "``GET``","quagga","bgp","get_peergroup","$uuid=null"
    "``GET``","quagga","bgp","get_prefixlist","$uuid=null"
    "``GET``","quagga","bgp","get_redistribution","$uuid=null"
    "``GET``","quagga","bgp","get_routemap","$uuid=null"
    "``POST,GET``","quagga","bgp","search_aspath",""
    "``POST,GET``","quagga","bgp","search_communitylist",""
    "``POST,GET``","quagga","bgp","search_neighbor",""
    "``POST,GET``","quagga","bgp","search_peergroup",""
    "``POST,GET``","quagga","bgp","search_prefixlist",""
    "``POST,GET``","quagga","bgp","search_redistribution",""
    "``POST,GET``","quagga","bgp","search_routemap",""
    "``POST``","quagga","bgp","set",""
    "``POST``","quagga","bgp","set_aspath","$uuid"
    "``POST``","quagga","bgp","set_communitylist","$uuid"
    "``POST``","quagga","bgp","set_neighbor","$uuid"
    "``POST``","quagga","bgp","set_peergroup","$uuid"
    "``POST``","quagga","bgp","set_prefixlist","$uuid"
    "``POST``","quagga","bgp","set_redistribution","$uuid"
    "``POST``","quagga","bgp","set_routemap","$uuid"
    "``POST``","quagga","bgp","toggle_aspath","$uuid"
    "``POST``","quagga","bgp","toggle_communitylist","$uuid"
    "``POST``","quagga","bgp","toggle_neighbor","$uuid"
    "``POST``","quagga","bgp","toggle_peergroup","$uuid"
    "``POST``","quagga","bgp","toggle_prefixlist","$uuid"
    "``POST``","quagga","bgp","toggle_redistribution","$uuid"
    "``POST``","quagga","bgp","toggle_routemap","$uuid"

    "``<<uses>>``", "", "", "", "*model* `BGP.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/BGP.xml>`__"

.. csv-table:: Resources (DiagnosticsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","quagga","diagnostics","bfdcounters",""
    "``GET``","quagga","diagnostics","bfdneighbors",""
    "``GET``","quagga","diagnostics","bfdsummary",""
    "``GET``","quagga","diagnostics","bgpneighbors",""
    "``GET``","quagga","diagnostics","bgpsummary",""
    "``GET``","quagga","diagnostics","generalrunningconfig",""
    "``GET``","quagga","diagnostics","ospfdatabase",""
    "``GET``","quagga","diagnostics","ospfinterface",""
    "``GET``","quagga","diagnostics","ospfoverview",""
    "``GET``","quagga","diagnostics","ospfv3interface",""
    "``GET``","quagga","diagnostics","ospfv3overview",""
    "``GET``","quagga","diagnostics","search_bgproute4",""
    "``GET``","quagga","diagnostics","search_bgproute6",""
    "``GET``","quagga","diagnostics","search_generalroute4",""
    "``GET``","quagga","diagnostics","search_generalroute6",""
    "``GET``","quagga","diagnostics","search_ospfneighbor",""
    "``GET``","quagga","diagnostics","search_ospfroute",""
    "``GET``","quagga","diagnostics","search_ospfv3database",""
    "``GET``","quagga","diagnostics","search_ospfv3route","$format=json"

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","quagga","general","get",""
    "``POST``","quagga","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/General.xml>`__"

.. csv-table:: Resources (Ospf6settingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","ospf6settings","add_interface",""
    "``POST``","quagga","ospf6settings","add_network",""
    "``POST``","quagga","ospf6settings","add_prefixlist",""
    "``POST``","quagga","ospf6settings","add_redistribution",""
    "``POST``","quagga","ospf6settings","add_routemap",""
    "``POST``","quagga","ospf6settings","del_interface","$uuid"
    "``POST``","quagga","ospf6settings","del_network","$uuid"
    "``POST``","quagga","ospf6settings","del_prefixlist","$uuid"
    "``POST``","quagga","ospf6settings","del_redistribution","$uuid"
    "``POST``","quagga","ospf6settings","del_routemap","$uuid"
    "``GET``","quagga","ospf6settings","get",""
    "``GET``","quagga","ospf6settings","get_interface","$uuid=null"
    "``GET``","quagga","ospf6settings","get_network","$uuid=null"
    "``GET``","quagga","ospf6settings","get_prefixlist","$uuid=null"
    "``GET``","quagga","ospf6settings","get_redistribution","$uuid=null"
    "``GET``","quagga","ospf6settings","get_routemap","$uuid=null"
    "``POST,GET``","quagga","ospf6settings","search_interface",""
    "``POST,GET``","quagga","ospf6settings","search_network",""
    "``POST,GET``","quagga","ospf6settings","search_prefixlist",""
    "``POST,GET``","quagga","ospf6settings","search_redistribution",""
    "``POST,GET``","quagga","ospf6settings","search_routemap",""
    "``POST``","quagga","ospf6settings","set",""
    "``POST``","quagga","ospf6settings","set_interface","$uuid"
    "``POST``","quagga","ospf6settings","set_network","$uuid"
    "``POST``","quagga","ospf6settings","set_prefixlist","$uuid"
    "``POST``","quagga","ospf6settings","set_redistribution","$uuid"
    "``POST``","quagga","ospf6settings","set_routemap","$uuid"
    "``POST``","quagga","ospf6settings","toggle_interface","$uuid"
    "``POST``","quagga","ospf6settings","toggle_network","$uuid"
    "``POST``","quagga","ospf6settings","toggle_prefixlist","$uuid"
    "``POST``","quagga","ospf6settings","toggle_redistribution","$uuid"
    "``POST``","quagga","ospf6settings","toggle_routemap","$uuid"

    "``<<uses>>``", "", "", "", "*model* `OSPF6.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/OSPF6.xml>`__"

.. csv-table:: Resources (OspfsettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","ospfsettings","add_interface",""
    "``POST``","quagga","ospfsettings","add_network",""
    "``POST``","quagga","ospfsettings","add_prefixlist",""
    "``POST``","quagga","ospfsettings","add_redistribution",""
    "``POST``","quagga","ospfsettings","add_routemap",""
    "``POST``","quagga","ospfsettings","del_interface","$uuid"
    "``POST``","quagga","ospfsettings","del_network","$uuid"
    "``POST``","quagga","ospfsettings","del_prefixlist","$uuid"
    "``POST``","quagga","ospfsettings","del_redistribution","$uuid"
    "``POST``","quagga","ospfsettings","del_routemap","$uuid"
    "``GET``","quagga","ospfsettings","get",""
    "``GET``","quagga","ospfsettings","get_interface","$uuid=null"
    "``GET``","quagga","ospfsettings","get_network","$uuid=null"
    "``GET``","quagga","ospfsettings","get_prefixlist","$uuid=null"
    "``GET``","quagga","ospfsettings","get_redistribution","$uuid=null"
    "``GET``","quagga","ospfsettings","get_routemap","$uuid=null"
    "``POST,GET``","quagga","ospfsettings","search_interface",""
    "``POST,GET``","quagga","ospfsettings","search_network",""
    "``POST,GET``","quagga","ospfsettings","search_prefixlist",""
    "``POST,GET``","quagga","ospfsettings","search_redistribution",""
    "``POST,GET``","quagga","ospfsettings","search_routemap",""
    "``POST``","quagga","ospfsettings","set",""
    "``POST``","quagga","ospfsettings","set_interface","$uuid"
    "``POST``","quagga","ospfsettings","set_network","$uuid"
    "``POST``","quagga","ospfsettings","set_prefixlist","$uuid"
    "``POST``","quagga","ospfsettings","set_redistribution","$uuid"
    "``POST``","quagga","ospfsettings","set_routemap","$uuid"
    "``POST``","quagga","ospfsettings","toggle_interface","$uuid"
    "``POST``","quagga","ospfsettings","toggle_network","$uuid"
    "``POST``","quagga","ospfsettings","toggle_prefixlist","$uuid"
    "``POST``","quagga","ospfsettings","toggle_redistribution","$uuid"
    "``POST``","quagga","ospfsettings","toggle_routemap","$uuid"

    "``<<uses>>``", "", "", "", "*model* `OSPF.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/OSPF.xml>`__"

.. csv-table:: Resources (RipController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","quagga","rip","get",""
    "``POST``","quagga","rip","set",""

    "``<<uses>>``", "", "", "", "*model* `RIP.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/RIP.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","service","reconfigure",""
    "``POST``","quagga","service","restart",""
    "``POST``","quagga","service","start",""
    "``GET``","quagga","service","status",""
    "``POST``","quagga","service","stop",""

.. csv-table:: Resources (StaticController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","static","add_route",""
    "``POST``","quagga","static","del_route","$uuid"
    "``GET``","quagga","static","get",""
    "``GET``","quagga","static","get_route","$uuid=null"
    "``POST,GET``","quagga","static","search_route",""
    "``POST``","quagga","static","set",""
    "``POST``","quagga","static","set_route","$uuid"
    "``POST``","quagga","static","toggle_route","$uuid"

    "``<<uses>>``", "", "", "", "*model* `STATICd.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/STATICd.xml>`__"
