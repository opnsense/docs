Dhcrelay
~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dhcrelay","service","reconfigure",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dhcrelay","settings","add_dest",""
    "``POST``","dhcrelay","settings","add_relay",""
    "``POST``","dhcrelay","settings","del_dest","$uuid"
    "``POST``","dhcrelay","settings","del_relay","$uuid"
    "``GET``","dhcrelay","settings","get",""
    "``GET``","dhcrelay","settings","get_dest","$uuid=null"
    "``GET``","dhcrelay","settings","get_relay","$uuid=null"
    "``GET,POST``","dhcrelay","settings","search_dest",""
    "``GET,POST``","dhcrelay","settings","search_relay",""
    "``POST``","dhcrelay","settings","set",""
    "``POST``","dhcrelay","settings","set_dest","$uuid"
    "``POST``","dhcrelay","settings","set_relay","$uuid"
    "``POST``","dhcrelay","settings","toggle_relay","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `DHCRelay.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/DHCRelay/DHCRelay.xml>`__"
