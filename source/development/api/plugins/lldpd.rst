lldpd
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","lldpd","general","get",""
   "``POST``","lldpd","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","lldpd","service","reconfigure",""
   "``POST``","lldpd","service","restart",""
   "``POST``","lldpd","service","start",""
   "``GET``","lldpd","service","status",""
   "``POST``","lldpd","service","stop",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","lldpd","service","neighbor",""
