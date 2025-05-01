Bind
~~~~

.. csv-table:: Resources (AclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","acl","add_acl",""
    "``POST``","bind","acl","del_acl","$uuid"
    "``GET``","bind","acl","get",""
    "``GET``","bind","acl","get_acl","$uuid=null"
    "``POST,GET``","bind","acl","search_acl",""
    "``POST``","bind","acl","set",""
    "``POST``","bind","acl","set_acl","$uuid"
    "``POST``","bind","acl","toggle_acl","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Acl.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Acl.xml>`__"

.. csv-table:: Resources (DnsblController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","bind","dnsbl","get",""
    "``POST``","bind","dnsbl","set",""

    "``<<uses>>``", "", "", "", "*model* `Dnsbl.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Dnsbl.xml>`__"

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","domain","add_primary_domain","$uuid=null"
    "``POST``","bind","domain","add_secondary_domain","$uuid=null"
    "``POST``","bind","domain","del_domain","$uuid"
    "``GET``","bind","domain","get",""
    "``GET``","bind","domain","get_domain","$uuid=null"
    "``GET``","bind","domain","search_master_domain",""
    "``POST,GET``","bind","domain","search_primary_domain",""
    "``POST,GET``","bind","domain","search_secondary_domain",""
    "``GET``","bind","domain","search_slave_domain",""
    "``POST``","bind","domain","set",""
    "``POST``","bind","domain","set_domain","$uuid=null"
    "``POST``","bind","domain","toggle_domain","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Domain.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/Domain.xml>`__"

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","bind","general","get",""
    "``POST``","bind","general","set",""
    "``GET``","bind","general","zoneshow","$zonename=null"
    "``GET``","bind","general","zonetest","$zonename=null"

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/dns/bind/src/opnsense/mvc/app/models/OPNsense/Bind/General.xml>`__"

.. csv-table:: Resources (RecordController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","bind","record","add_record",""
    "``POST``","bind","record","del_record","$uuid"
    "``GET``","bind","record","get",""
    "``GET``","bind","record","get_record","$uuid=null"
    "``POST,GET``","bind","record","search_record",""
    "``POST``","bind","record","set",""
    "``POST``","bind","record","set_record","$uuid=null"
    "``POST``","bind","record","toggle_record","$uuid"

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
