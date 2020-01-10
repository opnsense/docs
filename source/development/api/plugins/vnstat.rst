vnstat
~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","vnstat","general","get",""
   "``POST``","vnstat","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","vnstat","service","restart",""
   "``POST``","vnstat","service","start",""
   "``POST``","vnstat","service","status",""
   "``POST``","vnstat","service","stop",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","vnstat","service","hourly",""
   "","vnstat","service","daily",""
   "","vnstat","service","monthly",""
