Ids
~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ids","service","dropAlertLog",""
    "``GET``","ids","service","getAlertInfo","$alertId,$fileid="""""
    "``GET``","ids","service","getAlertLogs",""
    "``POST``","ids","service","queryAlerts",""
    "``POST``","ids","service","reconfigure",""
    "``GET``","ids","service","reconfigure",""
    "``POST``","ids","service","reloadRules",""
    "``POST``","ids","service","restart",""
    "``POST``","ids","service","start",""
    "``GET``","ids","service","status",""
    "``POST``","ids","service","stop",""
    "``POST``","ids","service","updateRules","$wait=null"

    "``<<uses>>``", "", "", "", "*model* `IDS.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IDS/IDS.xml>`__"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ids","settings","addPolicy",""
    "``POST``","ids","settings","addPolicyRule",""
    "``POST``","ids","settings","addUserRule",""
    "``GET``","ids","settings","checkPolicyRule",""
    "``POST``","ids","settings","delPolicy","$uuid"
    "``POST``","ids","settings","delPolicyRule","$uuid"
    "``POST``","ids","settings","delUserRule","$uuid"
    "``GET``","ids","settings","get",""
    "``GET``","ids","settings","getPolicy","$uuid=null"
    "``GET``","ids","settings","getPolicyRule","$uuid=null"
    "``GET``","ids","settings","getRuleInfo","$sid=null"
    "``GET``","ids","settings","getRuleset","$id"
    "``GET``","ids","settings","getRulesetproperties",""
    "``GET``","ids","settings","getUserRule","$uuid=null"
    "``GET``","ids","settings","listRuleMetadata",""
    "``GET``","ids","settings","listRulesets",""
    "``POST``","ids","settings","searchInstalledRules",""
    "``*``","ids","settings","searchPolicy",""
    "``*``","ids","settings","searchPolicyRule",""
    "``*``","ids","settings","searchUserRule",""
    "``GET``","ids","settings","set",""
    "``POST``","ids","settings","setPolicy","$uuid"
    "``POST``","ids","settings","setPolicyRule","$uuid"
    "``POST``","ids","settings","setRule","$sid"
    "``POST``","ids","settings","setRuleset","$filename"
    "``POST``","ids","settings","setRulesetproperties",""
    "``POST``","ids","settings","setUserRule","$uuid"
    "``POST``","ids","settings","togglePolicy","$uuid,$enabled=null"
    "``POST``","ids","settings","togglePolicyRule","$uuid,$enabled=null"
    "``POST``","ids","settings","toggleRule","$sids,$enabled=null"
    "``POST``","ids","settings","toggleRuleset","$filenames,$enabled=null"
    "``POST``","ids","settings","toggleUserRule","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `IDS.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IDS/IDS.xml>`__"
