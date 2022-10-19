Ipsec
~~~~~

.. csv-table:: Resources (KeyPairsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","key_pairs","addItem",""
    "``POST``","ipsec","key_pairs","delItem","$uuid"
    "``GET``","ipsec","key_pairs","genKeyPair","$type,$size=null"
    "``GET``","ipsec","key_pairs","get",""
    "``GET``","ipsec","key_pairs","getItem","$uuid=null"
    "``*``","ipsec","key_pairs","searchItem",""
    "``POST``","ipsec","key_pairs","set",""
    "``POST``","ipsec","key_pairs","setItem","$uuid=null"

    "``<<uses>>``", "", "", "", "*model* `IPsec.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/IPsec.xml>`__"

.. csv-table:: Resources (LeasesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ipsec","leases","pools",""
    "``GET``","ipsec","leases","search",""

.. csv-table:: Resources (LegacySubsystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","legacy_subsystem","applyConfig",""
    "``GET``","ipsec","legacy_subsystem","status",""

.. csv-table:: Resources (PreSharedKeysController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","pre_shared_keys","addItem",""
    "``POST``","ipsec","pre_shared_keys","delItem","$uuid"
    "``GET``","ipsec","pre_shared_keys","get",""
    "``GET``","ipsec","pre_shared_keys","getItem","$uuid=null"
    "``*``","ipsec","pre_shared_keys","searchItem",""
    "``POST``","ipsec","pre_shared_keys","set",""
    "``POST``","ipsec","pre_shared_keys","setItem","$uuid=null"

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

    "``<<uses>>``", "", "", "", "*model* `IPsec.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/IPsec.xml>`__"

.. csv-table:: Resources (SessionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","sessions","connect","$id"
    "``POST``","ipsec","sessions","disconnect","$id"
    "``GET``","ipsec","sessions","searchPhase1",""
    "``GET``","ipsec","sessions","searchPhase2",""

.. csv-table:: Resources (SpdController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","spd","delete","$id"
    "``GET``","ipsec","spd","search",""

.. csv-table:: Resources (TunnelController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","tunnel","delPhase1","$ikeid"
    "``POST``","ipsec","tunnel","delPhase2","$seqid"
    "``GET``","ipsec","tunnel","searchPhase1",""
    "``GET``","ipsec","tunnel","searchPhase2",""
    "``POST``","ipsec","tunnel","toggle","$enabled=null"
    "``POST``","ipsec","tunnel","togglePhase1","$ikeid,$enabled=null"
    "``POST``","ipsec","tunnel","togglePhase2","$seqid,$enabled=null"
