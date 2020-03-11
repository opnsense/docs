Ids
~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ids","service","dropAlertLog",""
    "``GET``","ids","service","getAlertInfo","$alertId,$fileid="""
    "``GET``","ids","service","getAlertLogs",""
    "``POST``","ids","service","queryAlerts",""
    "``POST``","ids","service","reconfigure",""
    "``POST``","ids","service","reloadRules",""
    "``POST``","ids","service","updateRules","$wait=null"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ids","settings","addUserRule",""
    "``POST``","ids","settings","delUserRule","$uuid"
    "``GET``","ids","settings","getRuleInfo","$sid=null"
    "``GET``","ids","settings","getRuleset","$id"
    "``GET``","ids","settings","getRulesetproperties",""
    "``GET``","ids","settings","getUserRule","$uuid=null"
    "``GET``","ids","settings","listRuleClasstypes",""
    "``GET``","ids","settings","listRulesets",""
    "``POST``","ids","settings","searchInstalledRules",""
    "``*``","ids","settings","searchUserRule",""
    "``POST``","ids","settings","setRule","$sid"
    "``POST``","ids","settings","setRuleset","$filename"
    "``POST``","ids","settings","setRulesetproperties",""
    "``POST``","ids","settings","setUserRule","$uuid"
    "``POST``","ids","settings","toggleRule","$sids,$enabled=null"
    "``POST``","ids","settings","toggleRuleset","$filenames,$enabled=null"
    "``POST``","ids","settings","toggleUserRule","$uuid,$enabled=null"
