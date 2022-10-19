Redis
~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","redis","service","reconfigure",""
    "``GET``","redis","service","resetdb",""
    "``POST``","redis","service","restart",""
    "``POST``","redis","service","start",""
    "``GET``","redis","service","status",""
    "``POST``","redis","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Redis.xml <https://github.com/opnsense/plugins/blob/master/databases/redis/src/opnsense/mvc/app/models/OPNsense/Redis/Redis.xml>`__"

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","redis","settings","get",""
    "``POST``","redis","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `Redis.xml <https://github.com/opnsense/plugins/blob/master/databases/redis/src/opnsense/mvc/app/models/OPNsense/Redis/Redis.xml>`__"
