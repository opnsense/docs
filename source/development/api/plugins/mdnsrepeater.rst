Mdnsrepeater
~~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","mdnsrepeater","service","restart",""
    "``GET``","mdnsrepeater","service","start",""
    "``GET``","mdnsrepeater","service","status",""
    "``GET``","mdnsrepeater","service","stop",""

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","mdnsrepeater","settings","get",""
    "``GET``","mdnsrepeater","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `MDNSRepeater.xml <https://github.com/opnsense/plugins/blob/master/net/mdns-repeater/src/opnsense/mvc/app/models/OPNsense/MDNSRepeater/MDNSRepeater.xml>`__"
