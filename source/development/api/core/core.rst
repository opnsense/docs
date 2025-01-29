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

.. csv-table:: Resources (DashboardController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","dashboard","getDashboard",""
    "``GET``","core","dashboard","picture",""
    "``GET``","core","dashboard","productInfoFeed",""
    "``POST``","core","dashboard","restoreDefaults",""
    "``POST``","core","dashboard","saveWidgets",""

.. csv-table:: Service (HasyncController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","hasync","get",""
    "``POST``","core","hasync","reconfigure",""
    "``POST``","core","hasync","set",""

    "``<<uses>>``", "", "", "", "*model* `Hasync.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Core/Hasync.xml>`__"

.. csv-table:: Resources (HasyncStatusController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","hasync_status","remoteService","$action,$service,$service_id"
    "``POST``","core","hasync_status","restart","$service=null,$service_id=null"
    "``POST``","core","hasync_status","restartAll","$service=null,$service_id=null"
    "``GET``","core","hasync_status","services",""
    "``POST``","core","hasync_status","start","$service=null,$service_id=null"
    "``POST``","core","hasync_status","stop","$service=null,$service_id=null"
    "``GET``","core","hasync_status","version",""

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

.. csv-table:: Resources (SnapshotsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","snapshots","activate","$uuid"
    "``POST``","core","snapshots","add",""
    "``POST``","core","snapshots","del","$uuid"
    "``GET``","core","snapshots","get","$uuid=null"
    "``GET``","core","snapshots","isSupported",""
    "``GET``","core","snapshots","search",""
    "``POST``","core","snapshots","set","$uuid"

.. csv-table:: Resources (SystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","system","dismissStatus",""
    "``POST``","core","system","halt",""
    "``POST``","core","system","reboot",""
    "``GET``","core","system","status",""

.. csv-table:: Resources (TunablesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","tunables","addItem",""
    "``POST``","core","tunables","delItem","$uuid"
    "``GET``","core","tunables","get",""
    "``GET``","core","tunables","getItem","$uuid=null"
    "``POST``","core","tunables","reconfigure",""
    "``POST``","core","tunables","reset",""
    "``*``","core","tunables","searchItem",""
    "``POST``","core","tunables","set",""
    "``POST``","core","tunables","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Tunables.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Core/Tunables.xml>`__"
