tinc
~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","tinc","service","reconfigure",""
   "``POST``","tinc","service","restart",""
   "``GET``","tinc","service","start",""
   "``POST``","tinc","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","tinc","settings","delhost","$uuid"
   "``POST``","tinc","settings","delnetwork","$uuid"
   "``GET``","tinc","settings","gethost","$uuid"
   "``GET``","tinc","settings","getnetwork","$uuid"
   "``GET``","tinc","settings","searchhost",""
   "``GET``","tinc","settings","searchnetwork",""
   "``POST``","tinc","settings","sethost",""
   "``POST``","tinc","settings","sethost","$uuid"
   "``POST``","tinc","settings","setnetwork",""
   "``POST``","tinc","settings","setnetwork","$uuid"
   "``POST``","tinc","settings","togglehost","$uuid/$enabled"
   "``POST``","tinc","settings","togglenetwork","$uuid/$enabled"
