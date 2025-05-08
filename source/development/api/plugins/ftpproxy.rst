Ftpproxy
~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ftpproxy","service","config",""
    "``GET``","ftpproxy","service","reload",""
    "``GET``","ftpproxy","service","restart","$uuid"
    "``GET``","ftpproxy","service","start","$uuid"
    "``GET``","ftpproxy","service","status","$uuid"
    "``GET``","ftpproxy","service","stop","$uuid"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ftpproxy","settings","add_proxy",""
    "``POST``","ftpproxy","settings","del_proxy","$uuid"
    "``GET``","ftpproxy","settings","get_proxy","$uuid=null"
    "``GET``","ftpproxy","settings","search_proxy",""
    "``POST``","ftpproxy","settings","set_proxy","$uuid"
    "``POST``","ftpproxy","settings","toggle_proxy","$uuid"
