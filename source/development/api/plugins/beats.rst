Beats
~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","beats","service","reconfigure",""
    "``POST``","beats","service","restart",""
    "``POST``","beats","service","start",""
    "``GET``","beats","service","status",""
    "``POST``","beats","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","beats","settings","get",""
    "``POST``","beats","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `Filebeat.xml <https://github.com/opnsense/plugins/blob/master/sysutils/beats/src/opnsense/mvc/app/models/OPNsense/Beats/Filebeat.xml>`__"
