Routes
~~~~~~

.. csv-table:: Resources (RoutesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","routes","routes","addroute",""
    "``POST``","routes","routes","delroute","$uuid"
    "``GET``","routes","routes","getroute","$uuid=null"
    "``POST``","routes","routes","reconfigure",""
    "``*``","routes","routes","searchroute",""
    "``POST``","routes","routes","setroute","$uuid"
    "``POST``","routes","routes","toggleroute","$uuid,$disabled=null"

