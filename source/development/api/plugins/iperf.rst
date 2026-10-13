Iperf
~~~~~

.. csv-table:: Resources (ClientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","iperf","client","get",""
    "``GET``","iperf","client","remove","$jobid"
    "``POST``","iperf","client","run_job","$jobid,$action"
    "``GET``","iperf","client","search_jobs",""
    "``POST``","iperf","client","set",""
    "``GET``","iperf","client","start","$jobid"
    "``GET``","iperf","client","stop","$jobid"
    "``GET``","iperf","client","view","$jobid"

    "``<<uses>>``", "", "", "", "*model* `Client.xml <https://github.com/opnsense/plugins/blob/master/benchmarks/iperf/src/opnsense/mvc/app/models/OPNsense/iperf/Client.xml>`__"

.. csv-table:: Resources (InstanceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","iperf","instance","get",""
    "``GET``","iperf","instance","remove","$jobId"
    "``POST``","iperf","instance","run_job","$jobId,$action"
    "``GET``","iperf","instance","search_jobs",""
    "``POST``","iperf","instance","set",""
    "``GET``","iperf","instance","start","$jobId"
    "``GET``","iperf","instance","stop","$jobId"
    "``GET``","iperf","instance","view","$jobId"

    "``<<uses>>``", "", "", "", "*model* `Instance.xml <https://github.com/opnsense/plugins/blob/master/benchmarks/iperf/src/opnsense/mvc/app/models/OPNsense/iperf/Instance.xml>`__"
