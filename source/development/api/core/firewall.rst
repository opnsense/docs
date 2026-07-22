.. _api_plugins_firewall:

Firewall
~~~~~~~~

The firewall API offers a way for machine to machine interaction between custom applications and OPNsense, it
is part of the core system.

Although the module does contains a basic user interface (in :menuselection:`Firewall --> Automation`), it's mirely intended
as a reference and testbed. There's no relation to any of the rules being managed via the core system.

.. Tip::

    Use your browsers "inspect" feature to compare requests easily, the user interface in terms of communication is exactly the same
    as offered by the API . Rules not visible in the web interface (:menuselection:`Firewall --> Automation`) will not be returned by the API either.



.. csv-table:: Resources (AliasController.php)  -- extends : ApiMutableModelControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","alias","add_item",""
    "``POST``","firewall","alias","del_item","$uuid"
    "``GET,POST``","firewall","alias","export",""
    "``GET``","firewall","alias","get",""
    "``GET``","firewall","alias","get_alias_u_u_i_d","$name"
    "``GET``","firewall","alias","get_geo_i_p",""
    "``GET``","firewall","alias","get_item","$uuid=null"
    "``GET``","firewall","alias","get_table_size",""
    "``POST``","firewall","alias","import",""
    "``GET``","firewall","alias","list_categories",""
    "``GET``","firewall","alias","list_countries",""
    "``GET``","firewall","alias","list_network_aliases",""
    "``GET``","firewall","alias","list_user_groups",""
    "``POST``","firewall","alias","reconfigure",""
    "``GET,POST``","firewall","alias","search_item",""
    "``POST``","firewall","alias","set",""
    "``POST``","firewall","alias","set_item","$uuid"
    "``POST``","firewall","alias","toggle_item","$uuid,$enabled=null"
    "``POST``","firewall","alias","update","$action=null"

    "``<<uses>>``", "", "", "", "*model* `Alias.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Alias.xml>`__"

.. csv-table:: Resources (AliasUtilController.php)  -- extends : ApiControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","alias_util","add","$alias"
    "``GET``","firewall","alias_util","aliases",""
    "``POST``","firewall","alias_util","delete","$alias"
    "``POST``","firewall","alias_util","find_references",""
    "``POST``","firewall","alias_util","flush","$alias"
    "``GET``","firewall","alias_util","list","$alias"

.. csv-table:: Resources (CategoryController.php)  -- extends : ApiMutableModelControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","category","add_item",""
    "``POST``","firewall","category","del_item","$uuid"
    "``GET``","firewall","category","download",""
    "``GET``","firewall","category","get",""
    "``GET``","firewall","category","get_item","$uuid=null"
    "``GET,POST``","firewall","category","search_item","$add_empty=0"
    "``POST``","firewall","category","set",""
    "``POST``","firewall","category","set_item","$uuid"
    "``POST``","firewall","category","upload",""

    "``<<uses>>``", "", "", "", "*model* `Category.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Category.xml>`__"

.. csv-table:: Resources (DNatController.php)  -- extends : FilterBaseController 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","d_nat","add_rule",""
    "``POST``","firewall","d_nat","del_rule","$uuid"
    "``GET``","firewall","d_nat","get_rule","$uuid=null"
    "``GET``","firewall","d_nat","move_rule_before","$selected_uuid,$target_uuid"
    "``GET,POST``","firewall","d_nat","search_rule",""
    "``POST``","firewall","d_nat","set_rule","$uuid"
    "``POST``","firewall","d_nat","toggle_rule","$uuid,$disabled=null"
    "``GET``","firewall","d_nat","toggle_rule_log","$uuid,$log"

    "``<<uses>>``", "", "", "", "*model* `DNat.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/DNat.xml>`__"

.. csv-table:: Abstract [non-callable] (FilterBaseController.php) 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","filter_base","apply",""
    "``GET``","firewall","filter_base","get",""
    "``GET``","firewall","filter_base","list_categories",""
    "``GET``","firewall","filter_base","list_network_select_options",""
    "``GET``","firewall","filter_base","list_port_select_options",""
    "``POST``","firewall","filter_base","set",""

    "``<<uses>>``", "", "", "", "*model* `Filter.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Filter.xml>`__"

.. csv-table:: Resources (FilterController.php)  -- extends : FilterBaseController 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","filter","add_rule",""
    "``POST``","firewall","filter","del_rule","$uuid"
    "``GET``","firewall","filter","download_rules",""
    "``POST``","firewall","filter","flush_inspect_cache",""
    "``GET``","firewall","filter","get_interface_list",""
    "``GET``","firewall","filter","get_rule","$uuid=null"
    "``POST``","firewall","filter","move_rule_before","$selected_uuid,$target_uuid"
    "``GET``","firewall","filter","search_rule",""
    "``POST``","firewall","filter","set_rule","$uuid"
    "``POST``","firewall","filter","toggle_rule","$uuid,$enabled=null"
    "``GET``","firewall","filter","toggle_rule_log","$uuid,$log"
    "``POST``","firewall","filter","upload_rules",""

.. csv-table:: Resources (FilterUtilController.php)  -- extends : ApiControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","firewall","filter_util","rule_stats",""

.. csv-table:: Resources (GroupController.php)  -- extends : ApiMutableModelControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","group","add_item",""
    "``POST``","firewall","group","del_item","$uuid"
    "``GET``","firewall","group","get",""
    "``GET``","firewall","group","get_item","$uuid=null"
    "``POST``","firewall","group","reconfigure",""
    "``GET,POST``","firewall","group","search_item",""
    "``POST``","firewall","group","set",""
    "``POST``","firewall","group","set_item","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Group.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/Firewall/Group.xml>`__"

.. csv-table:: Resources (MigrationController.php)  -- extends : ApiControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","firewall","migration","download_rules",""
    "``POST``","firewall","migration","flush",""

.. csv-table:: Resources (NptController.php)  -- extends : FilterBaseController 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","npt","add_rule",""
    "``POST``","firewall","npt","del_rule","$uuid"
    "``GET``","firewall","npt","get_rule","$uuid=null"
    "``GET``","firewall","npt","move_rule_before","$selected_uuid,$target_uuid"
    "``GET,POST``","firewall","npt","search_rule",""
    "``POST``","firewall","npt","set_rule","$uuid"
    "``POST``","firewall","npt","toggle_rule","$uuid,$enabled=null"
    "``GET``","firewall","npt","toggle_rule_log","$uuid,$log"

.. csv-table:: Resources (OneToOneController.php)  -- extends : FilterBaseController 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","one_to_one","add_rule",""
    "``POST``","firewall","one_to_one","del_rule","$uuid"
    "``GET``","firewall","one_to_one","get_rule","$uuid=null"
    "``GET``","firewall","one_to_one","move_rule_before","$selected_uuid,$target_uuid"
    "``GET,POST``","firewall","one_to_one","search_rule",""
    "``POST``","firewall","one_to_one","set_rule","$uuid"
    "``POST``","firewall","one_to_one","toggle_rule","$uuid,$enabled=null"
    "``GET``","firewall","one_to_one","toggle_rule_log","$uuid,$log"

.. csv-table:: Resources (SourceNatController.php)  -- extends : FilterBaseController 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","source_nat","add_rule",""
    "``POST``","firewall","source_nat","del_rule","$uuid"
    "``GET``","firewall","source_nat","get_rule","$uuid=null"
    "``GET``","firewall","source_nat","move_rule_before","$selected_uuid,$target_uuid"
    "``GET,POST``","firewall","source_nat","search_rule",""
    "``POST``","firewall","source_nat","set_rule","$uuid"
    "``POST``","firewall","source_nat","toggle_rule","$uuid,$enabled=null"
    "``GET``","firewall","source_nat","toggle_rule_log","$uuid,$log"



-----------------------
Concept
-----------------------

The firewall plugin injects rules in the standard OPNsense firewall while maintaining visibility on them in the
standard user interface.

We use our standard :code:`ApiMutableModelControllerBase` to allow crud operations on rule entries and offer an
:code:`apply` action to activate the new configuration.

.. blockdiag::
    :scale: 100%

    diagram init {
        administration [label = "administration"];
        apply [label = "apply()"];
        administration -> apply ;
    }


The diagram above contains the basic steps to change rules and activate them.
Changes made through the administrative endpoints are staged in the configuration; calling :code:`apply()` reloads
the firewall so the new ruleset becomes active.


.. Note::

    The examples in this document disable certificate validation, make sure when using this in a production environment to
    remove the :code:`verify=False` from the :code:`requests` calls


-----------------------
Administration example
-----------------------

Administrative endpoints are pretty standard use of :code:`ApiMutableModelControllerBase`, the example below searches for
a rule named "OPNsense_fw_api_testrule_1", when not found one will be added otherwise it will print the internal uuid.
Inline you will find a brief description of the steps performed.


.. literalinclude:: firewall.sample_create.py
    :language: python
    :linenos:
    :caption: administrative_example.py


.. Tip::

      Since our model contains default values for most attributes, we only need to feed the changes if we would like to keep the
      defaults. In this case the TCP/IP version was IPv4 by default for example. In most cases one would like to set all relevant properties
      in case defaults change over time.

-----------------------
Apply example
-----------------------

This example will disable the rule created in the previous example and apply the changes so they become active.


.. literalinclude:: firewall.apply.py
    :language: python
    :linenos:
    :caption: apply_example.py