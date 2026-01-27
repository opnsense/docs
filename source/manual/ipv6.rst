==================================================
IPv6 setup
==================================================

.. image:: images/IPv6.png
   :width: 100%


.. contents:: Index


Introduction
=================

To this day IPv6 remains an elusive topic. IPv6 has long been shipped as a default option in OPNsense and received
gradual improvements over the years, but configuration complexity, ISP problems and sometimes
also software bugs can cause connectivity to fail or not establish at all.
This guide aims to provide groundwork for how IPv6 can be configured and how to spot known mistakes and troubleshoot connectivity.

When talking about external and internal interfaces this guide uses "WAN" and "LAN",
not excluding the possibility for multiple interfaces on each side being used at the same time.

Note this guide will not cover NAT on IPv6 for simplicity's sake.

Technical background
============================

Overview
-------------------------------

When digging into IPv6, a lot of differences between IPv4 come to light, which is practical to be aware of when debugging issues.
In this chapter we want to explain some of the most relevant building blocks in IPv6 networks.

.. seqdiag::
   :caption: WAN configuration flow (most common)
   :desctable:

    seqdiag {
        client [label='WAN\nInterface']; rtsold; radvd; DHCPv6c; DHCPv6; LAN [label="LAN\nInterface"];
        client --> rtsold;
        rtsold  -> radvd [label = "Router Solicitation", leftnote = "client"];
        rtsold <-- radvd [label = "Router Advertisement", rightnote = "server"];
        rtsold -> DHCPv6c;
            DHCPv6c  -> DHCPv6 [label = "DHCP Request", leftnote = "client"];
            DHCPv6c <-- DHCPv6  [label = "DHCP Response", rightnote = "server"];
            DHCPv6c --> LAN  [label = "Update interface", rightnote = "client"];
            DHCPv6c --> client;
    }


*In the sequence diagram above, the client is the OPNsense firewall and the server the ISP, but clients inside the
network will act similar to what OPNsense is doing on the WAN interface.*

Most concepts explained in this paragraph are part of the `Neighbor Discovery Protocol <https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol>`__.


Finding your neighbors [NS,NA]
-------------------------------

For a machine to know its neighbors, it will use the neighbor discovery protocol (NDP), a bit similar to ARP on IPv4 networks,
but using Neighbor Solicitation (:code:`ICMPv6 type 135`) and Neighbor Advertisement :code:`ICMPv6 type 136`) messages.

In order to verify if a neighbor is known, you can use the NDP table in :menuselection:`Interfaces --> Diagnostics --> NDP Table`.


Router Solicitation [RS]
-------------------------------

Since a lot of home and branch office setups are auto-configured, it does make sense to explain router solicitations (RS)
first.

Compared to IPv4, dynamic configuration is quite different when it comes to addressing and routes.
A dynamically configured host starts with sending a router solicitation message using :code:`ICMPv6 type 133`, after which it
expects the other end to answer with a router advertisement (:code:`ICMPv6 type 134`).

The address a host will use depends partly on the answer it receives, when a DHCPv6 client configuration is used,
similar to IPv4 a dhcp client will be used to retrieve an address. When stateless auto configuration is used, the client
calculates an address to use based on its mac address and network received from the advertisement.

.. Note::

    For simplicity we're not going deeper into `stateless auto configuration <https://datatracker.ietf.org/doc/html/rfc2462>`__
    including optional features to prevent address duplication (`DAD <https://datatracker.ietf.org/doc/html/rfc4429>`__)


On OPNsense a service called :code:`rtsold` is used to send out these solicitations and can take some actions on the responses it
receives (from the advertisements). Although without explicitly asking for advertisements, you will likely still receive them,
but have little control over them. The kernel handles these advertisements when :code:`accept_rtadv` is enabled on the interface
anyway.


Router Advertisement [RA]
-------------------------------

The opposite of the solicitation is the advertisement, which we will also use on our end to inform our clients.
A router advertisement contains vital information for the client to exist within the network.
Usually a link-local (:code:`FE80::/8`) address is used as source address in the message, which will then be used as (default) gateway by the client.

Certain flags and options are offered to the client, the most prominent flags are the following ones (`rfc4861 <https://www.rfc-editor.org/rfc/rfc4861>`__):

====  ================================= ======================================================================
Code  Name                              Description
====  ================================= ======================================================================
M     Managed Address Configuration     When set, it indicates that addresses are available via DHCPv6
O     Other Configuration Flag          This indicates that other information, such as dns related options,
                                        are available via DHCPv6
====  ================================= ======================================================================

Relevant other information includes:

=================================  ============ ===============================================================
Purpose                            Option type  Description
=================================  ============ ===============================================================
Prefix information                 3            Prefix to use, when flag :code:`A` is set it may be
                                                used for stateless autoconfiguration (slaac).
Recursive DNS Server               25           DNS server information (RDNS)
Route Information                  24           Routes to install with their priority
=================================  ============ ===============================================================

Our clients (usually on LAN) will require a router advertisement daemon on our end, this service can be offered via
either :doc:`radvd <radvd>` or :doc:`dnsmasq <dnsmasq>` on our end.


DHCPv6
-------------------------------

Similar to IPv4, there's also a network configuration protocol for IPv6, but the scope of the service is different.
In the sequence diagram above we'll see that a dhcpv6 client will be executed after the router solicitation process.
Since dhcpv6 is not responsible for the routing part and address configuration may depend on routing advertisement reveived,
it needs this information first.

When debugging DHCPv6 communication, it's important to know clients listen on :code:`UDP port 546` and servers
receive their messages on :code:`UDP port 547`.

Depending on their role, clients may receive an address via DHCPv6 (or are auto-configured using `SLAAC <https://en.wikipedia.org/wiki/IPv6#Stateless_address_autoconfiguration_(SLAAC)>`__)
and information about surrounding servers like the DNS to use.

The other important aspect of DHCPv6 is the ability to send networks to use for attached routers, this process is called
`Prefix Delegation [PD] <https://en.wikipedia.org/wiki/Prefix_delegation>`__.
In most cases, OPNsense receives a PD from the provider which it can use for the networks attached. Usually these prefixes are larger
than the minimal :code:`/64` (e.g. :code:`/48`).

Our DHCP client is also responsible for configuring an address to the lan type interface based on the delegated prefix
received. This part of the configuration is specified on the lan interface as "tracking".

.. Note::

    When your provider or cloud hosting does not offer a PD, routing is not reliably possible. In some cases
    network address translation may be an option (example in  :doc:`ndproxy <ndproxy>`).
    There is an experimental `rfc <https://datatracker.ietf.org/doc/html/rfc4389>`__
    to proxy neighbor discovery packets, but no implementation exists yet.

.. Note::
    There is some overlap in what DHCPv6 offers and router advertisements bring to the table, but in most auto-configured
    environments both are being used.


Multiple options exist which may act as DHCPv6 server on our end, an overview of the options can be found in our :doc:`dhcp` documentation.


.. Note::

    Although not explained in detail here, when the firewall itself needs to connect to the outside world, it expects
    a global unicast address configured on the WAN interface. For this reason the dhcp IA_NA (non-temporary addresses)
    option is used.


Address categories
-------------------------------

When reading IPv6 documentation, some terms, which relate to network segments, are being used quite often.
For clarity we want to specify them below:

==============  =========== ================================================
Term            Network     Name
==============  =========== ================================================
GUA             2000::/3    Global Unicast Addresses
ULA             FC00::/7    Unique-local unicast addresses
LL              FE80::/10   Link-local unicast addresses
==============  =========== ================================================



Interface configuration modes
======================================

Depending on the IPv6 mode selected IPv6 behaviour differs in outcome. The matching mode must be selected for your ISP.
If in doubt ask for assistance via your ISP or ask on the forum how other users of your ISP configured it successfully.


None
-------------------------------

This mode turns off IPv6 connectivity for this particular interface.
Use this mode when the default mode (DHCPv6) does not work or causes broken connectivity with your ISP.
It does not prohibit IPv6 globally and some services might even locally require IPv6 in order to communicate to itself (such as Squid web proxy for example).

.. Note::

    You can use this mode for WAN and LAN connections.

Static IPv6
-------------------------------

When the ISP offers a static address block you can assign one /64 network to your WAN interface and other /64 networks to your LANs.
You can even delegate bigger networks within your prefix to downstream routers via DHCPv6 which is generally available in static mode.
Note that you need to create and set a gateway address for this mode to connect to your next
gateway hop which your ISP should provide to you as well.

.. Note::

    You can use this mode for WAN and LAN connections.

DHCPv6
-------------------------------

For dynamic address offerings (that most likely are also shifting the prefix) this mode is the most common configuration
and therefore also the default setting for a preset WAN.
In this mode a prefix will be acquired if offered, either with or without an additional IP address for your WAN.
Note that the interface will not assign a /64 to itself from the prefix in contrast to static IPv6. Internally,
a single globally unique address is either acquired via DHCP or SLAAC (not to be confused with SLAAC mode) but in general
an ISP-provided link-local address is automatically used for the connectivity to the next hop gateway.
Setting "Request only an IPv6 prefix" may be required in case the ISP refuses to hand out an address and/or prefix.

.. Note::

    You can use this mode for WAN connections only.


SLAAC
-------------------------------

Use "Stateless Address Autoconfiguration" for the IPv6 connectivity only.
In cases where Static IPv6 or DHCPv6 not available this mode may still provide ISP connectivity.

.. Note::

    You can use this mode for WAN connections only.

6to4 Tunnel
-------------------------------

This is an IPv6 over IPv4 tunnelling mode as specified in RFC3056 over a fixed IPv4 router address.
It does not require any client side configuration, but is not being used much anymore due to 6rd.

.. Note::

    You can use this mode for WAN connections only.

6rd Tunnel
-------------------------------

6rd means "IPv6 Rapid Deployment" which is a generalised form of 6to4 connectivity where a variable prefix can be
obtained through configuration. Some ISPs may still use this mode although it's not very popular in general.
The configuration for 6rd may be delivered by IPv4 DHCP connectivity,
but is currently not being parsed and presented to the user.

.. Note::

    You can use this mode for WAN connections only.

Identity Association
-------------------------------

This mode uses a WAN DHCPv6 interface to assign a single (/64) network to your LAN interfaces.

It is similar to Track Interface (legacy), with the important distinction that it does not auto-configure any IPv6 services
like :code:`radvd` or :code:`dnsmasq`.

Configuration of DHCPv6 and Router Advertisements must be done manually via the preferred available services.

.. Note::

    You can use this mode for LAN connections only.


Track Interface (legacy)
-------------------------------

This mode uses a WAN DHCPv6 interface to assign a single (/64) network to your LAN interfaces.
The "Manual configuration" option switches from automatically configuring router advertisements
and DHCPv6 (including prefix delegation if the prefix is big enough)
to how Static IPv6 configured devices are able to use it from the menu.

The primary function of a "track" interface is to prepare the addressing based on the configured "wan" interface,
this is either facilited statically (calculated) for :code:`6to4` , :code:`6rd` or requested via :code:`dhcp6c`.

.. Tip::

    As dhcpv6 is most commonly used, it helps to understand how networks are being distributed using the information
    received via dhcpv6 on the wan interface. Two properties play an important role here, being *Assign prefix ID* (:code:`sla-id`)
    , which is the Site-Level Aggregation Identifier and is specified on the LAN type interface, it identifies the network number
    (each network uses a unique number). The other option is *Prefix delegation size* (:code:`sla-len`),
    which is specified on the wan type interface and configures the prefix size to use for all attached networks (default :code:`/64`).


As soon as the interface has an address, we can start serving router advertisements using :code:`radvd` or :code:`dnsmasq`
and addresses using any of the available dhcpv6 servers.

.. Note::

    You can use this mode for LAN connections only.


Link Local
-------------------------------

This mode generates an automatic link-local address on the selected interfaces and does not process router advertisements,
which means SLAAC is not generated and routes are not installed automatically.

The usecases for this mode are more advanced, examples are:

-  Distribute a larger prefix that is received via a static or dynamic route (BGP). These routes most likely target
   the link-local address of the WAN interface. To delegate a prefix to customers, set the LAN interface to link-local and use KEA for DHCPv6-PD.
   KEA will set a route to the next hop link-local address automatically.

-  NDP proxying, as link-local prevents the same on-link prefix to appear on multiple links which would cause routing issues.
   Such a scenario requires an additional NDP proxy plugin.

.. Note::

    You can use this mode for WAN and LAN connections.


Basic setup and troubleshooting
=======================================

There are two steps for providing IPv6:

1.  Provide IPv6 to your WAN and the firewall itself.
2.  Provide IPv6 to your LAN including the clients behind it.

For step 1 start with selecting the appropriate IPv6 mode, reconfigure the WAN interface and try to ping an IPv6 address or host from the firewall itself, e.g.:

Test if ping over IPv6 to Internet is successful (also possible via :menuselection:`Interfaces-->Diagnostics-->Ping`).

::

  # ping -6 heise.de

Test if IPv6 default route exists (also possible via :menuselection:`System-->Routes-->Status` and search for default).

::

  # netstat -nr6 | grep default

.. Note::

    If one or both of these do not work you are looking at a configuration problem on the WAN side or your ISP does not support IPv6 for you at this point.
    Do not try to debug step 2 at this point wondering why clients cannot connect.

For step 2 static and tracking modes are what can be used on a LAN to provide attached clients with IPV6 connectivity.

Tracking mode is enabled by default and the DHCPv6 on the WAN automatically sets up both Router Advertisements and DHCPv6 server including the use of prefixes being delegated to clients if the present prefix has enough room left to delegate.

When using static mode or the "Manual configuration" setting in tracking you can configure both Router Advertisements and DHCPv6 server from the menu, but defaulting to off. Most endpoint devices work fine with only Router Advertisements set, but if you deal with downstream routers it can be beneficial to set up DHCPv6 server as well to delegate part of the prefix.

.. Note::

    Note that certain network stack implementations such as Android phones only support Router Advertisement configuration via SLAAC and DCHPv6 leases do not work there.


Make sure to test the following on multiple different clients to see if connectivity can be established at all or not:

*   https://test-ipv6.com/
*   https://ipv6-test.com/


These two pages can help you diagnose remaining issues as well.
Make sure to set up both DHCPv6 server and Router advertisements during testing when debugging IPv6 connectivity. If you eventually do not have any need for one or the other it's also ok to disable them. A completely static setup is also possible.


.. Tip::

    When you experience issues during setup, consider the sequence of events as explained earlier and use the packet capture
    to inspect if data is being exchanged using the expected protocols (e.g. :code:`ICMPv6` to find RS, RA traffic)



Configuration examples
=======================================

- :doc:`/manual/how-tos/IPv6_ZenUK`
- :doc:`/manual/how-tos/ipv6_tunnelbroker`
- :doc:`/manual/how-tos/ipv6_dsl`
