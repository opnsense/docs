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

    "``POST``","telegraf","key","addKey",""
    "``POST``","telegraf","key","delKey","$uuid"
    "``GET``","telegraf","key","getKey","$uuid=null"
    "``*``","telegraf","key","searchKey",""
    "``POST``","telegraf","key","setKey","$uuid"
    "``POST``","telegraf","key","toggleKey","$uuid"

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
