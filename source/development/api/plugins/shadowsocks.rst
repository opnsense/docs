Shadowsocks
~~~~~~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","shadowsocks","general","get",""
    "``POST``","shadowsocks","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/shadowsocks/src/opnsense/mvc/app/models/OPNsense/Shadowsocks/General.xml>`__"

.. csv-table:: Service (LocalController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","shadowsocks","local","get",""
    "``POST``","shadowsocks","local","set",""

    "``<<uses>>``", "", "", "", "*model* `Local.xml <https://github.com/opnsense/plugins/blob/master/net/shadowsocks/src/opnsense/mvc/app/models/OPNsense/Shadowsocks/Local.xml>`__"

.. csv-table:: Service (LocalserviceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","shadowsocks","localservice","reconfigure",""
    "``POST``","shadowsocks","localservice","restart",""
    "``POST``","shadowsocks","localservice","start",""
    "``GET``","shadowsocks","localservice","status",""
    "``POST``","shadowsocks","localservice","stop",""

    "``<<uses>>``", "", "", "", "*model* `Local.xml <https://github.com/opnsense/plugins/blob/master/net/shadowsocks/src/opnsense/mvc/app/models/OPNsense/Shadowsocks/Local.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","shadowsocks","service","reconfigure",""
    "``POST``","shadowsocks","service","restart",""
    "``POST``","shadowsocks","service","start",""
    "``GET``","shadowsocks","service","status",""
    "``POST``","shadowsocks","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/net/shadowsocks/src/opnsense/mvc/app/models/OPNsense/Shadowsocks/General.xml>`__"
