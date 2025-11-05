==================================================
ndp-proxy-go (IPv6 Neighbour Discovery Proxy)
==================================================

.. contents::
   :local:
   :depth: 2

This manual provides a quick overview of ndp-proxy-go and how to configure it for general use.


Introduction
==================================================

ndp-proxy-go is a userspace IPv6 Neighbour Discovery Proxy.

It can proxy SLAAC on-link prefixes to several downstream interfaces by proxying neighbor discovery protocol (NDP), router advertisements (RA) 
and duplicate address detection (DAD). For each discovered client it installs host routes automatically.

If your ISP provides only a single /64 prefix via RA, you can use ndp-proxy-go to provide this prefix to all devices
on separate downstream interfaces to create Layer 3 isolation.

The proxy handles privacy extension and changing prefixes gracefully; the setup is fully dynamic and self healing.

For the ISP, it will look like the proxy itself owns all global unicast addresses (GUA) with its WAN facing MAC address.

More technical details: `ndp-proxy-go <https://github.com/Monviech/ndp-proxy-go/blob/main/README.md>`_


Installation
--------------------------------------------------

Install ``os-ndp-proxy-go`` from :menuselection:`System --> Firmware --> Plugins`.


Important configuration details
--------------------------------------------------

- **WAN (upstream)**:
    The upstream WAN interface must be configured to allow SLAAC or DHCPv6, so it can configure an IPv6 address
    and a default route to the ISP. Router advertisements must be sent from the ISP to the WAN.

- **LAN (downstreams)**:
    The downstream LAN interface(s) must be configured in link-local mode, or via static IPv6 address with an unique local address (ULA).
    The requirement is that the interface must have an link-local address (LLA).


.. Tip::

   You can proxy the upstream prefix to any amount of downstream interfaces. Since this proxy includes DAD messages, IP address
   conflicts are unlikely to cause issues even in larger proxied networks or when using this with cloud providers.


Example setup
==================================================

Follow if you are a user with a router in a SLAAC only network (e.g. home, cloud VPS, mobile LTE/5G networks)
In such a setup, your router will not receive a prefix delegation via DHCPv6-PD, but only set an on-link /64 prefix.


Go to :menuselection:`Interfaces --> WAN`

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``SLAAC``
==============================================  ====================================================================

Save the settings.

Go to :menuselection:`Interfaces --> LAN` and choose either a link-local or a static IPv6 configuration.

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``link-local``
**or**
**IPv6 Configuration Type**                     ``Static IPv6``
**IPv6 address**                                ``fd80::1:1/64``
==============================================  ====================================================================

Save and apply the new interface settings.

Go to :menuselection:`Services --> NDP Proxy`

==============================================  ====================================================================
**Enable**                                      ``X``
**Uplink Interface**                            ``WAN``
**Downlink Interfaces**                         ``LAN``
**Proxy router advertisements**                 ``X``
**Install host routes**                         ``X``
==============================================  ====================================================================

After applying the configuration, all devices in your LAN network will autogenerate a GUA with SLAAC and receive
the OPNsense as their default gateway. Check the firewall rules on LAN if IPv6 is allowed to any destination.
Verify the setup by pinging an IPv6 location on the internet.

.. Attention::

    Since in the default setup, the router advertisements of the ISP are used, please stop any other router advertisement daemons on the LAN interface.

.. Tip::

    If you receive a DNS server from your ISP, but want the OPNsense to be the sole DNS server, use a Port Forward to force traffic destined to port 53 to the
    the local running Unbound server instead.

