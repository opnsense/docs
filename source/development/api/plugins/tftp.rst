Tftp
~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","tftp","general","get",""
    "``GET``","tftp","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/ftp/tftp/src/opnsense/mvc/app/models/OPNsense/Tftp/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","tftp","service","reconfigure",""
    "``GET``","tftp","service","restart",""
    "``GET``","tftp","service","start",""
    "``GET``","tftp","service","status",""
    "``GET``","tftp","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/ftp/tftp/src/opnsense/mvc/app/models/OPNsense/Tftp/General.xml>`__"
