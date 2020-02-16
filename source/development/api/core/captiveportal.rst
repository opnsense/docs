Captiveportal
~~~~~~~~~~~~~

.. csv-table:: Resources (AccessController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","captiveportal","access","logoff","$zoneid=0"
    "``POST``","captiveportal","access","logon","$zoneid=0"
    "``POST``","captiveportal","access","status","$zoneid=0"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","captiveportal","service","delTemplate","$uuid"
    "``GET``","captiveportal","service","getTemplate","$fileid=null"
    "``POST``","captiveportal","service","reconfigure",""
    "``POST``","captiveportal","service","saveTemplate",""
    "``GET``","captiveportal","service","searchTemplates",""

.. csv-table:: Resources (SessionController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","captiveportal","session","connect","$zoneid=0"
    "``POST``","captiveportal","session","disconnect","$zoneid=0"
    "``GET``","captiveportal","session","list","$zoneid=0"
    "``GET``","captiveportal","session","zones",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","captiveportal","settings","addZone",""
    "``POST``","captiveportal","settings","delZone","$uuid"
    "``GET``","captiveportal","settings","getZone","$uuid=null"
    "``*``","captiveportal","settings","searchZones",""
    "``POST``","captiveportal","settings","setZone","$uuid"
    "``POST``","captiveportal","settings","toggleZone","$uuid,$enabled=null"

.. csv-table:: Resources (VoucherController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","captiveportal","voucher","dropExpiredVouchers","$provider,$group"
    "``POST``","captiveportal","voucher","dropVoucherGroup","$provider,$group"
    "``POST``","captiveportal","voucher","expireVoucher","$provider"
    "``POST``","captiveportal","voucher","generateVouchers","$provider"
    "``GET``","captiveportal","voucher","listProviders",""
    "``GET``","captiveportal","voucher","listVoucherGroups","$provider"
    "``GET``","captiveportal","voucher","listVouchers","$provider,$group"

