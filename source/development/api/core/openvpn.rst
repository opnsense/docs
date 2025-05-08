Openvpn
~~~~~~~

.. csv-table:: Resources (ClientOverwritesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","openvpn","client_overwrites","add",""
    "``POST``","openvpn","client_overwrites","del","$uuid"
    "``GET``","openvpn","client_overwrites","get","$uuid=null"
    "``GET,POST``","openvpn","client_overwrites","search",""
    "``POST``","openvpn","client_overwrites","set","$uuid=null"
    "``POST``","openvpn","client_overwrites","toggle","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `OpenVPN.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/OpenVPN/OpenVPN.xml>`__"

.. csv-table:: Resources (ExportController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","openvpn","export","accounts","$vpnid=null"
    "``POST``","openvpn","export","download","$vpnid,$certref=null"
    "``GET``","openvpn","export","providers",""
    "``POST``","openvpn","export","store_presets","$vpnid"
    "``GET``","openvpn","export","templates",""
    "``POST``","openvpn","export","validate_presets","$vpnid"

.. csv-table:: Resources (InstancesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","openvpn","instances","add",""
    "``POST``","openvpn","instances","add_static_key",""
    "``POST``","openvpn","instances","del","$uuid"
    "``POST``","openvpn","instances","del_static_key","$uuid"
    "``GET``","openvpn","instances","gen_key","$type=secret"
    "``GET``","openvpn","instances","get","$uuid=null"
    "``GET``","openvpn","instances","get_static_key","$uuid=null"
    "``GET,POST``","openvpn","instances","search",""
    "``GET,POST``","openvpn","instances","search_static_key",""
    "``POST``","openvpn","instances","set","$uuid=null"
    "``POST``","openvpn","instances","set_static_key","$uuid=null"
    "``POST``","openvpn","instances","toggle","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `OpenVPN.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/OpenVPN/OpenVPN.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","openvpn","service","kill_session",""
    "``POST``","openvpn","service","reconfigure",""
    "``POST``","openvpn","service","restart_service","$id=null"
    "``GET``","openvpn","service","search_routes",""
    "``GET``","openvpn","service","search_sessions",""
    "``POST``","openvpn","service","start_service","$id=null"
    "``POST``","openvpn","service","stop_service","$id=null"
