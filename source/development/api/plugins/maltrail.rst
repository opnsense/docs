Maltrail
~~~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","maltrail","general","get",""
    "``GET``","maltrail","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/General.xml>`__"

.. csv-table:: Service (SensorController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","maltrail","sensor","get",""
    "``GET``","maltrail","sensor","set",""

    "``<<uses>>``", "", "", "", "*model* `Sensor.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/Sensor.xml>`__"

.. csv-table:: Service (ServerController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","maltrail","server","get",""
    "``GET``","maltrail","server","set",""

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/Server.xml>`__"

.. csv-table:: Service (ServerserviceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","maltrail","serverservice","reconfigure",""
    "``GET``","maltrail","serverservice","restart",""
    "``GET``","maltrail","serverservice","start",""
    "``GET``","maltrail","serverservice","status",""
    "``GET``","maltrail","serverservice","stop",""

    "``<<uses>>``", "", "", "", "*model* `Server.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/Server.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","maltrail","service","reconfigure",""
    "``GET``","maltrail","service","restart",""
    "``GET``","maltrail","service","start",""
    "``GET``","maltrail","service","status",""
    "``GET``","maltrail","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Sensor.xml <https://github.com/opnsense/plugins/blob/master/security/maltrail/src/opnsense/mvc/app/models/OPNsense/Maltrail/Sensor.xml>`__"
