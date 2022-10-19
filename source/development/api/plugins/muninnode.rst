Muninnode
~~~~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","muninnode","general","get",""
    "``POST``","muninnode","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/sysutils/munin-node/src/opnsense/mvc/app/models/OPNsense/Muninnode/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","muninnode","service","reconfigure",""
    "``POST``","muninnode","service","restart",""
    "``POST``","muninnode","service","start",""
    "``GET``","muninnode","service","status",""
    "``POST``","muninnode","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/sysutils/munin-node/src/opnsense/mvc/app/models/OPNsense/Muninnode/General.xml>`__"
