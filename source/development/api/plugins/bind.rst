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

    "``<<uses>>``", "", "", "", "*model* `Acl.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Acl.xml>`__"

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","domain","addDomain","$uuid=null"
    "``POST``","bind","domain","delDomain","$uuid"
    "``GET``","bind","domain","getDomain","$uuid=null"
    "``*``","bind","domain","searchDomain",""
    "``POST``","bind","domain","setDomain","$uuid=null"
    "``POST``","bind","domain","toggleDomain","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Domain.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Domain.xml>`__"

.. csv-table:: Resources (RecordController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","record","addRecord",""
    "``POST``","bind","record","delRecord","$uuid"
    "``GET``","bind","record","getRecord","$uuid=null"
    "``*``","bind","record","searchRecord",""
    "``POST``","bind","record","setRecord","$uuid=null"
    "``POST``","bind","record","toggleRecord","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Record.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Record.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","bind","service","dnsbl",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/General.xml>`__"
