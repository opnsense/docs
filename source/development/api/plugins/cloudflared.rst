Cloudflared
~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","cloudflared","service","reconfigure",""
    "``POST``","cloudflared","service","restart",""
    "``POST``","cloudflared","service","start",""
    "``GET``","cloudflared","service","status",""
    "``POST``","cloudflared","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","cloudflared","settings","get",""
    "``POST``","cloudflared","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `Cloudflared.xml <https://github.com/opnsense/plugins/blob/master/net/cloudflared/src/opnsense/mvc/app/models/OPNsense/Cloudflared/Cloudflared.xml>`__"
