Syslog
~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","syslog","service","stats",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","syslog","settings","addDestination",""
    "``POST``","syslog","settings","delDestination","$uuid"
    "``GET``","syslog","settings","getDestination","$uuid=null"
    "``*``","syslog","settings","searchDestinations",""
    "``POST``","syslog","settings","setDestination","$uuid"
    "``POST``","syslog","settings","toggleDestination","$uuid,$enabled=null"
