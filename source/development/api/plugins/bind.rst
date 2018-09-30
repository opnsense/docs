bind
~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","bind","general","get",""
   "``POST``","bind","general","set",""
   "``GET``","bind","dnsbl","get",""
   "``POST``","bind","dnsbl","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","bind","service","restart",""
   "``POST``","bind","service","start",""
   "``POST``","bind","service","status",""
   "``POST``","bind","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","bind","acl","addacl",""
   "``POST``","bind","acl","delacl","$uuid"
   "``GET``","bind","acl","getacl","$uuid"
   "``GET``","bind","acl","searchacl",""
   "``POST``","bind","acl","setacl","$uuid"
   "``POST``","bind","acl","toggleacl","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","bind","service","dnsbl",""
