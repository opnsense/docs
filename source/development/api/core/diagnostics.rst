Diagnostics
~~~~~~~~~~~

.. csv-table:: Resources (ActivityController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","activity","getActivity",""

.. csv-table:: Resources (DnsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","dns","reverseLookup",""

.. csv-table:: Resources (FirewallController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","diagnostics","firewall","delState","$stateid,$creatorid"
    "``POST``","diagnostics","firewall","flushSources",""
    "``POST``","diagnostics","firewall","flushStates",""
    "``POST``","diagnostics","firewall","killStates",""
    "``GET``","diagnostics","firewall","listRuleIds",""
    "``GET``","diagnostics","firewall","log",""
    "``GET``","diagnostics","firewall","logFilters",""
    "``POST``","diagnostics","firewall","queryPfTop",""
    "``POST``","diagnostics","firewall","queryStates",""
    "``GET``","diagnostics","firewall","stats",""

.. csv-table:: Resources (InterfaceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","diagnostics","interface","delRoute",""
    "``POST``","diagnostics","interface","flushArp",""
    "``GET``","diagnostics","interface","getArp",""
    "``GET``","diagnostics","interface","getBpfStatistics",""
    "``GET``","diagnostics","interface","getInterfaceNames",""
    "``GET``","diagnostics","interface","getInterfaceStatistics",""
    "``GET``","diagnostics","interface","getMemoryStatistics",""
    "``GET``","diagnostics","interface","getNdp",""
    "``GET``","diagnostics","interface","getNetisrStatistics",""
    "``GET``","diagnostics","interface","getProtocolStatistics",""
    "``GET``","diagnostics","interface","getRoutes",""
    "``GET``","diagnostics","interface","getSocketStatistics",""

.. csv-table:: Resources (LvtemplateController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","diagnostics","lvtemplate","addItem",""
    "``POST``","diagnostics","lvtemplate","delItem","$uuid"
    "``GET``","diagnostics","lvtemplate","get",""
    "``GET``","diagnostics","lvtemplate","getItem","$uuid=null"
    "``*``","diagnostics","lvtemplate","searchItem",""
    "``GET``","diagnostics","lvtemplate","set",""
    "``POST``","diagnostics","lvtemplate","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Lvtemplate.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Lvtemplate.xml>`__"

.. csv-table:: Resources (NetflowController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","netflow","cacheStats",""
    "``GET``","diagnostics","netflow","getconfig",""
    "``GET``","diagnostics","netflow","isEnabled",""
    "``POST``","diagnostics","netflow","reconfigure",""
    "``GET``","diagnostics","netflow","setconfig",""
    "``GET``","diagnostics","netflow","status",""

.. csv-table:: Resources (NetworkinsightController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","networkinsight","getInterfaces",""
    "``GET``","diagnostics","networkinsight","getMetadata",""
    "``GET``","diagnostics","networkinsight","getProtocols",""
    "``GET``","diagnostics","networkinsight","getServices",""

.. csv-table:: Resources (SystemhealthController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","systemhealth","getInterfaces",""
    "``GET``","diagnostics","systemhealth","getRRDlist",""

.. csv-table:: Resources (TrafficController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","traffic","Interface",""
    "``GET``","diagnostics","traffic","Top","$interfaces"
