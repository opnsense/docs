Bind
~~~~

.. csv-table:: Resources (AclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","acl","addAcl",""
    "``POST``","bind","acl","delAcl","$uuid"
    "``GET``","bind","acl","getAcl","$uuid=null"
    "``*``","bind","acl","searchAcl",""
    "``POST``","bind","acl","setAcl","$uuid"
    "``POST``","bind","acl","toggleAcl","$uuid"

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","domain","addDomain","$uuid=null"
    "``POST``","bind","domain","delDomain","$uuid"
    "``GET``","bind","domain","getDomain","$uuid=null"
    "``*``","bind","domain","searchDomain",""
    "``POST``","bind","domain","setDomain","$uuid=null"
    "``POST``","bind","domain","toggleDomain","$uuid"

.. csv-table:: Resources (RecordController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","record","addRecord",""
    "``POST``","bind","record","delRecord","$uuid"
    "``GET``","bind","record","getRecord","$uuid=null"
    "``*``","bind","record","searchRecord",""
    "``POST``","bind","record","setRecord","$uuid=null"
    "``POST``","bind","record","toggleRecord","$uuid"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","bind","service","dnsbl",""

