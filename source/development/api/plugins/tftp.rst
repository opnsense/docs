Tftp
~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","tftp","general","get",""
    "``POST``","tftp","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/ftp/tftp/src/opnsense/mvc/app/models/OPNsense/Tftp/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tftp","service","reconfigure",""
    "``POST``","tftp","service","restart",""
    "``POST``","tftp","service","start",""
    "``GET``","tftp","service","status",""
    "``POST``","tftp","service","stop",""
