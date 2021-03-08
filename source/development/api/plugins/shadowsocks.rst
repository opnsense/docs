Shadowsocks
~~~~~~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","shadowsocks","general","get",""
    "``GET``","shadowsocks","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/shadowsocks/src/opnsense/mvc/app/models/OPNsense/Shadowsocks/General.xml>`__"

.. csv-table:: Service (LocalController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","shadowsocks","local","get",""
    "``GET``","shadowsocks","local","set",""

    "``<<uses>>``", "", "", "", "*model* `Local.xml <https://github.com/opnsense/plugins/blob/master/net/shadowsocks/src/opnsense/mvc/app/models/OPNsense/Shadowsocks/Local.xml>`__"

.. csv-table:: Service (LocalserviceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","shadowsocks","localservice","reconfigure",""
    "``GET``","shadowsocks","localservice","restart",""
    "``GET``","shadowsocks","localservice","start",""
    "``GET``","shadowsocks","localservice","status",""
    "``GET``","shadowsocks","localservice","stop",""

    "``<<uses>>``", "", "", "", "*model* `Local.xml <https://github.com/opnsense/plugins/blob/master/net/shadowsocks/src/opnsense/mvc/app/models/OPNsense/Shadowsocks/Local.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","shadowsocks","service","reconfigure",""
    "``GET``","shadowsocks","service","restart",""
    "``GET``","shadowsocks","service","start",""
    "``GET``","shadowsocks","service","status",""
    "``GET``","shadowsocks","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/shadowsocks/src/opnsense/mvc/app/models/OPNsense/Shadowsocks/General.xml>`__"
