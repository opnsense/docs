monit
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","monit","settings","get","general"
   "``POST``","monit","settings","set","general"

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","monit","service","configtest",""
   "``POST``","monit","service","reconfigure",""
   "``POST``","monit","service","restart",""
   "``POST``","monit","service","start",""
   "``GET``","monit","service","status",""
   "``POST``","monit","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","monit","settings","add","test"
   "``POST``","monit","settings","add","service"
   "``POST``","monit","settings","add","alert"
   "``POST``","monit","settings","del","test/$uuid"
   "``POST``","monit","settings","del","service/$uuid"
   "``POST``","monit","settings","del","alert/$uuid"
   "``GET``","monit","settings","get","test/$uuid"
   "``GET``","monit","settings","get","service/$uuid"
   "``GET``","monit","settings","get","alert/$uuid"
   "``GET``","monit","settings","search","test"
   "``GET``","monit","settings","search","alert"
   "``GET``","monit","settings","search","service"
   "``POST``","monit","settings","set","service/$uuid"
   "``POST``","monit","settings","set","test/$uuid"
   "``POST``","monit","settings","set","alert/$uuid"
   "``POST``","monit","settings","toggle","alert/$uuid"
   "``POST``","monit","settings","toggle","service/$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","monit","settings","notification",""
   "","monit","status","get","html"
