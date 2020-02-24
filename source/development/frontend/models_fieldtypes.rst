----------------------
Standard field types
----------------------

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


AuthGroupField
------------------------------------

Returns and validates system (user) groups (found in :menuselection:`System --> Access --> Groups`)


AuthenticationServerField
------------------------------------

Select and validate authentication providers, maintained in :menuselection:`System --> Access --> Servers`.


AutoNumberField
------------------------------------

An integer sequence, which automatically increments on every new item of the same type in the same level.

BooleanField
------------------------------------

Boolean field, where 0 means :code:`false` and 1 is defined as :code:`true`

CSVListField
------------------------------------

List of (comma) separated values, which can be validated using a regex.

CertificateField
------------------------------------

Option list with system certificates defined in :menuselection:`System --> Trust`, use the `Type` keyword to distinct between the
available options (:code:`ca`, :code:`crl`, :code:`cert`), defaults to :code:`cert`.

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


CountryField
------------------------------------

Select and validate countries in the world.

EmailField
------------------------------------

Validate if the input contains an email address.

HostnameField
------------------------------------

Check if hostnames are valid (optionally allows IP addresses as well)

IntegerField
------------------------------------

Validate if the input contains an integere value, optionally constrained by minimum and maximum values.

InterfaceField
------------------------------------

Option list with interfaces defined in :menuselection:`Interfaces --> Assignments`, supports filters.
The example below shows a list of non-dhcp active interfaces, for which multiple items may be selected, but at least one
should be. It defaults to :code:`lan`

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



NetworkField
------------------------------------

Validate if the value is a valid network address (IPv4, IPv6).

NumericField
------------------------------------

Validate input to be of numeric type.

OptionField
------------------------------------

Validate against a static list of options.

PortField
------------------------------------

Check if the input contains a valid portnumber or (optionally) predefined service name. Can be a range when
:code:`EnableRanges` is set to :code:`Y`.

TextField
------------------------------------

Validate regular text using a regex.

UniqueIdField
==================================

Generate unique id numbers.

UpdateOnlyTextField
------------------------------------

Write only text fields, can be used to store passwords

UrlField
------------------------------------

Validate if the input contains a valid URL.
