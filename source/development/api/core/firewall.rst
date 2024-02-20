.. _api_core_firewall:

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
    "``GET``","firewall","alias","getTableSize",""
    "``POST``","firewall","alias","import",""
    "``GET``","firewall","alias","listCategories",""
    "``GET``","firewall","alias","listCountries",""
    "``GET``","firewall","alias","listNetworkAliases",""
    "``GET``","firewall","alias","listUserGroups",""
    "``POST``","firewall","alias","reconfigure",""
    "``*``","firewall","alias","searchItem",""
    "``POST``","firewall","alias","set",""
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
    "``POST``","firewall","category","set",""
    "``POST``","firewall","category","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Category.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Category.xml>`__"

.. csv-table:: Abstract [non-callable] (FilterBaseController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","filter_base","apply","$rollback_revision=null"
    "``POST``","firewall","filter_base","cancelRollback","$rollback_revision"
    "``GET``","firewall","filter_base","get",""
    "``GET``","firewall","filter_base","listCategories",""
    "``GET``","firewall","filter_base","listNetworkSelectOptions",""
    "``POST``","firewall","filter_base","revert","$revision"
    "``POST``","firewall","filter_base","savepoint",""
    "``POST``","firewall","filter_base","set",""

    "``<<uses>>``", "", "", "", "*model* `Filter.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Filter.xml>`__"

.. csv-table:: Resources (FilterController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","filter","addRule",""
    "``POST``","firewall","filter","delRule","$uuid"
    "``GET``","firewall","filter","getRule","$uuid=null"
    "``*``","firewall","filter","searchRule",""
    "``POST``","firewall","filter","setRule","$uuid"
    "``POST``","firewall","filter","toggleRule","$uuid,$enabled=null"

.. csv-table:: Resources (FilterUtilController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","firewall","filter_util","ruleStats",""

.. csv-table:: Resources (GroupController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","group","addItem",""
    "``POST``","firewall","group","delItem","$uuid"
    "``GET``","firewall","group","get",""
    "``GET``","firewall","group","getItem","$uuid=null"
    "``POST``","firewall","group","reconfigure",""
    "``*``","firewall","group","searchItem",""
    "``POST``","firewall","group","set",""
    "``POST``","firewall","group","setItem","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Group.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Group.xml>`__"

.. csv-table:: Resources (NptController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","npt","addRule",""
    "``POST``","firewall","npt","delRule","$uuid"
    "``GET``","firewall","npt","getRule","$uuid=null"
    "``*``","firewall","npt","searchRule",""
    "``POST``","firewall","npt","setRule","$uuid"
    "``POST``","firewall","npt","toggleRule","$uuid,$enabled=null"

.. csv-table:: Resources (SourceNatController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","source_nat","addRule",""
    "``POST``","firewall","source_nat","delRule","$uuid"
    "``GET``","firewall","source_nat","getRule","$uuid=null"
    "``*``","firewall","source_nat","searchRule",""
    "``POST``","firewall","source_nat","setRule","$uuid"
    "``POST``","firewall","source_nat","toggleRule","$uuid,$enabled=null"


.. Tip::

    In order to inject rules using an API, you may take a look at the :ref:`Firewall Plugin API <api_plugins_firewall>`,
    currently the core system does not support rule modifications via the API for this topic.