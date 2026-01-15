==========================
Router Advertisements
==========================

.. contents:: Index


radvd (the service responsible for this functionality) is the router advertisement daemon for IPv6.
It listens to router solicitations and sends router advertisements as described in
"Neighbor Discovery for IP Version 6 (IPv6)" (`RFC 4861 <https://tools.ietf.org/html/rfc4861>`__).
With these advertisements hosts can automatically configure their addresses and some other parameters.
It also defines "Neighbor Discovery Optimization for IPv6 over Low-Power Wireless Personal Area Networks (6LoWPANs)"
(`RFC6775 <https://tools.ietf.org/html/rfc6775>`__).  They also can choose a default router based on these advertisements.

.. Attention::

      Dnsmasq is the default RA daemon in new installations, deactivate its *Router Advertisement* setting if you want to use radvd.

-------------------------
General Settings
-------------------------

The service can be configured in :menuselection:`Services --> Router Advertisements`.

.. tabs::

    .. tab:: General Settings

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Enabled**                               Enable or disable this entry. If "Track Interface (legacy)" is used, an existing
                                                  disabled entry will also deactivate advertisements on that interface. Alternatively,
                                                  switch to "Identity association" for full manual configuration if needed.
        **Interface**                             Choose the interface that should send Router Advertisements. A prefix will be constructed
                                                  from the primary IP of that interface, which is assigned by "Identity association" or
                                                  "Track interface (legacy)" IPv6 modes of said interface. If additional virtual IP addresses exist on
                                                  this interface, their prefixes will also be advertised.
        **Mode**                                  Select which flags to set in Router Advertisements sent from this interface.
        **Minimum interval**                      The minimum time allowed between sending unsolicited multicast router advertisements
                                                  from the interface, in seconds.
        **Maximum interval**                      The maximum time allowed between sending unsolicited multicast router advertisements
                                                  from the interface, in seconds.
        **Recursive DNS Servers (RDNSS)**         The default is to use this interface IP address with an enabled DNS service or the
                                                  configured global DNS servers. You may specify up to three explict servers here instead.
        **DNS Search List (DNSSL)**               The default is to use the domain name of this system as the DNSSL option.
                                                  You may specify explicit domains here instead.
        **Routes**                                Routes are specified in CIDR format. The prefix of a route definition should be network prefix;
                                                  it can be used to advertise more specific routes to the hosts.
        ========================================= ====================================================================================

    .. tab:: Advanced Settings

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Constructor**                           Per default, the primary prefix of the given *Interface* in
                                                  *General Settings* is used. When setting a constructor,
                                                  the primary prefix of a WAN interface can be used instead.
                                                  An :doc:`NDP proxy </manual/ndp-proxy-go>` is required if the same WAN prefix is
                                                  shared by multiple LAN interfaces.
        **Preference**                            Select the Priority for the Router Advertisement (RA) Daemon.
        **Deprecate Prefix**                      Deprecate advertised prefixes on shutdown by announcing a zero preferred lifetime.
        **Shutdown Advertisement**                Upon shutdown, send a final advertisement with zero router lifetime.
        **Default Lifetime**                      Lifetime in seconds this router is considered a valid default router.
        **Preferred Lifetime**                    Lifetime in seconds addresses remain preferred for new connections.
        **Valid Lifetime**                        Lifetime in seconds addresses remain valid before becoming unusable.
        **Source Address**                        Select the source address embedded in the RA messages.
                                                  If a CARP address is used DeprecatePrefix and RemoveRoute are both set to "off" by default.
        **NAT64 prefix**                          The NAT64 prefix included in the router advertisements.
                                                  The "well-known prefix" reserved for this service is 64:ff9b::/96.
        **Link MTU**                              Advertise a specific MTU to clients. Must be equal or greater than 1280 and valid for the link.
        **Enable DNS**                            Control the sending of the embedded DNS configuration (RFC 8106).
        **Recursive DNS Servers Lifetime**        Lifetime in seconds for advertised recursive DNS servers.
        **DNS Search List Lifetime**              Lifetime in seconds for advertised DNS search domains.
        **Route Lifetime**         	              Lifetime in seconds for advertised routes.
        **Remove Route**                          Withdraw advertised routes on shutdown by sending a zero lifetime.
        ========================================= ====================================================================================


--------------------------------
Router Advertisements (Mode)
--------------------------------

The mode selection contains some predefined settings for radvd, which influence a set of configuration options
and are intended for specific implementation scenarios.
They define the type of client deployment used in your network.

=====================================================================================================================

====================================  ===============================================================================
Router Only                           Only advertise this router, clients are using static IPv6 addresses
Unmanaged                             Clients will use Stateless Address Autoconfiguration (SLAAC), without
                                      other (non-address) information being provided.
Managed                               Stateful configuration, address configuration provided by DHCPv6
Assisted                              Stateful configuration, address configuration provided by DHCPv6, although
                                      advertised routes can also be used on Stateless Address Autoconfiguration
                                      setups (SLAAC).
Stateless                             Clients will use Stateless Address Autoconfiguration (SLAAC)
====================================  ===============================================================================

A detailed overview of the :code:`radvd` settings determined by the mode can be found below:

+-----------------------------+--------------------+-------------+-----------+---------+----------+-----------+
| scope                       | Settings           | Router Only | Unmanaged | Managed | Assisted | Stateless |
+-----------------------------+--------------------+-------------+-----------+---------+----------+-----------+
|                             | AdvManagedFlag     |             |           |    X    |    X     |           |
|  Per interface              +--------------------+-------------+-----------+---------+----------+-----------+
|                             | AdvOtherConfigFlag |             |           |    X    |    X     |     X     |
+-----------------------------+--------------------+-------------+-----------+---------+----------+-----------+
|                             | AdvOnLink          |             |     X     |    X    |    X     |     X     |
|  Per prefix                 +--------------------+-------------+-----------+---------+----------+-----------+
|                             | AdvAutonomous      |             |     X     |         |    X     |     X     |
+-----------------------------+--------------------+-------------+-----------+---------+----------+-----------+

.. Note::

      Technical details about the options can be found in the `man <https://www.freebsd.org/cgi/man.cgi?query=radvd.conf>`__ page of radvd

--------------------------------
Configuration examples
--------------------------------


Advertise a prefix on LAN
--------------------------------------------------

The most common configuration would be DHCPv6 on the WAN interface and receiving a routed prefix via DHCPv6-PD.
When setting the LAN IPv6 configuration to either of "Track Interface (legacy)" or "Identity association" with a unique prefix ID,
router advertisements can send that prefix and a default route to clients.

Go to :menuselection:`Services --> Router Advertisements` and add a new entry:

========================================= ====================================================================================
**Option**                                **Description**
========================================= ====================================================================================
**Enabled**                               X
**Interface**                             LAN
========================================= ====================================================================================

Press **Save** and **Apply**

Per default, RDNSS and DNSSL options will be sent to clients, containing the IPv6 address of the LAN interface, and the default system domain.


Advertise multiple prefixes on LAN
--------------------------------------------------

If an ULA (Unique Local Address) prefix should be sent in addition to a GUA (Global Unicast Address) prefix, create a virtual IPv6 address
in :menuselection:`Interfaces --> Virtual IPs`. Configure it on the LAN interface, make sure the prefix length is /64.

Afterwards, applying the configuration in :menuselection:`Services --> Router Advertisements` will configure the additional prefix.


High availability
--------------------------------------------------

For high availability with IPv6, static prefixes are a requirement for seamless failover.

You can follow this setup example: :doc:`Configure CARP </manual/how-tos/carp>`
