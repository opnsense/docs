============================
Transparent Filtering Bridge
============================

.. contents:: Index


Introduction
============================

A transparent firewall can be used to filter traffic without creating different subnets.

The firewall bridges the same layer 2 broadcast domain across two or more ports.

If a VLAN trunk is connected, any VLAN tagged frames will also be bridged transparently.

This can be used to filter via firewall rules and use IDS/IPS to inspect all packets
via a netmap driver.

For more information on Filtering Bridged on FreeBSD, see
`filtering-bridges <https://www.freebsd.org/doc/en/articles/filtering-bridges/article.html>`__

.. Attention::

   The `Transparent Filtering Bridge` is not compatible with `Traffic Shaping`,
   do not enable it.

.. Attention::

   When vlan tagged frames should be passed through, do not create any vlans on the member ports of the bridge.
   Otherwise, vlan tagged frames would be filtered and the bridge would not be transparent anymore.


Requirements
----------------------------

For best compatibility and performance, a bare metal appliance with at least 3 physical ports should be used.
A virtualized appliance could also work, but there could be layer 2 issues with bridging or vlans, and degraded bridging performance.

.. Attention::

   If a vlan trunk is used, you should always use a bare metal appliance, and preferably Intel network cards.
   The native netmap driver used for IDS/IPS in combination with VLANs does not always work correctly with other vendors or
   virtualized NICs. Please also ensure that only tagged frames are sent over this trunk.


Configuration
============================

Our example appliance has 3 available network ports

- igc0 - LAN (Bridge)
- igc1 - WAN (Bridge)
- igc2 - Management


1. Assign a management interface (igc2)
---------------------------------------

We need an interface to manage the firewall and to enable access to the internet so it can pull firmware updates.

Go to :menuselection:`Interfaces --> Assignements`, and `Assign a new interface`.

Select one of the free available ports (e.g. igc2) and assign it, set the description to `Management`.

Afterwards go to `Interfaces --> Management` and set `IPv4 Configuration Type` to `DHCP` or `Static IPv4` dependant on your usecase.

Since this interface will be used for management and internet connection, `DHCP` would be the simplest.

Next we add a firewall rule to allow access to the OPNsense on this management interface.

Go to :menuselection:`Firewall --> Rules --> Management` and add a new rule that allows access to destination ``This Firewall``
on the WebGUI port you chose, most likely ``443``.

After applying all of these settings, connect to your appliance over the management port for the next steps.


2. Change system tuneables
--------------------------

Here we change that the firewall rules should match on the bridge, instead of the bridge members.

Go to :menuselection:`System --> Settings --> System Tuneables` and change:

**net.link.bridge.pfil_bridge** to 1
**net.link.bridge.pfil_member** to 0


3. Create the bridge
--------------------

Go to :menuselection:`Interfaces --> WAN` and :menuselection:`Interfaces --> LAN`

Ensure both `IPv4 Configuration Type` and `IPv6 Configuration Type` are ``None``,
and **Block private networks**, **Block bogon networks** are disabled.

.. Attention::

   Disable any DHCP servers that are bound to the LAN interface.

Go to :menuselection:`Interfaces --> Devices --> Bridge`.

Add a new bridge and select WAN and LAN as `Member interfaces`, Description `Bridge`

.. Attention::

   Do not select `Enable link-local address`, in this configuration the bridge interface
   should stay unnumbered (no IP addresses or any vlans assigned to it or its member interfaces)


4. Add Firewall rules
----------------------------

Add firewall rules on the new bridge interface to allow all traffic.

Go to :menuselection:`Firewall --> Rules --> Bridge` and add new rules that allows any traffic.

After installing the bridge, you can create more restrictive rules if required. If only IDS/IPS should be used,
any allow rules are sufficient. Since the bridge is fully transparent and unnumbered, no client can communicate
with the firewall directly via IP.


5. Enable IDS/IPS (optional)
----------------------------

To inspect all bridge traffic, we can enable the `Intrusion Detection` service.

Go to :menuselection:`Services --> Intrusion Detection --> Administration --> General Settings`

================================ ========================================================================================
Option                           Description
================================ ========================================================================================
Enabled                          ``X``
IPS mode                         ``X``
Promiscuous mode                 ``X`` (if vlan tagged frames are received on bridge members)
Interfaces                       ``WAN`` (Do not choose the bridge interface, since the netmap driver cannot process vlans on it)
================================ ========================================================================================

Afterwards download and activate the rules that you need and apply the configuration.


6. Connect interfaces to existing infrastructure
--------------------------------------------------------

Now you can patch the bridge member interfaces WAN and LAN to their respective switch or router.

WAN should be connected to a switch or router on the WAN facing side, and LAN on the internal side.

When installing the bridge, ensure that there is no better network path around it, both sides should be isolated and only connected via
the bridge.

Via the already connected Management port, the firewall will be able to connect to the internet to fetch the latest updates.
