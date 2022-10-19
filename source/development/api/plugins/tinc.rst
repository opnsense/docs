Tinc
~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tinc","service","reconfigure",""
    "``POST``","tinc","service","restart",""
    "``POST``","tinc","service","start",""
    "``POST``","tinc","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tinc","settings","delHost","$uuid"
    "``POST``","tinc","settings","delNetwork","$uuid"
    "``GET``","tinc","settings","get",""
    "``GET``","tinc","settings","getHost","$uuid=null"
    "``GET``","tinc","settings","getNetwork","$uuid=null"
    "``GET``","tinc","settings","searchHost",""
    "``GET``","tinc","settings","searchNetwork",""
    "``POST``","tinc","settings","set",""
    "``POST``","tinc","settings","setHost","$uuid=null"
    "``POST``","tinc","settings","setNetwork","$uuid=null"
    "``POST``","tinc","settings","toggleHost","$uuid,$enabled=null"
    "``POST``","tinc","settings","toggleNetwork","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Tinc.xml <https://github.com/opnsense/plugins/blob/master/security/tinc/src/opnsense/mvc/app/models/OPNsense/Tinc/Tinc.xml>`__"
