Bind
~~~~

.. csv-table:: Resources (AclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","acl","addAcl",""
    "``POST``","bind","acl","delAcl","$uuid"
    "``GET``","bind","acl","get",""
    "``GET``","bind","acl","getAcl","$uuid=null"
    "``*``","bind","acl","searchAcl",""
    "``POST``","bind","acl","set",""
    "``POST``","bind","acl","setAcl","$uuid"
    "``POST``","bind","acl","toggleAcl","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Acl.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Acl.xml>`__"

.. csv-table:: Service (DnsblController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","bind","dnsbl","get",""
    "``POST``","bind","dnsbl","set",""

    "``<<uses>>``", "", "", "", "*model* `Dnsbl.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Dnsbl.xml>`__"

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","domain","addPrimaryDomain","$uuid=null"
    "``POST``","bind","domain","addSecondaryDomain","$uuid=null"
    "``POST``","bind","domain","delDomain","$uuid"
    "``GET``","bind","domain","get",""
    "``GET``","bind","domain","getDomain","$uuid=null"
    "``GET``","bind","domain","searchMasterDomain",""
    "``*``","bind","domain","searchPrimaryDomain",""
    "``*``","bind","domain","searchSecondaryDomain",""
    "``GET``","bind","domain","searchSlaveDomain",""
    "``POST``","bind","domain","set",""
    "``POST``","bind","domain","setDomain","$uuid=null"
    "``POST``","bind","domain","toggleDomain","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Domain.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Domain.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","bind","general","get",""
    "``POST``","bind","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/General.xml>`__"

.. csv-table:: Resources (RecordController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","record","addRecord",""
    "``POST``","bind","record","delRecord","$uuid"
    "``GET``","bind","record","get",""
    "``GET``","bind","record","getRecord","$uuid=null"
    "``*``","bind","record","searchRecord",""
    "``POST``","bind","record","set",""
    "``POST``","bind","record","setRecord","$uuid=null"
    "``POST``","bind","record","toggleRecord","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Record.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Record.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","bind","service","dnsbl",""
    "``POST``","bind","service","reconfigure",""
    "``POST``","bind","service","restart",""
    "``POST``","bind","service","start",""
    "``GET``","bind","service","status",""
    "``POST``","bind","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/General.xml>`__"
