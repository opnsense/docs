Radvd
~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radvd","service","reconfigure",""
    "``POST``","radvd","service","restart",""
    "``POST``","radvd","service","start",""
    "``GET``","radvd","service","status",""
    "``POST``","radvd","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","radvd","settings","add_entry",""
    "``POST``","radvd","settings","del_entry","$uuid"
    "``GET``","radvd","settings","get",""
    "``GET``","radvd","settings","get_entry","$uuid=null"
    "``GET,POST``","radvd","settings","search_entry",""
    "``POST``","radvd","settings","set",""
    "``POST``","radvd","settings","set_entry","$uuid"
    "``POST``","radvd","settings","toggle_entry","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Radvd.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Radvd/Radvd.xml>`__"
