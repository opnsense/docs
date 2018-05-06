acmeclient
~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","acmeclient","settings","get",""
   "``POST``","acmeclient","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","acmeclient","service","configtest",""
   "``POST``","acmeclient","service","reconfigure",""
   "``POST``","acmeclient","service","restart",""
   "``POST``","acmeclient","service","start",""
   "``GET``","acmeclient","service","status",""
   "``POST``","acmeclient","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","acmeclient","accounts","add",""
   "``POST``","acmeclient","accounts","del","$uuid"
   "``GET``","acmeclient","accounts","get","$uuid"
   "``GET``","acmeclient","accounts","search",""
   "``POST``","acmeclient","accounts","set","$uuid"
   "``POST``","acmeclient","accounts","toggle","$uuid/$enabled"
   "``POST``","acmeclient","actions","add",""
   "``POST``","acmeclient","actions","del","$uuid"
   "``GET``","acmeclient","actions","get","$uuid"
   "``GET``","acmeclient","actions","search",""
   "``POST``","acmeclient","actions","set","$uuid"
   "``POST``","acmeclient","actions","toggle","$uuid/$enabled"
   "``POST``","acmeclient","certificates","add",""
   "``POST``","acmeclient","certificates","del","$uuid"
   "``GET``","acmeclient","certificates","get","$uuid"
   "``GET``","acmeclient","certificates","search",""
   "``POST``","acmeclient","certificates","set","$uuid"
   "``POST``","acmeclient","certificates","toggle","$uuid/$enabled"
   "``POST``","acmeclient","validations","add",""
   "``POST``","acmeclient","validations","del","$uuid"
   "``GET``","acmeclient","validations","get","$uuid"
   "``GET``","acmeclient","validations","search",""
   "``POST``","acmeclient","validations","set","$uuid"
   "``POST``","acmeclient","validations","toggle","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","acmeclient","certificates","revoke",""
   "","acmeclient","certificates","sign",""
   "","acmeclient","service","signallcerts",""
   "","acmeclient","settings","fetchCronIntegration",""
   "","acmeclient","settings","fetchHAProxyIntegration",""
