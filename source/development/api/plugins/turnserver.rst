Turnserver
~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","turnserver","service","reconfigure",""
    "``POST``","turnserver","service","restart",""
    "``POST``","turnserver","service","start",""
    "``GET``","turnserver","service","status",""
    "``POST``","turnserver","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Turnserver.xml <https://github.com/opnsense/plugins/blob/master/net/turnserver/src/opnsense/mvc/app/models/OPNsense/Turnserver/Turnserver.xml>`__"

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","turnserver","settings","get",""
    "``POST``","turnserver","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `Turnserver.xml <https://github.com/opnsense/plugins/blob/master/net/turnserver/src/opnsense/mvc/app/models/OPNsense/Turnserver/Turnserver.xml>`__"
