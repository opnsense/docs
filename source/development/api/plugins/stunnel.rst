Stunnel
~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","stunnel","service","reconfigure",""
    "``POST``","stunnel","service","restart",""
    "``POST``","stunnel","service","start",""
    "``GET``","stunnel","service","status",""
    "``POST``","stunnel","service","stop",""

.. csv-table:: Service (ServicesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","stunnel","services","add_item",""
    "``POST``","stunnel","services","del_item","$uuid"
    "``GET``","stunnel","services","get",""
    "``GET``","stunnel","services","get_item","$uuid=null"
    "``GET,POST``","stunnel","services","search_item",""
    "``POST``","stunnel","services","set",""
    "``POST``","stunnel","services","set_item","$uuid"
    "``POST``","stunnel","services","toggle_item","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Stunnel.xml <https://github.com/opnsense/plugins/blob/master/security/stunnel/src/opnsense/mvc/app/models/OPNsense/Stunnel/Stunnel.xml>`__"
