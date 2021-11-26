Relayd
~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","relayd","service","configtest",""
    "``POST``","relayd","service","reconfigure",""
    "``GET``","relayd","service","reconfigure",""
    "``GET``","relayd","service","restart",""
    "``GET``","relayd","service","start",""
    "``GET``","relayd","service","status",""
    "``GET``","relayd","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Relayd.xml <https://github.com/opnsense/plugins/blob/master/net/relayd/src/opnsense/mvc/app/models/OPNsense/Relayd/Relayd.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","relayd","settings","del","$nodeType=null,$uuid=null"
    "``GET``","relayd","settings","dirty",""
    "``GET``","relayd","settings","get","$nodeType=null,$uuid=null"
    "``GET``","relayd","settings","get",""
    "``POST``","relayd","settings","search","$nodeType=null"
    "``POST``","relayd","settings","set","$nodeType=null,$uuid=null"
    "``GET``","relayd","settings","set",""
    "``POST``","relayd","settings","toggle","$nodeType,$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Relayd.xml <https://github.com/opnsense/plugins/blob/master/net/relayd/src/opnsense/mvc/app/models/OPNsense/Relayd/Relayd.xml>`__"

.. csv-table:: Resources (StatusController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","relayd","status","sum","$wait=0"
    "``POST``","relayd","status","toggle","$nodeType=null,$id=null,$action=null"
