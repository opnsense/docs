Acmeclient
~~~~~~~~~~

.. csv-table:: Resources (AccountsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","acmeclient","accounts","add",""
    "``POST``","acmeclient","accounts","del","$uuid"
    "``GET``","acmeclient","accounts","get","$uuid=null"
    "``GET``","acmeclient","accounts","get",""
    "``POST``","acmeclient","accounts","register","$uuid"
    "``*``","acmeclient","accounts","search",""
    "``GET``","acmeclient","accounts","set",""
    "``POST``","acmeclient","accounts","toggle","$uuid,$enabled=null"
    "``POST``","acmeclient","accounts","update","$uuid"

    "``<<uses>>``", "", "", "", "*model* `AcmeClient.xml <https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml>`__"

.. csv-table:: Resources (ActionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","acmeclient","actions","add",""
    "``POST``","acmeclient","actions","del","$uuid"
    "``GET``","acmeclient","actions","get","$uuid=null"
    "``GET``","acmeclient","actions","get",""
    "``*``","acmeclient","actions","search",""
    "``GET``","acmeclient","actions","set",""
    "``GET``","acmeclient","actions","sftpGetIdentity",""
    "``GET``","acmeclient","actions","sftpTestConnection",""
    "``POST``","acmeclient","actions","toggle","$uuid,$enabled=null"
    "``POST``","acmeclient","actions","update","$uuid"

    "``<<uses>>``", "", "", "", "*model* `AcmeClient.xml <https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml>`__"

.. csv-table:: Resources (CertificatesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","acmeclient","certificates","add",""
    "``GET``","acmeclient","certificates","automation","$uuid"
    "``POST``","acmeclient","certificates","del","$uuid"
    "``GET``","acmeclient","certificates","get","$uuid=null"
    "``GET``","acmeclient","certificates","get",""
    "``GET``","acmeclient","certificates","removekey","$uuid"
    "``POST``","acmeclient","certificates","revoke","$uuid"
    "``*``","acmeclient","certificates","search",""
    "``GET``","acmeclient","certificates","set",""
    "``POST``","acmeclient","certificates","sign","$uuid"
    "``POST``","acmeclient","certificates","toggle","$uuid,$enabled=null"
    "``POST``","acmeclient","certificates","update","$uuid"

    "``<<uses>>``", "", "", "", "*model* `AcmeClient.xml <https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","acmeclient","service","configtest",""
    "``POST``","acmeclient","service","reconfigure",""
    "``GET``","acmeclient","service","reset",""
    "``POST``","acmeclient","service","restart",""
    "``GET``","acmeclient","service","signallcerts",""
    "``POST``","acmeclient","service","start",""
    "``GET``","acmeclient","service","status",""
    "``POST``","acmeclient","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","acmeclient","settings","fetchCronIntegration",""
    "``POST``","acmeclient","settings","fetchHAProxyIntegration",""
    "``GET``","acmeclient","settings","get",""
    "``GET``","acmeclient","settings","getBindPluginStatus",""
    "``GET``","acmeclient","settings","getGcloudPluginStatus",""
    "``GET``","acmeclient","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `AcmeClient.xml <https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml>`__"

.. csv-table:: Resources (ValidationsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","acmeclient","validations","add",""
    "``POST``","acmeclient","validations","del","$uuid"
    "``GET``","acmeclient","validations","get","$uuid=null"
    "``GET``","acmeclient","validations","get",""
    "``*``","acmeclient","validations","search",""
    "``GET``","acmeclient","validations","set",""
    "``POST``","acmeclient","validations","toggle","$uuid,$enabled=null"
    "``POST``","acmeclient","validations","update","$uuid"

    "``<<uses>>``", "", "", "", "*model* `AcmeClient.xml <https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml>`__"
