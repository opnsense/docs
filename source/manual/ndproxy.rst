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


Simple Setup for Home Users
==================================================

.. Note::

   Follow if you are a home user with a router in a SLAAC only network, e.g. mobile network via modem.
   In such a setup, your router will not receive a prefix delegation via RA (router advertisement); it must rely on NDP (neighbor discovery protocol).

Go to :menuselection:`Interfaces --> WAN`

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``SLAAC``
==============================================  ====================================================================

Save and apply the new interface settings.

Go to :menuselection:`Interfaces --> Overview`

Write down the IPv6 GUA (Global Unicast address) you received on the WAN interface.

We assume that we auto generated the IPv6 address ``2001:db8:85a3:8d3:1319:8a2e:0370:7344/64``

Go to :menuselection:`Interfaces --> WAN`

Set it as static IPv6 address on the WAN interface with a /128 prefix and enable promiscuous mode.

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``Static IPv6``
**Promiscuous Mode**                            ``X``
**IPv6 address**                                ``2001:db8:85a3:8d3:1319:8a2e:0370:7344/128``
==============================================  ====================================================================

.. Attention::

   It could happen that the default IPv6 gateway vanishes due to the static IPv6 setup on WAN. If that happens,
   go to :menuselection:`System --> Gateways --> Configuration` and add the **Uplink IPv6 Address** ``fe80::200:ff:fe00:0`` as gateway.

Save, then go to :menuselection:`Interfaces --> LAN`

Here we set a /64 prefix in the same range as the WAN interface, e.g., ``2001:db8:85a3:8d3:1319:8a2e:0370:7345/64``.
Note how we incremented the address from ``7344`` to ``7345``.

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``Static IPv6``
**IPv6 address**                                ``2001:db8:85a3:8d3:1319:8a2e:0370:7345/64``
==============================================  ====================================================================

Save and apply the new interface settings.

Go to :menuselection:`Services --> Ndproxy`

==============================================  ====================================================================
**Enable**                                      ``X``
**Uplink Interface**                            ``WAN``
**Downlink MAC Address**                        ``aa:bb:cc:dd:ee:ff``
                                                (MAC address of the WAN interface)
**Uplink IPv6 Addresses**                       ``fe80::200:ff:fe00:0``
                                                (Link-local address of the ISP router)
**Exception IPv6 Addresses**                    `leave empty`
==============================================  ====================================================================

.. Note::

   The MAC address can be found in :menuselection:`Interfaces --> Overview`. Click the details button of
   the WAN interface.

.. Note::

   The link-local address of the ISP router can be found in :menuselection:`System --> Routes --> Status`.
   Search for the ipv6 default route, the `Gateway` of this route will be the link local address; ``fe80::200:ff:fe00:0%igb0``.
   Only use the part before ``%``, in this case ``fe80::200:ff:fe00:0``.


After applying the configuration, all devices in your LAN network will autogenerate a GUA with SLAAC and receive
the OPNsense as their default gateway. Check the firewall rules on LAN if IPv6 is allowed to any destination.
Verify the setup by pinging an IPv6 location on the internet.


Confirming the Setup
--------------------------------------------------

Introduce a client to the CPE router's LAN. This client will autoconfigure an IPv6 GUA inside the available /64 prefix, e.g., ``2001:db8:85a3:8d3:5f1b:4a6c:7d9e:1b22/64``.
Ping an IPv6 only destination on the internet. The ping should work. If you disable the ndproxy service, the ping should stop working.

This happens because without ndproxy, the Neighbor Discovery Protocol (NDP) messages are not relayed between the WAN and LAN interfaces of the CPE router.

.. Attention::

   Since there is no DAD (Duplicate Address Detection) Proxy between WAN and LAN, if the same IPv6 GUAs are used in both segments, there can be address conflicts.
   This can also happen with auto generated IPv6 addresses, so make sure you limit their use in the WAN segment to only necessary ones.
