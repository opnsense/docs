Captiveportal
~~~~~~~~~~~~~

.. csv-table:: Resources (AccessController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","captiveportal","access","api",""
    "``GET``","captiveportal","access","logoff","$zoneid=0"
    "``POST``","captiveportal","access","logon","$zoneid=0"
    "``POST,GET``","captiveportal","access","status","$zoneid=0"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","captiveportal","service","del_template","$uuid"
    "``GET``","captiveportal","service","get_template","$fileid=null"
    "``POST``","captiveportal","service","reconfigure",""
    "``POST``","captiveportal","service","save_template",""
    "``GET``","captiveportal","service","search_templates",""

.. csv-table:: Resources (SessionController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","captiveportal","session","connect","$zoneid=0"
    "``POST``","captiveportal","session","disconnect","$zoneid=''"
    "``GET``","captiveportal","session","list","$zoneid=0"
    "``GET``","captiveportal","session","search",""
    "``GET``","captiveportal","session","zones",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","captiveportal","settings","add_zone",""
    "``POST``","captiveportal","settings","del_zone","$uuid"
    "``GET``","captiveportal","settings","get",""
    "``GET``","captiveportal","settings","get_zone","$uuid=null"
    "``POST,GET``","captiveportal","settings","search_zones",""
    "``POST``","captiveportal","settings","set",""
    "``POST``","captiveportal","settings","set_zone","$uuid"
    "``POST``","captiveportal","settings","toggle_zone","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `CaptivePortal.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/CaptivePortal/CaptivePortal.xml>`__"

.. csv-table:: Resources (VoucherController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","captiveportal","voucher","drop_expired_vouchers","$provider,$group"
    "``POST``","captiveportal","voucher","drop_voucher_group","$provider,$group"
    "``POST``","captiveportal","voucher","expire_voucher","$provider"
    "``POST``","captiveportal","voucher","generate_vouchers","$provider"
    "``GET``","captiveportal","voucher","list_providers",""
    "``GET``","captiveportal","voucher","list_voucher_groups","$provider"
    "``GET``","captiveportal","voucher","list_vouchers","$provider,$group"
