postfix
~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","postfix","antispam","get",""
   "``POST``","postfix","antispam","set",""
   "``GET``","postfix","general","get",""
   "``POST``","postfix","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","postfix","service","reconfigure",""
   "``POST``","postfix","service","restart",""
   "``POST``","postfix","service","start",""
   "``GET``","postfix","service","status",""
   "``POST``","postfix","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","postfix","domain","adddomain",""
   "``POST``","postfix","domain","deldomain","$uuid"
   "``GET``","postfix","domain","getdomain","$uuid"
   "``GET``","postfix","domain","searchdomain",""
   "``POST``","postfix","domain","setdomain","$uuid"
   "``POST``","postfix","domain","toggledomain","$uuid"
   "``POST``","postfix","recipient","addrecipient",""
   "``POST``","postfix","recipient","delrecipient","$uuid"
   "``GET``","postfix","recipient","getrecipient","$uuid"
   "``GET``","postfix","recipient","searchrecipient",""
   "``POST``","postfix","recipient","setrecipient","$uuid"
   "``POST``","postfix","recipient","togglerecipient","$uuid"
   "``POST``","postfix","sender","addsender",""
   "``POST``","postfix","sender","delsender","$uuid"
   "``GET``","postfix","sender","getsender","$uuid"
   "``GET``","postfix","sender","searchsender",""
   "``POST``","postfix","sender","setsender","$uuid"
   "``POST``","postfix","sender","togglesender","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","postfix","service","checkrspamd",""
