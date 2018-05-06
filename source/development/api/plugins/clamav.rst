clamav
~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","clamav","general","get",""
   "``POST``","clamav","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","clamav","service","reconfigure",""
   "``POST``","clamav","service","restart",""
   "``POST``","clamav","service","start",""
   "``GET``","clamav","service","status",""
   "``POST``","clamav","service","stop",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","clamav","service","freshclam",""
   "","clamav","service","version",""
