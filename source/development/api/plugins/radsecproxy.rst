Radsecproxy
~~~~~~~~~~~

.. csv-table:: Resources (ClientsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","clients","add_item",""
    "``POST``","radsecproxy","clients","del_item","$uuid"
    "``GET``","radsecproxy","clients","get",""
    "``GET``","radsecproxy","clients","get_item","$uuid=null"
    "``*``","radsecproxy","clients","search_item",""
    "``POST``","radsecproxy","clients","set",""
    "``POST``","radsecproxy","clients","set_item","$uuid"
    "``POST``","radsecproxy","clients","toggle_item","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","radsecproxy","general","get",""
    "``POST``","radsecproxy","general","set",""

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"

.. csv-table:: Resources (RealmsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","realms","add_item",""
    "``POST``","radsecproxy","realms","del_item","$uuid"
    "``GET``","radsecproxy","realms","get",""
    "``GET``","radsecproxy","realms","get_item","$uuid=null"
    "``*``","radsecproxy","realms","search_item",""
    "``POST``","radsecproxy","realms","set",""
    "``POST``","radsecproxy","realms","set_item","$uuid"
    "``POST``","radsecproxy","realms","toggle_item","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"

.. csv-table:: Resources (RewritesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","rewrites","add_item",""
    "``POST``","radsecproxy","rewrites","del_item","$uuid"
    "``GET``","radsecproxy","rewrites","get",""
    "``GET``","radsecproxy","rewrites","get_item","$uuid=null"
    "``*``","radsecproxy","rewrites","search_item",""
    "``POST``","radsecproxy","rewrites","set",""
    "``POST``","radsecproxy","rewrites","set_item","$uuid"
    "``POST``","radsecproxy","rewrites","toggle_item","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"

.. csv-table:: Resources (ServersController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","servers","add_item",""
    "``POST``","radsecproxy","servers","del_item","$uuid"
    "``GET``","radsecproxy","servers","get",""
    "``GET``","radsecproxy","servers","get_item","$uuid=null"
    "``*``","radsecproxy","servers","search_item",""
    "``POST``","radsecproxy","servers","set",""
    "``POST``","radsecproxy","servers","set_item","$uuid"
    "``POST``","radsecproxy","servers","toggle_item","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","service","reconfigure",""
    "``POST``","radsecproxy","service","restart",""
    "``POST``","radsecproxy","service","start",""
    "``GET``","radsecproxy","service","status",""
    "``POST``","radsecproxy","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"

.. csv-table:: Resources (TlsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","tls","add_item",""
    "``POST``","radsecproxy","tls","del_item","$uuid"
    "``GET``","radsecproxy","tls","get",""
    "``GET``","radsecproxy","tls","get_item","$uuid=null"
    "``*``","radsecproxy","tls","search_item",""
    "``POST``","radsecproxy","tls","set",""
    "``POST``","radsecproxy","tls","set_item","$uuid"
    "``POST``","radsecproxy","tls","toggle_item","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"
