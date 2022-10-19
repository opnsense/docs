Proxysso
~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","proxysso","service","createkeytab",""
    "``GET``","proxysso","service","deletekeytab",""
    "``GET``","proxysso","service","getCheckList",""
    "``GET``","proxysso","service","showkeytab",""
    "``POST``","proxysso","service","testkerblogin",""

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","proxysso","settings","get",""
    "``POST``","proxysso","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `ProxySSO.xml <https://github.com/opnsense/plugins/blob/master/www/web-proxy-sso/src/opnsense/mvc/app/models/OPNsense/ProxySSO/ProxySSO.xml>`__"
