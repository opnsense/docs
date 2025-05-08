Telegraf
~~~~~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","telegraf","general","get",""
    "``POST``","telegraf","general","set",""

.. csv-table:: Resources (InputController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","telegraf","input","get",""
    "``POST``","telegraf","input","set",""

.. csv-table:: Resources (KeyController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","telegraf","key","add_key",""
    "``POST``","telegraf","key","del_key","$uuid"
    "``GET``","telegraf","key","get",""
    "``GET``","telegraf","key","get_key","$uuid=null"
    "``GET,POST``","telegraf","key","search_key",""
    "``POST``","telegraf","key","set",""
    "``POST``","telegraf","key","set_key","$uuid"
    "``POST``","telegraf","key","toggle_key","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Key.xml <https://github.com/opnsense/plugins/blob/master/net-mgmt/telegraf/src/opnsense/mvc/app/models/OPNsense/Telegraf/Key.xml>`__"

.. csv-table:: Resources (OutputController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","telegraf","output","get",""
    "``POST``","telegraf","output","set",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","telegraf","service","reconfigure",""
    "``POST``","telegraf","service","restart",""
    "``POST``","telegraf","service","start",""
    "``GET``","telegraf","service","status",""
    "``POST``","telegraf","service","stop",""
