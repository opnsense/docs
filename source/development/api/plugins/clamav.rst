Clamav
~~~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","clamav","general","get",""
    "``POST``","clamav","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/security/clamav/src/opnsense/mvc/app/models/OPNsense/ClamAV/General.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","clamav","service","freshclam",""
    "``POST``","clamav","service","reconfigure",""
    "``POST``","clamav","service","restart",""
    "``POST``","clamav","service","start",""
    "``GET``","clamav","service","status",""
    "``POST``","clamav","service","stop",""
    "``GET``","clamav","service","version",""

.. csv-table:: Resources (UrlController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","clamav","url","add_url",""
    "``POST``","clamav","url","del_url","$uuid"
    "``GET``","clamav","url","get",""
    "``GET``","clamav","url","get_url","$uuid=null"
    "``POST,GET``","clamav","url","search_url",""
    "``POST``","clamav","url","set",""
    "``POST``","clamav","url","set_url","$uuid"
    "``POST``","clamav","url","toggle_url","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Url.xml <https://github.com/opnsense/plugins/blob/master/security/clamav/src/opnsense/mvc/app/models/OPNsense/ClamAV/Url.xml>`__"
