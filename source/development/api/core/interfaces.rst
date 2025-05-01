Interfaces
~~~~~~~~~~

.. csv-table:: Resources (GifSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","gif_settings","add_item",""
    "``POST``","interfaces","gif_settings","del_item","$uuid"
    "``GET``","interfaces","gif_settings","get",""
    "``GET``","interfaces","gif_settings","get_if_options",""
    "``GET``","interfaces","gif_settings","get_item","$uuid=null"
    "``POST``","interfaces","gif_settings","reconfigure",""
    "``GET,POST``","interfaces","gif_settings","search_item",""
    "``POST``","interfaces","gif_settings","set",""
    "``POST``","interfaces","gif_settings","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Gif.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Gif.xml>`__"

.. csv-table:: Resources (GreSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","gre_settings","add_item",""
    "``POST``","interfaces","gre_settings","del_item","$uuid"
    "``GET``","interfaces","gre_settings","get",""
    "``GET``","interfaces","gre_settings","get_if_options",""
    "``GET``","interfaces","gre_settings","get_item","$uuid=null"
    "``POST``","interfaces","gre_settings","reconfigure",""
    "``GET,POST``","interfaces","gre_settings","search_item",""
    "``POST``","interfaces","gre_settings","set",""
    "``POST``","interfaces","gre_settings","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Gre.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Gre.xml>`__"

.. csv-table:: Resources (LaggSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","lagg_settings","add_item",""
    "``POST``","interfaces","lagg_settings","del_item","$uuid"
    "``GET``","interfaces","lagg_settings","get",""
    "``GET``","interfaces","lagg_settings","get_item","$uuid=null"
    "``POST``","interfaces","lagg_settings","reconfigure",""
    "``GET,POST``","interfaces","lagg_settings","search_item",""
    "``POST``","interfaces","lagg_settings","set",""
    "``POST``","interfaces","lagg_settings","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Lagg.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Lagg.xml>`__"

.. csv-table:: Resources (LoopbackSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","loopback_settings","add_item",""
    "``POST``","interfaces","loopback_settings","del_item","$uuid"
    "``GET``","interfaces","loopback_settings","get",""
    "``GET``","interfaces","loopback_settings","get_item","$uuid=null"
    "``POST``","interfaces","loopback_settings","reconfigure",""
    "``GET,POST``","interfaces","loopback_settings","search_item",""
    "``POST``","interfaces","loopback_settings","set",""
    "``POST``","interfaces","loopback_settings","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Loopback.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Loopback.xml>`__"

.. csv-table:: Resources (NeighborSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","neighbor_settings","add_item",""
    "``POST``","interfaces","neighbor_settings","del_item","$uuid"
    "``GET``","interfaces","neighbor_settings","get",""
    "``GET``","interfaces","neighbor_settings","get_item","$uuid=null"
    "``POST``","interfaces","neighbor_settings","reconfigure",""
    "``GET,POST``","interfaces","neighbor_settings","search_item",""
    "``POST``","interfaces","neighbor_settings","set",""
    "``POST``","interfaces","neighbor_settings","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Neighbor.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Neighbor.xml>`__"

.. csv-table:: Resources (OverviewController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","interfaces","overview","export",""
    "``GET``","interfaces","overview","get_interface","$if=null"
    "``GET``","interfaces","overview","interfaces_info","$details=false"
    "``GET``","interfaces","overview","reload_interface","$identifier=null"

.. csv-table:: Resources (VipSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","vip_settings","add_item",""
    "``POST``","interfaces","vip_settings","del_item","$uuid"
    "``GET``","interfaces","vip_settings","get",""
    "``GET``","interfaces","vip_settings","get_item","$uuid=null"
    "``GET``","interfaces","vip_settings","get_unused_vhid",""
    "``POST``","interfaces","vip_settings","reconfigure",""
    "``GET,POST``","interfaces","vip_settings","search_item",""
    "``POST``","interfaces","vip_settings","set",""
    "``POST``","interfaces","vip_settings","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Vip.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Vip.xml>`__"

.. csv-table:: Resources (VlanSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","vlan_settings","add_item",""
    "``POST``","interfaces","vlan_settings","del_item","$uuid"
    "``GET``","interfaces","vlan_settings","get",""
    "``GET``","interfaces","vlan_settings","get_item","$uuid=null"
    "``POST``","interfaces","vlan_settings","reconfigure",""
    "``GET,POST``","interfaces","vlan_settings","search_item",""
    "``POST``","interfaces","vlan_settings","set",""
    "``POST``","interfaces","vlan_settings","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Vlan.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Vlan.xml>`__"

.. csv-table:: Resources (VxlanSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","vxlan_settings","add_item",""
    "``POST``","interfaces","vxlan_settings","del_item","$uuid"
    "``GET``","interfaces","vxlan_settings","get",""
    "``GET``","interfaces","vxlan_settings","get_item","$uuid=null"
    "``POST``","interfaces","vxlan_settings","reconfigure",""
    "``GET,POST``","interfaces","vxlan_settings","search_item",""
    "``POST``","interfaces","vxlan_settings","set",""
    "``POST``","interfaces","vxlan_settings","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `VxLan.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/VxLan.xml>`__"
