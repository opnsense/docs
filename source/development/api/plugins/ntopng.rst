Ntopng
~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ntopng","general","get",""
    "``POST``","ntopng","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/ntopng/src/opnsense/mvc/app/models/OPNsense/Ntopng/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ntopng","service","checkredis",""
    "``POST``","ntopng","service","reconfigure",""
    "``POST``","ntopng","service","restart",""
    "``POST``","ntopng","service","start",""
    "``GET``","ntopng","service","status",""
    "``POST``","ntopng","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/ntopng/src/opnsense/mvc/app/models/OPNsense/Ntopng/General.xml>`__"
