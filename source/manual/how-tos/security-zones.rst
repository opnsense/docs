========================================
Security Zones
========================================

**Summary**

Use security zones to group network interfaces and establish a consistent, top-level firewall ruleset.

.. contents::
   :local:
   :depth: 2


----------------------------
Introduction
----------------------------

Firewalls manage traffic between network segments. Utilizing **zones** simplifies configurations by grouping interfaces with similar security trust levels. This approach is beneficial when managing numerous interfaces that require a consistent and unified ruleset.

Zones allow administrators to define policies based on trust levels rather than individual interfaces. Common examples include:

- **Trust**: Secure internal networks
- **Untrust**: External networks, such as the Internet
- **DMZ**: Public-facing services
- **Guest**: Limited access for guest users

.. Tip::

   For more details about constraints, refer to the `Firewall Groups <https://docs.opnsense.org/manual/firewall_groups.html>`_
   and `Processing Order <https://docs.opnsense.org/manual/firewall.html#processing-order>`_ sections of the documentation.

When a packet arrives at a firewall interface, it is assigned to a zone based on the inbound interface. This **packet tagging** process involves:

1. Determining the receiving interface
2. Assigning the packet to the interface's configured zone
3. Applying security policies between the source and destination zones

======================  ================
Zone (Interface Group)  Interfaces
======================  ================
**Trust**               igc0, igc1, igc2
**Untrust**             igc3, igc4
======================  ================

A packet arriving on `igc0`, `igc1`, or `igc2` is tagged as **Trust**. If it needs to traverse to `igc3` or `igc4`, tagged as **Untrust**, the firewall applies the relevant policies.

.. Note::

   - Intrazone rules handle similar trust levels collectively, e.g., `from Trust to Trust`
   - Interzone rules define boundaries between areas with different trust levels, e.g., `from Trust to Untrust`


----------------------------
Benefit of Zones
----------------------------

Defining uniform policies between zones reduces the number of rules and the complexity of the ruleset. 
For example, allowing all networks in **Trust** to access HTTPS services in **Untrust** can be achieved with a single rule.

Without Zones (6 Rules):

- Allow HTTPS from `igc0` to `igc3`
- Allow HTTPS from `igc0` to `igc4`
- Allow HTTPS from `igc1` to `igc3`
- Allow HTTPS from `igc1` to `igc4`
- Allow HTTPS from `igc2` to `igc3`
- Allow HTTPS from `igc2` to `igc4`

With Zones (1 Rule):

- Allow HTTPS from **Trust** to **Untrust**

Additionally, a zone-based ruleset allows new interfaces to be added without requiring additional rules, reducing administrative overhead.
This approach also enhances configuration clarity, simplifies troubleshooting, and streamlines audits.

.. Note::

   Constraints may arise when using Multi-WAN configurations because the `reply-to` option does not apply to rules within interface groups.


----------------------------
Setup Overview
----------------------------

In our example setup, we will create a unified ruleset, leveraging interface groups as security trust zones. This unified ruleset
will be created in :menuselection:`Firewall --> Rules --> Floating` to match first.

Our goals are the following zones:

======================  ====================================  ========================================================================
Zone                    Interface                             Description
======================  ====================================  ========================================================================
**TRUST**               `igc0_vlan1` to `igc0_vlan9`          Trusted internal networks like LAN
**UNTRUST**             `igc0_vlan10` to `igc0_vlan19`        Untrusted external networks like VPN, WAN, GUEST
**WIFI**                `igc0_vlan20` to `igc0_vlan29`        Wireless networks with limited trust like WIFI
======================  ====================================  ========================================================================

.. Note::

   When interfaces are assigned to devices, their default technical identifier is `optX`. For clarity, the description of each interface
   was changed to reflect their `interface+vlan` name. E.g., if the interface identifier is `opt19`, and the device is `vlan0.19` with parent
   `igc0`, the description is `igc0_vlan19`.


Setup Interface Groups
-------------------------------------------

The first step is to create interface groups that contain our vlans. This will group them together into the same security trust zones for our
planned unified ruleset.

- | Go to :menuselection:`Firewall --> Groups` and add new entries for the required zones:

.. tabs::

    .. tab:: Trust

       ======================  ====================================
       **Name**                TRUST
       **Members**             vlan0.10, vlan0.11, ..., vlan0.19
       **(no) GUI groups**     unchecked
       **Sequence**            0
       **Description**         Zone for all trusted networks
       ======================  ====================================

    .. tab:: Untrust

       ======================  ====================================
       **Name**                UNTRUST
       **Members**             vlan0.20, vlan0.21, ..., vlan0.29
       **(no) GUI groups**     unchecked  
       **Sequence**            1
       **Description**         Zone for all untrusted networks
       ======================  ====================================

    .. tab:: Wifi

       ======================  ====================================
       **Name**                WIFI
       **Members**             vlan0.30, vlan0.31, ..., vlan0.39
       **(no) GUI groups**     unchecked
       **Sequence**            2
       **Description**         Zone for all wireless networks
       ======================  ====================================


.. Tip::

   Do not create too many zones, they should be defined as broadly as possible as they are the highest level of hierarchy.


The interfaces will be grouped together in :menuselection:`Firewall --> Rules` and :menuselection:`Interfaces`.
When configuring the zone based ruleset, keep the firewall rule precedence in mind.


Verify Aliases
----------------------------

After creating the interface groups, we can check if the automatic aliases contain the expected content.

- | Go to :menuselection:`Firewall --> Diagnostics --> Aliases`

In the dropdown, choose `TRUST net`, `UNTRUST net` and `WIFI net`. Their corresponding IP networks will be displayed as they are automatically
gathered from the configured interface IP addresses.

When using these aliases, all of these networks are automatically part of the firewall rule.


Create Security Zone Policies
--------------------------------------

Our unified ruleset will create a baseline that will always match on top-level. Afterwards, we can create more selective allow rules in
the individual interface groups. The following policies give a short overview about zone based rules and their results.

Go to :menuselection:`Firewall --> Rules --> Floating`

.. Tip::

   With the multiselect feature in source and destination you can select multiple aliases per rule. Each alias represents the interface group created before.
   Each interface group represent a zone.


.. tabs::

    .. tab:: Rule 1

       - Allow `Trust`, `Untrust` and `Wifi` to use ICMP between and inside all networks in their zones

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   any
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    ICMP
       **Source**                                      ``TRUST net, UNTRUST net, WIFI net``
       **Source port**                                 any
       **Destination**                                 ``TRUST net, UNTRUST net, WIFI net``
       **Destination port**                            any
       **Description**                                 Allow ICMP between TRUST, UNTRUST, WIFI
       ==============================================  ===================================================================================

       .. Note::

          This single GUI rule will create a `Cartesian product` and result in six firewall rules in pf(4). Be mindful using inversions in rules
          or inverted aliases, since they can be generated in an order that creates an unexpected result.

       .. Attention::

          This rule will also allow ICMP between all networks inside a zone, that means it is a mixed interzone and intrazone rule.
          Use these sparingly for broad diagnostic or administrative rules, as they overrule more selective policies that come later in
          the same ruleset.


    .. tab:: Rule 2

       - Allow `Trust` to access the other zones; excluding its own zone

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   any
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    any
       **Source**                                      ``TRUST net``
       **Source port**                                 any
       **Destination**                                 ``UNTRUST net, WIFI net``
       **Destination port**                            any
       **Description**                                 Allow any from TRUST to UNTRUST, WIFI
       ==============================================  ===================================================================================

       .. Note::

          This single GUI rule will result in two firewall rules in pf(4). It is a clean interzone rule, allowing
          `Trust` to `Untrust` and `Wifi`, but not the other way around.


    .. tab:: Rule 3

       - Allow `Wifi` to access `Untrust`

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   any
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    any
       **Source**                                      ``WIFI net``
       **Source port**                                 any
       **Destination**                                 ``UNTRUST net``
       **Destination port**                            any
       **Description**                                 Allow any from WIFI to UNTRUST
       ==============================================  ===================================================================================


    .. tab:: Rule 4

       - Allow `Untrust` to access HTTPS in `Trust`

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   any
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    ``TCP/UDP``
       **Source**                                      ``UNTRUST net``
       **Source port**                                 any
       **Destination**                                 ``TRUST net``
       **Destination port**                            ``HTTPS``
       **Description**                                 Allow HTTPS from UNTRUST to TRUST
       ==============================================  ===================================================================================


Adding Additional Interfaces
------------------------------------

Now that the unified ruleset is established, new interfaces can be added without the need of duplicating firewall rules.

If we expand the LAN network with more vlans that are on the same level of trust as the existing ones, we simply add the new interfaces
to the `TRUST` interface group. All existing rules will automatically apply to any new member interfaces.

Vice versa, if a network should become untrusted, we remove it from `TRUST` and add it to `UNTRUST`.

This makes administration and auditing the ruleset more efficient. Deployment of new firewalls or via central management is simplified.
