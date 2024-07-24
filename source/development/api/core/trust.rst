Trust
~~~~~

.. csv-table:: Resources (CaController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","trust","ca","add",""
    "``GET``","trust","ca","caInfo","$caref"
    "``GET``","trust","ca","caList",""
    "``POST``","trust","ca","del","$uuid"
    "``POST``","trust","ca","generateFile","$uuid=null,$type='crt'"
    "``GET``","trust","ca","get","$uuid=null"
    "``GET``","trust","ca","get",""
    "``GET``","trust","ca","rawDump","$uuid"
    "``*``","trust","ca","search",""
    "``POST``","trust","ca","set","$uuid=null"
    "``POST``","trust","ca","set",""

    "``<<uses>>``", "", "", "", "*model* `Ca.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Trust/Ca.xml>`__"

.. csv-table:: Resources (CertController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","trust","cert","add",""
    "``GET``","trust","cert","caInfo","$caref"
    "``GET``","trust","cert","caList",""
    "``POST``","trust","cert","del","$uuid"
    "``POST``","trust","cert","generateFile","$uuid=null,$type='crt'"
    "``GET``","trust","cert","get","$uuid=null"
    "``GET``","trust","cert","get",""
    "``GET``","trust","cert","rawDump","$uuid"
    "``*``","trust","cert","search",""
    "``POST``","trust","cert","set","$uuid=null"
    "``POST``","trust","cert","set",""

    "``<<uses>>``", "", "", "", "*model* `Cert.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Trust/Cert.xml>`__"

.. csv-table:: Resources (CrlController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","trust","crl","get","$caref"
    "``GET``","trust","crl","rawDump","$caref"
    "``GET``","trust","crl","search",""
    "``POST``","trust","crl","set","$caref"
