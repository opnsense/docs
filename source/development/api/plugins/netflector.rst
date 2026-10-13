Netflector
~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","netflector","service","reconfigure",""
    "``POST``","netflector","service","restart",""
    "``POST``","netflector","service","start",""
    "``GET``","netflector","service","status",""
    "``POST``","netflector","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","netflector","settings","add_reflector",""
    "``POST``","netflector","settings","del_reflector","$uuid"
    "``GET``","netflector","settings","get",""
    "``GET``","netflector","settings","get_reflector","$uuid=null"
    "``GET,POST``","netflector","settings","search_reflector",""
    "``POST``","netflector","settings","set",""
    "``POST``","netflector","settings","set_reflector","$uuid"
    "``POST``","netflector","settings","toggle_reflector","$uuids,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Netflector.xml <https://github.com/opnsense/plugins/blob/master/net/netflector/src/opnsense/mvc/app/models/OPNsense/Netflector/Netflector.xml>`__"
