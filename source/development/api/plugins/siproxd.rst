Siproxd
~~~~~~~

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","siproxd","domain","add_domain",""
    "``POST``","siproxd","domain","del_domain","$uuid"
    "``GET``","siproxd","domain","get",""
    "``GET``","siproxd","domain","get",""
    "``GET``","siproxd","domain","get_domain","$uuid=null"
    "``GET``","siproxd","domain","search_domain",""
    "``POST``","siproxd","domain","set",""
    "``POST``","siproxd","domain","set",""
    "``POST``","siproxd","domain","set_domain","$uuid"
    "``GET``","siproxd","domain","toggle_domain","$uuid"

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

    "``POST``","siproxd","user","add_user",""
    "``POST``","siproxd","user","del_user","$uuid"
    "``GET``","siproxd","user","get",""
    "``GET``","siproxd","user","get",""
    "``GET``","siproxd","user","get_user","$uuid=null"
    "``GET``","siproxd","user","search_user",""
    "``POST``","siproxd","user","set",""
    "``POST``","siproxd","user","set",""
    "``POST``","siproxd","user","set_user","$uuid"
    "``GET``","siproxd","user","toggle_user","$uuid"

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/plugins/blob/master/net/siproxd/src/opnsense/mvc/app/models/OPNsense/Siproxd/User.xml>`__"
