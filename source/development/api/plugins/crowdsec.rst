Crowdsec
~~~~~~~~

.. csv-table:: Resources (AlertsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","alerts","search",""

.. csv-table:: Resources (AppsecconfigsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","appsecconfigs","search",""

.. csv-table:: Resources (AppsecrulesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","appsecrules","search",""

.. csv-table:: Resources (BouncersController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","bouncers","search",""

.. csv-table:: Resources (CollectionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","collections","search",""

.. csv-table:: Resources (DecisionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","crowdsec","decisions","del","$decision_id"
    "``GET``","crowdsec","decisions","search",""

.. csv-table:: Resources (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","general","get",""
    "``POST``","crowdsec","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/security/crowdsec/src/opnsense/mvc/app/models/OPNsense/CrowdSec/General.xml>`__"

.. csv-table:: Resources (MachinesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","machines","search",""

.. csv-table:: Resources (ParsersController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","parsers","search",""

.. csv-table:: Resources (PostoverflowsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","postoverflows","search",""

.. csv-table:: Resources (ScenariosController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","scenarios","search",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","crowdsec","service","reload",""
    "``GET``","crowdsec","service","status",""

.. csv-table:: Resources (VersionController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","crowdsec","version","get",""
