netsnmp
~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","netsnmp","general","get",""
   "``POST``","netsnmp","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","netsnmp","service","restart",""
   "``POST``","netsnmp","service","start",""
   "``POST``","netsnmp","service","status",""
   "``POST``","netsnmp","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","netsnmp","user","adduser",""
   "``POST``","netsnmp","user","deluser","$uuid"
   "``GET``","netsnmp","user","getuser","$uuid"
   "``GET``","netsnmp","user","searchuser",""
   "``POST``","netsnmp","user","setuser","$uuid"
   "``POST``","netsnmp","user","toggleuser","$uuid"
