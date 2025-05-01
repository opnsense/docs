Dnscryptproxy
~~~~~~~~~~~~~

.. csv-table:: Resources (CloakController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnscryptproxy","cloak","add_cloak",""
    "``POST``","dnscryptproxy","cloak","del_cloak","$uuid"
    "``GET``","dnscryptproxy","cloak","get",""
    "``GET``","dnscryptproxy","cloak","get_cloak","$uuid=null"
    "``POST,GET``","dnscryptproxy","cloak","search_cloak",""
    "``POST``","dnscryptproxy","cloak","set",""
    "``POST``","dnscryptproxy","cloak","set_cloak","$uuid"
    "``POST``","dnscryptproxy","cloak","toggle_cloak","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Cloak.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Cloak.xml>`__"

.. csv-table:: Resources (DnsblController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dnscryptproxy","dnsbl","get",""
    "``POST``","dnscryptproxy","dnsbl","set",""

    "``<<uses>>``", "", "", "", "*model* `Dnsbl.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Dnsbl.xml>`__"

.. csv-table:: Resources (ForwardController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnscryptproxy","forward","add_forward",""
    "``POST``","dnscryptproxy","forward","del_forward","$uuid"
    "``GET``","dnscryptproxy","forward","get",""
    "``GET``","dnscryptproxy","forward","get_forward","$uuid=null"
    "``POST,GET``","dnscryptproxy","forward","search_forward",""
    "``POST``","dnscryptproxy","forward","set",""
    "``POST``","dnscryptproxy","forward","set_forward","$uuid"
    "``POST``","dnscryptproxy","forward","toggle_forward","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Forward.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Forward.xml>`__"

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dnscryptproxy","general","get",""
    "``POST``","dnscryptproxy","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/General.xml>`__"

.. csv-table:: Resources (ServerController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnscryptproxy","server","add_server",""
    "``POST``","dnscryptproxy","server","del_server","$uuid"
    "``GET``","dnscryptproxy","server","get",""
    "``GET``","dnscryptproxy","server","get_server","$uuid=null"
    "``POST,GET``","dnscryptproxy","server","search_server",""
    "``POST``","dnscryptproxy","server","set",""
    "``POST``","dnscryptproxy","server","set_server","$uuid"
    "``POST``","dnscryptproxy","server","toggle_server","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Server.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dnscryptproxy","service","dnsbl",""
    "``POST``","dnscryptproxy","service","reconfigure",""
    "``POST``","dnscryptproxy","service","restart",""
    "``POST``","dnscryptproxy","service","start",""
    "``GET``","dnscryptproxy","service","status",""
    "``POST``","dnscryptproxy","service","stop",""

.. csv-table:: Resources (WhitelistController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnscryptproxy","whitelist","add_whitelist",""
    "``POST``","dnscryptproxy","whitelist","del_whitelist","$uuid"
    "``GET``","dnscryptproxy","whitelist","get",""
    "``GET``","dnscryptproxy","whitelist","get_whitelist","$uuid=null"
    "``POST,GET``","dnscryptproxy","whitelist","search_whitelist",""
    "``POST``","dnscryptproxy","whitelist","set",""
    "``POST``","dnscryptproxy","whitelist","set_whitelist","$uuid"
    "``POST``","dnscryptproxy","whitelist","toggle_whitelist","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Whitelist.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Whitelist.xml>`__"
