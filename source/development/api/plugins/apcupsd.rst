Apcupsd
~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","apcupsd","service","get_ups_status",""
    "``POST``","apcupsd","service","reconfigure",""
    "``POST``","apcupsd","service","restart",""
    "``POST``","apcupsd","service","start",""
    "``GET``","apcupsd","service","status",""
    "``POST``","apcupsd","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Apcupsd.xml <https://github.com/opnsense/plugins/blob/master/sysutils/apcupsd/src/opnsense/mvc/app/models/OPNsense/Apcupsd/Apcupsd.xml>`__"

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","apcupsd","settings","get",""
    "``POST``","apcupsd","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `Apcupsd.xml <https://github.com/opnsense/plugins/blob/master/sysutils/apcupsd/src/opnsense/mvc/app/models/OPNsense/Apcupsd/Apcupsd.xml>`__"
