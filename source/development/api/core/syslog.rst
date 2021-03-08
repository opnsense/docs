Syslog
~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","syslog","service","reconfigure",""
    "``GET``","syslog","service","restart",""
    "``GET``","syslog","service","start",""
    "``GET``","syslog","service","stats",""
    "``GET``","syslog","service","status",""
    "``GET``","syslog","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Syslog.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Syslog/Syslog.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","syslog","settings","addDestination",""
    "``POST``","syslog","settings","delDestination","$uuid"
    "``GET``","syslog","settings","get",""
    "``GET``","syslog","settings","getDestination","$uuid=null"
    "``*``","syslog","settings","searchDestinations",""
    "``GET``","syslog","settings","set",""
    "``POST``","syslog","settings","setDestination","$uuid"
    "``POST``","syslog","settings","toggleDestination","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Syslog.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Syslog/Syslog.xml>`__"
