Core
~~~~

.. csv-table:: Resources (BackupController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","backup","backups","$host"
    "``GET``","core","backup","delete_backup","$backup"
    "``GET``","core","backup","diff","$host,$backup1,$backup2"
    "``GET``","core","backup","download","$host,$backup=null"
    "``GET``","core","backup","providers",""
    "``GET``","core","backup","revert_backup","$backup"

.. csv-table:: Resources (DashboardController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","dashboard","get_dashboard",""
    "``GET``","core","dashboard","picture",""
    "``GET``","core","dashboard","product_info_feed",""
    "``POST``","core","dashboard","restore_defaults",""
    "``POST``","core","dashboard","save_widgets",""

.. csv-table:: Resources (HasyncController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","hasync","get",""
    "``POST``","core","hasync","reconfigure",""
    "``POST``","core","hasync","set",""

    "``<<uses>>``", "", "", "", "*model* `Hasync.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Core/Hasync.xml>`__"

.. csv-table:: Resources (HasyncStatusController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","core","hasync_status","remote_service","$action,$service,$service_id"
    "``POST``","core","hasync_status","restart","$service=null,$service_id=null"
    "``POST``","core","hasync_status","restart_all","$service=null,$service_id=null"
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
    "``GET``","core","snapshots","is_supported",""
    "``GET``","core","snapshots","search",""
    "``POST``","core","snapshots","set","$uuid"

.. csv-table:: Resources (SystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","system","dismiss_status",""
    "``POST``","core","system","halt",""
    "``POST``","core","system","reboot",""
    "``GET``","core","system","status",""

.. csv-table:: Resources (TunablesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","tunables","add_item",""
    "``POST``","core","tunables","del_item","$uuid"
    "``GET``","core","tunables","get",""
    "``GET``","core","tunables","get_item","$uuid=null"
    "``POST``","core","tunables","reconfigure",""
    "``POST``","core","tunables","reset",""
    "``GET,POST``","core","tunables","search_item",""
    "``POST``","core","tunables","set",""
    "``POST``","core","tunables","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Tunables.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Core/Tunables.xml>`__"
