Trafficshaper
~~~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","trafficshaper","service","flushreload",""
    "``POST``","trafficshaper","service","reconfigure",""
    "``GET``","trafficshaper","service","statistics",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","trafficshaper","settings","add_pipe",""
    "``POST``","trafficshaper","settings","add_queue",""
    "``POST``","trafficshaper","settings","add_rule",""
    "``POST``","trafficshaper","settings","del_pipe","$uuid"
    "``POST``","trafficshaper","settings","del_queue","$uuid"
    "``POST``","trafficshaper","settings","del_rule","$uuid"
    "``GET``","trafficshaper","settings","get",""
    "``GET``","trafficshaper","settings","get_pipe","$uuid=null"
    "``GET``","trafficshaper","settings","get_queue","$uuid=null"
    "``GET``","trafficshaper","settings","get_rule","$uuid=null"
    "``*``","trafficshaper","settings","search_pipes",""
    "``*``","trafficshaper","settings","search_queues",""
    "``*``","trafficshaper","settings","search_rules",""
    "``POST``","trafficshaper","settings","set",""
    "``POST``","trafficshaper","settings","set_pipe","$uuid"
    "``POST``","trafficshaper","settings","set_queue","$uuid"
    "``POST``","trafficshaper","settings","set_rule","$uuid"
    "``POST``","trafficshaper","settings","toggle_pipe","$uuid,$enabled=null"
    "``POST``","trafficshaper","settings","toggle_queue","$uuid,$enabled=null"
    "``POST``","trafficshaper","settings","toggle_rule","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `TrafficShaper.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/TrafficShaper/TrafficShaper.xml>`__"
