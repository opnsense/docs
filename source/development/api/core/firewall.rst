Firewall
~~~~~~~~

.. csv-table:: Resources (AliasController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","alias","addItem",""
    "``POST``","firewall","alias","delItem","$uuid"
    "``GET``","firewall","alias","export",""
    "``GET``","firewall","alias","get",""
    "``GET``","firewall","alias","getAliasUUID","$name"
    "``GET``","firewall","alias","getGeoIP",""
    "``GET``","firewall","alias","getItem","$uuid=null"
    "``POST``","firewall","alias","import",""
    "``GET``","firewall","alias","listCountries",""
    "``GET``","firewall","alias","listNetworkAliases",""
    "``POST``","firewall","alias","reconfigure",""
    "``*``","firewall","alias","searchItem",""
    "``GET``","firewall","alias","set",""
    "``POST``","firewall","alias","setItem","$uuid"
    "``POST``","firewall","alias","toggleItem","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Alias.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Alias.xml>`__"

.. csv-table:: Resources (AliasUtilController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","alias_util","add","$alias"
    "``GET``","firewall","alias_util","aliases",""
    "``POST``","firewall","alias_util","delete","$alias"
    "``POST``","firewall","alias_util","findReferences",""
    "``POST``","firewall","alias_util","flush","$alias"
    "``GET``","firewall","alias_util","list","$alias"
    "``GET``","firewall","alias_util","updateBogons",""

.. csv-table:: Resources (CategoryController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","category","addItem",""
    "``POST``","firewall","category","delItem","$uuid"
    "``GET``","firewall","category","get",""
    "``GET``","firewall","category","getItem","$uuid=null"
    "``*``","firewall","category","searchItem",""
    "``*``","firewall","category","searchNoCategoryItem",""
    "``GET``","firewall","category","set",""
    "``POST``","firewall","category","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Category.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Category.xml>`__"
