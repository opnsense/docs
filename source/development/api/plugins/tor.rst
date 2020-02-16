Tor
~~~

.. csv-table:: Resources (ExitaclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","exitacl","addacl",""
    "``POST``","tor","exitacl","delacl","$uuid"
    "``GET``","tor","exitacl","getacl","$uuid=null"
    "``*``","tor","exitacl","searchacl",""
    "``POST``","tor","exitacl","setacl","$uuid"
    "``POST``","tor","exitacl","toggleacl","$uuid"

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","general","addhidservauth",""
    "``POST``","tor","general","delhidservauth","$uuid"
    "``GET``","tor","general","gethidservauth","$uuid=null"
    "``*``","tor","general","searchhidservauth",""
    "``POST``","tor","general","set",""
    "``POST``","tor","general","sethidservauth","$uuid"
    "``POST``","tor","general","togglehidservauth","$uuid"

.. csv-table:: Service (HiddenserviceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","hiddenservice","addservice",""
    "``POST``","tor","hiddenservice","delservice","$uuid"
    "``GET``","tor","hiddenservice","getservice","$uuid=null"
    "``*``","tor","hiddenservice","searchservice",""
    "``POST``","tor","hiddenservice","setservice","$uuid"
    "``POST``","tor","hiddenservice","toggleservice","$uuid"

.. csv-table:: Service (HiddenserviceaclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","hiddenserviceacl","addacl",""
    "``POST``","tor","hiddenserviceacl","delacl","$uuid"
    "``GET``","tor","hiddenserviceacl","getacl","$uuid=null"
    "``*``","tor","hiddenserviceacl","searchacl",""
    "``POST``","tor","hiddenserviceacl","setacl","$uuid"
    "``POST``","tor","hiddenserviceacl","toggleacl","$uuid"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","tor","service","circuits",""
    "``GET``","tor","service","get_hidden_services",""
    "``POST``","tor","service","reconfigure",""
    "``POST``","tor","service","restart",""
    "``POST``","tor","service","start",""
    "``GET``","tor","service","status",""
    "``POST``","tor","service","stop",""
    "``GET``","tor","service","streams",""

.. csv-table:: Resources (SocksaclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","socksacl","addacl",""
    "``POST``","tor","socksacl","delacl","$uuid"
    "``GET``","tor","socksacl","getacl","$uuid=null"
    "``*``","tor","socksacl","searchacl",""
    "``POST``","tor","socksacl","setacl","$uuid"
    "``POST``","tor","socksacl","toggleacl","$uuid"

