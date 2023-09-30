Wazuhagent
~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wazuhagent","service","reconfigure",""
    "``POST``","wazuhagent","service","restart",""
    "``POST``","wazuhagent","service","start",""
    "``GET``","wazuhagent","service","status",""
    "``POST``","wazuhagent","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `WazuhAgent.xml <https://github.com/opnsense/plugins/blob/master/security/wazuh-agent/src/opnsense/mvc/app/models/OPNsense/WazuhAgent/WazuhAgent.xml>`__"

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","wazuhagent","settings","get",""
    "``POST``","wazuhagent","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `WazuhAgent.xml <https://github.com/opnsense/plugins/blob/master/security/wazuh-agent/src/opnsense/mvc/app/models/OPNsense/WazuhAgent/WazuhAgent.xml>`__"
