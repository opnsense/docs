Openvpn
~~~~~~~

.. csv-table:: Resources (ExportController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","openvpn","export","accounts","$vpnid=null"
    "``POST``","openvpn","export","download","$vpnid,$certref=null"
    "``GET``","openvpn","export","providers",""
    "``POST``","openvpn","export","storePresets","$vpnid"
    "``GET``","openvpn","export","templates",""
    "``POST``","openvpn","export","validatePresets","$vpnid"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","openvpn","service","killSession",""
    "``POST``","openvpn","service","restartService","$id=null"
    "``GET``","openvpn","service","searchRoutes",""
    "``GET``","openvpn","service","searchSessions",""
    "``POST``","openvpn","service","startService","$id=null"
    "``POST``","openvpn","service","stopService","$id=null"
