Ndpproxy
~~~~~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ndpproxy","general","get",""
    "``POST``","ndpproxy","general","set",""

    "``<<uses>>``", "", "", "", "*model* `NdpProxy.xml <https://github.com/opnsense/plugins/blob/master/net/ndp-proxy-go/src/opnsense/mvc/app/models/OPNsense/NdpProxy/NdpProxy.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ndpproxy","service","reconfigure",""
    "``POST``","ndpproxy","service","restart",""
    "``POST``","ndpproxy","service","start",""
    "``GET``","ndpproxy","service","status",""
    "``POST``","ndpproxy","service","stop",""
