haproxy
~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","haproxy","settings","get",""
   "``POST``","haproxy","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","haproxy","service","configtest",""
   "``POST``","haproxy","service","reconfigure",""
   "``POST``","haproxy","service","restart",""
   "``POST``","haproxy","service","start",""
   "``GET``","haproxy","service","status",""
   "``POST``","haproxy","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","haproxy","settings","addacl",""
   "``POST``","haproxy","settings","addaction",""
   "``POST``","haproxy","settings","addbackend",""
   "``POST``","haproxy","settings","adderrorfile",""
   "``POST``","haproxy","settings","addfrontend",""
   "``POST``","haproxy","settings","addhealthcheck",""
   "``POST``","haproxy","settings","addlua",""
   "``POST``","haproxy","settings","addserver",""
   "``POST``","haproxy","settings","delacl","$uuid"
   "``POST``","haproxy","settings","delaction","$uuid"
   "``POST``","haproxy","settings","delbackend","$uuid"
   "``POST``","haproxy","settings","delerrorfile","$uuid"
   "``POST``","haproxy","settings","delfrontend","$uuid"
   "``POST``","haproxy","settings","delhealthcheck","$uuid"
   "``POST``","haproxy","settings","dellua","$uuid"
   "``POST``","haproxy","settings","delserver","$uuid"
   "``GET``","haproxy","settings","getacl","$uuid"
   "``GET``","haproxy","settings","getaction","$uuid"
   "``GET``","haproxy","settings","getbackend","$uuid"
   "``GET``","haproxy","settings","geterrorfile","$uuid"
   "``GET``","haproxy","settings","getfrontend","$uuid"
   "``GET``","haproxy","settings","gethealthcheck","$uuid"
   "``GET``","haproxy","settings","getlua","$uuid"
   "``GET``","haproxy","settings","getserver","$uuid"
   "``GET``","haproxy","settings","searchacls",""
   "``GET``","haproxy","settings","searchactions",""
   "``GET``","haproxy","settings","searchbackends",""
   "``GET``","haproxy","settings","searcherrorfiles",""
   "``GET``","haproxy","settings","searchfrontends",""
   "``GET``","haproxy","settings","searchhealthchecks",""
   "``GET``","haproxy","settings","searchluas",""
   "``GET``","haproxy","settings","searchservers",""
   "``POST``","haproxy","settings","setacl","$uuid"
   "``POST``","haproxy","settings","setaction","$uuid"
   "``POST``","haproxy","settings","setbackend","$uuid"
   "``POST``","haproxy","settings","seterrorfile","$uuid"
   "``POST``","haproxy","settings","setfrontend","$uuid"
   "``POST``","haproxy","settings","sethealthcheck","$uuid"
   "``POST``","haproxy","settings","setlua","$uuid"
   "``POST``","haproxy","settings","setserver","$uuid"
   "``POST``","haproxy","settings","togglebackend","$uuid/$enabled"
   "``POST``","haproxy","settings","togglefrontend","$uuid/$enabled"
   "``POST``","haproxy","settings","togglelua","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","haproxy","statistics","counters",""
   "","haproxy","statistics","info",""
   "","haproxy","statistics","tables",""
