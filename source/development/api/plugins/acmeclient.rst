Acmeclient
~~~~~~~~~~

.. csv-table:: Resources (AccountsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","acmeclient","accounts","add",""
    "``POST``","acmeclient","accounts","del","$uuid"
    "``GET``","acmeclient","accounts","get","$uuid=null"
    "``POST``","acmeclient","accounts","register","$uuid"
    "``POST,GET``","acmeclient","accounts","search",""
    "``POST``","acmeclient","accounts","set",""
    "``POST``","acmeclient","accounts","toggle","$uuid,$enabled=null"
    "``POST``","acmeclient","accounts","update","$uuid"

    "``<<uses>>``", "", "", "", "*model* `AcmeClient.xml <https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml>`__"

.. csv-table:: Resources (ActionsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","acmeclient","actions","add",""
    "``POST``","acmeclient","actions","del","$uuid"
    "``GET``","acmeclient","actions","get","$uuid=null"
    "``POST,GET``","acmeclient","actions","search",""
    "``POST``","acmeclient","actions","set",""
    "``GET``","acmeclient","actions","sftp_get_identity",""
    "``GET``","acmeclient","actions","sftp_test_connection",""
    "``GET``","acmeclient","actions","ssh_get_identity",""
    "``GET``","acmeclient","actions","ssh_test_connection",""
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
    "``GET``","acmeclient","certificates","import","$uuid"
    "``GET``","acmeclient","certificates","removekey","$uuid"
    "``POST``","acmeclient","certificates","revoke","$uuid"
    "``POST,GET``","acmeclient","certificates","search",""
    "``POST``","acmeclient","certificates","set",""
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

    "``POST``","acmeclient","settings","fetch_cron_integration",""
    "``POST``","acmeclient","settings","fetch_h_a_proxy_integration",""
    "``GET``","acmeclient","settings","get",""
    "``GET``","acmeclient","settings","get_bind_plugin_status",""
    "``GET``","acmeclient","settings","get_gcloud_plugin_status",""
    "``POST``","acmeclient","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `AcmeClient.xml <https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml>`__"

.. csv-table:: Resources (ValidationsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","acmeclient","validations","add",""
    "``POST``","acmeclient","validations","del","$uuid"
    "``GET``","acmeclient","validations","get","$uuid=null"
    "``POST,GET``","acmeclient","validations","search",""
    "``POST``","acmeclient","validations","set",""
    "``POST``","acmeclient","validations","toggle","$uuid,$enabled=null"
    "``POST``","acmeclient","validations","update","$uuid"

    "``<<uses>>``", "", "", "", "*model* `AcmeClient.xml <https://github.com/opnsense/plugins/blob/master/security/acme-client/src/opnsense/mvc/app/models/OPNsense/AcmeClient/AcmeClient.xml>`__"
