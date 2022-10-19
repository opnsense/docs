Crowdsec
~~~~~~~~

.. csv-table:: Resources (AlertsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","alerts","get",""

.. csv-table:: Resources (BouncersController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","bouncers","get",""

.. csv-table:: Resources (CollectionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","collections","get",""

.. csv-table:: Resources (DecisionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","decisions","delete","$decision_id"
    "``GET``","crowdsec","decisions","get",""

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","general","get",""
    "``POST``","crowdsec","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/security/crowdsec/src/opnsense/mvc/app/models/OPNsense/CrowdSec/General.xml>`__"

.. csv-table:: Resources (MachinesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","machines","get",""

.. csv-table:: Resources (ParsersController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","parsers","get",""

.. csv-table:: Resources (PostoverflowsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","postoverflows","get",""

.. csv-table:: Resources (ScenariosController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","scenarios","get",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","service","debug",""
    "``POST``","crowdsec","service","reload",""
    "``GET``","crowdsec","service","status",""

.. csv-table:: Resources (VersionController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","version","get",""
