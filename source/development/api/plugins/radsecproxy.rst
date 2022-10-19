Radsecproxy
~~~~~~~~~~~

.. csv-table:: Resources (ClientsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","clients","addItem",""
    "``POST``","radsecproxy","clients","delItem","$uuid"
    "``GET``","radsecproxy","clients","get",""
    "``GET``","radsecproxy","clients","getItem","$uuid=null"
    "``*``","radsecproxy","clients","searchItem",""
    "``POST``","radsecproxy","clients","set",""
    "``POST``","radsecproxy","clients","setItem","$uuid"
    "``POST``","radsecproxy","clients","toggleItem","$uuid,$enabled=null"

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

    "``POST``","radsecproxy","realms","addItem",""
    "``POST``","radsecproxy","realms","delItem","$uuid"
    "``GET``","radsecproxy","realms","get",""
    "``GET``","radsecproxy","realms","getItem","$uuid=null"
    "``*``","radsecproxy","realms","searchItem",""
    "``POST``","radsecproxy","realms","set",""
    "``POST``","radsecproxy","realms","setItem","$uuid"
    "``POST``","radsecproxy","realms","toggleItem","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"

.. csv-table:: Resources (RewritesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","rewrites","addItem",""
    "``POST``","radsecproxy","rewrites","delItem","$uuid"
    "``GET``","radsecproxy","rewrites","get",""
    "``GET``","radsecproxy","rewrites","getItem","$uuid=null"
    "``*``","radsecproxy","rewrites","searchItem",""
    "``POST``","radsecproxy","rewrites","set",""
    "``POST``","radsecproxy","rewrites","setItem","$uuid"
    "``POST``","radsecproxy","rewrites","toggleItem","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"

.. csv-table:: Resources (ServersController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radsecproxy","servers","addItem",""
    "``POST``","radsecproxy","servers","delItem","$uuid"
    "``GET``","radsecproxy","servers","get",""
    "``GET``","radsecproxy","servers","getItem","$uuid=null"
    "``*``","radsecproxy","servers","searchItem",""
    "``POST``","radsecproxy","servers","set",""
    "``POST``","radsecproxy","servers","setItem","$uuid"
    "``POST``","radsecproxy","servers","toggleItem","$uuid,$enabled=null"

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

    "``POST``","radsecproxy","tls","addItem",""
    "``POST``","radsecproxy","tls","delItem","$uuid"
    "``GET``","radsecproxy","tls","get",""
    "``GET``","radsecproxy","tls","getItem","$uuid=null"
    "``*``","radsecproxy","tls","searchItem",""
    "``POST``","radsecproxy","tls","set",""
    "``POST``","radsecproxy","tls","setItem","$uuid"
    "``POST``","radsecproxy","tls","toggleItem","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `RadSecProxy.xml <https://github.com/opnsense/plugins/blob/master/net/radsecproxy/src/opnsense/mvc/app/models/OPNsense/RadSecProxy/RadSecProxy.xml>`__"
