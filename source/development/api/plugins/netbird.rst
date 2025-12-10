Netbird
~~~~~~~

.. csv-table:: Resources (AuthenticationController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","netbird","authentication","down",""
    "``GET``","netbird","authentication","get",""
    "``POST``","netbird","authentication","set",""
    "``GET``","netbird","authentication","up",""

    "``<<uses>>``", "", "", "", "*model* `Authentication.xml <https://github.com/opnsense/plugins/blob/master/security/netbird/src/opnsense/mvc/app/models/OPNsense/Netbird/Authentication.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","netbird","service","reconfigure",""
    "``POST``","netbird","service","restart",""
    "``POST``","netbird","service","start",""
    "``GET``","netbird","service","status",""
    "``POST``","netbird","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","netbird","settings","get",""
    "``POST``","netbird","settings","set",""
    "``GET``","netbird","settings","sync",""

    "``<<uses>>``", "", "", "", "*model* `Settings.xml <https://github.com/opnsense/plugins/blob/master/security/netbird/src/opnsense/mvc/app/models/OPNsense/Netbird/Settings.xml>`__"

.. csv-table:: Resources (StatusController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","netbird","status","get",""
    "``POST``","netbird","status","set",""
    "``GET``","netbird","status","status",""

    "``<<uses>>``", "", "", "", "*model* `Status.xml <https://github.com/opnsense/plugins/blob/master/security/netbird/src/opnsense/mvc/app/models/OPNsense/Netbird/Status.xml>`__"
