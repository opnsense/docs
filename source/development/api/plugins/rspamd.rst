rspamd
~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","rspamd","settings","get",""
   "``POST``","rspamd","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","rspamd","service","reconfigure",""
   "``POST``","rspamd","service","restart",""
   "``POST``","rspamd","service","start",""
   "``GET``","rspamd","service","status",""
   "``POST``","rspamd","service","stop",""
