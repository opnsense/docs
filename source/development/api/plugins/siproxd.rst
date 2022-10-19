Siproxd
~~~~~~~

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","siproxd","domain","addDomain",""
    "``POST``","siproxd","domain","delDomain","$uuid"
    "``GET``","siproxd","domain","get",""
    "``GET``","siproxd","domain","get",""
    "``GET``","siproxd","domain","getDomain","$uuid=null"
    "``GET``","siproxd","domain","searchDomain",""
    "``POST``","siproxd","domain","set",""
    "``POST``","siproxd","domain","set",""
    "``POST``","siproxd","domain","setDomain","$uuid"
    "``GET``","siproxd","domain","toggleDomain","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Domain.xml <https://github.com/opnsense/plugins/blob/master/net/siproxd/src/opnsense/mvc/app/models/OPNsense/Siproxd/Domain.xml>`__"

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","siproxd","general","get",""
    "``POST``","siproxd","general","set",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","siproxd","service","reconfigure",""
    "``POST``","siproxd","service","restart",""
    "``GET``","siproxd","service","showregistrations",""
    "``POST``","siproxd","service","start",""
    "``GET``","siproxd","service","status",""
    "``POST``","siproxd","service","stop",""

.. csv-table:: Resources (UserController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","siproxd","user","addUser",""
    "``POST``","siproxd","user","delUser","$uuid"
    "``GET``","siproxd","user","get",""
    "``GET``","siproxd","user","get",""
    "``GET``","siproxd","user","getUser","$uuid=null"
    "``GET``","siproxd","user","searchUser",""
    "``POST``","siproxd","user","set",""
    "``POST``","siproxd","user","set",""
    "``POST``","siproxd","user","setUser","$uuid"
    "``GET``","siproxd","user","toggleUser","$uuid"

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/plugins/blob/master/net/siproxd/src/opnsense/mvc/app/models/OPNsense/Siproxd/User.xml>`__"
