Dnsmasq
~~~~~~~

.. csv-table:: Resources (LeasesController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","dnsmasq","leases","search",""

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnsmasq","service","reconfigure",""
    "``POST``","dnsmasq","service","restart",""
    "``POST``","dnsmasq","service","start",""
    "``GET``","dnsmasq","service","status",""
    "``POST``","dnsmasq","service","stop",""

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","dnsmasq","settings","add_boot",""
    "``POST``","dnsmasq","settings","add_domain",""
    "``POST``","dnsmasq","settings","add_host",""
    "``POST``","dnsmasq","settings","add_option",""
    "``POST``","dnsmasq","settings","add_range",""
    "``POST``","dnsmasq","settings","add_tag",""
    "``POST``","dnsmasq","settings","del_boot","$uuid"
    "``POST``","dnsmasq","settings","del_domain","$uuid"
    "``POST``","dnsmasq","settings","del_host","$uuid"
    "``POST``","dnsmasq","settings","del_option","$uuid"
    "``POST``","dnsmasq","settings","del_range","$uuid"
    "``POST``","dnsmasq","settings","del_tag","$uuid"
    "``GET``","dnsmasq","settings","download_hosts",""
    "``GET``","dnsmasq","settings","get",""
    "``GET``","dnsmasq","settings","get_boot","$uuid=null"
    "``GET``","dnsmasq","settings","get_domain","$uuid=null"
    "``GET``","dnsmasq","settings","get_host","$uuid=null"
    "``GET``","dnsmasq","settings","get_option","$uuid=null"
    "``GET``","dnsmasq","settings","get_range","$uuid=null"
    "``GET``","dnsmasq","settings","get_tag","$uuid=null"
    "``GET``","dnsmasq","settings","get_tag_list",""
    "``POST,GET``","dnsmasq","settings","search_boot",""
    "``POST,GET``","dnsmasq","settings","search_domain",""
    "``POST,GET``","dnsmasq","settings","search_host",""
    "``POST,GET``","dnsmasq","settings","search_option",""
    "``POST,GET``","dnsmasq","settings","search_range",""
    "``POST,GET``","dnsmasq","settings","search_tag",""
    "``POST``","dnsmasq","settings","set",""
    "``POST``","dnsmasq","settings","set_boot","$uuid"
    "``POST``","dnsmasq","settings","set_domain","$uuid"
    "``POST``","dnsmasq","settings","set_host","$uuid"
    "``POST``","dnsmasq","settings","set_option","$uuid"
    "``POST``","dnsmasq","settings","set_range","$uuid"
    "``POST``","dnsmasq","settings","set_tag","$uuid"
    "``POST``","dnsmasq","settings","upload_hosts",""

    "``<<uses>>``", "", "", "", "*model* `Dnsmasq.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Dnsmasq/Dnsmasq.xml>`__"
