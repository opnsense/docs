===========================
Rules [new]
===========================

.. contents:: Index



Available rule parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /manual/forms/Firewall/dialogfilterrule.rst


Sort Order and Sequence
-------------------------------

While rules in :menuselection:`Firewall --> Rules` are processed implicitely by the order they appear in the configuration file,
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



