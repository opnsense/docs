Core
~~~~

.. csv-table:: Resources (BackupController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","backup","backups","$host"
    "``GET``","core","backup","deleteBackup","$backup"
    "``GET``","core","backup","diff","$host,$backup1,$backup2"
    "``GET``","core","backup","download","$host,$backup=null"
    "``GET``","core","backup","providers",""
    "``GET``","core","backup","revertBackup","$backup"

.. csv-table:: Resources (MenuController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","menu","search",""
    "``GET``","core","menu","tree",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","service","restart","$name,$id=''"
    "``GET``","core","service","search",""
    "``POST``","core","service","start","$name,$id=''"
    "``POST``","core","service","stop","$name,$id=''"

.. csv-table:: Resources (SystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","system","dismissStatus",""
    "``POST``","core","system","halt",""
    "``POST``","core","system","reboot",""
    "``GET``","core","system","status",""
