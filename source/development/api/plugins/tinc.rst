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

    "``POST``","tinc","settings","del_host","$uuid"
    "``POST``","tinc","settings","del_network","$uuid"
    "``GET``","tinc","settings","get",""
    "``GET``","tinc","settings","get_host","$uuid=null"
    "``GET``","tinc","settings","get_network","$uuid=null"
    "``GET``","tinc","settings","search_host",""
    "``GET``","tinc","settings","search_network",""
    "``POST``","tinc","settings","set",""
    "``POST``","tinc","settings","set_host","$uuid=null"
    "``POST``","tinc","settings","set_network","$uuid=null"
    "``POST``","tinc","settings","toggle_host","$uuid,$enabled=null"
    "``POST``","tinc","settings","toggle_network","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Tinc.xml <https://github.com/opnsense/plugins/blob/master/security/tinc/src/opnsense/mvc/app/models/OPNsense/Tinc/Tinc.xml>`__"
