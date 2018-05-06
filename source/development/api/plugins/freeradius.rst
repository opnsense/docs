freeradius
~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","freeradius","eap","get",""
   "``POST``","freeradius","eap","set",""
   "``GET``","freeradius","general","get",""
   "``POST``","freeradius","general","set",""
   "``GET``","freeradius","ldap","get",""
   "``POST``","freeradius","ldap","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","freeradius","service","reconfigure",""
   "``POST``","freeradius","service","restart",""
   "``POST``","freeradius","service","start",""
   "``GET``","freeradius","service","status",""
   "``POST``","freeradius","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","freeradius","client","addclient",""
   "``POST``","freeradius","client","delclient","$uuid"
   "``GET``","freeradius","client","getclient","$uuid"
   "``GET``","freeradius","client","searchclient",""
   "``POST``","freeradius","client","setclient","$uuid"
   "``POST``","freeradius","client","toggleclient","$uuid"
   "``POST``","freeradius","user","adduser",""
   "``POST``","freeradius","user","deluser","$uuid"
   "``GET``","freeradius","user","getuser","$uuid"
   "``GET``","freeradius","user","searchuser",""
   "``POST``","freeradius","user","setuser","$uuid"
   "``POST``","freeradius","user","toggleuser","$uuid"
