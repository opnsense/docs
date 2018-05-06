siproxd
~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","siproxd","general","get",""
   "``POST``","siproxd","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","siproxd","service","reconfigure",""
   "``POST``","siproxd","service","restart",""
   "``POST``","siproxd","service","start",""
   "``GET``","siproxd","service","status",""
   "``POST``","siproxd","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","siproxd","domain","adddomain",""
   "``POST``","siproxd","domain","deldomain","$uuid"
   "``GET``","siproxd","domain","getdomain","$uuid"
   "``GET``","siproxd","domain","searchdomain",""
   "``POST``","siproxd","domain","setdomain","$uuid"
   "``POST``","siproxd","domain","toggledomain","$uuid"
   "``POST``","siproxd","user","adduser",""
   "``POST``","siproxd","user","deluser","$uuid"
   "``GET``","siproxd","user","getuser","$uuid"
   "``GET``","siproxd","user","searchuser",""
   "``POST``","siproxd","user","setuser","$uuid"
   "``POST``","siproxd","user","toggleuser","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","siproxd","domain","set",""
   "","siproxd","service","showregistrations",""
   "","siproxd","user","set",""
