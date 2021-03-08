Dnscryptproxy
~~~~~~~~~~~~~

.. csv-table:: Resources (CloakController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnscryptproxy","cloak","addCloak",""
    "``POST``","dnscryptproxy","cloak","delCloak","$uuid"
    "``GET``","dnscryptproxy","cloak","get",""
    "``GET``","dnscryptproxy","cloak","getCloak","$uuid=null"
    "``*``","dnscryptproxy","cloak","searchCloak",""
    "``GET``","dnscryptproxy","cloak","set",""
    "``POST``","dnscryptproxy","cloak","setCloak","$uuid"
    "``POST``","dnscryptproxy","cloak","toggleCloak","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Cloak.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Cloak.xml>`__"

.. csv-table:: Service (DnsblController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dnscryptproxy","dnsbl","get",""
    "``GET``","dnscryptproxy","dnsbl","set",""

    "``<<uses>>``", "", "", "", "*model* `Dnsbl.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Dnsbl.xml>`__"

.. csv-table:: Resources (ForwardController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnscryptproxy","forward","addForward",""
    "``POST``","dnscryptproxy","forward","delForward","$uuid"
    "``GET``","dnscryptproxy","forward","get",""
    "``GET``","dnscryptproxy","forward","getForward","$uuid=null"
    "``*``","dnscryptproxy","forward","searchForward",""
    "``GET``","dnscryptproxy","forward","set",""
    "``POST``","dnscryptproxy","forward","setForward","$uuid"
    "``POST``","dnscryptproxy","forward","toggleForward","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Forward.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Forward.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dnscryptproxy","general","get",""
    "``GET``","dnscryptproxy","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/General.xml>`__"

.. csv-table:: Resources (ServerController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnscryptproxy","server","addServer",""
    "``POST``","dnscryptproxy","server","delServer","$uuid"
    "``GET``","dnscryptproxy","server","get",""
    "``GET``","dnscryptproxy","server","getServer","$uuid=null"
    "``*``","dnscryptproxy","server","searchServer",""
    "``GET``","dnscryptproxy","server","set",""
    "``POST``","dnscryptproxy","server","setServer","$uuid"
    "``POST``","dnscryptproxy","server","toggleServer","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Server.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dnscryptproxy","service","dnsbl",""
    "``GET``","dnscryptproxy","service","reconfigure",""
    "``GET``","dnscryptproxy","service","restart",""
    "``GET``","dnscryptproxy","service","start",""
    "``GET``","dnscryptproxy","service","status",""
    "``GET``","dnscryptproxy","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/General.xml>`__"

.. csv-table:: Resources (WhitelistController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnscryptproxy","whitelist","addWhitelist",""
    "``POST``","dnscryptproxy","whitelist","delWhitelist","$uuid"
    "``GET``","dnscryptproxy","whitelist","get",""
    "``GET``","dnscryptproxy","whitelist","getWhitelist","$uuid=null"
    "``*``","dnscryptproxy","whitelist","searchWhitelist",""
    "``GET``","dnscryptproxy","whitelist","set",""
    "``POST``","dnscryptproxy","whitelist","setWhitelist","$uuid"
    "``POST``","dnscryptproxy","whitelist","toggleWhitelist","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Whitelist.xml <https://github.com/opnsense/plugins/blob/master/dns/dnscrypt-proxy/src/opnsense/mvc/app/models/OPNsense/Dnscryptproxy/Whitelist.xml>`__"
