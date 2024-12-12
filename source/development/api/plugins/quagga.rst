Quagga
~~~~~~

.. csv-table:: Resources (BfdController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","bfd","addNeighbor",""
    "``POST``","quagga","bfd","delNeighbor","$uuid"
    "``GET``","quagga","bfd","get",""
    "``GET``","quagga","bfd","getNeighbor","$uuid=null"
    "``*``","quagga","bfd","searchNeighbor",""
    "``POST``","quagga","bfd","set",""
    "``POST``","quagga","bfd","setNeighbor","$uuid"
    "``POST``","quagga","bfd","toggleNeighbor","$uuid"

    "``<<uses>>``", "", "", "", "*model* `BFD.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/BFD.xml>`__"

.. csv-table:: Resources (BgpController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","bgp","addAspath",""
    "``POST``","quagga","bgp","addCommunitylist",""
    "``POST``","quagga","bgp","addNeighbor",""
    "``POST``","quagga","bgp","addPeergroup",""
    "``POST``","quagga","bgp","addPrefixlist",""
    "``POST``","quagga","bgp","addRoutemap",""
    "``POST``","quagga","bgp","delAspath","$uuid"
    "``POST``","quagga","bgp","delCommunitylist","$uuid"
    "``POST``","quagga","bgp","delNeighbor","$uuid"
    "``POST``","quagga","bgp","delPeergroup","$uuid"
    "``POST``","quagga","bgp","delPrefixlist","$uuid"
    "``POST``","quagga","bgp","delRoutemap","$uuid"
    "``GET``","quagga","bgp","get",""
    "``GET``","quagga","bgp","getAspath","$uuid=null"
    "``GET``","quagga","bgp","getCommunitylist","$uuid=null"
    "``GET``","quagga","bgp","getNeighbor","$uuid=null"
    "``GET``","quagga","bgp","getPeergroup","$uuid=null"
    "``GET``","quagga","bgp","getPrefixlist","$uuid=null"
    "``GET``","quagga","bgp","getRoutemap","$uuid=null"
    "``*``","quagga","bgp","searchAspath",""
    "``*``","quagga","bgp","searchCommunitylist",""
    "``*``","quagga","bgp","searchNeighbor",""
    "``*``","quagga","bgp","searchPeergroup",""
    "``*``","quagga","bgp","searchPrefixlist",""
    "``*``","quagga","bgp","searchRoutemap",""
    "``POST``","quagga","bgp","set",""
    "``POST``","quagga","bgp","setAspath","$uuid"
    "``POST``","quagga","bgp","setCommunitylist","$uuid"
    "``POST``","quagga","bgp","setNeighbor","$uuid"
    "``POST``","quagga","bgp","setPeergroup","$uuid"
    "``POST``","quagga","bgp","setPrefixlist","$uuid"
    "``POST``","quagga","bgp","setRoutemap","$uuid"
    "``POST``","quagga","bgp","toggleAspath","$uuid"
    "``POST``","quagga","bgp","toggleCommunitylist","$uuid"
    "``POST``","quagga","bgp","toggleNeighbor","$uuid"
    "``POST``","quagga","bgp","togglePeergroup","$uuid"
    "``POST``","quagga","bgp","togglePrefixlist","$uuid"
    "``POST``","quagga","bgp","toggleRoutemap","$uuid"

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
    "``GET``","quagga","diagnostics","searchBgproute4",""
    "``GET``","quagga","diagnostics","searchBgproute6",""
    "``GET``","quagga","diagnostics","searchGeneralroute4",""
    "``GET``","quagga","diagnostics","searchGeneralroute6",""
    "``GET``","quagga","diagnostics","searchOspfneighbor",""
    "``GET``","quagga","diagnostics","searchOspfroute",""
    "``GET``","quagga","diagnostics","searchOspfv3database",""
    "``GET``","quagga","diagnostics","searchOspfv3route","$format=""json"""

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","quagga","general","get",""
    "``POST``","quagga","general","set",""

.. csv-table:: Resources (Ospf6settingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","ospf6settings","addInterface",""
    "``POST``","quagga","ospf6settings","addNetwork",""
    "``POST``","quagga","ospf6settings","addPrefixlist",""
    "``POST``","quagga","ospf6settings","addRoutemap",""
    "``POST``","quagga","ospf6settings","delInterface","$uuid"
    "``POST``","quagga","ospf6settings","delNetwork","$uuid"
    "``POST``","quagga","ospf6settings","delPrefixlist","$uuid"
    "``POST``","quagga","ospf6settings","delRoutemap","$uuid"
    "``GET``","quagga","ospf6settings","get",""
    "``GET``","quagga","ospf6settings","getInterface","$uuid=null"
    "``GET``","quagga","ospf6settings","getNetwork","$uuid=null"
    "``GET``","quagga","ospf6settings","getPrefixlist","$uuid=null"
    "``GET``","quagga","ospf6settings","getRoutemap","$uuid=null"
    "``*``","quagga","ospf6settings","searchInterface",""
    "``*``","quagga","ospf6settings","searchNetwork",""
    "``*``","quagga","ospf6settings","searchPrefixlist",""
    "``*``","quagga","ospf6settings","searchRoutemap",""
    "``POST``","quagga","ospf6settings","set",""
    "``POST``","quagga","ospf6settings","setInterface","$uuid"
    "``POST``","quagga","ospf6settings","setNetwork","$uuid"
    "``POST``","quagga","ospf6settings","setPrefixlist","$uuid"
    "``POST``","quagga","ospf6settings","setRoutemap","$uuid"
    "``POST``","quagga","ospf6settings","toggleInterface","$uuid"
    "``POST``","quagga","ospf6settings","toggleNetwork","$uuid"
    "``POST``","quagga","ospf6settings","togglePrefixlist","$uuid"
    "``POST``","quagga","ospf6settings","toggleRoutemap","$uuid"

    "``<<uses>>``", "", "", "", "*model* `OSPF6.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/OSPF6.xml>`__"

.. csv-table:: Resources (OspfsettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","ospfsettings","addInterface",""
    "``POST``","quagga","ospfsettings","addNetwork",""
    "``POST``","quagga","ospfsettings","addPrefixlist",""
    "``POST``","quagga","ospfsettings","addRoutemap",""
    "``POST``","quagga","ospfsettings","delInterface","$uuid"
    "``POST``","quagga","ospfsettings","delNetwork","$uuid"
    "``POST``","quagga","ospfsettings","delPrefixlist","$uuid"
    "``POST``","quagga","ospfsettings","delRoutemap","$uuid"
    "``GET``","quagga","ospfsettings","get",""
    "``GET``","quagga","ospfsettings","getInterface","$uuid=null"
    "``GET``","quagga","ospfsettings","getNetwork","$uuid=null"
    "``GET``","quagga","ospfsettings","getPrefixlist","$uuid=null"
    "``GET``","quagga","ospfsettings","getRoutemap","$uuid=null"
    "``*``","quagga","ospfsettings","searchInterface",""
    "``*``","quagga","ospfsettings","searchNetwork",""
    "``*``","quagga","ospfsettings","searchPrefixlist",""
    "``*``","quagga","ospfsettings","searchRoutemap",""
    "``POST``","quagga","ospfsettings","set",""
    "``POST``","quagga","ospfsettings","setInterface","$uuid"
    "``POST``","quagga","ospfsettings","setNetwork","$uuid"
    "``POST``","quagga","ospfsettings","setPrefixlist","$uuid"
    "``POST``","quagga","ospfsettings","setRoutemap","$uuid"
    "``POST``","quagga","ospfsettings","toggleInterface","$uuid"
    "``POST``","quagga","ospfsettings","toggleNetwork","$uuid"
    "``POST``","quagga","ospfsettings","togglePrefixlist","$uuid"
    "``POST``","quagga","ospfsettings","toggleRoutemap","$uuid"

    "``<<uses>>``", "", "", "", "*model* `OSPF.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/OSPF.xml>`__"

.. csv-table:: Service (RipController.php)
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

    "``POST``","quagga","static","addRoute",""
    "``POST``","quagga","static","delRoute","$uuid"
    "``GET``","quagga","static","get",""
    "``GET``","quagga","static","getRoute","$uuid=null"
    "``*``","quagga","static","searchRoute",""
    "``POST``","quagga","static","set",""
    "``POST``","quagga","static","setRoute","$uuid"
    "``POST``","quagga","static","toggleRoute","$uuid"

    "``<<uses>>``", "", "", "", "*model* `STATICd.xml <https://github.com/opnsense/plugins/blob/master/net/frr/src/opnsense/mvc/app/models/OPNsense/Quagga/STATICd.xml>`__"
