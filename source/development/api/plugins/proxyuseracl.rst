Proxyuseracl
~~~~~~~~~~~~

.. csv-table:: Resources (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","proxyuseracl","settings","addACL",""
    "``POST``","proxyuseracl","settings","delACL","$uuid"
    "``GET``","proxyuseracl","settings","get",""
    "``GET``","proxyuseracl","settings","getACL","$uuid=null"
    "``GET``","proxyuseracl","settings","searchACL",""
    "``GET``","proxyuseracl","settings","set",""
    "``POST``","proxyuseracl","settings","setACL","$uuid"
    "``POST``","proxyuseracl","settings","updownACL","$uuid"

    "``<<uses>>``", "", "", "", "*model* `ProxyUserACL.xml <https://github.com/opnsense/plugins/blob/master/www/web-proxy-useracl/src/opnsense/mvc/app/models/OPNsense/ProxyUserACL/ProxyUserACL.xml>`__"
