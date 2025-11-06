==================================================
ndproxy (Neighbour Discovery Proxy)
==================================================

.. contents::
   :local:
   :depth: 2

This manual provides a quick overview of ndproxy and how to configure it for general use.

.. Attention::

   The ndproxy setup is pretty fragile. Only use it as a last resort if there are no better alternatives.
   Due to limitations, ndproxy can only work with static prefixes. If your prefix changes often,
   it is not a permanent working solution. And even if it works, it can just randomly decide to stop working
   due to various reasons out of your control.


Introduction to ndproxy
==================================================

Ndproxy is a kernel module that acts as a proxy for IPv6 Neighbor Discovery (ND) messages between a Provider Edge (PE) router
and Customer Premises Equipment (CPE).

When ndproxy runs on the same device as the CPE (e.g., OPNsense), it allows the device
to act as both the home network’s router and the proxy for handling ND messages. This setup is particularly useful in cases
where an ISP only provides limited IPv6 delegation (e.g., a single /64 prefix). By using ndproxy, such limitations can be
bypassed to allow the LAN to use the ISP provided prefix.

For more technical details: `ndproxy(4) <https://man.freebsd.org/cgi/man.cgi?query=ndproxy>`_


Installation
--------------------------------------------------

Install ``os-ndproxy`` from :menuselection:`System --> Firmware --> Plugins`.


Important configuration details
--------------------------------------------------

- **IPv6 Global Unicast Address**:
    The WAN and LAN interface must not configure a GUA in the same /64 prefix. A GUA on WAN is required,
    ensure it is /128.

- **Promiscuous Mode**:
    The listening interface (WAN) must be set to promiscuous mode.
    If it is a VLAN, it must be set on the parent interface.
    The router must join multicast groups to respond to solicitations for hosts in the LAN.

.. Attention::

   You can proxy from WAN to one internal interface (e.g., LAN), not to multiple interfaces.


Offering services behind NAT (cloud setup)
==================================================

Introduction
--------------------------------------------------

Quite some cloud providers only offer a single :code:`/64` block via SLAAC which you can't easily push
down to your LAN interface when offering services with a firewall in between.

In these types of setups, it's usually practical to offer a private range to the machines (servers) behind
the firewall and forward the traffic mapping external addresses on the firewall via NAT.

One of the challenges of these setups is the need to configure (virtual) addresses on the firewall in order
to send it to the machine on the LAN interface, without a local address on the firewall, it wouldn't answer to neighbor discoveries
as these addresses are not local.

This is where :code:`ndproxy` can play a role and answer to neighbor discoveries for addresses only used in network addresses
translation rules.

Setup
--------------------------------------------------

First we configure the wan interface via :menuselection:`Interfaces --> WAN`

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``SLAAC``
**Promiscuous mode**                            ``X``
==============================================  ====================================================================


Next we allocate an address from a private range in :menuselection:`Interfaces --> LAN`

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``Static IPv6``
**IPv6 address**                                ``fd12:3456:789a:ffff::/64``
==============================================  ====================================================================

.. Note::

   The unique local address (ULA) prefix to use for machines in your network within the :code:`fc00::/7` range.

And configure router advertisements on LAN, :menuselection:`Services --> Router Advertisements --> [LAN]`, using the
settings below:

==============================================  ====================================================================
**Router Advertisements**                       ``Stateless``
==============================================  ====================================================================


In :menuselection:`Services --> Ndproxy` we will enable the ndproxy service, for this we need the MAC address of our WAN interface
and the default gateway received via WAN (Search for :code:`default` in :menuselection:`System --> Routes --> Status`), which is usually
quite static information.


==============================================  ====================================================================
**Enable**                                      ``X``
**Uplink Interface**                            ``WAN``
**Downlink MAC Address**                        ``1a:11:22:33:44:55``         (WAN MAC)
**Uplink IPv6 Addresses**                       ``fe80::fc00:ff:1111:2222``   (default route)
==============================================  ====================================================================

Finally we will map the internal addresses to the external ones using :menuselection:`Firewall --> NAT --> NPTv6`,
add a new rule using the following settings:


==============================================  ====================================================================
**Interface**                                   ``WAN``
**Internal IPv6 Prefix (source)**               ``fd12:3456:789a:ffff::/64``
==============================================  ====================================================================


Test
--------------------------------------------------

When all goes well, a client on LAN should receive an address via SLAAC in the ``fd12:3456:789a:ffff::/64`` range
and you should be able to ping an address on the internet.

Debugging
--------------------------------------------------

In case of malfunction, make sure to capture `icmp6` packets on both interfaces to inspect neighbor discovery packets.
