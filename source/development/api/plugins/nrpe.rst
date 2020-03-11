Nrpe
~~~~

.. csv-table:: Resources (CommandController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","nrpe","command","addCommand",""
    "``POST``","nrpe","command","delCommand","$uuid"
    "``GET``","nrpe","command","getCommand","$uuid=null"
    "``*``","nrpe","command","searchCommand",""
    "``POST``","nrpe","command","setCommand","$uuid"
    "``POST``","nrpe","command","toggleCommand","$uuid"
