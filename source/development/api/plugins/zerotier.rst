zerotier
~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","zerotier","settings","get",""
   "``POST``","zerotier","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","zerotier","settings","status",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","zerotier","network","add",""
   "``POST``","zerotier","network","del","$uuid"
   "``GET``","zerotier","network","get","$uuid"
   "``GET``","zerotier","network","search",""
   "``POST``","zerotier","network","set","$uuid"
   "``POST``","zerotier","network","toggle","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","zerotier","network","info",""
