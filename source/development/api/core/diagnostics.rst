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

.. csv-table:: Service (DnsDiagnosticsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","dns_diagnostics","get",""
    "``GET``","diagnostics","dns_diagnostics","set",""
    "``POST``","diagnostics","dns_diagnostics","set",""

    "``<<uses>>``", "", "", "", "*model* `DnsDiagnostics.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/DnsDiagnostics.xml>`__"

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
    "``GET``","diagnostics","firewall","pfStatistics","$section=null"
    "``POST``","diagnostics","firewall","queryPfTop",""
    "``POST``","diagnostics","firewall","queryStates",""
    "``GET``","diagnostics","firewall","stats",""

.. csv-table:: Resources (InterfaceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","diagnostics","interface","CarpStatus","$status"
    "``POST``","diagnostics","interface","delRoute",""
    "``POST``","diagnostics","interface","flushArp",""
    "``GET``","diagnostics","interface","getArp",""
    "``GET``","diagnostics","interface","getBpfStatistics",""
    "``GET``","diagnostics","interface","getInterfaceConfig",""
    "``GET``","diagnostics","interface","getInterfaceNames",""
    "``GET``","diagnostics","interface","getInterfaceStatistics",""
    "``GET``","diagnostics","interface","getMemoryStatistics",""
    "``GET``","diagnostics","interface","getNdp",""
    "``GET``","diagnostics","interface","getNetisrStatistics",""
    "``GET``","diagnostics","interface","getPfSyncNodes",""
    "``GET``","diagnostics","interface","getProtocolStatistics",""
    "``GET``","diagnostics","interface","getRoutes",""
    "``GET``","diagnostics","interface","getSocketStatistics",""
    "``GET``","diagnostics","interface","getVipStatus",""
    "``GET``","diagnostics","interface","searchArp",""
    "``GET``","diagnostics","interface","searchNdp",""

.. csv-table:: Resources (LvtemplateController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","diagnostics","lvtemplate","addItem",""
    "``POST``","diagnostics","lvtemplate","delItem","$uuid"
    "``GET``","diagnostics","lvtemplate","get",""
    "``GET``","diagnostics","lvtemplate","getItem","$uuid=null"
    "``*``","diagnostics","lvtemplate","searchItem",""
    "``POST``","diagnostics","lvtemplate","set",""
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

.. csv-table:: Resources (PacketCaptureController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","packet_capture","download","$jobid"
    "``GET``","diagnostics","packet_capture","get",""
    "``GET``","diagnostics","packet_capture","macInfo","$macaddr"
    "``POST``","diagnostics","packet_capture","remove","$jobid"
    "``GET``","diagnostics","packet_capture","searchJobs",""
    "``GET``","diagnostics","packet_capture","set",""
    "``POST``","diagnostics","packet_capture","set",""
    "``POST``","diagnostics","packet_capture","start","$jobid"
    "``POST``","diagnostics","packet_capture","stop","$jobid"
    "``GET``","diagnostics","packet_capture","view","$jobid,$detail='normal'"

    "``<<uses>>``", "", "", "", "*model* `PacketCapture.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/PacketCapture.xml>`__"

.. csv-table:: Service (PingController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","ping","get",""
    "``POST``","diagnostics","ping","remove","$jobid"
    "``GET``","diagnostics","ping","searchJobs",""
    "``GET``","diagnostics","ping","set",""
    "``POST``","diagnostics","ping","set",""
    "``POST``","diagnostics","ping","start","$jobid"
    "``POST``","diagnostics","ping","stop","$jobid"

    "``<<uses>>``", "", "", "", "*model* `Ping.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Ping.xml>`__"

.. csv-table:: Service (PortprobeController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","portprobe","get",""
    "``GET``","diagnostics","portprobe","set",""
    "``POST``","diagnostics","portprobe","set",""

    "``<<uses>>``", "", "", "", "*model* `Portprobe.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Portprobe.xml>`__"

.. csv-table:: Resources (SystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","system","memory",""

.. csv-table:: Resources (SystemhealthController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","systemhealth","getInterfaces",""
    "``GET``","diagnostics","systemhealth","getRRDlist",""

.. csv-table:: Service (TracerouteController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","traceroute","get",""
    "``GET``","diagnostics","traceroute","set",""
    "``POST``","diagnostics","traceroute","set",""

    "``<<uses>>``", "", "", "", "*model* `Traceroute.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Traceroute.xml>`__"

.. csv-table:: Resources (TrafficController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","traffic","Interface",""
    "``GET``","diagnostics","traffic","Top","$interfaces"
