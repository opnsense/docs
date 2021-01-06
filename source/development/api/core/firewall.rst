Firewall
~~~~~~~~

.. csv-table:: Resources (AliasController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","alias","addItem",""
    "``POST``","firewall","alias","delItem","$uuid"
    "``GET``","firewall","alias","export",""
    "``GET``","firewall","alias","getAliasUUID","$name"
    "``GET``","firewall","alias","getGeoIP",""
    "``GET``","firewall","alias","getItem","$uuid=null"
    "``POST``","firewall","alias","import",""
    "``GET``","firewall","alias","listCountries",""
    "``GET``","firewall","alias","listNetworkAliases",""
    "``POST``","firewall","alias","reconfigure",""
    "``*``","firewall","alias","searchItem",""
    "``POST``","firewall","alias","setItem","$uuid"
    "``POST``","firewall","alias","toggleItem","$uuid,$enabled=null"

    "``<<uses>>``", "", "", "", "*model* `Alias.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Alias.xml>`__"

.. csv-table:: Resources (AliasUtilController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","alias_util","add","$alias"
    "``GET``","firewall","alias_util","aliases",""
    "``POST``","firewall","alias_util","delete","$alias"
    "``POST``","firewall","alias_util","find_references",""
    "``POST``","firewall","alias_util","flush","$alias"
    "``GET``","firewall","alias_util","list","$alias"
    "``GET``","firewall","alias_util","update_bogons",""
