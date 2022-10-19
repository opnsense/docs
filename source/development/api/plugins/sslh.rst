Sslh
~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","sslh","service","reconfigure",""
    "``POST``","sslh","service","restart",""
    "``POST``","sslh","service","start",""
    "``GET``","sslh","service","status",""
    "``POST``","sslh","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Settings.xml <https://github.com/opnsense/plugins/blob/master/net/sslh/src/opnsense/mvc/app/models/OPNsense/Sslh/Settings.xml>`__"

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","sslh","settings","get",""
    "``GET``","sslh","settings","index",""
    "``POST``","sslh","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `Settings.xml <https://github.com/opnsense/plugins/blob/master/net/sslh/src/opnsense/mvc/app/models/OPNsense/Sslh/Settings.xml>`__"
