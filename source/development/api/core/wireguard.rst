Wireguard
~~~~~~~~~

.. csv-table:: Resources (ClientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wireguard","client","addClient",""
    "``POST``","wireguard","client","addClientBuilder",""
    "``POST``","wireguard","client","delClient","$uuid"
    "``GET``","wireguard","client","get",""
    "``GET``","wireguard","client","getClient","$uuid=null"
    "``GET``","wireguard","client","getClientBuilder",""
    "``GET``","wireguard","client","getServerInfo","$uuid=null"
    "``GET``","wireguard","client","listServers",""
    "``GET``","wireguard","client","psk",""
    "``*``","wireguard","client","searchClient",""
    "``POST``","wireguard","client","set",""
    "``POST``","wireguard","client","setClient","$uuid"
    "``POST``","wireguard","client","toggleClient","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Client.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Wireguard/Client.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wireguard","general","get",""
    "``POST``","wireguard","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml>`__"

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

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Wireguard/Server.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","service","reconfigure",""
    "``POST``","wireguard","service","reconfigure",""
    "``POST``","wireguard","service","restart",""
    "``GET``","wireguard","service","show",""
    "``POST``","wireguard","service","start",""
    "``GET``","wireguard","service","status",""
    "``POST``","wireguard","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml>`__"
