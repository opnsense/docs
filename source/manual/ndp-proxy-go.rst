==================================================
ndp-proxy-go (Neighbor Discovery Proxy)
==================================================

.. contents::
   :local:
   :depth: 2


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
==================================================

Install ``os-ndp-proxy-go`` from :menuselection:`System --> Firmware --> Plugins`.


Proxy Settings
==================================================

.. tabs::

    .. tab:: General

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Enable**                                Enable or disable this service.
        **Upstream interface**                    Choose the upstream interface which receives the external IPv6 prefix from the ISP.
                                                  Usually, this is the WAN interface. Ethernet interfaces are fully supported,
                                                  point-to-point (PPPoE) devices are experimental.
        **Downstream interfaces**                 Choose one or multiple downstream interfaces which should proxy the upstream IPv6 prefix.
                                                  Only ethernet interfaces are supported.
        **Proxy router advertisements**           Proxy upstream RAs to downstream interfaces. Disable this if you use your own RA daemon.
        **Install host routes**                   Automatically create host routes for discovered clients. Disabling this means you must
                                                  manually handle all routing decisions.
        **Neighbor cache lifetime**               Neighbor cache lifetime in minutes. This controls when stale clients, host routes and
                                                  firewall aliases are cleaned up. When using a point-to-point interface as upstream,
                                                  increasing this lifetime is necessary to not prematurely clean up routes.
        **Maximum learned neighbors**             Maximum learned neighbors, increase for large networks.
        **Neighbor cache file**                   Persist cache to file on service stop and load it on service start. Only neighbors
                                                  with a valid cache lifetime are loaded. This helps on system reboots to minimize
                                                  downtime of individual clients.
        **Max route operations**                  Max route operations per second, increase for large networks.
        **Packet capture timeout**                Controls CPU usage vs. NDP responsiveness. Lower values (e.g., 25 ms) minimize
                                                  latency during cache refresh at the cost of more CPU. Higher values (100–250 ms)
                                                  reduce CPU use but may introduce small latency spikes.
        **Debug log**                             Enable debug logging.
        ========================================= ====================================================================================

    .. tab:: Aliases

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Interface**                             Add IPv6 addresses to the firewall alias that belongs to this proxied interface.
                                                  When choosing any, all IPv6 addresses will be added.
        **Firewall alias**                        Choose an "external (advanced)" type alias from "Firewall - Aliases". Whenever a client
                                                  is discovered, the IPv6 address will be automatically added to the chosen alias.
                                                  When the neighbor cache lifetime expires, the IPv6 address will be removed from the alias.
        ========================================= ====================================================================================

Link Types
==================================================

The proxy supports different link types on the upstream interface with some important differences.


Ethernet Links
--------------------------------------------------

- **WAN (upstream)**:
    The upstream ethernet interface must be configured to allow SLAAC, so it can configure an IPv6 address
    and a default route to the ISP. Periodic router advertisements must be sent from the ISP to the WAN.

- **LAN (downstreams)**:
    The downstream interfaces must be ethernet and configure a link-local address (LLA).

Using ethernet interfaces is the recommended setup for best performance, rapid host discovery and self-healing of IPv6 after firewall reboots.
Since the ISP router will perform Neighbor Discovery (ND) for every unknown client GUA,
the proxy can instantly relearn clients when they send any traffic to the internet.

.. Tip::

   You can proxy the upstream prefix to any amount of downstream interfaces. Since this proxy includes DAD messages, IP address
   conflicts are unlikely to cause issues even in larger proxied networks or when using this with cloud providers.


Point-to-point Links
--------------------------------------------------

- **WAN (upstream)**:
    The upstream point-to-point interface must be configured to allow SLAAC, so it can configure an IPv6 address
    and a default route to the ISP. Periodic router advertisements must be sent from the ISP to the WAN.

- **LAN (downstreams)**:
    The downstream interface must be ethernet and configure a link-local address (LLA).

The proxy includes experimental support for point-to-point upstream interfaces such as PPPoE.
Unlike Ethernet links, a point-to-point link does not perform Neighbor Discovery (ND) for downstream GUAs.
This has some important implications:

- Only Router Solicitations (RS) are forwarded upstream.
- NS/NA forwarding is intentionally disabled on point-to-point links.
- The `cache-ttl` must be increased, since there are less NA containing a GUA to learn from, otherwise routes might get removed prematurely.

.. Attention::

   If you receive a single /64 prefix via DHCPv6-PD on a PPPoE link, it must be terminated on a router **before** the proxy.
   This could be another OPNsense, or a device like a Fritzbox. The proxy does not listen and learn a prefix from DHCPv6.
   To use PPPoE as upstream, IPv6 configuration must be set to SLAAC.

.. Attention::
   
   After a firewall reboot, IPv6 connectivity may be delayed until downstream clients perform SLAAC and DAD again.
   This is expected behavior on PPPoE, as the upstream (ISP) router never probes GUAs via Neighbor Discovery (ND) like on ethernet links.
   The behavior can be mitigated by using the `Neighbor cache file` option.


Example Setup
==================================================

Follow if you are a user with a router in a SLAAC only network (e.g. home, cloud VPS, mobile LTE/5G networks)
In such a setup, your router will not receive a prefix delegation via DHCPv6-PD, but only set an on-link /64 prefix.

Settings
--------------------------------------------------

Go to :menuselection:`Interfaces --> WAN`

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``SLAAC``
==============================================  ====================================================================

Save the settings.

Go to :menuselection:`Interfaces --> LAN` and choose either a link-local IPv6 configuration.

==============================================  ====================================================================
**IPv6 Configuration Type**                     ``link-local``
==============================================  ====================================================================

Save and apply the new interface settings.

Go to :menuselection:`Services --> NDP Proxy --> Settings`

==============================================  ====================================================================
**Enable**                                      ``X``
**Upstream interface**                          ``WAN``
**Downstream interfaces**                       ``LAN``
**Proxy router advertisements**                 ``X``
**Install host routes**                         ``X``
**Neighbor cache lifetime**                     Increase to a few hours when using a point-to-point upstream.
**Neighbor cache file**                         Enable when using a point-to-point upstream.
==============================================  ====================================================================

After applying the configuration, all devices in your LAN network will autogenerate a GUA with SLAAC and receive
the router as their default gateway. Check the firewall rules on LAN if IPv6 is allowed to any destination.
Verify the setup by pinging an IPv6 location on the internet.

.. Attention::

    Since in the default setup, the router advertisements of the ISP are used, please stop any other router advertisement daemons on the LAN interface.

.. Tip::

    If you receive a DNS server from your ISP, but want the router to be the sole DNS server, use a Port Forward to force traffic destined to port 53 to
    the local running Unbound server instead. Please note that ``::1`` is not a valid redirect target, use a dynamic IPv6 alias instead.


Firewall Rules
--------------------------------------------------

The proxy supports populating firewall aliases with IPv6 addresses of learned clients. This can be used to only permit access to the internet,
while blocking requests to other networks that also receive IPv6 addresses from the same on-link prefix.

Since only learned clients are added, the alias will always have an up to date state that reflects the proxied interface.

.. Note::

   The proxy only learns IPv6 addresses that are inside the WAN on-link prefix and only of clients it manages.
   These aliases are not for general use, but only for combination with the proxy to ease creating the correct firewall rules.


- Go to :menuselection:`Firewall --> Aliases` and create these aliases:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``ndp_proxy_all`` (Will contain all learned IPv6 addresses)
**Type**                            ``External (advanced)``
==================================  =======================================================================================================

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``ndp_proxy_lan`` (Will contain only LAN IPv6 addresses)
**Type**                            ``External (advanced)``
==================================  =======================================================================================================

- Press **Apply**

- Go to :menuselection:`Services --> NDP Proxy --> Settings --> Aliases` and map these two aliases so the proxy can populate them:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Interface**                       ``any``
**Name**                            ``ndp_proxy_global``
==================================  =======================================================================================================

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Interface**                       ``LAN``
**Name**                            ``ndp_proxy_lan``
==================================  =======================================================================================================

- Press **Apply**

- Go to :menuselection:`Firewall --> Rules --> LAN` and create a rule that allows Internet access, but denies communication with other segments in the same IPv6 prefix:

==============================================  ====================================================================================================
**Action**                                      Pass
**Interface**                                   LAN
**Direction**                                   In
**TCP/IP Version**                              IPv6
**Protocol**                                    Any
**Source**                                      ``ndp_proxy_lan``
**Source port**                                 Any
**Invert Destination**                          ``X``
**Destination**                                 ``ndp_proxy_global``
**Destination port**                            Any
**Description**                                 Allow IPv6 internet access for all LAN clients known by NDP Proxy
==============================================  ====================================================================================================

- Press **Apply**

Now your IPv6 firewalling is tight. It is self-healing when client addresses change due to IPv6 privacy extensions or when the on-link prefix changes.
   
.. Tip::
   
    If additional networks are proxied, just add more aliases (e.g., ``ndp_proxy_vlan1``) and create the same rule on that interface.


.. Tip::

    If you need client specific aliases, take a look at the ``Mac address`` alias type in :menuselection:`Firewall --> Aliases`,
    which can dynamically track IPv4 and IPv6 addresses of a single client.


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

.. Attention::

   The proxy does not clean up installed host routes when it is stopped. This is intentional to minimize downtime of IPv6 clients between service restarts.
   It does automatically prune routes while it runs when the ``cache-ttl`` of a discovered neighbor expires.

