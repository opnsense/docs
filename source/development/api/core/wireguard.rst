Wireguard
~~~~~~~~~

.. csv-table:: Resources (ClientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wireguard","client","add_client",""
    "``POST``","wireguard","client","add_client_builder",""
    "``POST``","wireguard","client","del_client","$uuid"
    "``GET``","wireguard","client","get",""
    "``GET``","wireguard","client","get_client","$uuid=null"
    "``GET``","wireguard","client","get_client_builder",""
    "``GET``","wireguard","client","get_server_info","$uuid=null"
    "``GET``","wireguard","client","list_servers",""
    "``GET``","wireguard","client","psk",""
    "``POST,GET``","wireguard","client","search_client",""
    "``POST``","wireguard","client","set",""
    "``POST``","wireguard","client","set_client","$uuid"
    "``POST``","wireguard","client","toggle_client","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Client.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Wireguard/Client.xml>`__"

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wireguard","general","get",""
    "``POST``","wireguard","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Wireguard/General.xml>`__"

.. csv-table:: Resources (ServerController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","server","add_server","$uuid=null"
    "``POST``","wireguard","server","del_server","$uuid"
    "``GET``","wireguard","server","get",""
    "``GET``","wireguard","server","get_server","$uuid=null"
    "``GET``","wireguard","server","key_pair",""
    "``POST,GET``","wireguard","server","search_server",""
    "``POST``","wireguard","server","set",""
    "``POST``","wireguard","server","set_server","$uuid=null"
    "``POST``","wireguard","server","toggle_server","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Wireguard/Server.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","service","reconfigure",""
    "``POST``","wireguard","service","restart",""
    "``GET``","wireguard","service","show",""
    "``POST``","wireguard","service","start",""
    "``GET``","wireguard","service","status",""
    "``POST``","wireguard","service","stop",""
