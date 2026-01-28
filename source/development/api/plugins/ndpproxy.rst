Ndpproxy
~~~~~~~~

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ndpproxy","general","add_alias",""
    "``POST``","ndpproxy","general","del_alias","$uuid"
    "``GET``","ndpproxy","general","get",""
    "``GET``","ndpproxy","general","get_alias","$uuid=null"
    "``GET,POST``","ndpproxy","general","search_alias",""
    "``POST``","ndpproxy","general","set",""
    "``POST``","ndpproxy","general","set_alias","$uuid"

    "``<<uses>>``", "", "", "", "*model* `NdpProxy.xml <https://github.com/opnsense/plugins/blob/master/net/ndp-proxy-go/src/opnsense/mvc/app/models/OPNsense/NdpProxy/NdpProxy.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ndpproxy","service","reconfigure",""
    "``POST``","ndpproxy","service","restart",""
    "``POST``","ndpproxy","service","start",""
    "``GET``","ndpproxy","service","status",""
    "``POST``","ndpproxy","service","stop",""
