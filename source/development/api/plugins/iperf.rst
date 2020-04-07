Iperf
~~~~~

.. csv-table:: Resources (InstanceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","iperf","instance","query",""
    "``GET``","iperf","instance","set",""

    "``<<uses>>``", "", "", "", "*model* `FakeInstance.xml <https://github.com/opnsense/plugins/blob/master/benchmarks/iperf/src/opnsense/mvc/app/models/OPNsense/iperf/FakeInstance.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","iperf","service","restart",""
    "``GET``","iperf","service","start",""
    "``GET``","iperf","service","status",""
    "``GET``","iperf","service","stop",""
