Core
~~~~

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

.. csv-table:: Resources (SystemController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","system","dismissStatus",""
    "``POST``","core","system","halt",""
    "``POST``","core","system","reboot",""
    "``GET``","core","system","status",""
