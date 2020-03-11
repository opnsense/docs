Quagga
~~~~~~

.. csv-table:: Resources (BgpController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","bgp","addAspath",""
    "``POST``","quagga","bgp","addNeighbor",""
    "``POST``","quagga","bgp","addPrefixlist",""
    "``POST``","quagga","bgp","addRoutemap",""
    "``POST``","quagga","bgp","delAspath","$uuid"
    "``POST``","quagga","bgp","delNeighbor","$uuid"
    "``POST``","quagga","bgp","delPrefixlist","$uuid"
    "``POST``","quagga","bgp","delRoutemap","$uuid"
    "``GET``","quagga","bgp","getAspath","$uuid=null"
    "``GET``","quagga","bgp","getNeighbor","$uuid=null"
    "``GET``","quagga","bgp","getPrefixlist","$uuid=null"
    "``GET``","quagga","bgp","getRoutemap","$uuid=null"
    "``*``","quagga","bgp","searchAspath",""
    "``*``","quagga","bgp","searchNeighbor",""
    "``*``","quagga","bgp","searchPrefixlist",""
    "``*``","quagga","bgp","searchRoutemap",""
    "``POST``","quagga","bgp","setAspath","$uuid"
    "``POST``","quagga","bgp","setNeighbor","$uuid"
    "``POST``","quagga","bgp","setPrefixlist","$uuid"
    "``POST``","quagga","bgp","setRoutemap","$uuid"
    "``POST``","quagga","bgp","toggleAspath","$uuid"
    "``POST``","quagga","bgp","toggleNeighbor","$uuid"
    "``POST``","quagga","bgp","togglePrefixlist","$uuid"
    "``POST``","quagga","bgp","toggleRoutemap","$uuid"

.. csv-table:: Resources (DiagnosticsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","quagga","diagnostics","generalroutes",""
    "``GET``","quagga","diagnostics","generalroutes6",""
    "``GET``","quagga","diagnostics","log",""
    "``GET``","quagga","diagnostics","ospfdatabase",""
    "``GET``","quagga","diagnostics","ospfinterface",""
    "``GET``","quagga","diagnostics","ospfneighbor",""
    "``GET``","quagga","diagnostics","ospfoverview",""
    "``GET``","quagga","diagnostics","ospfroute",""
    "``GET``","quagga","diagnostics","ospfv3database",""
    "``GET``","quagga","diagnostics","ospfv3interface",""
    "``GET``","quagga","diagnostics","ospfv3neighbor",""
    "``GET``","quagga","diagnostics","ospfv3overview",""
    "``GET``","quagga","diagnostics","ospfv3route",""
    "``GET``","quagga","diagnostics","showipbgp",""
    "``GET``","quagga","diagnostics","showipbgpsummary",""
    "``GET``","quagga","diagnostics","showrunningconfig",""

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","quagga","general","get",""
    "``POST``","quagga","general","set",""

.. csv-table:: Resources (Ospf6settingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","ospf6settings","addInterface",""
    "``POST``","quagga","ospf6settings","delInterface","$uuid"
    "``GET``","quagga","ospf6settings","getInterface","$uuid=null"
    "``*``","quagga","ospf6settings","searchInterface",""
    "``POST``","quagga","ospf6settings","setInterface","$uuid"
    "``POST``","quagga","ospf6settings","toggleInterface","$uuid"

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
    "``GET``","quagga","ospfsettings","getInterface","$uuid=null"
    "``GET``","quagga","ospfsettings","getNetwork","$uuid=null"
    "``GET``","quagga","ospfsettings","getPrefixlist","$uuid=null"
    "``GET``","quagga","ospfsettings","getRoutemap","$uuid=null"
    "``*``","quagga","ospfsettings","searchInterface",""
    "``*``","quagga","ospfsettings","searchNetwork",""
    "``*``","quagga","ospfsettings","searchPrefixlist",""
    "``*``","quagga","ospfsettings","searchRoutemap",""
    "``POST``","quagga","ospfsettings","setInterface","$uuid"
    "``POST``","quagga","ospfsettings","setNetwork","$uuid"
    "``POST``","quagga","ospfsettings","setPrefixlist","$uuid"
    "``POST``","quagga","ospfsettings","setRoutemap","$uuid"
    "``POST``","quagga","ospfsettings","toggleInterface","$uuid"
    "``POST``","quagga","ospfsettings","toggleNetwork","$uuid"
    "``POST``","quagga","ospfsettings","togglePrefixlist","$uuid"
    "``POST``","quagga","ospfsettings","toggleRoutemap","$uuid"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","quagga","service","reconfigure",""
    "``POST``","quagga","service","restart",""
    "``POST``","quagga","service","start",""
    "``GET``","quagga","service","status",""
    "``POST``","quagga","service","stop",""
