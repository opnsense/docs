Auth
~~~~

.. csv-table:: Resources (GroupController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","auth","group","add",""
    "``POST``","auth","group","del","$uuid"
    "``GET``","auth","group","get","$uuid=null"
    "``GET``","auth","group","get",""
    "``*``","auth","group","search",""
    "``POST``","auth","group","set","$uuid=null"
    "``POST``","auth","group","set",""

    "``<<uses>>``", "", "", "", "*model* `Group.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Auth/Group.xml>`__"

.. csv-table:: Service (PrivController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","auth","priv","get",""
    "``GET``","auth","priv","getItem","$id"
    "``GET``","auth","priv","search",""
    "``POST``","auth","priv","set",""
    "``POST``","auth","priv","setItem","$id"

    "``<<uses>>``", "", "", "", "*model* `Priv.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Auth/Priv.xml>`__"

.. csv-table:: Resources (UserController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","auth","user","add",""
    "``POST``","auth","user","addApiKey","$username"
    "``POST``","auth","user","del","$uuid"
    "``POST``","auth","user","delApiKey","$id"
    "``GET``","auth","user","get","$uuid=null"
    "``GET``","auth","user","get",""
    "``GET``","auth","user","newOtpSeed",""
    "``*``","auth","user","search",""
    "``GET``","auth","user","searchApiKey",""
    "``POST``","auth","user","set","$uuid=null"
    "``POST``","auth","user","set",""

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Auth/User.xml>`__"
