Collectd
~~~~~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","collectd","general","get",""
    "``POST``","collectd","general","set",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","collectd","service","reconfigure",""
    "``POST``","collectd","service","restart",""
    "``POST``","collectd","service","start",""
    "``GET``","collectd","service","status",""
    "``POST``","collectd","service","stop",""
