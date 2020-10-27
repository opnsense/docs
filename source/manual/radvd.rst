==========================
Router Advertisements
==========================

radvd (the service responsible for this functionality) is the router advertisement daemon for IPv6.
It listens to router solicitations and sends router advertisements as described in
"Neighbor Discovery for IP Version 6 (IPv6)" (`RFC 4861 <https://tools.ietf.org/html/rfc4861>`__).
With these advertisements hosts can automatically configure their addresses and some other parameters.
It also defines "Neighbor Discovery Optimization for IPv6 over Low-Power Wireless Personal Area Networks (6LoWPANs)"
(`RFC6775 <https://tools.ietf.org/html/rfc6775>`__).  They also can choose a default router based on these advertisements.


--------------------------------
Router Advertisements (Mode)
--------------------------------

The mode selection contains some predefined settings for radvd, which influence a set of configuration options
and are intended for specific implementation scenarios.
They define the type of client deployment used in your network.

=====================================================================================================================

====================================  ===============================================================================
Router Only                           Only advertise this router, clients are using static IPv6 addressses
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
General
--------------------------------


====================================  ===============================================================================
Priority                              The  preference  associated  with	 the default router,
                                      as	either "low", "medium" (default), or "high".
RA Interface                          Interface to use prefix from.
Advertise Default Gateway             uses :code:`AdvDefaultLifetime` to disable advertising as default router when
                                      unset.
Advertise Routes                      Advertise more specific specific routes to the clients.
====================================  ===============================================================================


--------------------------------
DNS
--------------------------------

For supported clients, DNS settings can also be propagated by radvd as detailed in `RFC 8106 <https://tools.ietf.org/html/rfc8106>`__

====================================  ===============================================================================
DNS servers                           Define which dns servers to publish to the clients, either the ones
                                      defined here or (when **Use the DNS settings of the DHCPv6 server** is set)
                                      the ones defined in the DHCPv6 server for this interface.
                                      (:code:`RDNSS` in :code:`radvd`)
Domain search list                    Domain search list to push to the clients, when not specified the local
                                      domain name from this firewall is used. (:code:`DNSSL` in :code:`radvd`)
====================================  ===============================================================================

--------------------------------
Intervals
--------------------------------

The time between unsolicited multicast router advertisement can be configured, using the following settings,
usually these are left default.

====================================  ===============================================================================
Minimum Interval                      The  minimum  time allowed between sending unsolicited multicast
                                      router advertisements from the interface,	in seconds.
                                      Must be no less than 3 seconds and no greater than 0.75 *	 "Maximum Interval".
Maximum Interval                      The  maximum  time allowed between sending unsolicited multicast
                                      router advertisements from the interface,	in seconds.
                                      Must be no less than 4 seconds and no greater than 1800 seconds.
====================================  ===============================================================================
