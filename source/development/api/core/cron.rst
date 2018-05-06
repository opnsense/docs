Cron
~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","cron","service","reconfigure",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","cron","settings","addjob",""
   "``POST``","cron","settings","deljob","$uuid"
   "``GET``","cron","settings","getjob","$uuid"
   "``GET``","cron","settings","searchjobs",""
   "``POST``","cron","settings","setjob","$uuid"
   "``POST``","cron","settings","togglejob","$uuid/$enabled"
