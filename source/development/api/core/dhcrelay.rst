Dhcrelay
~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dhcrelay","service","reconfigure",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dhcrelay","settings","addDest",""
    "``POST``","dhcrelay","settings","addRelay",""
    "``POST``","dhcrelay","settings","delDest","$uuid"
    "``POST``","dhcrelay","settings","delRelay","$uuid"
    "``GET``","dhcrelay","settings","get",""
    "``GET``","dhcrelay","settings","getDest","$uuid=null"
    "``GET``","dhcrelay","settings","getRelay","$uuid=null"
    "``*``","dhcrelay","settings","searchDest",""
    "``*``","dhcrelay","settings","searchRelay",""
    "``POST``","dhcrelay","settings","set",""
    "``POST``","dhcrelay","settings","setDest","$uuid"
    "``POST``","dhcrelay","settings","setRelay","$uuid"
    "``POST``","dhcrelay","settings","toggleRelay","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `DHCRelay.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/DHCRelay/DHCRelay.xml>`__"
