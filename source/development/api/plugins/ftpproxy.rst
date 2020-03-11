Ftpproxy
~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ftpproxy","service","config",""
    "``POST``","ftpproxy","service","reload",""
    "``POST``","ftpproxy","service","restart","$uuid"
    "``POST``","ftpproxy","service","start","$uuid"
    "``POST``","ftpproxy","service","status","$uuid"
    "``POST``","ftpproxy","service","stop","$uuid"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ftpproxy","settings","addProxy",""
    "``POST``","ftpproxy","settings","delProxy","$uuid"
    "``GET``","ftpproxy","settings","getProxy","$uuid=null"
    "``GET``","ftpproxy","settings","searchProxy",""
    "``POST``","ftpproxy","settings","setProxy","$uuid"
    "``POST``","ftpproxy","settings","toggleProxy","$uuid"
