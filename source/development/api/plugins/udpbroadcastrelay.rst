Udpbroadcastrelay
~~~~~~~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","udpbroadcastrelay","service","config",""
    "``GET``","udpbroadcastrelay","service","get",""
    "``GET``","udpbroadcastrelay","service","reload",""
    "``GET``","udpbroadcastrelay","service","restart","$uuid"
    "``POST``","udpbroadcastrelay","service","set",""
    "``GET``","udpbroadcastrelay","service","start","$uuid"
    "``GET``","udpbroadcastrelay","service","status","$uuid"
    "``GET``","udpbroadcastrelay","service","stop","$uuid"

    "``<<uses>>``", "", "", "", "*model* `UDPBroadcastRelay.xml <https://github.com/opnsense/plugins/blob/master/net/udpbroadcastrelay/src/opnsense/mvc/app/models/OPNsense/UDPBroadcastRelay/UDPBroadcastRelay.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","udpbroadcastrelay","settings","add_relay",""
    "``POST``","udpbroadcastrelay","settings","del_relay","$uuid"
    "``GET``","udpbroadcastrelay","settings","get",""
    "``GET``","udpbroadcastrelay","settings","get_relay","$uuid=null"
    "``GET``","udpbroadcastrelay","settings","search_relay",""
    "``POST``","udpbroadcastrelay","settings","set",""
    "``POST``","udpbroadcastrelay","settings","set_relay","$uuid"
    "``POST``","udpbroadcastrelay","settings","toggle_relay","$uuid"
