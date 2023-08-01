Openvpn
~~~~~~~

.. csv-table:: Resources (ClientOverwritesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","openvpn","client_overwrites","add",""
    "``POST``","openvpn","client_overwrites","del","$uuid"
    "``GET``","openvpn","client_overwrites","get","$uuid=null"
    "``GET``","openvpn","client_overwrites","get",""
    "``*``","openvpn","client_overwrites","search",""
    "``POST``","openvpn","client_overwrites","set","$uuid=null"
    "``POST``","openvpn","client_overwrites","set",""
    "``POST``","openvpn","client_overwrites","toggle","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `OpenVPN.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/OpenVPN/OpenVPN.xml>`__"

.. csv-table:: Resources (ExportController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","openvpn","export","accounts","$vpnid=null"
    "``POST``","openvpn","export","download","$vpnid,$certref=null"
    "``GET``","openvpn","export","providers",""
    "``POST``","openvpn","export","storePresets","$vpnid"
    "``GET``","openvpn","export","templates",""
    "``POST``","openvpn","export","validatePresets","$vpnid"

.. csv-table:: Resources (InstancesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","openvpn","instances","add",""
    "``POST``","openvpn","instances","addStaticKey",""
    "``POST``","openvpn","instances","del","$uuid"
    "``GET``","openvpn","instances","delStaticKey","$uuid"
    "``GET``","openvpn","instances","genKey",""
    "``GET``","openvpn","instances","get","$uuid=null"
    "``GET``","openvpn","instances","get",""
    "``GET``","openvpn","instances","getStaticKey","$uuid=null"
    "``*``","openvpn","instances","search",""
    "``*``","openvpn","instances","searchStaticKey",""
    "``POST``","openvpn","instances","set","$uuid=null"
    "``POST``","openvpn","instances","set",""
    "``POST``","openvpn","instances","setStaticKey","$uuid=null"
    "``POST``","openvpn","instances","toggle","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `OpenVPN.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/OpenVPN/OpenVPN.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","openvpn","service","killSession",""
    "``POST``","openvpn","service","reconfigure",""
    "``POST``","openvpn","service","restartService","$id=null"
    "``GET``","openvpn","service","searchRoutes",""
    "``GET``","openvpn","service","searchSessions",""
    "``POST``","openvpn","service","startService","$id=null"
    "``POST``","openvpn","service","stopService","$id=null"
