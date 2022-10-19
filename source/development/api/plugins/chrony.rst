Chrony
~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","chrony","general","get",""
    "``POST``","chrony","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/chrony/src/opnsense/mvc/app/models/OPNsense/Chrony/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","chrony","service","chronyauthdata",""
    "``GET``","chrony","service","chronysources",""
    "``GET``","chrony","service","chronysourcestats",""
    "``GET``","chrony","service","chronytracking",""
    "``POST``","chrony","service","reconfigure",""
    "``POST``","chrony","service","restart",""
    "``POST``","chrony","service","start",""
    "``GET``","chrony","service","status",""
    "``POST``","chrony","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/chrony/src/opnsense/mvc/app/models/OPNsense/Chrony/General.xml>`__"
