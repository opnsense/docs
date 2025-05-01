Auth
~~~~

.. csv-table:: Resources (GroupController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","auth","group","add",""
    "``POST``","auth","group","del","$uuid"
    "``GET``","auth","group","get","$uuid=null"
    "``GET,POST``","auth","group","search",""
    "``POST``","auth","group","set","$uuid=null"

    "``<<uses>>``", "", "", "", "*model* `Group.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Auth/Group.xml>`__"

.. csv-table:: Resources (PrivController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","auth","priv","get",""
    "``GET``","auth","priv","get_item","$id"
    "``GET``","auth","priv","search",""
    "``POST``","auth","priv","set",""
    "``POST``","auth","priv","set_item","$id"

    "``<<uses>>``", "", "", "", "*model* `Priv.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Auth/Priv.xml>`__"

.. csv-table:: Resources (UserController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","auth","user","add",""
    "``POST``","auth","user","add_api_key","$username"
    "``POST``","auth","user","del","$uuid"
    "``POST``","auth","user","del_api_key","$id"
    "``GET``","auth","user","download",""
    "``GET``","auth","user","get","$uuid=null"
    "``GET``","auth","user","new_otp_seed",""
    "``GET,POST``","auth","user","search",""
    "``GET``","auth","user","search_api_key",""
    "``POST``","auth","user","set","$uuid=null"
    "``POST``","auth","user","upload",""

    "``<<uses>>``", "", "", "", "*model* `User.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Auth/User.xml>`__"
