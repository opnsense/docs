Routing
~~~~~~~

.. csv-table:: Resources (GroupSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","routing","group_settings","add",""
    "``POST``","routing","group_settings","del","$uuids"
    "``GET``","routing","group_settings","get","$uuid=null"
    "``POST``","routing","group_settings","reconfigure",""
    "``GET,POST``","routing","group_settings","search",""
    "``POST``","routing","group_settings","set","$uuid=null"

    "``<<uses>>``", "", "", "", "*model* `GatewayGroups.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Routing/GatewayGroups.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","routing","settings","add_gateway",""
    "``POST``","routing","settings","del_gateway","$uuid"
    "``GET``","routing","settings","get",""
    "``GET``","routing","settings","get_gateway","$uuid=null"
    "``POST``","routing","settings","reconfigure",""
    "``GET``","routing","settings","search_gateway",""
    "``POST``","routing","settings","set",""
    "``POST``","routing","settings","set_gateway","$uuid"
    "``POST``","routing","settings","toggle_gateway","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Gateways.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Routing/Gateways.xml>`__"
