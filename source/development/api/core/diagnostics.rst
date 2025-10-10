Diagnostics
~~~~~~~~~~~

.. csv-table:: Resources (ActivityController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","activity","get_activity",""

.. csv-table:: Resources (CpuUsageController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","cpu_usage","get_c_p_u_type",""
    "``GET``","diagnostics","cpu_usage","stream",""

.. csv-table:: Resources (DnsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","dns","reverse_lookup",""

.. csv-table:: Resources (DnsDiagnosticsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","dns_diagnostics","get",""
    "``POST``","diagnostics","dns_diagnostics","set",""

    "``<<uses>>``", "", "", "", "*model* `DnsDiagnostics.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/DnsDiagnostics.xml>`__"

.. csv-table:: Resources (FirewallController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","diagnostics","firewall","del_state","$stateid,$creatorid"
    "``POST``","diagnostics","firewall","flush_sources",""
    "``POST``","diagnostics","firewall","flush_states",""
    "``POST``","diagnostics","firewall","kill_states",""
    "``GET``","diagnostics","firewall","list_rule_ids",""
    "``GET``","diagnostics","firewall","log",""
    "``GET``","diagnostics","firewall","log_filters",""
    "``GET``","diagnostics","firewall","pf_states",""
    "``GET``","diagnostics","firewall","pf_statistics","$section=null"
    "``POST``","diagnostics","firewall","query_pf_top",""
    "``POST``","diagnostics","firewall","query_states",""
    "``GET``","diagnostics","firewall","stats",""
    "``GET``","diagnostics","firewall","stream_log",""

.. csv-table:: Resources (InterfaceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","diagnostics","interface","_carp_status","$status"
    "``POST``","diagnostics","interface","del_route",""
    "``POST``","diagnostics","interface","flush_arp",""
    "``GET``","diagnostics","interface","get_arp",""
    "``GET``","diagnostics","interface","get_bpf_statistics",""
    "``GET``","diagnostics","interface","get_interface_config",""
    "``GET``","diagnostics","interface","get_interface_names",""
    "``GET``","diagnostics","interface","get_interface_statistics",""
    "``GET``","diagnostics","interface","get_memory_statistics",""
    "``GET``","diagnostics","interface","get_ndp",""
    "``GET``","diagnostics","interface","get_netisr_statistics",""
    "``GET``","diagnostics","interface","get_pfsync_nodes",""
    "``GET``","diagnostics","interface","get_protocol_statistics",""
    "``GET``","diagnostics","interface","get_routes",""
    "``GET``","diagnostics","interface","get_socket_statistics",""
    "``GET``","diagnostics","interface","get_vip_status",""
    "``GET``","diagnostics","interface","search_arp",""
    "``GET``","diagnostics","interface","search_ndp",""

.. csv-table:: Resources (LvtemplateController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","diagnostics","lvtemplate","add_item",""
    "``POST``","diagnostics","lvtemplate","del_item","$uuid"
    "``GET``","diagnostics","lvtemplate","get",""
    "``GET``","diagnostics","lvtemplate","get_item","$uuid=null"
    "``GET,POST``","diagnostics","lvtemplate","search_item",""
    "``POST``","diagnostics","lvtemplate","set",""
    "``POST``","diagnostics","lvtemplate","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Lvtemplate.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Lvtemplate.xml>`__"

.. csv-table:: Resources (NetflowController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","netflow","cache_stats",""
    "``GET``","diagnostics","netflow","getconfig",""
    "``GET``","diagnostics","netflow","is_enabled",""
    "``POST``","diagnostics","netflow","reconfigure",""
    "``POST``","diagnostics","netflow","setconfig",""
    "``GET``","diagnostics","netflow","status",""

.. csv-table:: Resources (NetworkinsightController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","networkinsight","export","$provider=null,$from_date=null,$to_date=null,$resolution=null"
    "``GET``","diagnostics","networkinsight","get_interfaces",""
    "``GET``","diagnostics","networkinsight","get_metadata",""
    "``GET``","diagnostics","networkinsight","get_protocols",""
    "``GET``","diagnostics","networkinsight","get_services",""
    "``GET``","diagnostics","networkinsight","timeserie","$provider=null,$measure=null,$from_date=null,$to_date=null,$resolution=null,$field=null,$emulation=null"
    "``GET``","diagnostics","networkinsight","top","$provider=null,$from_date=null,$to_date=null,$field=null,$measure=null,$max_hits=null"

.. csv-table:: Resources (PacketCaptureController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","packet_capture","download","$jobid"
    "``GET``","diagnostics","packet_capture","get",""
    "``GET``","diagnostics","packet_capture","mac_info","$macaddr"
    "``POST``","diagnostics","packet_capture","remove","$jobid"
    "``GET``","diagnostics","packet_capture","search_jobs",""
    "``POST``","diagnostics","packet_capture","set",""
    "``POST``","diagnostics","packet_capture","start","$jobid"
    "``POST``","diagnostics","packet_capture","stop","$jobid"
    "``GET``","diagnostics","packet_capture","view","$jobid,$detail=normal"

    "``<<uses>>``", "", "", "", "*model* `PacketCapture.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/PacketCapture.xml>`__"

.. csv-table:: Resources (PingController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","ping","get",""
    "``POST``","diagnostics","ping","remove","$jobid"
    "``GET``","diagnostics","ping","search_jobs",""
    "``POST``","diagnostics","ping","set",""
    "``POST``","diagnostics","ping","start","$jobid"
    "``POST``","diagnostics","ping","stop","$jobid"

    "``<<uses>>``", "", "", "", "*model* `Ping.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Ping.xml>`__"

.. csv-table:: Resources (PortprobeController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","portprobe","get",""
    "``POST``","diagnostics","portprobe","set",""

    "``<<uses>>``", "", "", "", "*model* `Portprobe.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Portprobe.xml>`__"

.. csv-table:: Resources (SystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","system","memory",""
    "``GET``","diagnostics","system","system_disk",""
    "``GET``","diagnostics","system","system_information",""
    "``GET``","diagnostics","system","system_mbuf",""
    "``GET``","diagnostics","system","system_resources",""
    "``GET``","diagnostics","system","system_swap",""
    "``GET``","diagnostics","system","system_temperature",""
    "``GET``","diagnostics","system","system_time",""

.. csv-table:: Resources (SystemhealthController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","systemhealth","export_as_c_s_v","$rrd='',$detail=-1"
    "``GET``","diagnostics","systemhealth","get_interfaces",""
    "``GET``","diagnostics","systemhealth","get_rrd_list",""
    "``GET``","diagnostics","systemhealth","get_system_health","$rrd='',$detail=-1"

.. csv-table:: Resources (TracerouteController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","traceroute","get",""
    "``POST``","diagnostics","traceroute","set",""

    "``<<uses>>``", "", "", "", "*model* `Traceroute.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Diagnostics/Traceroute.xml>`__"

.. csv-table:: Resources (TrafficController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","traffic","_interface",""
    "``GET``","diagnostics","traffic","_top","$interfaces"
    "``GET``","diagnostics","traffic","stream","$poll_interval=1"
