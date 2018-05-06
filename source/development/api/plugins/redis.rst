redis
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","redis","settings","get",""
   "``GET``","redis","settings","set",""
   "``POST``","redis","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","redis","service","reconfigure",""
   "``POST``","redis","service","restart",""
   "``POST``","redis","service","start",""
   "``GET``","redis","service","status",""
   "``POST``","redis","service","stop",""
