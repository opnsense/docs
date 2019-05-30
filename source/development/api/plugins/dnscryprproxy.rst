dnscryptproxy
~~~~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","dnscryptproxy","general","get",""
   "``POST``","dnscryptproxy","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","dnscryptproxy","service","reconfigure",""
   "``POST``","dnscryptproxy","service","restart",""
   "``POST``","dnscryptproxy","service","start",""
   "``GET``","dnscryptproxy","service","status",""
   "``POST``","dnscryptproxy","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","dnscryptproxy","cloak","addcloak",""
   "``POST``","dnscryptproxy","cloak","delcloak","$uuid"
   "``GET``","dnscryptproxy","cloak","getcloak","$uuid"
   "``GET``","dnscryptproxy","cloak","searchcloak",""
   "``POST``","dnscryptproxy","cloak","setcloak","$uuid"
   "``POST``","dnscryptproxy","cloak","togglecloak","$uuid"
   "``POST``","dnscryptproxy","forward","addforward",""
   "``POST``","dnscryptproxy","forward","delforward","$uuid"
   "``GET``","dnscryptproxy","forward","getforward","$uuid"
   "``GET``","dnscryptproxy","forward","searchforward",""
   "``POST``","dnscryptproxy","forward","setforward","$uuid"
   "``POST``","dnscryptproxy","forward","toggleforward","$uuid"
   "``POST``","dnscryptproxy","server","addserver",""
   "``POST``","dnscryptproxy","server","delserver","$uuid"
   "``GET``","dnscryptproxy","server","getserver","$uuid"
   "``GET``","dnscryptproxy","server","searchserver",""
   "``POST``","dnscryptproxy","server","setserver","$uuid"
   "``POST``","dnscryptproxy","server","toggleserver","$uuid"
   "``POST``","dnscryptproxy","whilelist","addwhilelist",""
   "``POST``","dnscryptproxy","whilelist","delwhilelist","$uuid"
   "``GET``","dnscryptproxy","whilelist","getwhilelist","$uuid"
   "``GET``","dnscryptproxy","whilelist","searchwhilelist",""
   "``POST``","dnscryptproxy","whilelist","setwhilelist","$uuid"
   "``POST``","dnscryptproxy","whilelist","togglewhilelist","$uuid"
