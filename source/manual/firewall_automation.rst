===========================
Automation
===========================

.. contents:: Index

The automation component offers API access to firewall and source nat rules.

Partial API access is described in more detail in the :doc:`firewall <../development/api/core/firewall>` API reference manual.


--------------------
Overview
--------------------

The automation filter pages use the MVC framework. This means, the component only has knowledge of rules created within it.
Any firewall filter and NAT rules created outside the automation filter pages will not be collected via its API endpoint.

The UI component can be found in :menuselection:`Firewall --> Automation`.
This shows a preview of the direction where the current :menuselection:`Firewall --> Rules` pages will be eventually
superseded by the automation component.


-------------------------------
Automation - Filter
-------------------------------

In :menuselection:`Firewall --> Automation -> Filter`, new firewall rules can be created.


User Interface
-------------------------------

At the top of the page, there are two selectpickers for interfaces and firewall groups and an inspect button.


Interface filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose an interface to filter the current view. Floating, group and single interfaces can be selected.

If you choose the "LAN" interface, you will be presented with all floating, group and single interface
rules that influence packet decisions of the LAN interface.

If you create a new rule while having an interface selected, it will be automatically added to dialog.


Categories filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose one or multiple categories to filter the current view. This combines with the selection of the interface filter.

Categories can be created in :menuselection:`Firewall --> Categories` and can enable grouping different logic constructs.

If you create a category for mailservers and tag rules with it, you can simply filter for this tag and only see your mailservers.

As with the interface filter, selecting one or multiple tags will add them automatically to a new rule.


Inspect button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The inspect button will reveal all system defined firewall rules and show rule statistics. It can be enabled at any time
to get a complete view of the current active ruleset.


Available rule parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /manual/forms/Firewall/dialogfilterrule.rst


Sort Order and Sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While rules in :menuselection:`Firewall --> Rules` are processed implicitly by the order they appear in the configuration file,
:menuselection:`Firewall --> Automation` filter rules implement a more explicit **Sort order**.

A **Sort order** will have this structure: ``200000.0000250``:

    - ``200000`` The **Prefix**, defines the hierarchy the rule belongs to. It can be influenced by the interface in a rule.
    - ``.0000250`` The **Sequence**, it defines the exact spot of the rule in context of the interface hierarchy. It can be influenced with the `Sequence` field inside a rule, or with the `Move rule before this rule` button.

As example, we create a few different rules:

    - ``200000.0000100`` (Floating rule)
    - ``200000.0000200`` (Floating rule)
    - ``300000.0000050`` (Group rule)
    - ``300000.0000060`` (Group rule)
    - ``400000.0002000`` (Interface rule)
    - ``400000.0003100`` (Interface rule)

When applying the filter, the rules will be processed in this **Sort order**.

.. Note::

    The `Sequence` does not have to be unique, multiple rules can share the same number.
    Though what this means is that the filter is not populated as strictly in order as if all rules have a unique sequence.

.. Tip::

    When adding a new rule, the `Sequence` will be automatically populated with a unique number. You can either change this number manually
    to adjust the exact position of the rule, or use the `Move rule before this rule` button.


Processing Order
-------------------------------

Since :menuselection:`Firewall --> Automation` and :menuselection:`Firewall --> Rules` component exist side by side,
there are some considerations regarding the processing order of rules.

If an :menuselection:`Firewall --> Automation` filter rule has:

    - a single interface defined, it is an **Interface Rule**
    - a group interface defined, it is a **Group Rule**
    - any number of interfaces defined, it is a **Floating Rule**

Processing order:

    1. System defined rules at the beginning of the ruleset
    2. :menuselection:`Firewall --> Automation` and :menuselection:`Firewall --> Rules` floating rules
    3. :menuselection:`Firewall --> Automation` and :menuselection:`Firewall --> Rules` group rules
    4. :menuselection:`Firewall --> Automation` single interface rules
    5. :menuselection:`Firewall --> Rules` single interface rules
    6. System defined rules at the end of the ruleset


-------------------------------
Automation - Source NAT
-------------------------------

In :menuselection:`Firewall --> Automation -> Source NAT`, new source NAT rules (also known as Outbound NAT or Masquerading)
can be created.

These automation source NAT rules will match before :menuselection:`Firewall --> NAT` defined ones.

