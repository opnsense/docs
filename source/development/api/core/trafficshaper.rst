TrafficShaper
~~~~~~~~~~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","trafficshaper","service","reconfigure",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","trafficshaper","settings","addpipe",""
   "``POST``","trafficshaper","settings","addqueue",""
   "``POST``","trafficshaper","settings","addrule",""
   "``POST``","trafficshaper","settings","delpipe","$uuid"
   "``POST``","trafficshaper","settings","delqueue","$uuid"
   "``POST``","trafficshaper","settings","delrule","$uuid"
   "``GET``","trafficshaper","settings","getpipe","$uuid"
   "``GET``","trafficshaper","settings","getqueue","$uuid"
   "``GET``","trafficshaper","settings","getrule","$uuid"
   "``GET``","trafficshaper","settings","searchpipes",""
   "``GET``","trafficshaper","settings","searchqueues",""
   "``GET``","trafficshaper","settings","searchrules",""
   "``POST``","trafficshaper","settings","setpipe","$uuid"
   "``POST``","trafficshaper","settings","setqueue","$uuid"
   "``POST``","trafficshaper","settings","setrule","$uuid"
   "``POST``","trafficshaper","settings","togglepipe","$uuid/$enabled"
   "``POST``","trafficshaper","settings","togglequeue","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","trafficshaper","service","flushreload",""
