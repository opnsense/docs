Udpbroadcastrelay
~~~~~~~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","udpbroadcastrelay","service","config",""
    "``GET``","udpbroadcastrelay","service","get",""
    "``POST``","udpbroadcastrelay","service","reload",""
    "``POST``","udpbroadcastrelay","service","restart","$uuid"
    "``GET``","udpbroadcastrelay","service","set",""
    "``POST``","udpbroadcastrelay","service","start","$uuid"
    "``POST``","udpbroadcastrelay","service","status","$uuid"
    "``POST``","udpbroadcastrelay","service","stop","$uuid"

    "``<<uses>>``", "", "", "", "*model* `UDPBroadcastRelay.xml <https://github.com/opnsense/plugins/blob/master/net/udpbroadcastrelay/src/opnsense/mvc/app/models/OPNsense/UDPBroadcastRelay/UDPBroadcastRelay.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","udpbroadcastrelay","settings","addRelay",""
    "``POST``","udpbroadcastrelay","settings","delRelay","$uuid"
    "``GET``","udpbroadcastrelay","settings","get",""
    "``GET``","udpbroadcastrelay","settings","getRelay","$uuid=null"
    "``GET``","udpbroadcastrelay","settings","searchRelay",""
    "``GET``","udpbroadcastrelay","settings","set",""
    "``POST``","udpbroadcastrelay","settings","setRelay","$uuid"
    "``POST``","udpbroadcastrelay","settings","toggleRelay","$uuid"
