=================================
Creating Models / Field types
=================================

OPNsense comes with a collection of standard field types, which can be used to perform standard field type validations.
These field types can be found in `/usr/local/opnsense/mvc/app/models/OPNsense/Base/FieldTypes/ <https://github.com/opnsense/core/tree/master/src/opnsense/mvc/app/models/OPNsense/Base/FieldTypes>`__
and usually decent from the `BaseField` type.

This paragraph aims to provide an overview of the types included by default and their use.


.. Tip::

    When using lists, the :code:`Multiple` (Y/N) keyword defines if there may be more than one item selected at a time.

.. Tip::

    The xml keyword :code:`Required` can be used to mark a field as being required.


ArrayField
------------------------------------

The basic field type to describe a container of objects, such as a list of addresses.

.. Note::

  This type can't be nested, only one level of ArrayField types is supported, you can use ModelRelationField to
  describe master-detail constructions.

.. Tip::

   In case a model needs static (non persistent) records, the :code:`getStaticChildren()` method may be implemented
   to spawn static entries. See also the custom field chapter for implementation scenarios.


AuthGroupField
------------------------------------

Returns and validates system (user) groups (found in :menuselection:`System --> Access --> Groups`)


.. csv-table:: AuthGroupField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"


AuthenticationServerField
------------------------------------

Select and validate authentication providers, maintained in :menuselection:`System --> Access --> Servers`.

.. csv-table:: AuthenticationServerField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "Filters", "Y,N", "A structure of regex filters per atribute to exclude certain options from the list"

AutoNumberField
------------------------------------

An integer sequence, which automatically increments on every new item of the same type in the same level.


.. csv-table:: AutoNumberField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "MinimumValue", ":code:`int`", "Minimum number also starting point of the sequence"
   "MaximumValue", ":code:`int`", "Maximum number"


Base64Field
------------------------------------
Validate if a given string contains a valid base64 decodable value.

.. csv-table:: Base64Field
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "Mask", ":code:`regex`", "Optional validation regex"


BooleanField
------------------------------------

Boolean field, where 0 means :code:`false` and 1 is defined as :code:`true`

.. csv-table:: BooleanField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"


CertificateField
------------------------------------

Option list with system certificates defined in :menuselection:`System --> Trust`.

.. csv-table:: CertificateField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "Type", ":code:`ca`, :code:`crl`, :code:`cert`", "Type of certificate to select, defaults to :code:`cert`"

CSVListField
------------------------------------

List of (comma) separated values, which can be validated using a regex.

.. csv-table:: CSVListField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "Mask", ":code:`regex`", "Optional validation regex"
   "MaskPerItem", "Y,N", "Apply regex validation to each item separately"


ConfigdActionsField
------------------------------------

Select available configd actions, supports filters to limit the number of choices. For example, the example below
only shows actions which have a description.

.. code-block:: xml

    <command type="ConfigdActionsField">
        <filters>
            <description>/(.){1,255}/</description>
        </filters>
    </command>

.. csv-table:: ConfigdActionsField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "Filters", "Y,N", "A structure of regex filters per atribute to exclude certain options from the list"



CountryField
------------------------------------

Select and validate countries in the world.

.. csv-table:: CountryField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "AddInverted", "Y,N", "Add 'inverted'/excluded countries to the list, copies contry codes prefixes an :code:`!` (e.g. :code:`!NL`)"



EmailField
------------------------------------

Validate if the input contains an email address.

.. csv-table:: EmailField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"


HostnameField
------------------------------------

Check if hostnames are valid, includes the following options:

.. csv-table:: HostnameField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "IpAllowed", "Y,N", "Allow an ip address"
   "HostWildcardAllowed", "Y,N", "Allow :code:`*` for all hostnames"
   "FqdnWildcardAllowed", "Y,N", "Allow partial wildcard for fully qualified domain names (e.g. :code:`*.my.top.level.domain`)"
   "ZoneRootAllowed", "Y,N", "Allow the zone root marker (:code:`@`)"


IntegerField
------------------------------------

Validate if the input contains an integere value, optionally constrained by minimum and maximum values.

.. csv-table:: EmailField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "MinimumValue", ":code:`int`", "Minimum number"
   "MaximumValue", ":code:`int`", "Maximum number"


InterfaceField
------------------------------------

Option list with interfaces defined in :menuselection:`Interfaces --> Assignments`, supports filters.
The example below shows a list of non-dhcp active interfaces, for which multiple items may be selected, but at least one
should be. It defaults to :code:`lan`

.. csv-table:: InterfaceField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "Filters", "Y,N", "A structure of regex filters per atribute to exclude certain options from the list"
   "AddParentDevices", "Y,N", "Add parent devices in the list when not assigned"
   "AllowDynamic", "Y,N,S", "Allow dynamic (hotplug) interfaces, when set to :code:`S` hotplug interfaces without a static address are ignored"

.. code-block:: xml

    <interfaces type="InterfaceField">
        <Required>Y</Required>
        <multiple>Y</multiple>
        <default>lan</default>
        <filters>
            <enable>/^(?!0).*$/</enable>
            <ipaddr>/^((?!dhcp).)*$/</ipaddr>
        </filters>
    </interfaces>


JsonKeyValueStoreField
------------------------------------

A construct to validate against a json dataset retreived via configd, such as

.. code-block:: xml

    <program type="JsonKeyValueStoreField">
      <ConfigdPopulateAct>syslog list applications</ConfigdPopulateAct>
      <SourceFile>/tmp/syslog_applications.json</SourceFile>
      <ConfigdPopulateTTL>20</ConfigdPopulateTTL>
      <SortByValue>Y</SortByValue>
    </program>


In which case :code:`syslog list applications` is called to retrieved options, which is valid for 20 seconds (TTL) before fetching again.

.. csv-table:: JsonKeyValueStoreField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "ConfigdPopulateAct", ":code:`text`", "Configd command responsible for the data"
   "SourceFile", ":code:`text`", "Temporary filename where results are stored"
   "ConfigdPopulateTTL", ":code:`int`", "Time To Live in seconds"
   "SortByValue", "Y,N", "Sort by value, default sorts by key"


LegacyLinkField
------------------------------------

Read-only pointer to legacy config data, reads (single) property from the legacy configuration and returns its content
when it exists (:code:`null` if xml item doesn't exist).

The following example would read the enabled property from the config xml, which resides in :code:`<ipsec><enabled>1</enabled></ipsec>`

.. code-block:: xml

    <enabled type="LegacyLinkField">
        <Source>ipsec.enable</Source>
    </enabled>


.. Note::

      Values stored into this fieldtype will be discarded without further notice, which practically means the target structure
      will always contain an empty field as long as its used as a pointer.
      When functionality migrates to mvc, you can switch the type and supply migration code to load the initial values.


ModelRelationField
------------------------------------

Define relations to other nodes in the model, such as to point the attribute :code:`pipe` to a :code:`pipe` node in the TrafficShaper model.

.. code-block:: xml

    <pipe type="ModelRelationField">
        <Model>
            <pipes>
                <source>OPNsense.TrafficShaper.TrafficShaper</source>
                <items>pipes.pipe</items>
                <display>description</display>
            </pipes>
        </Model>
    </pipe>

.. csv-table:: ModelRelationField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "display", ":code:`text`", "Comma separated list of fields to display"
   "display_format", ":code:`text`", ":code:`vsprintf()` format string"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "Model", ":code:`xml`", "structure as described in the sample above"


NetworkAliasField
------------------------------------

Validate if the value is a valid network address (IPv4, IPv6), special net or alias.
Predefined special networks contain the following choices:

  * any
      *   any network
  * (self)
      *   This firewall
  * [interface]
      *   Interface network, where interface is one of :code:`lan`, :code:`wan`, :code:`opt[XX]` (e.g. opt1, opt2)
  * [interface]ip
      *   Interface address

All network/host type aliases (including, but not limited to GeoIP) defined in :menuselection:`Firewall -> Aliases` are
also valid choices.



.. csv-table:: NetworkAliasField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"


NetworkField
------------------------------------

Validate if the value is a valid network address (IPv4, IPv6).

.. csv-table:: NetworkField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "Mask", ":code:`regex`", "Optional validation regex"
   "NetMaskRequired", "Y,N", "Is a netmask required"
   "NetMaskAllowed", "Y,N", "Is a netmask allowed"
   "AddressFamily", ":code:`ipv4`, :code:`ipv6`", "Which address family to use, blank means ipv4+ipv6"
   "FieldSeparator", ":code:`text`", "Separator character to use"
   "WildcardEnabled", "Y,N", "Allow the use of the :code:`any` clause"
   "AsList", "Y,N", "Field type should return list items"
   "Strict", "Y,N", "Disallow the usage of host bits when a netmask is used"

NumericField
------------------------------------

Validate input to be of numeric type.


.. csv-table:: NumericField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "MinimumValue", ":code:`int`", "Minimum number"
   "MaximumValue", ":code:`int`", "Maximum number"


OptionField
------------------------------------

Validate against a static list of options.

.. csv-table:: OptionField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "OptionValues", ":code:`xml`", "Xml structure containing keys and values, when keys should be numeric, the value tag is also supported :code:`<opt1 value='1'>option1</opt1>`"

PortField
------------------------------------

Check if the input contains a valid portnumber or (optionally) predefined service name. Can be a range when
:code:`EnableRanges` is set to :code:`Y`.


.. csv-table:: PortField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options, when set the type is treated as a list"
   "EnableWellKnown", "Y,N", "Allow the usage of well known names such as 'http' and 'ssh'"
   "EnableRanges", "Y,N", "Allow the usa of ranges, such as :code:`80:100`"


ProtocolField
------------------------------------

List field type to validate if the provided value is a valid protocol name as defined by /etc/protocols
(e.g. TCP, UDP) extended with the :code:`any` option.

.. csv-table:: ProtocolField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"


TextField
------------------------------------

Validate regular text using a regex.

.. csv-table:: TextField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "Mask", ":code:`regex`", "Optional validation regex"


UniqueIdField
------------------------------------

Generate unique id numbers.

.. csv-table:: UniqueIdField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"


UpdateOnlyTextField
------------------------------------

Write only text fields, can be used to store passwords

.. csv-table:: TextField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "Mask", ":code:`regex`", "Optional validation regex"


UrlField
------------------------------------

Validate if the input contains a valid URL.

.. csv-table:: UrlField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"


VirtualIPField
------------------------------------

Select a virtual address defined in :menuselection:`Interfaces -> Virtual IPs -> Settings`, use with a bit of care as
the keys (addresses) are subjected to change.

.. csv-table:: VirtualIPField
   :header: "Parameter", "Options", "Purpose"
   :widths: 30, 20, 40

   "default", ":code:`text`", "Default value for new attributes"
   "Required", "Y,N", "Mark field as required"
   "ValidationMessage", ":code:`text`", "Error message on validation failure"
   "BlankDesc", ":code:`text`", "Set a label for the empty option"
   "Multiple", "Y,N", "Allow to select multiple options"
   "Type", ":code:`text`", "The virtual ip type to select, :code:`*` for all (default)"
