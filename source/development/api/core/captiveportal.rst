
CaptivePortal
~~~~~~~~~~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","captiveportal","service","reconfigure",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","captiveportal","service","addtemplate",""
   "``POST``","captiveportal","service","deltemplate","$uuid"
   "``GET``","captiveportal","service","gettemplate","$fileid"
   "``GET``","captiveportal","service","searchtemplates",""
   "``GET``","captiveportal","service","searchtemplates","$uuid"
   "``POST``","captiveportal","service","settemplate","$uuid"
   "``POST``","captiveportal","settings","addzone",""
   "``POST``","captiveportal","settings","delzone","$uuid"
   "``GET``","captiveportal","settings","getzone","$uuid"
   "``GET``","captiveportal","settings","searchzones",""
   "``POST``","captiveportal","settings","setzone","$uuid"
   "``POST``","captiveportal","settings","togglezone","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","captiveportal","service","saveTemplate",""
   "","captiveportal","session","disconnect",""
   "","captiveportal","session","list",""
   "","captiveportal","session","zones",""
   "","captiveportal","voucher","dropExpiredVouchers",""
   "","captiveportal","voucher","dropVoucherGroup",""
   "","captiveportal","voucher","expireVoucher",""
   "","captiveportal","voucher","generateVouchers",""
   "","captiveportal","voucher","listProviders",""
   "","captiveportal","voucher","listVoucherGroups",""
   "","captiveportal","voucher","listVouchers",""
