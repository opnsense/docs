.. _api_plugins_firewall:

Firewall
~~~~~~~~

The firewall API plugin (**os-firewall**) offers a way for machine to machine interaction between custom applications and OPNsense, it can
easily be installed like any other plugin via :menuselection:`System --> Firmware --> Plugins`.

Although the plugin does contains a basic user interface (in :menuselection:`Firewall --> Automation`), it's mirely intended
as a reference and testbed. There's no relation to any of the rules being managed via the core system.

.. Tip::

    Use your browsers "inspect" feature to compare requests easily, the user interface in terms of communication is exactly the same
    as offered by the API . Rules not visible in the web interface (:menuselection:`Firewall --> Automation`) will not be returned by the API either.



.. csv-table:: Resources (AliasController.php)  -- extends : ApiMutableModelControllerBase 
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

.. csv-table:: Resources (AliasUtilController.php)  -- extends : ApiControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","alias_util","add","$alias"
    "``GET``","firewall","alias_util","aliases",""
    "``POST``","firewall","alias_util","delete","$alias"
    "``POST``","firewall","alias_util","findReferences",""
    "``POST``","firewall","alias_util","flush","$alias"
    "``GET``","firewall","alias_util","list","$alias"
    "``GET``","firewall","alias_util","updateBogons",""

.. csv-table:: Resources (CategoryController.php)  -- extends : ApiMutableModelControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","category","addItem",""
    "``POST``","firewall","category","delItem","$uuid"
    "``GET``","firewall","category","get",""
    "``GET``","firewall","category","getItem","$uuid=null"
    "``*``","firewall","category","searchItem","$add_empty='0'"
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

.. csv-table:: Resources (FilterController.php)  -- extends : FilterBaseController 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","filter","addRule",""
    "``POST``","firewall","filter","delRule","$uuid"
    "``GET``","firewall","filter","getRule","$uuid=null"
    "``*``","firewall","filter","searchRule",""
    "``POST``","firewall","filter","setRule","$uuid"
    "``POST``","firewall","filter","toggleRule","$uuid,$enabled=null"

.. csv-table:: Resources (FilterUtilController.php)  -- extends : ApiControllerBase 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","firewall","filter_util","ruleStats",""

.. csv-table:: Resources (GroupController.php)  -- extends : ApiMutableModelControllerBase 
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

.. csv-table:: Resources (NptController.php)  -- extends : FilterBaseController 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","npt","addRule",""
    "``POST``","firewall","npt","delRule","$uuid"
    "``GET``","firewall","npt","getRule","$uuid=null"
    "``*``","firewall","npt","searchRule",""
    "``POST``","firewall","npt","setRule","$uuid"
    "``POST``","firewall","npt","toggleRule","$uuid,$enabled=null"

.. csv-table:: Resources (SourceNatController.php)  -- extends : FilterBaseController 
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","firewall","source_nat","addRule",""
    "``POST``","firewall","source_nat","delRule","$uuid"
    "``GET``","firewall","source_nat","getRule","$uuid=null"
    "``*``","firewall","source_nat","searchRule",""
    "``POST``","firewall","source_nat","setRule","$uuid"
    "``POST``","firewall","source_nat","toggleRule","$uuid,$enabled=null"



-----------------------
Concept
-----------------------

The firewall plugin injects rules in the standard OPNsense firewall while maintaining visibility on them in the
standard user interface.

We use our standard :code:`ApiMutableModelControllerBase` to allow crud operations on rule entries and offer a set of
specific actions to apply the new configuration.
Since firewall rules can be quite sensitive with a higher risk of lockout, we also support a rollback mechanism here,
which offers the ability to rollback this components changes.

.. blockdiag::
    :scale: 100%

    diagram init {
        savepoint [label = "savepoint()"];
        administration [label = "administration"];
        apply [label = "apply(savepoint)"];
        cancelRollback [label = "cancelRollback(sp)"];
        savepoint -> administration -> apply ;
        apply -> cancelRollback [label = ".. 60s", style = dashed];
    }


The diagram above contains the basic steps to change rules, apply and eventually rollback if not being able to access the machine again.
When calling :code:`savepoint()` a new config revision will be created and the timestamp will be returned for later use.
If the :code:`cancelRollback(savepoint)` is not called within 60 seconds, the firewall will rollback to the previous state
identified by the savepoint timestamp (if available).


.. Note::

    The examples in this document disable certificate validation, make sure when using this in a production environment to
    remove the :code:`verify=False` from the :code:`requests` calls

.. Tip::

    The number of versions kept can be configured as "backup count" in :menuselection:`System -> Configuration -> History`.
    This affectively determines within how many configuration changes you can still rollback, if the backup is removed, a rollback
    will keep the current state (do nothing).


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
Apply / revert example
-----------------------

This example will disable the rule created in the previous example and apply the changes using a savepoint, since we're not
calling :code:`cancelRollback(savepoint)` it will revert after 60 seconds to the original state.


.. literalinclude:: firewall.savepoint.py
    :language: python
    :linenos:
    :caption: savepoint_example.py


.. Note::

    The savepoint will only revert this components changes, other changes won't be affected by this revert, for example
    add an additional interface between savepoint and revert won't be affected.