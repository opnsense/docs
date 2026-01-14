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

      :menuselection:`Services --> Dnsmasq DNS & DHCP` is the default RA daemon in new installations, deactivate it if you want to use radvd.

-------------------------
General Settings
-------------------------

The service can be configured in :menuselection:`Services --> Router Advertisements`.

.. tabs::

    .. tab:: General

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Enabled**                               Enable or disable this entry.
        **Interface**                             Choose the interface that should send Router Advertisements. The prefix will be automatically
                                                  constructed from available IPv6 addresses of this interface.
        **Constructor**                           Construct a prefix out of IPv6 addresses of an additional interface (e.g. the WAN interface).
                                                  In most cases an NDP proxy is required if the same prefix is shared by multiple interfaces.
        **Mode**                                  Select which flags to set in Router Advertisements sent from this interface.
        **Minimum interval**                      The minimum time allowed between sending unsolicited multicast router advertisements
                                                  from the interface, in seconds.
        **Maximum interval**                      The maximum time allowed between sending unsolicited multicast router advertisements
                                                  from the interface, in seconds.
        **Preference**                            Select the Priority for the Router Advertisement (RA) Daemon.
        **Deprecate Prefix**                      Deprecate advertised prefixes on shutdown by announcing a zero preferred lifetime.
        **Default Lifetime**                      Lifetime in seconds this router is considered a valid default router.
        **Preferred Lifetime**                    Lifetime in seconds addresses remain preferred for new connections.
        **Valid Lifetime**                        Lifetime in seconds addresses remain valid before becoming unusable.
        **Source Address**                        Select the source address embedded in the RA messages.
                                                  If a CARP address is used DeprecatePrefix and RemoveRoute are both set to "off" by default.
        **NAT64 prefix**                          The NAT64 prefix included in the router advertisements.
                                                  The "well-known prefix" reserved for this service is 64:ff9b::/96.
        **Link MTU**                              Advertise a specific MTU to clients. Must be equal or greater than 1280 and valid for the link.
        ========================================= ====================================================================================

    .. tab:: DNS Settings

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Enable DNS**                            Control the sending of the embedded DNS configuration (RFC 8106).
        **Recursive DNS Servers (RDNSS)**         The default is to use this interface IP address with an enabled DNS service or the
                                                  configured global DNS servers. You may specify up to three explict servers here instead.
        **Recursive DNS Servers Lifetime**        Lifetime in seconds for advertised recursive DNS servers.
        **DNS Search List (DNSSL)**               The default is to use the domain name of this system as the DNSSL option.
                                                  You may specify explicit domains here instead.
        **DNS Search List Lifetime**              Lifetime in seconds for advertised DNS search domains.
        ========================================= ====================================================================================

        For supported clients, DNS settings can also be propagated by radvd as detailed in `RFC 8106 <https://tools.ietf.org/html/rfc8106>`__


    .. tab:: Routes

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Routes**                                Routes are specified in CIDR format. The prefix of a route definition should be network prefix;
                                                  it can be used to advertise more specific routes to the hosts.
        **Route Lifetime**         	              Lifetime in seconds for advertised routes.
                                                  configured global DNS servers. You may specify up to three explict servers here instead.
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

# TODO
