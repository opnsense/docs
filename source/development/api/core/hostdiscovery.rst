Hostdiscovery
~~~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","hostdiscovery","service","reconfigure",""
    "``POST``","hostdiscovery","service","restart",""
    "``GET``","hostdiscovery","service","search",""
    "``POST``","hostdiscovery","service","start",""
    "``GET``","hostdiscovery","service","status",""
    "``POST``","hostdiscovery","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","hostdiscovery","settings","get",""
    "``POST``","hostdiscovery","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `Hostwatch.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Hostdiscovery/Hostwatch.xml>`__"
