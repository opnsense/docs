Ipsec
~~~~~

.. csv-table:: Resources (ConnectionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","connections","add_child",""
    "``POST``","ipsec","connections","add_connection",""
    "``POST``","ipsec","connections","add_local",""
    "``POST``","ipsec","connections","add_remote",""
    "``GET``","ipsec","connections","connection_exists","$uuid"
    "``POST``","ipsec","connections","del_child","$uuid"
    "``POST``","ipsec","connections","del_connection","$uuid"
    "``POST``","ipsec","connections","del_local","$uuid"
    "``POST``","ipsec","connections","del_remote","$uuid"
    "``GET``","ipsec","connections","get",""
    "``GET``","ipsec","connections","get_child","$uuid=null"
    "``GET``","ipsec","connections","get_connection","$uuid=null"
    "``GET``","ipsec","connections","get_local","$uuid=null"
    "``GET``","ipsec","connections","get_remote","$uuid=null"
    "``GET``","ipsec","connections","is_enabled",""
    "``POST,GET``","ipsec","connections","search_child",""
    "``POST,GET``","ipsec","connections","search_connection",""
    "``POST,GET``","ipsec","connections","search_local",""
    "``POST,GET``","ipsec","connections","search_remote",""
    "``POST``","ipsec","connections","set",""
    "``POST``","ipsec","connections","set_child","$uuid=null"
    "``POST``","ipsec","connections","set_connection","$uuid=null"
    "``POST``","ipsec","connections","set_local","$uuid=null"
    "``POST``","ipsec","connections","set_remote","$uuid=null"
    "``GET``","ipsec","connections","swanctl",""
    "``POST``","ipsec","connections","toggle","$enabled=null"
    "``POST``","ipsec","connections","toggle_child","$uuid,$enabled=null"
    "``POST``","ipsec","connections","toggle_connection","$uuid,$enabled=null"
    "``POST``","ipsec","connections","toggle_local","$uuid,$enabled=null"
    "``POST``","ipsec","connections","toggle_remote","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Swanctl.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/Swanctl.xml>`__"

.. csv-table:: Resources (KeyPairsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","key_pairs","add_item",""
    "``POST``","ipsec","key_pairs","del_item","$uuid"
    "``GET``","ipsec","key_pairs","gen_key_pair","$type,$size=null"
    "``GET``","ipsec","key_pairs","get",""
    "``GET``","ipsec","key_pairs","get_item","$uuid=null"
    "``POST,GET``","ipsec","key_pairs","search_item",""
    "``POST``","ipsec","key_pairs","set",""
    "``POST``","ipsec","key_pairs","set_item","$uuid=null"

    "``<<uses>>``", "", "", "", "*model* `IPsec.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/IPsec.xml>`__"

.. csv-table:: Resources (LeasesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ipsec","leases","pools",""
    "``GET``","ipsec","leases","search",""

.. csv-table:: Resources (LegacySubsystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","legacy_subsystem","apply_config",""
    "``GET``","ipsec","legacy_subsystem","status",""

.. csv-table:: Resources (ManualSpdController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","manual_spd","add",""
    "``POST``","ipsec","manual_spd","del","$uuid"
    "``GET``","ipsec","manual_spd","get","$uuid=null"
    "``POST,GET``","ipsec","manual_spd","search",""
    "``POST``","ipsec","manual_spd","set","$uuid=null"
    "``POST``","ipsec","manual_spd","toggle","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Swanctl.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/Swanctl.xml>`__"

.. csv-table:: Resources (PoolsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","pools","add",""
    "``POST``","ipsec","pools","del","$uuid"
    "``GET``","ipsec","pools","get","$uuid=null"
    "``POST,GET``","ipsec","pools","search",""
    "``POST``","ipsec","pools","set","$uuid=null"
    "``POST``","ipsec","pools","toggle","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Swanctl.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/Swanctl.xml>`__"

.. csv-table:: Resources (PreSharedKeysController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","pre_shared_keys","add_item",""
    "``POST``","ipsec","pre_shared_keys","del_item","$uuid"
    "``GET``","ipsec","pre_shared_keys","get",""
    "``GET``","ipsec","pre_shared_keys","get_item","$uuid=null"
    "``POST,GET``","ipsec","pre_shared_keys","search_item",""
    "``POST``","ipsec","pre_shared_keys","set",""
    "``POST``","ipsec","pre_shared_keys","set_item","$uuid=null"

    "``<<uses>>``", "", "", "", "*model* `IPsec.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/IPsec.xml>`__"

.. csv-table:: Resources (SadController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","sad","delete","$id"
    "``GET``","ipsec","sad","search",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","service","reconfigure",""
    "``POST``","ipsec","service","restart",""
    "``POST``","ipsec","service","start",""
    "``GET``","ipsec","service","status",""
    "``POST``","ipsec","service","stop",""

.. csv-table:: Resources (SessionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","sessions","connect","$id"
    "``POST``","ipsec","sessions","disconnect","$id"
    "``GET``","ipsec","sessions","search_phase1",""
    "``GET``","ipsec","sessions","search_phase2",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ipsec","settings","get",""
    "``POST``","ipsec","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `IPsec.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/IPsec.xml>`__"

.. csv-table:: Resources (SpdController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","spd","delete","$id"
    "``GET``","ipsec","spd","search",""

.. csv-table:: Resources (TunnelController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","tunnel","del_phase1","$ikeid"
    "``POST``","ipsec","tunnel","del_phase2","$seqid"
    "``GET``","ipsec","tunnel","search_phase1",""
    "``GET``","ipsec","tunnel","search_phase2",""
    "``POST``","ipsec","tunnel","toggle","$enabled=null"
    "``POST``","ipsec","tunnel","toggle_phase1","$ikeid,$enabled=null"
    "``POST``","ipsec","tunnel","toggle_phase2","$seqid,$enabled=null"

.. csv-table:: Resources (VtiController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","vti","add",""
    "``POST``","ipsec","vti","del","$uuid"
    "``GET``","ipsec","vti","get","$uuid=null"
    "``POST,GET``","ipsec","vti","search",""
    "``POST``","ipsec","vti","set","$uuid=null"
    "``POST``","ipsec","vti","toggle","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Swanctl.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/Swanctl.xml>`__"
