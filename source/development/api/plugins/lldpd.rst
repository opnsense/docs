Lldpd
~~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","lldpd","general","get",""
    "``POST``","lldpd","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/lldpd/src/opnsense/mvc/app/models/OPNsense/Lldpd/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","lldpd","service","neighbor",""
    "``POST``","lldpd","service","reconfigure",""
    "``POST``","lldpd","service","restart",""
    "``POST``","lldpd","service","start",""
    "``GET``","lldpd","service","status",""
    "``POST``","lldpd","service","stop",""
