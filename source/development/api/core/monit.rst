Monit
~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","monit","service","check",""
    "``POST``","monit","service","reconfigure",""
    "``POST``","monit","service","restart",""
    "``POST``","monit","service","start",""
    "``GET``","monit","service","status",""
    "``POST``","monit","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","monit","settings","add_alert",""
    "``POST``","monit","settings","add_service",""
    "``POST``","monit","settings","add_test",""
    "``POST``","monit","settings","del_alert","$uuid"
    "``POST``","monit","settings","del_service","$uuid"
    "``POST``","monit","settings","del_test","$uuid"
    "``GET``","monit","settings","get",""
    "``GET``","monit","settings","get_alert","$uuid=null"
    "``GET``","monit","settings","get_general",""
    "``GET``","monit","settings","get_service","$uuid=null"
    "``GET``","monit","settings","get_test","$uuid=null"
    "``GET,POST``","monit","settings","search_alert",""
    "``GET,POST``","monit","settings","search_service",""
    "``GET,POST``","monit","settings","search_test",""
    "``POST``","monit","settings","set",""
    "``POST``","monit","settings","set_alert","$uuid"
    "``POST``","monit","settings","set_service","$uuid"
    "``POST``","monit","settings","set_test","$uuid"
    "``POST``","monit","settings","toggle_alert","$uuid,$enabled=null"
    "``POST``","monit","settings","toggle_service","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Monit.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Monit/Monit.xml>`__"

.. csv-table:: Resources (StatusController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","monit","status","get","$format=xml"
