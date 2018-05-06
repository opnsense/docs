tor
~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","tor","general","get",""
   "``POST``","tor","general","set",""
   "``GET``","tor","relay","get",""
   "``POST``","tor","relay","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","tor","service","reconfigure",""
   "``POST``","tor","service","restart",""
   "``POST``","tor","service","start",""
   "``GET``","tor","service","status",""
   "``POST``","tor","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","tor","exitacl","addacl",""
   "``POST``","tor","exitacl","delacl","$uuid"
   "``GET``","tor","exitacl","getacl","$uuid"
   "``GET``","tor","exitacl","searchacl",""
   "``POST``","tor","exitacl","setacl","$uuid"
   "``POST``","tor","exitacl","toggleacl","$uuid"
   "``POST``","tor","general","addhidservauth",""
   "``POST``","tor","general","delhidservauth","$uuid"
   "``GET``","tor","general","gethidservauth","$uuid"
   "``GET``","tor","general","searchhidservauth",""
   "``POST``","tor","general","sethidservauth","$uuid"
   "``POST``","tor","general","togglehidservauth","$uuid"
   "``POST``","tor","hiddenservice","addservice",""
   "``POST``","tor","hiddenservice","delservice","$uuid"
   "``GET``","tor","hiddenservice","getservice","$uuid"
   "``GET``","tor","hiddenservice","searchservice",""
   "``POST``","tor","hiddenservice","setservice","$uuid"
   "``POST``","tor","hiddenservice","toggleservice","$uuid"
   "``POST``","tor","hiddenserviceacl","addacl",""
   "``POST``","tor","hiddenserviceacl","delacl","$uuid"
   "``GET``","tor","hiddenserviceacl","getacl","$uuid"
   "``GET``","tor","hiddenserviceacl","searchacl",""
   "``POST``","tor","hiddenserviceacl","setacl","$uuid"
   "``POST``","tor","hiddenserviceacl","toggleacl","$uuid"
   "``POST``","tor","socksacl","addacl",""
   "``POST``","tor","socksacl","delacl","$uuid"
   "``GET``","tor","socksacl","getacl","$uuid"
   "``GET``","tor","socksacl","searchacl",""
   "``POST``","tor","socksacl","setacl","$uuid"
   "``POST``","tor","socksacl","toggleacl","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","tor","service","circuits",""
   "","tor","service","get",""
   "","tor","service","streams",""
