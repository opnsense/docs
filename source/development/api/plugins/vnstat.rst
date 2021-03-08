Vnstat
~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","vnstat","general","get",""
    "``GET``","vnstat","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/vnstat/src/opnsense/mvc/app/models/OPNsense/Vnstat/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","vnstat","service","daily",""
    "``GET``","vnstat","service","hourly",""
    "``GET``","vnstat","service","monthly",""
    "``GET``","vnstat","service","reconfigure",""
    "``GET``","vnstat","service","resetdb",""
    "``GET``","vnstat","service","restart",""
    "``GET``","vnstat","service","start",""
    "``GET``","vnstat","service","status",""
    "``GET``","vnstat","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/vnstat/src/opnsense/mvc/app/models/OPNsense/Vnstat/General.xml>`__"
