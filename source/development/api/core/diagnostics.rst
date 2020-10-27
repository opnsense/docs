Diagnostics
~~~~~~~~~~~

.. csv-table:: Resources (ActivityController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","activity","getActivity",""

.. csv-table:: Resources (DnsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","dns","reverse_lookup",""

.. csv-table:: Resources (FirewallController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","diagnostics","firewall","log",""
    "``GET``","diagnostics","firewall","log_filters",""
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
