Wireguard
~~~~~~~~~

.. csv-table:: Resources (ClientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","client","addClient",""
    "``POST``","wireguard","client","delClient","$uuid"
    "``GET``","wireguard","client","getClient","$uuid=null"
    "``*``","wireguard","client","searchClient",""
    "``POST``","wireguard","client","setClient","$uuid"
    "``POST``","wireguard","client","toggleClient","$uuid"

.. csv-table:: Resources (ServerController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wireguard","server","addServer","$uuid=null"
    "``POST``","wireguard","server","delServer","$uuid"
    "``GET``","wireguard","server","getServer","$uuid=null"
    "``*``","wireguard","server","searchServer",""
    "``POST``","wireguard","server","setServer","$uuid=null"
    "``POST``","wireguard","server","toggleServer","$uuid"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wireguard","service","showconf",""
    "``GET``","wireguard","service","showhandshake",""
