Dhcpv4
~~~~~~

.. csv-table:: Resources (LeasesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dhcpv4","leases","delLease","$ip"
    "``GET``","dhcpv4","leases","searchLease",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dhcpv4","service","reconfigure",""
    "``POST``","dhcpv4","service","restart",""
    "``POST``","dhcpv4","service","start",""
    "``GET``","dhcpv4","service","status",""
    "``POST``","dhcpv4","service","stop",""
