Wireguard
~~~~~~~~~

.. csv-table:: Resources (ClientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","client","addClient",""
    "``POST``","wireguard","client","delClient","$uuid"
    "``GET``","wireguard","client","get",""
    "``GET``","wireguard","client","getClient","$uuid=null"
    "``*``","wireguard","client","searchClient",""
    "``POST``","wireguard","client","set",""
    "``POST``","wireguard","client","setClient","$uuid"
    "``POST``","wireguard","client","toggleClient","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Client.xml <https://github.com/opnsense/plugins/blob/master/net/wireguard-go/src/opnsense/mvc/app/models/OPNsense/Wireguard/Client.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wireguard","general","get",""
    "``GET``","wireguard","general","getStatus",""
    "``POST``","wireguard","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/wireguard-go/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml>`__"

.. csv-table:: Resources (ServerController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","server","addServer","$uuid=null"
    "``POST``","wireguard","server","delServer","$uuid"
    "``GET``","wireguard","server","get",""
    "``GET``","wireguard","server","getServer","$uuid=null"
    "``*``","wireguard","server","searchServer",""
    "``POST``","wireguard","server","set",""
    "``POST``","wireguard","server","setServer","$uuid=null"
    "``POST``","wireguard","server","toggleServer","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/plugins/blob/master/net/wireguard-go/src/opnsense/mvc/app/models/OPNsense/Wireguard/Server.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","service","reconfigure",""
    "``POST``","wireguard","service","restart",""
    "``GET``","wireguard","service","showconf",""
    "``GET``","wireguard","service","showhandshake",""
    "``POST``","wireguard","service","start",""
    "``GET``","wireguard","service","status",""
    "``POST``","wireguard","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/wireguard-go/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml>`__"

.. csv-table:: Resources (ClientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wireguard","client","addClient",""
    "``POST``","wireguard","client","delClient","$uuid"
    "``GET``","wireguard","client","get",""
    "``GET``","wireguard","client","getClient","$uuid=null"
    "``*``","wireguard","client","searchClient",""
    "``POST``","wireguard","client","set",""
    "``POST``","wireguard","client","setClient","$uuid"
    "``POST``","wireguard","client","toggleClient","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Client.xml <https://github.com/opnsense/plugins/blob/master/net/wireguard/src/opnsense/mvc/app/models/OPNsense/Wireguard/Client.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wireguard","general","get",""
    "``GET``","wireguard","general","getStatus",""
    "``POST``","wireguard","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/wireguard/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml>`__"

.. csv-table:: Resources (ServerController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","server","addServer","$uuid=null"
    "``POST``","wireguard","server","delServer","$uuid"
    "``GET``","wireguard","server","get",""
    "``GET``","wireguard","server","getServer","$uuid=null"
    "``GET``","wireguard","server","keyPair",""
    "``*``","wireguard","server","searchServer",""
    "``POST``","wireguard","server","set",""
    "``POST``","wireguard","server","setServer","$uuid=null"
    "``POST``","wireguard","server","toggleServer","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/plugins/blob/master/net/wireguard/src/opnsense/mvc/app/models/OPNsense/Wireguard/Server.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","service","reconfigure",""
    "``POST``","wireguard","service","reconfigure",""
    "``POST``","wireguard","service","restart",""
    "``GET``","wireguard","service","show",""
    "``GET``","wireguard","service","showconf",""
    "``GET``","wireguard","service","showhandshake",""
    "``POST``","wireguard","service","start",""
    "``GET``","wireguard","service","status",""
    "``POST``","wireguard","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/wireguard/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml>`__"
