Zerotier
~~~~~~~~

.. csv-table:: Resources (NetworkController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","zerotier","network","add",""
    "``POST``","zerotier","network","del","$uuid=null"
    "``GET``","zerotier","network","get","$uuid=null"
    "``GET``","zerotier","network","get",""
    "``GET``","zerotier","network","info","$uuid=null"
    "``GET``","zerotier","network","search",""
    "``POST``","zerotier","network","set","$uuid=null"
    "``GET``","zerotier","network","set",""
    "``POST``","zerotier","network","toggle","$uuid=null"

    "``<<uses>>``", "", "", "", "*model* `Zerotier.xml <https://github.com/opnsense/plugins/blob/master/net/zerotier/src/opnsense/mvc/app/models/OPNsense/Zerotier/Zerotier.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","zerotier","settings","get",""
    "``GET``","zerotier","settings","get",""
    "``POST``","zerotier","settings","set",""
    "``GET``","zerotier","settings","set",""
    "``GET``","zerotier","settings","status",""

    "``<<uses>>``", "", "", "", "*model* `Zerotier.xml <https://github.com/opnsense/plugins/blob/master/net/zerotier/src/opnsense/mvc/app/models/OPNsense/Zerotier/Zerotier.xml>`__"
