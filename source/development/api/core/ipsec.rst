Ipsec
~~~~~

.. csv-table:: Resources (KeyPairsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","key_pairs","addItem",""
    "``POST``","ipsec","key_pairs","delItem","$uuid"
    "``GET``","ipsec","key_pairs","getItem","$uuid=null"
    "``*``","ipsec","key_pairs","searchItem",""
    "``POST``","ipsec","key_pairs","setItem","$uuid=null"

.. csv-table:: Resources (LegacySubsystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ipsec","legacy_subsystem","applyConfig",""
    "``GET``","ipsec","legacy_subsystem","status",""
