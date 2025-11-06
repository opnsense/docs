==================================================
ndp-proxy-go (Neighbor Discovery Proxy)
==================================================

.. contents::
   :local:
   :depth: 2

This manual provides a quick overview of ndp-proxy-go and how to configure it for general use.


Introduction
==================================================

ndp-proxy-go is a userspace IPv6 Neighbor Discovery Proxy.

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
    The upstream WAN interface must be configured to allow SLAAC, so it can configure an IPv6 address
    and a default route to the ISP. Router advertisements must be sent from the ISP to the WAN.

- **LAN (downstreams)**:
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
**IPv6 address**                                ``fe80::/64``
==============================================  ====================================================================

Save and apply the new interface settings.

Go to :menuselection:`Services --> NDP Proxy --> Settings`

==============================================  ====================================================================
**Enable**                                      ``X``
**Uplink Interface**                            ``WAN``
**Downlink Interfaces**                         ``LAN``
**Proxy router advertisements**                 ``X``
**Install host routes**                         ``X``
==============================================  ====================================================================

After applying the configuration, all devices in your LAN network will autogenerate a GUA with SLAAC and receive
the router as their default gateway. Check the firewall rules on LAN if IPv6 is allowed to any destination.
Verify the setup by pinging an IPv6 location on the internet.

.. Attention::

    Since in the default setup, the router advertisements of the ISP are used, please stop any other router advertisement daemons on the LAN interface.

.. Tip::

    If you receive a DNS server from your ISP, but want the router to be the sole DNS server, use a Port Forward to force traffic destined to port 53 to
    the local running Unbound server instead.


Logging
==================================================

With the debug logging you can find out the details of the proxies behavior.

You can see logs of received and sent RA, NDP (NS, NA) and DPD messages. If something does not work as expected,
reading the log file is the first step to troubleshoot.

Go to :menuselection:`Services --> NDP Proxy --> Settings`

==============================================  ====================================================================
**Debug log**                                   ``X``
==============================================  ====================================================================

Apply this setting and go to :menuselection:`Services --> NDP Proxy --> Log File`

The proxy must learn the prefix from RAs:

   - RA prefix learned: "::/64" (valid 2h0m0s)
      - A prefix was learned from an RA on the upstream interface. Without this message appearing
        the proxy will not learn any addresses, and your downstream clients will most likely not receive RAs to autoconfigure SLAAC addresses.

   - skip learn "IPv6 address" (not in allowed RA prefixes)
      - No prefix was learned from RAs yet or there are clients with IPv6 addresses outside of the learned prefix.
        The proxy only caches neighbors in the prefixes it learned via RAs. This prevents the cache from being poisoned.

The proxy must install host routes to target the individual downstream clients:

   - route installed: "IPv6 address" via eth0
      - A route was successfully installed, the client should be able to reach the internet now.

   - route deleted: "IPv6 address"
      - A route was deleted, most likely the client was offline longer than the neighbor caching time, or it changed its IPv6 address via privacy
        extension. On a clean shutdown, all routes of learned clients in the cache will be deleted.

   - route add err: exit status 1 (out: add host "IPv6 address": gateway eth0 fib 0: route already in table)
      - There is already a different route that would overlap with the one the proxy tries to install.
        To fix this ensure the prefix does not have static routes you manually configured, or turn off
        the automatic hoste route installation if you want to handle all routes manually.
