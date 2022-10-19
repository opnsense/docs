Vnstat
~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","vnstat","general","get",""
    "``POST``","vnstat","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/vnstat/src/opnsense/mvc/app/models/OPNsense/Vnstat/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","vnstat","service","daily",""
    "``GET``","vnstat","service","hourly",""
    "``GET``","vnstat","service","monthly",""
    "``POST``","vnstat","service","reconfigure",""
    "``GET``","vnstat","service","resetdb",""
    "``POST``","vnstat","service","restart",""
    "``POST``","vnstat","service","start",""
    "``GET``","vnstat","service","status",""
    "``POST``","vnstat","service","stop",""
    "``GET``","vnstat","service","yearly",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/vnstat/src/opnsense/mvc/app/models/OPNsense/Vnstat/General.xml>`__"
