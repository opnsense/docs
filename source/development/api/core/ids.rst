Ids
~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ids","service","drop_alert_log",""
    "``GET``","ids","service","get_alert_info","$alertId,$fileid=''"
    "``GET``","ids","service","get_alert_logs",""
    "``POST``","ids","service","query_alerts",""
    "``POST``","ids","service","reconfigure",""
    "``POST``","ids","service","reload_rules",""
    "``POST``","ids","service","restart",""
    "``POST``","ids","service","start",""
    "``GET``","ids","service","status",""
    "``POST``","ids","service","stop",""
    "``POST``","ids","service","update_rules","$wait=null"

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","ids","settings","add_policy",""
    "``POST``","ids","settings","add_policy_rule",""
    "``POST``","ids","settings","add_user_rule",""
    "``GET``","ids","settings","check_policy_rule",""
    "``POST``","ids","settings","del_policy","$uuid"
    "``POST``","ids","settings","del_policy_rule","$uuid"
    "``POST``","ids","settings","del_user_rule","$uuid"
    "``GET``","ids","settings","get",""
    "``GET``","ids","settings","get_policy","$uuid=null"
    "``GET``","ids","settings","get_policy_rule","$uuid=null"
    "``GET``","ids","settings","get_rule_info","$sid=null"
    "``GET``","ids","settings","get_ruleset","$id"
    "``GET``","ids","settings","get_rulesetproperties",""
    "``GET``","ids","settings","get_user_rule","$uuid=null"
    "``GET``","ids","settings","list_rule_metadata",""
    "``GET``","ids","settings","list_rulesets",""
    "``POST``","ids","settings","search_installed_rules",""
    "``GET,POST``","ids","settings","search_policy",""
    "``GET,POST``","ids","settings","search_policy_rule",""
    "``GET,POST``","ids","settings","search_user_rule",""
    "``POST``","ids","settings","set",""
    "``POST``","ids","settings","set_policy","$uuid"
    "``POST``","ids","settings","set_policy_rule","$uuid"
    "``POST``","ids","settings","set_rule","$sid"
    "``POST``","ids","settings","set_ruleset","$filename"
    "``POST``","ids","settings","set_rulesetproperties",""
    "``POST``","ids","settings","set_user_rule","$uuid"
    "``POST``","ids","settings","toggle_policy","$uuid,$enabled=null"
    "``POST``","ids","settings","toggle_policy_rule","$uuid,$enabled=null"
    "``POST``","ids","settings","toggle_rule","$sids,$enabled=null"
    "``POST``","ids","settings","toggle_ruleset","$filenames,$enabled=null"
    "``POST``","ids","settings","toggle_user_rule","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `IDS.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/IDS/IDS.xml>`__"
