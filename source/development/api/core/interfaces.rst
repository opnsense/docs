Interfaces
~~~~~~~~~~

.. csv-table:: Resources (LaggSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","lagg_settings","addItem",""
    "``POST``","interfaces","lagg_settings","delItem","$uuid"
    "``GET``","interfaces","lagg_settings","get",""
    "``GET``","interfaces","lagg_settings","getItem","$uuid=null"
    "``POST``","interfaces","lagg_settings","reconfigure",""
    "``*``","interfaces","lagg_settings","searchItem",""
    "``POST``","interfaces","lagg_settings","set",""
    "``POST``","interfaces","lagg_settings","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Lagg.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Lagg.xml>`__"

.. csv-table:: Resources (LoopbackSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","loopback_settings","addItem",""
    "``POST``","interfaces","loopback_settings","delItem","$uuid"
    "``GET``","interfaces","loopback_settings","get",""
    "``GET``","interfaces","loopback_settings","getItem","$uuid=null"
    "``POST``","interfaces","loopback_settings","reconfigure",""
    "``*``","interfaces","loopback_settings","searchItem",""
    "``POST``","interfaces","loopback_settings","set",""
    "``POST``","interfaces","loopback_settings","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Loopback.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Loopback.xml>`__"

.. csv-table:: Resources (NeighborSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","neighbor_settings","addItem",""
    "``POST``","interfaces","neighbor_settings","delItem","$uuid"
    "``GET``","interfaces","neighbor_settings","get",""
    "``GET``","interfaces","neighbor_settings","getItem","$uuid=null"
    "``POST``","interfaces","neighbor_settings","reconfigure",""
    "``*``","interfaces","neighbor_settings","searchItem",""
    "``POST``","interfaces","neighbor_settings","set",""
    "``POST``","interfaces","neighbor_settings","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Neighbor.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Neighbor.xml>`__"

.. csv-table:: Resources (OverviewController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","interfaces","overview","export",""
    "``GET``","interfaces","overview","getInterface","$if=null"
    "``GET``","interfaces","overview","interfacesInfo","$details=false"
    "``GET``","interfaces","overview","reloadInterface","$identifier=null"

.. csv-table:: Resources (VipSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","vip_settings","addItem",""
    "``POST``","interfaces","vip_settings","delItem","$uuid"
    "``GET``","interfaces","vip_settings","get",""
    "``GET``","interfaces","vip_settings","getItem","$uuid=null"
    "``GET``","interfaces","vip_settings","getUnusedVhid",""
    "``POST``","interfaces","vip_settings","reconfigure",""
    "``*``","interfaces","vip_settings","searchItem",""
    "``POST``","interfaces","vip_settings","set",""
    "``POST``","interfaces","vip_settings","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Vip.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Vip.xml>`__"

.. csv-table:: Resources (VlanSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","vlan_settings","addItem",""
    "``POST``","interfaces","vlan_settings","delItem","$uuid"
    "``GET``","interfaces","vlan_settings","get",""
    "``GET``","interfaces","vlan_settings","getItem","$uuid=null"
    "``POST``","interfaces","vlan_settings","reconfigure",""
    "``*``","interfaces","vlan_settings","searchItem",""
    "``POST``","interfaces","vlan_settings","set",""
    "``POST``","interfaces","vlan_settings","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Vlan.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Vlan.xml>`__"

.. csv-table:: Resources (VxlanSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","vxlan_settings","addItem",""
    "``POST``","interfaces","vxlan_settings","delItem","$uuid"
    "``GET``","interfaces","vxlan_settings","get",""
    "``GET``","interfaces","vxlan_settings","getItem","$uuid=null"
    "``POST``","interfaces","vxlan_settings","reconfigure",""
    "``*``","interfaces","vxlan_settings","searchItem",""
    "``POST``","interfaces","vxlan_settings","set",""
    "``POST``","interfaces","vxlan_settings","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `VxLan.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/VxLan.xml>`__"
