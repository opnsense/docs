Ndproxy
~~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ndproxy","general","get",""
    "``POST``","ndproxy","general","set",""

    "``<<uses>>``", "", "", "", "*model* `Ndproxy.xml <https://github.com/opnsense/plugins/blob/master/net/ndproxy/src/opnsense/mvc/app/models/OPNsense/Ndproxy/Ndproxy.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ndproxy","service","reconfigure",""
    "``POST``","ndproxy","service","restart",""
    "``POST``","ndproxy","service","start",""
    "``GET``","ndproxy","service","status",""
    "``POST``","ndproxy","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `Ndproxy.xml <https://github.com/opnsense/plugins/blob/master/net/ndproxy/src/opnsense/mvc/app/models/OPNsense/Ndproxy/Ndproxy.xml>`__"
