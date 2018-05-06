IDS
~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","ids","settings","get",""
   "``POST``","ids","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","ids","service","reconfigure",""
   "``POST``","ids","service","restart",""
   "``POST``","ids","service","start",""
   "``GET``","ids","service","status",""
   "``POST``","ids","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","ids","settings","adduserrule",""
   "``POST``","ids","settings","deluserrule","$uuid"
   "``GET``","ids","settings","getruleset","$uuid"
   "``GET``","ids","settings","getuserrule","$uuid"
   "``GET``","ids","settings","searchinstalledrules",""
   "``GET``","ids","settings","searchuserrule",""
   "``POST``","ids","settings","setrule","$uuid"
   "``POST``","ids","settings","setruleset","$uuid"
   "``POST``","ids","settings","setuserrule","$uuid"
   "``POST``","ids","settings","togglerule","$uuid/$enabled"
   "``POST``","ids","settings","toggleruleset","$uuid/$enabled"
   "``POST``","ids","settings","toggleuserrule","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","ids","service","dropAlertLog",""
   "","ids","service","getAlertInfo",""
   "","ids","service","getAlertLogs",""
   "","ids","service","queryAlerts",""
   "","ids","service","reloadRules",""
   "","ids","service","updateRules",""
   "","ids","settings","getRuleInfo",""
   "","ids","settings","getRulesetproperties",""
   "","ids","settings","listRuleClasstypes",""
   "","ids","settings","listRulesets",""
   "","ids","settings","setRulesetproperties",""
