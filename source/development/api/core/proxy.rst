Proxy
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","proxy","settings","get",""
   "``POST``","proxy","settings","set",""
   "``GET``","proxy","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","proxy","service","reconfigure",""
   "``POST``","proxy","service","restart",""
   "``POST``","proxy","service","start",""
   "``GET``","proxy","service","status",""
   "``POST``","proxy","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","proxy","settings","addremoteblacklist",""
   "``POST``","proxy","settings","delremoteblacklist","$uuid"
   "``GET``","proxy","settings","getremoteblacklist","$uuid"
   "``GET``","proxy","settings","searchremoteblacklists",""
   "``POST``","proxy","settings","setremoteblacklist","$uuid"
   "``POST``","proxy","settings","toggleremoteblacklist","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","proxy","service","downloadacls",""
   "","proxy","service","fetchacls",""
   "","proxy","settings","fetchRBCron",""
