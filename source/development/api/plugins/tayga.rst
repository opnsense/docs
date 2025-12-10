Tayga
~~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","tayga","general","get",""
    "``POST``","tayga","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/tayga/src/opnsense/mvc/app/models/OPNsense/Tayga/General.xml>`__"

.. csv-table:: Resources (MappingController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tayga","mapping","add_staticmapping",""
    "``POST``","tayga","mapping","del_staticmapping","$uuid"
    "``GET``","tayga","mapping","get",""
    "``GET``","tayga","mapping","get_staticmapping","$uuid=null"
    "``GET,POST``","tayga","mapping","search_staticmapping",""
    "``POST``","tayga","mapping","set",""
    "``POST``","tayga","mapping","set_staticmapping","$uuid"
    "``POST``","tayga","mapping","toggle_staticmapping","$uuid"

    "``<<uses>>``", "", "", "", "*model* `StaticMapping.xml <https://github.com/opnsense/plugins/blob/master/net/tayga/src/opnsense/mvc/app/models/OPNsense/Tayga/StaticMapping.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","tayga","service","reconfigure",""
    "``POST``","tayga","service","restart",""
    "``POST``","tayga","service","start",""
    "``GET``","tayga","service","status",""
    "``POST``","tayga","service","stop",""
