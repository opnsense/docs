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
Any firewall filter and NAT rules created via legacy pages will not be editable via this API endpoint.

The UI component can be found in :menuselection:`Firewall --> Automation` and has been redesigned in version 25.1.5.
This shows a preview of the direction where the legacy firewall pages will be eventually superseded by the automation component.

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
-------------------------------

.. include:: /manual/forms/Firewall/dialogfilterrule.rst


Processing Order
-------------------------------

Since the automation and legacy component exist side by side, there are some considerations regarding the processing
order of rules.

If an automation filter rule has:
    - a single interface defined, it will match before a single interface rule created in the legacy filter
    - two or more interfaces defined, it will match in the same scope as a group rule in the legacy filter
    - any interface defined, it will match in the same scope as a floating rule in the legacy filter

Processing order:
    1. System defined rules at the beginning of the ruleset
    2. Automation and legacy floating rules
    3. Automation and legacy group rules
    4. Automation single interface rules
    5. Legacy single interface rules
    6. System defined rules at the end of the ruleset

-------------------------------
Automation - Source NAT
-------------------------------

In :menuselection:`Firewall --> Automation -> Source NAT`, new source NAT rules (also known as Outbound NAT or Masquerading)
can be created.

These automation source NAT rules will match before legacy defined ones.

