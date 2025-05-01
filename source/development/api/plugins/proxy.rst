Proxy
~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","proxy","service","downloadacls",""
    "``POST``","proxy","service","fetchacls",""
    "``POST``","proxy","service","reconfigure",""
    "``POST``","proxy","service","refresh_template",""
    "``POST``","proxy","service","reset",""
    "``GET``","proxy","service","restart",""
    "``GET``","proxy","service","start",""
    "``GET``","proxy","service","status",""
    "``POST``","proxy","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","proxy","settings","add_p_a_c_match",""
    "``POST``","proxy","settings","add_p_a_c_proxy",""
    "``POST``","proxy","settings","add_p_a_c_rule",""
    "``POST``","proxy","settings","add_remote_blacklist",""
    "``POST``","proxy","settings","del_p_a_c_match","$uuid"
    "``POST``","proxy","settings","del_p_a_c_proxy","$uuid"
    "``POST``","proxy","settings","del_p_a_c_rule","$uuid"
    "``POST``","proxy","settings","del_remote_blacklist","$uuid"
    "``POST``","proxy","settings","fetch_r_b_cron",""
    "``GET``","proxy","settings","get",""
    "``GET``","proxy","settings","get_p_a_c_match","$uuid=null"
    "``GET``","proxy","settings","get_p_a_c_proxy","$uuid=null"
    "``GET``","proxy","settings","get_p_a_c_rule","$uuid=null"
    "``GET``","proxy","settings","get_remote_blacklist","$uuid=null"
    "``GET,POST``","proxy","settings","search_p_a_c_match",""
    "``GET,POST``","proxy","settings","search_p_a_c_proxy",""
    "``GET,POST``","proxy","settings","search_p_a_c_rule",""
    "``GET``","proxy","settings","search_remote_blacklists",""
    "``POST``","proxy","settings","set",""
    "``POST``","proxy","settings","set_p_a_c_match","$uuid"
    "``POST``","proxy","settings","set_p_a_c_proxy","$uuid"
    "``POST``","proxy","settings","set_p_a_c_rule","$uuid"
    "``POST``","proxy","settings","set_remote_blacklist","$uuid"
    "``POST``","proxy","settings","toggle_p_a_c_rule","$uuid"
    "``POST``","proxy","settings","toggle_remote_blacklist","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Proxy.xml <https://github.com/opnsense/plugins/blob/master/www/squid/src/opnsense/mvc/app/models/OPNsense/Proxy/Proxy.xml>`__"

.. csv-table:: Resources (TemplateController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","proxy","template","get",""
    "``POST``","proxy","template","reset",""
    "``POST``","proxy","template","set",""

    "``<<uses>>``", "", "", "", "*model* `Proxy.xml <https://github.com/opnsense/plugins/blob/master/www/squid/src/opnsense/mvc/app/models/OPNsense/Proxy/Proxy.xml>`__"

.. csv-table:: Resources (AclController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","proxy","acl","add_custom_policy",""
    "``POST``","proxy","acl","add_policy",""
    "``POST``","proxy","acl","apply",""
    "``POST``","proxy","acl","del_custom_policy","$uuid"
    "``POST``","proxy","acl","del_policy","$uuid"
    "``GET``","proxy","acl","get",""
    "``GET``","proxy","acl","get_custom_policy","$uuid=null"
    "``GET``","proxy","acl","get_policy","$uuid=null"
    "``GET,POST``","proxy","acl","search_custom_policy",""
    "``GET,POST``","proxy","acl","search_policy",""
    "``POST``","proxy","acl","set",""
    "``POST``","proxy","acl","set_custom_policy","$uuid"
    "``POST``","proxy","acl","set_policy","$uuid"
    "``POST``","proxy","acl","test",""
    "``POST``","proxy","acl","toggle_custom_policy","$uuid,$enabled=null"
    "``POST``","proxy","acl","toggle_policy","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `ACL.xml <https://github.com/opnsense/plugins/blob/master/www/OPNProxy/src/opnsense/mvc/app/models/Deciso/Proxy/ACL.xml>`__"
