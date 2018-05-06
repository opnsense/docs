Routes
~~~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","routes","routes","reconfigure",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","routes","routes","addroute",""
   "``POST``","routes","routes","delroute","$uuid"
   "``GET``","routes","routes","getroute","$uuid"
   "``GET``","routes","routes","searchroute",""
   "``POST``","routes","routes","setroute","$uuid"
   "``POST``","routes","routes","toggleroute","$uuid/$disabled"
