Routing
~~~~~~~

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","routing","settings","addGateway",""
    "``POST``","routing","settings","delGateway","$uuid"
    "``GET``","routing","settings","get",""
    "``GET``","routing","settings","getGateway","$uuid=null"
    "``POST``","routing","settings","reconfigure",""
    "``GET``","routing","settings","searchGateway",""
    "``POST``","routing","settings","set",""
    "``POST``","routing","settings","setGateway","$uuid"
    "``POST``","routing","settings","toggleGateway","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Gateways.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Routing/Gateways.xml>`__"
