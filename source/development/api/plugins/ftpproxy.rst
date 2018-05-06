ftpproxy
~~~~~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","ftpproxy","service","reload",""
   "``POST``","ftpproxy","service","restart",""
   "``POST``","ftpproxy","service","start",""
   "``GET``","ftpproxy","service","status",""
   "``POST``","ftpproxy","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","ftpproxy","settings","addproxy",""
   "``POST``","ftpproxy","settings","delproxy","$uuid"
   "``GET``","ftpproxy","settings","getproxy","$uuid"
   "``GET``","ftpproxy","settings","searchproxy",""
   "``POST``","ftpproxy","settings","setproxy","$uuid"
   "``POST``","ftpproxy","settings","toggleproxy","$uuid"
