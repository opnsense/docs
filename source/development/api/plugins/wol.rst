Wol
~~~

.. csv-table:: Resources (WolController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wol","wol","addHost",""
    "``POST``","wol","wol","delHost","$uuid"
    "``GET``","wol","wol","getHost","$uuid=null"
    "``GET``","wol","wol","getwake",""
    "``*``","wol","wol","searchHost",""
    "``POST``","wol","wol","set",""
    "``POST``","wol","wol","setHost","$uuid"
    "``POST``","wol","wol","wakeall",""

    "``<<uses>>``", "", "", "", "*model* `Wol.xml <https://github.com/opnsense/plugins/blob/master/net/wol/src/opnsense/mvc/app/models/OPNsense/Wol/Wol.xml>`__"
