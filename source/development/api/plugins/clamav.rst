Clamav
~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","clamav","service","freshclam",""
    "``GET``","clamav","service","version",""

.. csv-table:: Resources (UrlController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","clamav","url","addUrl",""
    "``POST``","clamav","url","delUrl","$uuid"
    "``GET``","clamav","url","getUrl","$uuid=null"
    "``*``","clamav","url","searchUrl",""
    "``POST``","clamav","url","setUrl","$uuid"
    "``POST``","clamav","url","toggleUrl","$uuid"
