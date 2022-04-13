Interfaces
~~~~~~~~~~

.. csv-table:: Resources (LoopbackSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","loopback_settings","addItem",""
    "``POST``","interfaces","loopback_settings","delItem","$uuid"
    "``GET``","interfaces","loopback_settings","get",""
    "``GET``","interfaces","loopback_settings","getItem","$uuid=null"
    "``POST``","interfaces","loopback_settings","reconfigure",""
    "``*``","interfaces","loopback_settings","searchItem",""
    "``GET``","interfaces","loopback_settings","set",""
    "``POST``","interfaces","loopback_settings","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Loopback.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/Loopback.xml>`__"

.. csv-table:: Resources (VlanSettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","interfaces","vlan_settings","addItem",""
    "``POST``","interfaces","vlan_settings","delItem","$uuid"
    "``GET``","interfaces","vlan_settings","get",""
    "``GET``","interfaces","vlan_settings","getItem","$uuid=null"
    "``POST``","interfaces","vlan_settings","reconfigure",""
    "``*``","interfaces","vlan_settings","searchItem",""
    "``GET``","interfaces","vlan_settings","set",""
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
    "``GET``","interfaces","vxlan_settings","set",""
    "``POST``","interfaces","vxlan_settings","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `VxLan.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Interfaces/VxLan.xml>`__"
