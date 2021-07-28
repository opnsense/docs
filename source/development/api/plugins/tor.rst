Tor
~~~

.. csv-table:: Resources (ExitaclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","exitacl","addacl",""
    "``POST``","tor","exitacl","delacl","$uuid"
    "``GET``","tor","exitacl","get",""
    "``GET``","tor","exitacl","getacl","$uuid=null"
    "``*``","tor","exitacl","searchacl",""
    "``GET``","tor","exitacl","set",""
    "``POST``","tor","exitacl","setacl","$uuid"
    "``POST``","tor","exitacl","toggleacl","$uuid"

    "``<<uses>>``", "", "", "", "*model* `ACLExitPolicy.xml <https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/ACLExitPolicy.xml>`__"

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","general","addhidservauth",""
    "``POST``","tor","general","delhidservauth","$uuid"
    "``GET``","tor","general","get",""
    "``GET``","tor","general","gethidservauth","$uuid=null"
    "``*``","tor","general","searchhidservauth",""
    "``POST``","tor","general","set",""
    "``GET``","tor","general","set",""
    "``POST``","tor","general","sethidservauth","$uuid"
    "``POST``","tor","general","togglehidservauth","$uuid"

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/General.xml>`__"

.. csv-table:: Service (HiddenserviceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","hiddenservice","addservice",""
    "``POST``","tor","hiddenservice","delservice","$uuid"
    "``GET``","tor","hiddenservice","get",""
    "``GET``","tor","hiddenservice","getservice","$uuid=null"
    "``*``","tor","hiddenservice","searchservice",""
    "``GET``","tor","hiddenservice","set",""
    "``POST``","tor","hiddenservice","setservice","$uuid"
    "``POST``","tor","hiddenservice","toggleservice","$uuid"

    "``<<uses>>``", "", "", "", "*model* `HiddenService.xml <https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/HiddenService.xml>`__"

.. csv-table:: Service (HiddenserviceaclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tor","hiddenserviceacl","addacl",""
    "``POST``","tor","hiddenserviceacl","delacl","$uuid"
    "``GET``","tor","hiddenserviceacl","get",""
    "``GET``","tor","hiddenserviceacl","getacl","$uuid=null"
    "``*``","tor","hiddenserviceacl","searchacl",""
    "``GET``","tor","hiddenserviceacl","set",""
    "``POST``","tor","hiddenserviceacl","setacl","$uuid"
    "``POST``","tor","hiddenserviceacl","toggleacl","$uuid"

    "``<<uses>>``", "", "", "", "*model* `HiddenServiceACL.xml <https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/HiddenServiceACL.xml>`__"

.. csv-table:: Service (RelayController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","tor","relay","get",""
    "``GET``","tor","relay","set",""

    "``<<uses>>``", "", "", "", "*model* `Relay.xml <https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/Relay.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","tor","service","circuits",""
    "``GET``","tor","service","getHiddenServices",""
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
    "``GET``","tor","socksacl","get",""
    "``GET``","tor","socksacl","getacl","$uuid=null"
    "``*``","tor","socksacl","searchacl",""
    "``GET``","tor","socksacl","set",""
    "``POST``","tor","socksacl","setacl","$uuid"
    "``POST``","tor","socksacl","toggleacl","$uuid"

    "``<<uses>>``", "", "", "", "*model* `ACLSocksPolicy.xml <https://github.com/opnsense/plugins/blob/master/security/tor/src/opnsense/mvc/app/models/OPNsense/Tor/ACLSocksPolicy.xml>`__"
