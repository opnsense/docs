Cicap
~~~~~

.. csv-table:: Service (AntivirusController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","cicap","antivirus","get",""
    "``GET``","cicap","antivirus","set",""

    "``<<uses>>``", "", "", "", "*model* `Antivirus.xml <https://github.com/opnsense/plugins/blob/master/www/c-icap/src/opnsense/mvc/app/models/OPNsense/CICAP/Antivirus.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","cicap","general","get",""
    "``GET``","cicap","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/www/c-icap/src/opnsense/mvc/app/models/OPNsense/CICAP/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","cicap","service","checkclamav",""
    "``GET``","cicap","service","reconfigure",""
    "``GET``","cicap","service","restart",""
    "``GET``","cicap","service","start",""
    "``GET``","cicap","service","status",""
    "``GET``","cicap","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/www/c-icap/src/opnsense/mvc/app/models/OPNsense/CICAP/General.xml>`__"
