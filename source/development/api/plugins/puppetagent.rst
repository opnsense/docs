Puppetagent
~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","puppetagent","service","reconfigure",""
    "``GET``","puppetagent","service","restart",""
    "``GET``","puppetagent","service","start",""
    "``GET``","puppetagent","service","status",""
    "``GET``","puppetagent","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `PuppetAgent.xml <https://github.com/opnsense/plugins/blob/master/sysutils/puppet-agent/src/opnsense/mvc/app/models/OPNsense/PuppetAgent/PuppetAgent.xml>`__"

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","puppetagent","settings","get",""
    "``GET``","puppetagent","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `PuppetAgent.xml <https://github.com/opnsense/plugins/blob/master/sysutils/puppet-agent/src/opnsense/mvc/app/models/OPNsense/PuppetAgent/PuppetAgent.xml>`__"
