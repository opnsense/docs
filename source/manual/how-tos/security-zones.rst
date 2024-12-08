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

Our goal are the following zones and policies:

======================  ====================================  ========================================================================
Zone                    Interface                             Description
======================  ====================================  ========================================================================
**TRUST**               `igc0_vlan1` to `igc0_vlan9`
**UNTRUST**             `igc0_vlan10` to `igc0_vlan19`
**WIFI**.               `igc0_vlan20` to `igc0_vlan29`
======================  ====================================  ========================================================================

.. Note::

   When interfaces are assigned to devices, their default technical identifier is ``optX``. For clarity, the description of each interface
   was changed to reflect their interface+vlan name. E.g., if the interface identifier is opt19, and the device is vlan0.19 and the parent
   is igc0, the description is igc0_vlan19.


Interzone Policy:

- Allow `Trust`, `Untrust` and `Wifi` to use ICMP between their zones
- Allow `Trust` to access all other zones; excluding its own zone
- Allow `Wifi` to access `Untrust`
- Allow `Untrust` to access HTTPS in `Trust`

Intrazone Policy:

- Allow `Trust` to access `Trust`
- Allow `Wifi` to access SSH in `Wifi`

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

.. Tip::

   Do not create too many zones, they should be defined as broadly as possible.
   The more zones you maintain, the more aliases you need for all combinations.


- | Go to :menuselection:`Firewall --> Aliases` and add a new alias that contains all interface groups:

.. tabs::

    .. tab:: Alias 1

       ======================  ========================================================================
       **Name**                ZONES_TRUST_UNTRUST
       **Type**                Network group
       **Members**             __TRUST_network, __UNTRUST_network
       **Description**         Zones Trust, Untrust
       ======================  ========================================================================

    .. tab:: Alias 2

       ======================  ========================================================================
       **Name**                ZONES_TRUST_WIFI
       **Type**                Network group
       **Members**             __TRUST_network, __WIFI_network
       **Description**         Zones Trust, Wifi
       ======================  ========================================================================

    .. tab:: Alias 3

       ======================  ========================================================================
       **Name**                ZONES_UNTRUST_WIFI
       **Type**                Network group
       **Members**             __UNTRUST_network, __WIFI_network
       **Description**         Zones Untrust, Wifi
       ======================  ========================================================================

    .. tab:: Alias 4

       ======================  ========================================================================
       **Name**                ZONES_ALL
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

.. Attention::

   Be careful when crafting this ruleset so you do not accidentally mix interzone and intrazone rules unintentionally.


Go to :menuselection:`Firewall --> Rules --> Floating`

.. tabs::

    .. tab:: Rule 1

       Allow `Trust`, `Untrust` and `Wifi` to use ICMP between their zones.

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``TRUST``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    ICMP
       **Source**                                      any
       **Source port**                                 any
       **Destination**                                 ``ZONES_UNTRUST_WIFI``
       **Destination port**                            any
       **Description**                                 Allow ICMP between Trust and Untrust, Wifi
       ==============================================  ===================================================================================

    .. tab:: Rule 2

       Allow `Trust`, `Untrust` and `Wifi` to use ICMP between their zones.

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``UNTRUST``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    ICMP
       **Source**                                      any
       **Source port**                                 any
       **Destination**                                 ``ZONES_TRUST_WIFI``
       **Destination port**                            any
       **Description**                                 Allow ICMP between Untrust and Trust, Wifi
       ==============================================  ===================================================================================

    .. tab:: Rule 3

       Allow `Trust`, `Untrust` and `Wifi` to use ICMP between their zones.

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``WIFI``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    ICMP
       **Source**                                      any
       **Source port**                                 any
       **Destination**                                 ``ZONES_TRUST_UNTRUST``
       **Destination port**                            any
       **Description**                                 Allow ICMP between Wifi and Trust, Untrust
       ==============================================  ===================================================================================

    .. tab:: Rule 4

       Allow `Trust` to access all other zones; excluding its own zone.

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
       **Destination**                                 ``ZONES_UNTRUST_WIFI``
       **Destination port**                            any
       **Description**                                 Allow Any from Trust to other zones
       ==============================================  ===================================================================================

       .. Attention::

          This rule does not allow devices in TRUST to communicate with other devices in TRUST. For that, an intrazone policy will be
          established later.

    .. tab:: Rule 5

       Allow `Wifi` to access `Untrust`

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

    .. tab:: Rule 6

       Allow `Untrust` to access HTTPS in `Trust`

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

The next step is to create a selective ruleset that only concern traffic inside a single zone.
These can be outside the scope of the unified ruleset by leveraging the zone rulesets themselves. Please keep in mind that
matching floating rules will overrule selective rules.

.. tabs::

    .. tab:: Rule 1

       Allow `Trust` to access `Trust`

       - Go to :menuselection:`Firewall --> Rules --> TRUST`

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``TRUST``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    any
       **Source**                                      any
       **Source port**                                 any
       **Destination**                                 ``TRUST net``
       **Destination port**                            any
       **Description**                                 Allow Any from Trust to Trust
       ==============================================  ===================================================================================

       .. Note::

          Since we trust all devices inside the TRUST zone unconditionally, we allow free communication.

    .. tab:: Rule 2

       Allow `Wifi` to access SSH in `Wifi`

       - Go to :menuselection:`Firewall --> Rules --> WIFI`

       ==============================================  ===================================================================================
       **Action**                                      Pass
       **Quick**                                       ``X``
       **Interface**                                   ``WIFI``
       **Direction**                                   in
       **TCP/IP Version**                              IPv4
       **Protocol**                                    TCP
       **Source**                                      any
       **Source port**                                 any
       **Destination**                                 ``WIFI net``
       **Destination port**                            SSH
       **Description**                                 Allow SSH from WIFI to WIFI
       ==============================================  ===================================================================================

Interface Policies
------------------------------------

With the zone rulesets established, even more selective rules can be created on individual interfaces inside zones. These rules can allow selective
traffic from one interface to another interface for granular control.

If we want to allow HTTPS from a host_1 in vlan0.10 to a host_2 in vlan0.20, we create a rule like this:

- Go to :menuselection:`Firewall --> Rules --> vlan0.10`

==============================================  ===================================================================================
**Action**                                      Pass
**Quick**                                       ``X``
**Interface**                                   ``vlan0.10``
**Direction**                                   in
**TCP/IP Version**                              IPv4
**Protocol**                                    TCP
**Source**                                      host_1
**Source port**                                 any
**Destination**                                 host_2
**Destination port**                            HTTPS
**Description**                                 Allow HTTPS from host_1 to host_2
==============================================  ===================================================================================

.. Tip::

   Adding aliases for hosts is good practice.


Adding Additional Interfaces
------------------------------------

Now that the unified and selective rulesets are established, new interfaces can be added without the need of duplicating firewall rules.

If we need to expand the LAN network with more vlans that are on the same level of trust as the existing ones, we simply add the new interfaces
to the `TRUST` interface group. All existing rules will automatically apply to any new member interfaces.

Vice versa, if a network should become untrusted, we remove it from `TRUST` and add it to `UNTRUST`.

This makes administration and auditing the ruleset more efficient. Deployment of new firewalls or via central management is simplified.
