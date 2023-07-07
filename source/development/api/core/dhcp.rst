Dhcp
~~~~

.. csv-table:: Resources (Leases4Controller.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dhcp","leases4","delLease","$ip"
    "``GET``","dhcp","leases4","searchLease",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dhcp","service","restart",""
    "``POST``","dhcp","service","start",""
    "``GET``","dhcp","service","status",""
    "``POST``","dhcp","service","stop",""
