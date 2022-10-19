Puppetagent
~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","puppetagent","service","reconfigure",""
    "``POST``","puppetagent","service","restart",""
    "``POST``","puppetagent","service","start",""
    "``GET``","puppetagent","service","status",""
    "``POST``","puppetagent","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `PuppetAgent.xml <https://github.com/opnsense/plugins/blob/master/sysutils/puppet-agent/src/opnsense/mvc/app/models/OPNsense/PuppetAgent/PuppetAgent.xml>`__"

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","puppetagent","settings","get",""
    "``POST``","puppetagent","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `PuppetAgent.xml <https://github.com/opnsense/plugins/blob/master/sysutils/puppet-agent/src/opnsense/mvc/app/models/OPNsense/PuppetAgent/PuppetAgent.xml>`__"
