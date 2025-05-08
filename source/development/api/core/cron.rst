Cron
~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","cron","service","reconfigure",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","cron","settings","add_job",""
    "``POST``","cron","settings","del_job","$uuid"
    "``GET``","cron","settings","get",""
    "``GET``","cron","settings","get_job","$uuid=null"
    "``GET,POST``","cron","settings","search_jobs",""
    "``POST``","cron","settings","set",""
    "``POST``","cron","settings","set_job","$uuid"
    "``POST``","cron","settings","toggle_job","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Cron.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Cron/Cron.xml>`__"
