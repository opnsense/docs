Wol
~~~

.. csv-table:: Resources (WolController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","wol","wol","add_host",""
    "``POST``","wol","wol","del_host","$uuid"
    "``GET``","wol","wol","get",""
    "``GET``","wol","wol","get_host","$uuid=null"
    "``GET``","wol","wol","getwake",""
    "``*``","wol","wol","search_host",""
    "``POST``","wol","wol","set",""
    "``POST``","wol","wol","set",""
    "``POST``","wol","wol","set_host","$uuid"
    "``POST``","wol","wol","wakeall",""

    "``<<uses>>``", "", "", "", "*model* `Wol.xml <https://github.com/opnsense/plugins/blob/master/net/wol/src/opnsense/mvc/app/models/OPNsense/Wol/Wol.xml>`__"
