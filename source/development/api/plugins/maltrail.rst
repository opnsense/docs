Maltrail
~~~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","maltrail","general","get",""
    "``POST``","maltrail","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/General.xml>`__"

.. csv-table:: Service (SensorController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","maltrail","sensor","get",""
    "``POST``","maltrail","sensor","set",""

    "``<<uses>>``", "", "", "", "*model* `Sensor.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/Sensor.xml>`__"

.. csv-table:: Service (ServerController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","maltrail","server","get",""
    "``POST``","maltrail","server","set",""

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/Server.xml>`__"

.. csv-table:: Service (ServerserviceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","maltrail","serverservice","reconfigure",""
    "``POST``","maltrail","serverservice","restart",""
    "``POST``","maltrail","serverservice","start",""
    "``GET``","maltrail","serverservice","status",""
    "``POST``","maltrail","serverservice","stop",""

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/Server.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","maltrail","service","reconfigure",""
    "``POST``","maltrail","service","restart",""
    "``POST``","maltrail","service","start",""
    "``GET``","maltrail","service","status",""
    "``POST``","maltrail","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Sensor.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/Sensor.xml>`__"
