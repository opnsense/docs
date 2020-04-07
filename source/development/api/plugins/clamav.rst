Clamav
~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","clamav","service","freshclam",""
    "``GET``","clamav","service","version",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/security/clamav/src/opnsense/mvc/app/models/OPNsense/ClamAV/General.xml>`__"

.. csv-table:: Resources (UrlController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","clamav","url","addUrl",""
    "``POST``","clamav","url","delUrl","$uuid"
    "``GET``","clamav","url","getUrl","$uuid=null"
    "``*``","clamav","url","searchUrl",""
    "``POST``","clamav","url","setUrl","$uuid"
    "``POST``","clamav","url","toggleUrl","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Url.xml <https://github.com/opnsense/plugins/blob/master/security/clamav/src/opnsense/mvc/app/models/OPNsense/ClamAV/Url.xml>`__"
