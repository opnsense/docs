==================================================
ndproxy (Neighbour Discovery Proxy)
==================================================

.. contents::
   :local:
   :depth: 2

This manual provides a quick overview of ndproxy and how to configure it for general use.


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

- **Promiscuous Mode**:
    The listening interface (WAN) must be set to promiscuous mode. 
    Otherwise the router can not join multicast groups to respond to solicitations for hosts in the LAN.
  
- **Link-Local Address**:
    The listening interface (WAN) requires at least a link-local IPv6 address.
    If you want to add a GUA (Global Unicast Address) to WAN, it must be with /128 Prefix.
  
.. Attention::

   If WAN and LAN both have a GUA configured with the same /64 Prefix, this setup will not work. The network stack will not be able
   to decide the sending interface, and routing will fail.
   
- **Switch configuration**:

   If there is a switch between the PE and CPE router, ensure there is no MLD snooping or Multicast (IGMP) snooping configured
   on the VLAN.


Proxy /64 Prefix from WAN to LAN
==================================================

There must be a Provider Edge (PE) router that delegates an IPv6 Prefix to your OPNsense (CPE). You need to acquire the link-local IPv6 address of this PE router.
The simplest way to do that is to check your IPv6 routing table on the CPE router. The link-local IPv6 address of the IPv6 default route will be the PE router.

To explain this setup in more detail, two OPNsense will be used to simulate the PE and CPE router.


Network Diagram
------------------------------------------

::

        +-----------------+       Prefix Delegation: /64     +-----------------+
        |                 | LAN                          WAN |                 |
        |    Router PE    |----------------------------------|    Router CPE   |
        |                 | fe80::1/64            fe80::2/64 |    (ndproxy)    |
        +-----------------+ 2001:db8::1/64   2001:db8::2/128 +-----------------+
                | WAN                                             LAN |
                |                                                     |
        Prefix Delegation: /56                                        |
                |                                                     |
          fe80::1/64                                            fe80::1/64
          2001:db8::/56                                         2001:db8::3/64
                |                                                     |
                |                                                     |
            INTERNET                                     IPv6 Client: 2001:db8::200/64

.. Note::

   The link-local (LLA) and global unicast (GUA) addresses are most likely auto generated in real environments.
   The IPv6 default routes are always the LLAs.


Setup PE Router (Optional)
--------------------------------------------------

.. Tip::

   This configuration step can be skipped as it explains what the PE router does. In a home setup, this router is not in your control.
   If you plan to configure your own router cascade with limited IPv6 prefixes, this step will be helpful.


We assume:

    - The network we receive from the ISP is ``2001:db8::/56``
    - We want to delegate ``2001:db8::/64`` downstream
    - The WAN configuration of the CPE router is already configured and has a static prefix
    - The interface setup is like the Network Diagram


Go to :menuselection:`Interfaces --> LAN`

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``Static IPv6``
**IPv6 address**                                ``2001:db8::1/64``
==============================================  ====================================================================

Go to :menuselection:`Services --> ISC DHCPv6 --> LAN`

==============================================  ====================================================================
**Enable**                                      ``X``
**Range**                                       from: ``2001:db8::2`` to: ``2001:db8::2``
**Prefix Delegation Range**                     from: ``2001:db8::`` to: ``2001:db8::``
**Prefix Delegation Size**                      ``64``
==============================================  ====================================================================

Go to :menuselection:`Services --> Router Advertisements --> LAN`

==============================================  ====================================================================
**Router Advertisements**                       ``Router Only``
**Advertise Default Gateway**                   ``X``
==============================================  ====================================================================

With this configuration, the ``2001:db8::/64`` network will be delegated to the downstream CPE router. It will receive ``2001:db8::2/128`` on its WAN interface, and
a default IPv6 route to the PE router's LLA ``fe80::1``.


Setup CPE Router
--------------------------------------------------

This is the OPNsense attached to PE router, it will receive the delegated /64 Prefix on its WAN interface. The goal is to use this prefix on the LAN interface by proxying NDP messages with ndproxy. Without it, only the router itself could use this network.

With ndproxy, NDP (Neighbor Discovery Procotol) will be proxied from LAN to WAN so all LAN IPv6 devices can be discovered by the PE router.

Go to :menuselection:`Interfaces --> WAN`

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``DHCPv6``
**Promiscous Mode**                             ``X`` 
                                                (important to respond to all NDP Multicasts)
**Prefix Delegation Size**                      ``64``
**Request Prefix Only**                         ``X``
                                                (optional)
==============================================  ====================================================================

.. Note::

   `Request Prefix Only` is optional, but needed if your WAN interface would autoconfigure a /64 GUA. 
   Since that would break routing this setting is recommended. If WAN autoconfigures a /128 GUA,
   this setting can stay disabled.


Go to :menuselection:`Interfaces --> LAN`

=============================================================================  =====================================
**IPv6 Configuration Type**                                                    ``Track Interface``
**Parent Interface**                                                           ``WAN``
**Assign Prefix ID**                                                           ``0``
**Allow manual adjustement of DHCPv6 and Router Advertisements**               ``X``
                                                                               (optional)
=============================================================================  =====================================

.. Note::

   `Allow manual adjustement of DHCPv6 and Router Advertisements` is optional, not setting it makes configuration easier.
   Only set it if you need to make manual adjustements, like sending an IPv6 DNS Server, configure DHCPv6 or change Router Priority.


Go to :menuselection:`Services --> Ndproxy`

==============================================  ====================================================================
**Enable**                                      ``X``
**Uplink Interface**                            ``WAN``
                                                (Interface must be in promiscuous mode)
**Downlink MAC Address**                        ``aa:bb:cc:dd:ee:ff``
                                                (MAC address of the CPE router's LAN interface)
**Uplink IPv6 Addresses**                       ``fe80::1``
                                                (Link-local address of the PE router's WAN interface)
**Exception IPv6 Addresses**                    `leave empty`
==============================================  ====================================================================

.. Note::

   Ensure that firewall rules allow IPv6 traffic.


Confirming the Setup
--------------------------------------------------

Introduce a client to the CPE router's LAN. This client will autoconfigure an IPv6 GUA inside the delegated /64 prefix, e.g., 2001:db8::200/64.
Ping an IPv6 only destination on the internet. The ping should work. If you disable the ndproxy service, the ping should stop working.

This happens because without ndproxy, the Neighbor Discovery Protocol (NDP) messages are not relayed between the WAN and LAN interfaces of the CPE router.

.. Attention::

   Since there is no DAD (Duplicate Address Detection) Proxy between WAN and LAN, if the same IPv6 GUAs are used in both segments, there can be address conflicts.
   This can also happen with auto generated IPv6 addresses, so make sure you limit their use in the WAN segment to only necessary ones.


Packet Flow Explained
--------------------------------------------------

1. **LAN Client**

   The IPv6 client on the LAN (e.g., with address ``2001:db8::200/64``) initiates a ping to an IPv6-only destination on the internet. The client sends the ICMPv6 Echo Request to its default gateway, which is the CPE router's LAN interface (``fe80::1``).

2. **CPE Router**

   The CPE router receives the packet on its LAN interface and forwards it out through its WAN interface (``2001:db8::2/128`` or ``fe80::2/64``) towards the PE router. Since the packet is destined for an external network, the CPE router uses its routing table to send the packet upstream.

3. **PE Router**

   The PE router forwards the packet to the intended internet destination. The external host responds with an ICMPv6 Echo Reply, which is routed back to the PE router.

   To deliver the Echo Reply to the LAN client (``2001:db8::200``), the PE router needs to resolve the client's IPv6 address to a link-layer (MAC) address. The PE router sends a NDP **Neighbor Solicitation** message for ``2001:db8::200`` out of its interface connected to the CPE router (the WAN interface of the CPE router).

4. **Role of ndproxy**

    - The **ndproxy** service on the CPE router listens for NDP messages on both WAN and LAN interfaces.
    - When the Neighbor Solicitation arrives at the CPE router's WAN interface, **ndproxy** intercepts it and proxies it to the LAN interface.
    - The LAN client receives the Neighbor Solicitation and responds with a Neighbor Advertisement, providing its MAC address.
    - **ndproxy** proxies this Neighbor Advertisement back to the WAN interface, sending it to the PE router.
    - The PE router now has the necessary link-layer information to forward the Echo Reply to the LAN client.
