Ipsec
~~~~~

.. csv-table:: Resources (KeyPairsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","key_pairs","addItem",""
    "``POST``","ipsec","key_pairs","delItem","$uuid"
    "``GET``","ipsec","key_pairs","get",""
    "``GET``","ipsec","key_pairs","getItem","$uuid=null"
    "``*``","ipsec","key_pairs","searchItem",""
    "``GET``","ipsec","key_pairs","set",""
    "``POST``","ipsec","key_pairs","setItem","$uuid=null"

    "``<<uses>>``", "", "", "", "*model* `IPsec.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/IPsec.xml>`__"

.. csv-table:: Resources (LegacySubsystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","legacy_subsystem","applyConfig",""
    "``GET``","ipsec","legacy_subsystem","status",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","ipsec","service","reconfigure",""
    "``GET``","ipsec","service","restart",""
    "``GET``","ipsec","service","start",""
    "``GET``","ipsec","service","status",""
    "``GET``","ipsec","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `IPsec.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IPsec/IPsec.xml>`__"

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
