Nrpe
~~~~

.. csv-table:: Resources (CommandController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","nrpe","command","addCommand",""
    "``POST``","nrpe","command","delCommand","$uuid"
    "``GET``","nrpe","command","get",""
    "``GET``","nrpe","command","getCommand","$uuid=null"
    "``*``","nrpe","command","searchCommand",""
    "``POST``","nrpe","command","set",""
    "``POST``","nrpe","command","setCommand","$uuid"
    "``POST``","nrpe","command","toggleCommand","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Command.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/nrpe/src/opnsense/mvc/app/models/OPNsense/Nrpe/Command.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","nrpe","general","get",""
    "``POST``","nrpe","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/nrpe/src/opnsense/mvc/app/models/OPNsense/Nrpe/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","nrpe","service","reconfigure",""
    "``POST``","nrpe","service","restart",""
    "``POST``","nrpe","service","start",""
    "``GET``","nrpe","service","status",""
    "``POST``","nrpe","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/nrpe/src/opnsense/mvc/app/models/OPNsense/Nrpe/General.xml>`__"
