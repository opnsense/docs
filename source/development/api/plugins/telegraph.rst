telegraf
~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","telegraf","general","get",""
   "``POST``","telegraf","general","set",""
   "``GET``","telegraf","input","get",""
   "``POST``","telegraf","input","set",""
   "``GET``","telegraf","output","get",""
   "``POST``","telegraf","output","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","telegraf","service","reconfigure",""
   "``POST``","telegraf","service","restart",""
   "``POST``","telegraf","service","start",""
   "``GET``","telegraf","service","status",""
   "``POST``","telegraf","service","stop",""
