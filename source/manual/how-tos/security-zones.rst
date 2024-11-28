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
**Trust**               eth0, eth1, eth2
**Untrust**             eth3, eth4
======================  ================

A packet arriving on `eth0`, `eth1`, or `eth2` is tagged as **Trust**. If it needs to traverse to `eth3` or `eth4`, tagged as **Untrust**, the firewall applies the relevant policies.

.. Note::

   - Intrazone rules handle similar trust levels collectively, e.g., `from Trust to Trust`
   - Interzone rules define boundaries between areas with different trust levels, e.g., `from Trust to Untrust`


----------------------------
Benefit of Zones
----------------------------

Defining uniform policies between zones reduces the number of rules and the complexity of the ruleset. 
For example, allowing all networks in **Trust** to access HTTPS services in **Untrust** can be achieved with a single rule.

Without Zones (6 Rules):

- Allow HTTPS from `eth0` to `eth3`
- Allow HTTPS from `eth0` to `eth4`
- Allow HTTPS from `eth1` to `eth3`
- Allow HTTPS from `eth1` to `eth4`
- Allow HTTPS from `eth2` to `eth3`
- Allow HTTPS from `eth2` to `eth4`

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

The zones from the introduction will be used. Our goal is the following ruleset:

- Rule 1: Allowing `Trust`, `Untrust` and `Wifi` to use ICMP between their zones
- Rule 2: Allowing `Trust` to access all zones, including itself, with no restrictions
- Rule 3: Allowing `Wifi` to access `Untrust`
- Rule 4: Allowing `Untrust` to access HTTPS in `Trust`
- Rule 5: Allowing `vlan0.30` to access HTTPS in `vlan0.39`
- Rule 6: Allowing `vlan0.25` to access SSH to `172.16.1.10`

We have multiple VLANs that will be unified into security trust zones:

- `vlan0.10` to `vlan0.19` contain trusted internal networks
- `vlan0.20` to `vlan0.29` contain untrusted external networks
- `vlan0.30` to `vlan0.39` contain wireless networks


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
       **Description**         All trusted networks
       ======================  ====================================

    .. tab:: Untrust

       ======================  ====================================
       **Name**                UNTRUST
       **Members**             vlan0.20, vlan0.21, ..., vlan0.29
       **(no) GUI groups**     unchecked  
       **Sequence**            1
       **Description**         All untrusted networks
       ======================  ====================================

    .. tab:: Wifi

       ======================  ====================================
       **Name**                WIFI
       **Members**             vlan0.30, vlan0.31, ..., vlan0.39
       **(no) GUI groups**     unchecked
       **Sequence**            2
       **Description**         All wireless networks
       ======================  ====================================


- | Go to :menuselection:`Firewall --> Aliases` and add a new alias that contains all interface groups:

======================  ========================================================================
**Name**                ALL_ZONES
**Type**                Network group
**Members**             __TRUST_network, __UNTRUST_network, __WIFI_network
**Description**         All security zones
======================  ========================================================================


After applying the configuration, the interfaces will be grouped together in :menuselection:`Firewall --> Rules` and :menuselection:`Interfaces`.
When configuring the zone based ruleset, keep the firewall rule precedence in mind. Since we require a unified ruleset for zones,
most of our rules will be created in :menuselection:`Firewall --> Rules --> Floating` so they match first before all other rulesets.


Verify Aliases
----------------------------

After creating the interface groups, we can check if the aliases contain the expected content.

- | Go to :menuselection:`Firewall --> Diagnostics --> Aliases`

In the dropdown, choose `TRUST net`, `UNTRUST net` and `WIFI net`. Their corresponding IP networks will be displayed as they are automatically
gathered from the interface IP addresses of the vlans.

When using this alias, all of these networks are automatically part of the firewall rule.


Interzone Policies (from Zone to Zone)
--------------------------------------

The first step in our unified ruleset is creating a baseline that will always match on top-level. Afterwards, we can create more selective allow rules in
the individual interface groups.

.. Note::

   Interzone rules are best-suited for the floating ruleset.
   Here, multiple zones can be selected per rule, giving us much more flexibility.


Go to :menuselection:`Firewall --> Rules --> Floating`

.. tabs::

    .. tab:: Rule 1

       - Allowing `Trust`, `Untrust` and `Wifi` to use ICMP between their zones

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``TRUST``,``UNTRUST``, ``WIFI``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    ICMP
       **Source**                                      any
       **Source port**                                 any
       **Destination**                                 ``ALL_ZONES``
       **Destination port**                            any
       **Description**                                 Allow ICMP between Trust, Untrust and Wifi and all zones
       ==============================================  ===================================================================================

    .. tab:: Rule 2

       - Allowing `Trust` to access all zones, including itself, with no restrictions

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``TRUST``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    any
       **Source**                                      any
       **Source port**                                 any
       **Destination / Invert**                        ``X``
       **Destination**                                 ``TRUST net``
       **Destination port**                            any
       **Description**                                 Allow Any from Trust to all other zones
       ==============================================  ===================================================================================

       .. Attention::

          Since the destination is inverted, `TRUST` will be allowed to access all networks that are **not** defined in `TRUST net`.
          You can create the same rule without the inversion, to allow all intrazone traffic inside TRUST per default. This comes with the
          constraint that more selective rules will not match in the `TRUST` interface group anymore,
          as they are processed after floating rules.


    .. tab:: Rule 3

       - Allowing `Wifi` to access `Untrust`

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``WIFI``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    any
       **Source**                                      any
       **Source port**                                 any
       **Destination**                                 ``UNTRUST net``
       **Destination port**                            any
       **Description**                                 Allow Any from Wifi to Untrust
       ==============================================  ===================================================================================

    .. tab:: Rule 4

       - Allowing `Untrust` to access HTTPS in `Trust`

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``UNTRUST``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    TCP
       **Source**                                      any
       **Source port**                                 any
       **Destination**                                 ``TRUST net``
       **Destination port**                            HTTPS
       **Description**                                 Allow HTTPS from Untrust to Trust
       ==============================================  ===================================================================================


Intrazone Policies (in same Zone)
------------------------------------

The next step is to create a selective ruleset for rules that only concern single or multiple interfaces inside a single zone.
These can be outside the scope of the unified ruleset by leveraging the zone rulesets themselves. Please keep in mind that
matching floating rules will overrule selective rules.

.. tabs::

    .. tab:: Rule 5

       - Allowing `vlan0.30` to access HTTPS in `vlan0.39`

       Go to :menuselection:`Firewall --> Rules --> WIFI`

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``WIFI``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    TCP
       **Source**                                      ``vlan0.30 net``
       **Source port**                                 any
       **Destination**                                 ``vlan0.39 net``
       **Destination port**                            HTTPS
       **Description**                                 Allow HTTPS from vlan0.30 to vlan0.39
       ==============================================  ===================================================================================

    .. tab:: Rule 6

       - Rule 6: Allowing `vlan0.250` to access SSH to `172.16.1.10`

       Go to :menuselection:`Firewall --> Rules --> UNTRUST`

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``UNTRUST``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    TCP
       **Source**                                      ``vlan0.25 net``
       **Source port**                                 any
       **Destination**                                 ``172.16.1.10/32``
       **Destination port**                            SSH
       **Description**                                 Allow SSH from vlan0.25 to 172.16.1.10
       ==============================================  ===================================================================================


.. Tip::

   To maintain the conciseness of the ruleset,
   all interzone rules should be in `Floating` and all intrazone or host specific rules in their respective interface group.
   Creating rules on single interfaces should be avoided.


Adding Additional Interfaces
------------------------------------

Now that the unified and selective rulesets are established, new interfaces can be added without the need of duplicating firewall rules.

If we need to expand the LAN network with more vlans that are on the same level of trust as the existing ones, we simply add the new interfaces
to the `TRUST` interface group. All existing rules will automatically apply to any new member interfaces.

Vice versa, if a network should become untrusted, we remove it from `TRUST` and add it to `UNTRUST`.

This makes administration and auditing of the ruleset more efficient. Deployment to new firewalls or via central management is simplified.
