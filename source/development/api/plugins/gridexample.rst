Gridexample
~~~~~~~~~~~

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","gridexample","settings","add_item",""
    "``POST``","gridexample","settings","del_item","$uuid"
    "``GET``","gridexample","settings","get",""
    "``GET``","gridexample","settings","get_item","$uuid=null"
    "``POST,GET``","gridexample","settings","search_item",""
    "``POST``","gridexample","settings","set",""
    "``POST``","gridexample","settings","set_item","$uuid"
    "``POST``","gridexample","settings","toggle_item","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `GridExample.xml <https://github.com/opnsense/plugins/blob/master/devel/grid_example/src/opnsense/mvc/app/models/OPNsense/GridExample/GridExample.xml>`__"
