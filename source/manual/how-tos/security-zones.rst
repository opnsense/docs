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

Firewalls manage traffic between network segments. Utilizing **zones** simplifies configurations by grouping interfaces with similar security trust levels. This approach is especially beneficial when managing numerous interfaces that require a consistent and unified ruleset.

Zones allow administrators to define policies based on trust levels rather than individual interfaces. Common examples include:

- **Trust**: Secure internal networks
- **Untrust**: External networks, such as the Internet
- **DMZ**: Public-facing services
- **Guest**: Limited access for guest users

.. Tip::

   For more details about constraints, refer to the `Firewall Groups <https://docs.opnsense.org/manual/firewall_groups.html>`_
   and `Processing Order <https://docs.opnsense.org/manual/firewall.html#processing-order>`_ sections of the documentation.

Packet Tagging Process
----------------------------

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

Benefits
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

The zones from the introduction will be used. Our goal is: 

- Allowing `Trust`, `Untrust` and `Wifi` to use ICMP between their zones
- Allowing `Trust` to access the other security zones with no restrictions
- Allowing `Untrust` to access HTTPS in `Trust`
- Allowing `Wifi` to access `Untrust`


We have multiple VLANs that will be unified into security trust zones:

- vlan0.100 to vlan0.199 contain trusted LAN networks
- vlan0.200 to vlan0.299 contain untrusted external networks
- vlan0.300 to vlan0.399 contain limited trusted guest networks, e.g., WIFIs


1. Setup Interface Groups
-------------------------------------------

The first step is to create interface groups that contain our vlans. This will group them together into the same security trust zones for our
planned unified ruleset.

- | Go to :menuselection:`Firewall --> Groups` and add new entries for the required zones:

.. tabs::

    .. tab:: Trust

       ======================  ====================================
       **Name**                TRUST
       **Members**             vlan0.100, vlan0.101, ..., vlan0.199
       **(no) GUI groups**     unchecked
       **Sequence**            0
       **Description**         All trusted networks like LAN
       ======================  ====================================

    .. tab:: Untrust

       ======================  ====================================
       **Name**                UNTRUST
       **Members**             vlan0.200, vlan0.201, ..., vlan0.299
       **(no) GUI groups**     unchecked  
       **Sequence**            1
       **Description**         All untrusted networks like WAN/VPN
       ======================  ====================================

    .. tab:: Wifi

       ======================  ====================================
       **Name**                WIFI
       **Members**             vlan0.300,vlan0.301, ..., vlan0.399
       **(no) GUI groups**     unchecked
       **Sequence**            2
       **Description**         All wireless networks
       ======================  ====================================


After applying the configuration, the interfaces will be grouped together in :menuselection:`Firewall --> Rules` and :menuselection:`Interfaces`
When configuring the zone based ruleset keep the firewall rule precedence in mind. Since we require a unified ruleset for zones,
all of our rules will be created in :menuselection:`Firewall --> Rules --> Floating` so they match first before all other rulesets.


2. Verify Aliases
----------------------------


3. Create Firewall rules
----------------------------

