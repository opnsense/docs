Relayd
~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","relayd","service","configtest",""
    "``POST``","relayd","service","reconfigure",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","relayd","settings","del","$nodeType=null,$uuid=null"
    "``GET``","relayd","settings","dirty",""
    "``GET``","relayd","settings","get","$nodeType=null,$uuid=null"
    "``POST``","relayd","settings","search","$nodeType=null"
    "``POST``","relayd","settings","set","$nodeType=null,$uuid=null"

.. csv-table:: Resources (StatusController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","relayd","status","sum",""
    "``POST``","relayd","status","toggle","$nodeType=null,$id=null,$action=null"
