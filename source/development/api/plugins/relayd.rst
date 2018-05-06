relayd
~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","relayd","settings","get","general"

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","relayd","service","configtest",""
   "``POST``","relayd","service","reconfigure",""
   "``POST``","relayd","service","restart",""
   "``POST``","relayd","service","start",""
   "``GET``","relayd","service","status",""
   "``POST``","relayd","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","relayd","settings","del","tablecheck/$uuid"
   "``POST``","relayd","settings","del","protocol/$uuid"
   "``POST``","relayd","settings","del","virtualserver/$uuid"
   "``POST``","relayd","settings","del","table/$uuid"
   "``POST``","relayd","settings","del","host/$uuid"
   "``GET``","relayd","settings","get","host/$uuid"
   "``GET``","relayd","settings","get","tablecheck/$uuid"
   "``GET``","relayd","settings","get","virtualserver/$uuid"
   "``GET``","relayd","settings","get","table/$uuid"
   "``GET``","relayd","settings","get","protocol/$uuid"
   "``GET``","relayd","settings","search","host/"
   "``GET``","relayd","settings","search","virtualserver/"
   "``GET``","relayd","settings","search","protocol/"
   "``GET``","relayd","settings","search","tablecheck/"
   "``GET``","relayd","settings","search","table/"
   "``POST``","relayd","settings","set","virtualserver/$uuid"
   "``POST``","relayd","settings","set","host/$uuid"
   "``POST``","relayd","settings","set","table/$uuid"
   "``POST``","relayd","settings","set","protocol/$uuid"
   "``POST``","relayd","settings","set","tablecheck/$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","relayd","status","sum",""
   "","relayd","status","toggle",""
