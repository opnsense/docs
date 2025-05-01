Trust
~~~~~

.. csv-table:: Resources (CaController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","trust","ca","ca_info","$caref"
    "``GET``","trust","ca","ca_list",""
    "``POST``","trust","ca","del","$uuid"
    "``POST``","trust","ca","generate_file","$uuid=null,$type=crt"
    "``GET``","trust","ca","get",""
    "``GET``","trust","ca","raw_dump","$uuid"
    "``POST,GET``","trust","ca","search",""
    "``POST``","trust","ca","set","$uuid=null"

    "``<<uses>>``", "", "", "", "*model* `Ca.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Trust/Ca.xml>`__"

.. csv-table:: Resources (CertController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","trust","cert","add",""
    "``GET``","trust","cert","ca_info","$caref=null"
    "``GET``","trust","cert","ca_list",""
    "``POST``","trust","cert","del","$uuid"
    "``POST``","trust","cert","generate_file","$uuid=null,$type=crt"
    "``GET``","trust","cert","get","$uuid=null"
    "``GET``","trust","cert","raw_dump","$uuid"
    "``POST,GET``","trust","cert","search",""
    "``POST``","trust","cert","set","$uuid=null"
    "``GET``","trust","cert","user_list",""

    "``<<uses>>``", "", "", "", "*model* `Cert.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Trust/Cert.xml>`__"

.. csv-table:: Resources (CrlController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","trust","crl","del","$caref"
    "``GET``","trust","crl","get","$caref"
    "``GET``","trust","crl","get_ocsp_info_data","$caref"
    "``GET``","trust","crl","raw_dump","$caref"
    "``GET``","trust","crl","search",""
    "``POST``","trust","crl","set","$caref"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","trust","settings","get",""
    "``POST``","trust","settings","reconfigure",""
    "``POST``","trust","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Trust/General.xml>`__"
