Tayga
~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","tayga","general","get",""
    "``POST``","tayga","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/tayga/src/opnsense/mvc/app/models/OPNsense/Tayga/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tayga","service","reconfigure",""
    "``POST``","tayga","service","restart",""
    "``POST``","tayga","service","start",""
    "``GET``","tayga","service","status",""
    "``POST``","tayga","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/tayga/src/opnsense/mvc/app/models/OPNsense/Tayga/General.xml>`__"
