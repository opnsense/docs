Proxy
~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","proxy","service","downloadacls",""
    "``POST``","proxy","service","fetchacls",""
    "``POST``","proxy","service","refreshTemplate",""
    "``POST``","proxy","service","reset",""

    "``<<uses>>``", "", "", "", "*model* `Proxy.xml <https://github.com/opnsense/core/blob/master/../core/src/opnsense/mvc/app/models/OPNsense/Proxy/Proxy.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","proxy","settings","addPACMatch",""
    "``POST``","proxy","settings","addPACProxy",""
    "``POST``","proxy","settings","addPACRule",""
    "``POST``","proxy","settings","addRemoteBlacklist",""
    "``POST``","proxy","settings","delPACMatch","$uuid"
    "``POST``","proxy","settings","delPACProxy","$uuid"
    "``POST``","proxy","settings","delPACRule","$uuid"
    "``POST``","proxy","settings","delRemoteBlacklist","$uuid"
    "``POST``","proxy","settings","fetchRBCron",""
    "``GET``","proxy","settings","getPACMatch","$uuid=null"
    "``GET``","proxy","settings","getPACProxy","$uuid=null"
    "``GET``","proxy","settings","getPACRule","$uuid=null"
    "``GET``","proxy","settings","getRemoteBlacklist","$uuid=null"
    "``*``","proxy","settings","searchPACMatch",""
    "``*``","proxy","settings","searchPACProxy",""
    "``*``","proxy","settings","searchPACRule",""
    "``GET``","proxy","settings","searchRemoteBlacklists",""
    "``POST``","proxy","settings","setPACMatch","$uuid"
    "``POST``","proxy","settings","setPACProxy","$uuid"
    "``POST``","proxy","settings","setPACRule","$uuid"
    "``POST``","proxy","settings","setRemoteBlacklist","$uuid"
    "``POST``","proxy","settings","togglePACRule","$uuid"
    "``POST``","proxy","settings","toggleRemoteBlacklist","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Proxy.xml <https://github.com/opnsense/core/blob/master/../core/src/opnsense/mvc/app/models/OPNsense/Proxy/Proxy.xml>`__"
