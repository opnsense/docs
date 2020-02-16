Trafficshaper
~~~~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","trafficshaper","service","flushreload",""
    "``POST``","trafficshaper","service","reconfigure",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","trafficshaper","settings","addPipe",""
    "``POST``","trafficshaper","settings","addQueue",""
    "``POST``","trafficshaper","settings","addRule",""
    "``POST``","trafficshaper","settings","delPipe","$uuid"
    "``POST``","trafficshaper","settings","delQueue","$uuid"
    "``POST``","trafficshaper","settings","delRule","$uuid"
    "``GET``","trafficshaper","settings","getPipe","$uuid=null"
    "``GET``","trafficshaper","settings","getQueue","$uuid=null"
    "``GET``","trafficshaper","settings","getRule","$uuid=null"
    "``*``","trafficshaper","settings","searchPipes",""
    "``*``","trafficshaper","settings","searchQueues",""
    "``*``","trafficshaper","settings","searchRules",""
    "``POST``","trafficshaper","settings","setPipe","$uuid"
    "``POST``","trafficshaper","settings","setQueue","$uuid"
    "``POST``","trafficshaper","settings","setRule","$uuid"
    "``POST``","trafficshaper","settings","togglePipe","$uuid,$enabled=null"
    "``POST``","trafficshaper","settings","toggleQueue","$uuid,$enabled=null"
    "``POST``","trafficshaper","settings","toggleRule","$uuid,$enabled=null"

