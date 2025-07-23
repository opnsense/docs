Netbird
~~~~~~~

.. csv-table:: Resources (InitialController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","netbird","initial","get",""
    "``POST``","netbird","initial","set",""

    "``<<uses>>``", "", "", "", "*model* `Initial.xml <https://github.com/opnsense/plugins/blob/master/security/netbird/src/opnsense/mvc/app/models/OPNsense/Netbird/Initial.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","netbird","service","con_status",""
    "``GET``","netbird","service","initial_up",""
    "``POST``","netbird","service","reconfigure",""
    "``POST``","netbird","service","reload",""
    "``POST``","netbird","service","restart",""
    "``GET``","netbird","service","search",""
    "``GET``","netbird","service","set_down",""
    "``GET``","netbird","service","set_up",""
    "``POST``","netbird","service","start",""
    "``GET``","netbird","service","status",""
    "``POST``","netbird","service","stop",""
    "``GET``","netbird","service","up_down_status",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","netbird","settings","get",""
    "``POST``","netbird","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `Netbird.xml <https://github.com/opnsense/plugins/blob/master/security/netbird/src/opnsense/mvc/app/models/OPNsense/Netbird/Netbird.xml>`__"
