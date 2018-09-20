wireguard
~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","wireguard","general","get",""
   "``POST``","wireguard","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","wireguard","service","restart",""
   "``POST``","wireguard","service","start",""
   "``POST``","wireguard","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","wireguard","client","addclient",""
   "``POST``","wireguard","client","delclient","$uuid"
   "``GET``","wireguard","client","getclient","$uuid"
   "``GET``","wireguard","client","searchclient",""
   "``POST``","wireguard","client","setclient","$uuid"
   "``POST``","wireguard","client","toggleclient","$uuid"
   "``POST``","wireguard","user","addserver",""
   "``POST``","wireguard","user","delserver","$uuid"
   "``GET``","wireguard","user","getserver","$uuid"
   "``GET``","wireguard","user","searchserver",""
   "``POST``","wireguard","user","setserver","$uuid"
   "``POST``","wireguard","user","toggleserver","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","wireguard","service","showconf",""
   "","wireguard","service","showhandshake",""
