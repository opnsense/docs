Chrony
~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","chrony","general","get",""
    "``GET``","chrony","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/chrony/src/opnsense/mvc/app/models/OPNsense/Chrony/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","chrony","service","reconfigure",""
    "``GET``","chrony","service","restart",""
    "``GET``","chrony","service","start",""
    "``GET``","chrony","service","status",""
    "``GET``","chrony","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/chrony/src/opnsense/mvc/app/models/OPNsense/Chrony/General.xml>`__"
