================
Devices
================

Besides wired, wireless and VPN interfaces, there are also some other, virtual interfaces, as well as some
miscellaneous interface-related. These options can be found under :menuselection:`Interfaces --> Devices`.
This document briefly explains these options.

------
Bridge
------

Bridging allows to create a connection between separate networks, allow traffic on network A destined for network B
(where both networks are connected to your OPNsense device) to reach it via this bridge. Note that this does not
include DHCP services—this needs to set using :ref:`DHCP relaying <dhcrelay>`.

A bridge works like a (layer-2) switch, forwarding traffic from one interface to another.
Multicast and broadcast packets are always forwarded to all interfaces that are part of the bridge.
For unicast traffic, the bridge learns which MAC addresses are associated with which interfaces and will forward the traffic selectively.

Optionally a bridge can be configured to support `(Rapid) Spanning Tree Protocol <https://en.wikipedia.org/wiki/Spanning_Tree_Protocol>`__ (RSTP/RTP)
to prevent loops in the network topology. These options are provided in the "advanced" section of the configuration and include the following settings:

==================================  ==================================================================================================
Option                              Description
==================================  ==================================================================================================
Enable                              Enable the (Rapid) Spanning Tree Protocol
Protocol                            Protocol to use, rapid or regular spanning tree
STP interfaces                      The interfaces tith [R]STP enabled, from the ones in the bridge
Valid time (maxage)                 Set the time that a Spanning Tree Protocol configuration is valid. The default is 20 seconds.
Forward time (fwddelay)             Set the time that must pass before an interface begins forwarding packets when
                                    Spanning Tree is enabled. The default is 15 seconds.
Hold count (holdcnt)                Set the transmit hold count for Spanning Tree. This is the number of packets transmitted
                                    before being rate limited. The default is 6. The minimum is 1 and the maximum is 10.
==================================  ==================================================================================================

Other advanced options available in the bottom section of the screen and include the following settings:

==================================  ==================================================================================================
Option                              Description
==================================  ==================================================================================================
Cache size (maxaddr)                Set the size of the bridge address cache to size. The default is 2000 entries.
Cache entry expire time (timeout)   Set the timeout of address cache entries to this number of seconds. If seconds is zero,
                                    then address cache entries will not be expired. The default is 1200 seconds.
Span port                           Span ports transmit a copy of every frame received by the bridge.
                                    This is most useful for snooping a bridged network passively on another host connected to one
                                    of the span ports of the bridge.
Edge ports                          Set interface as an edge port. An edge port connects directly to end stations and
                                    cannot create bridging loops in the network; this allows it to transition straight to forwarding.
Auto Edge ports                     Allow interface to automatically detect edge status.
                                    This is the default for all interfaces added to a bridge, selecting interfaces will disable
                                    auto mode.
PTP ports                           Set the interface as a point-to-point link.
                                    This is required for straight transitions to forwarding and should be
                                    enabled on a direct link to another RSTP-capable switch.
Auto PTP ports                      Automatically detect the point-to-point status on interface by checking the
                                    full duplex link status.
                                    This is the default for interfaces added to the bridge, selecting interfaces will disable
                                    auto mode.
Sticky ports                        Mark an interface as a "sticky" interface. Dynamically learned address entries are
                                    treated as static once entered into the cache.
                                    Sticky entries are never aged out of the cache or replaced,
                                    even if the address is seen on a different interface.
Private ports                       Mark an interface as a "private" interface. A private interface does not forward any traffic
                                    to any other port that is also a private interface.
==================================  ==================================================================================================



---
GIF
---

GIF (``gif(4)``, Generic Tunnel Interface) can be used to tunnel IPv6 via IPv4 connections. A common use for this is the
IPv6 tunnel of Hurricane Electric (he.net).

.. Note::

    In :doc:`/manual/how-tos/ipv6_tunnelbroker` you can find information on how to setup a tunnel using Hurricane Electric


As with all tunnel devices, the most important settings relate to how both ends connect and which addressing will be used to
route traffic over the tunnel. The rest of the settings usually are best left to their defaults.

==================================  ==================================================================================================
Option                              Description
==================================  ==================================================================================================
Parent interface                    Actually the source address the tunnel will use to connect from.
GIF remote address                  Peer address where encapsulated gif packets will be sent.
GIF tunnel local address            The tunnel's local address which will be configured on the interface.
GIF tunnel remote address           The tunnel's remote address which will be configured on the interface.
Disable Ingress filtering           Ingress filtering on outer tunnel source can break tunnel operation in an asymmetrically
                                    routed networks, in which case this can be disabled by marking this option.
ECN friendly behavior               Note that the ECN friendly behavior violates RFC2893.
                                    This should be used in mutual agreement with the peer.
Description                         User friendly description for this tunnel
==================================  ==================================================================================================


---
GRE
---

GRE (``gre(4)``, Generic Routing Encapsulation) is used to create a virtual point-to-point connection, through which
encapsulated packages can be sent. This can be used to utilize (OSI-layer 3) protocols between devices over a connection that
does not normally support these protocols.

Since the GRE protocol was designed by Cisco, it is often used as default tunnel technology when using their solutions.

A common use-case of GRE is also to forward (no routable) multicast traffic,
although this will need additional software such as IGMP-proxy or PIMD, which are less commonly used on OPNsense.

The available settings are similar to those described for the GIF tunnel type:

==================================  ==================================================================================================
Option                              Description
==================================  ==================================================================================================
Parent interface                    Actually the source address the tunnel will use to connect from.
GRE remote address                  Peer address where encapsulated gif packets will be sent.
GRE tunnel local address            The tunnel's local address which will be configured on the interface.
GRE tunnel remote address           The tunnel's remote address which will be configured on the interface.
Description                         User friendly description for this tunnel
==================================  ==================================================================================================


----
LAGG
----

LAGG (``lagg(4)``) allows for link aggregation, bonding and fault tolerance. This works best if your network switches
support. Only unassigned interfaces can be added to LAGG.

The userinterface supports the following options:

==================================  ==================================================================================================
Option                              Description
==================================  ==================================================================================================
Parent interface                    Members of the link aggregation
Lag proto                           Protocol to use for aggregation, available options are described in the next table. LACP is most
                                    commonly used.
Description                         User friendly description for this interface
Fast timeout                        Enable lacp fast-timeout on the interface.
Use flowid                          Use the RSS hash from the network card if available,
                                    otherwise a hash is locally calculated.
                                    The default depends on the system tunable in net.link.lagg.default_use_flowid.
Hash Layers                         Set the packet layers to hash for aggregation protocols which load balance.
Use strict                          Enable lacp strict compliance on the interface.
                                    The default depends on the system tunable in `net.link.lagg.lacp.default_strict_mode`.
MTU                                 MTU size, when unset the smallest mtu of the LAGG children will be used.
==================================  ==================================================================================================

.. Note::

    Hash Layers, specifies how the device will loadbalance the traffic across physical links in the LAGG bundle.
    This is done per the 5-tuple if the LACP device implementation allows it. 
    Hash Layers, do not need to be the same between two connecting devices, it can be considered as a best practice but its not a rule of must be.

**Available protocols**

==================================  ==================================================================================================
Name                                Description
==================================  ==================================================================================================
failover                            Sends and receives traffic only through the master port.
                                    If the master port becomes unavailable, the next active port is used.
                                    The first interface added is the master port; any interfaces added after that are used
                                    as failover devices.
fec                                 Supports Cisco EtherChannel. This is a static setup and does not negotiate
                                    aggregation with the peer or exchange frames to monitor the link.
lacp                                Supports the IEEE 802.3ad Link Aggregation Control Protocol (LACP) and the Marker Protocol.
                                    LACP will negotiate a set of aggregated links with the peer in to one or more
                                    Link Aggregated Groups. Each LAG is composed of ports of the same speed,
                                    set to full-duplex operation. The traffic will be balanced across the ports in the LAG
                                    with the greatest total speed, in most cases there will only be one LAG which contains all ports.
                                    In the event of changes in physical connectivity, Link Aggregation will quickly
                                    converge to a new configuration.
loadbalance                         Balances outgoing traffic across the active ports based on hashed protocol
                                    header information and accepts incoming traffic from any active port.
                                    This is a static setup and does not negotiate aggregation with the peer or exchange
                                    frames to monitor the link. The hash includes the Ethernet source and destination address,
                                    and, if available, the VLAN tag, and the IP source and destination address.
roundrobin                          Distributes outgoing traffic using a round-robin scheduler through all
                                    active ports and accepts incoming traffic from any active port.
none                                This protocol is intended to do nothing: It disables any traffic without
                                    disabling the lagg interface itself.
==================================  ==================================================================================================

.. Attention::

    The LAGG protocol should match with the one your switch supports. It is best practice to use LACP if possible.
    Devices connected via LAGG require the same protocol.  

**LACP timeout**

LACP timeout has two modes; Slow/normal and Fast. It handles how fast the re-convergence occurs in case of link failure.
This specifies how often the heartbeats are sent between the two LAGG connected devices.

==================================  =================================  =================================================================
LACP mode                           Heartbeat/Timeout interval         Enable
==================================  =================================  =================================================================
Slow/Normal                         30s                                Fast timeout turned off
Fast                                1s                                 Fast timeout turned on
==================================  =================================  =================================================================

The Slow/normal timeout should be the default in most cases.
Due to possible vendor implementation issues, keeping the LACP timeout on Slow/normal is preferable. Fast timeout can cause connectivity disruption in some cases.
LACP timeout requires the same value on both devices connected via LAGG. If not, heartbeats can be missed which will cause connectivity disruption.

Read `LAGG Setup </manual/how-tos/vlan_and_lagg.html>`_ for an example configuration.

--------------
Loopback
--------------

Loopbacks are logical virtual interfaces which emulate real interfaces and can be used for different setup scenarios,
which require always-on interfaces. Below you will find some scenario's for which these devices are used.

*   Administrative access to services on your machine, which can bind to an address configured on top of the loopback.
*   Using loopback addresses as router IDs for OSPF or BGP, which helps to identify your nodes and eases administration

----
VLAN
----

VLANs (Virtual LANs) can be used to segment a single physical network into multiple virtual networks. This can be
done for QoS purposes, among other things. For this reason, most ISP-issued IPTV devices utilize VLANs.

The following settings are available for these devices:

==================================  =======================================================================================================
Name                                Description
==================================  =======================================================================================================
Device                              Device name of this virtual interface, usually starts with **vlan** or **qinq** depending on the type
Parent interface                    The interface to use as parent which it will send/receive vlan tagged traffic on
VLAN tag                            802.1Q VLAN tag (between 1 and 4094)
VLAN priority                       802.1Q VLAN PCP (priority code point)
Description                         User friendly description for this interface
==================================  =======================================================================================================

.. Note::

    `802.1ad <https://en.wikipedia.org/wiki/IEEE_802.1ad>`__ , also known as QinQ, is supported via the VLAN configuration
    in which case you would stack a :code:`vlan` on top of a :code:`vlan`, the device name should start with qinq in that case.


Read `VLAN Setup </manual/how-tos/vlan_and_lagg.html>`_ for an example configuration.

------
VXLAN
------

Virtual eXtensible Local Area Networks (VXLAN) are used to overlay virtualized layer 2 networks over layer 3 networks
as described by `rfc7348 <https://tools.ietf.org/html/rfc7348>`__.

Tunnels can be setup in point to point (parameter :code:`Remote address`) or multicast (parameters :code:`Multicast group` and :code:`Device`).
The `Source address` must be an existing (statically assigned) address assigned at this firewall, which will be used as
source in the encapsulating IPv4/IPv6 header.

.. Note::

  Since the vxlan interface encapsulates the Ethernet frame with an IP, UDP, and vxlan header,
  the resulting frame may be larger than the MTU of the physical network.  The vxlan specification recommends the physical
  network MTU be configured to use jumbo frames to accommodate the encapsulated frame size.
  Alternatively, the MTU size on the vxlan interface might be reduced to allow the encapsulated frame to fit in
  the current MTU of the physical network.


Read `VXLAN Bridge </manual/how-tos/vxlan_bridge.html>`_ for an example configuration with a common setup.

----------------
Point-to-Point
----------------

Point-to-Point (PP) interfaces provide direct connectivity between two endpoints without any intermediary devices. These interfaces are commonly used for WAN connections,
tunneling, or direct link setups where `broadcast` and `multiple access` are not needed.

The following `Link Types` are available for these interfaces:

.. tabs::

   .. tab:: PPP (Point-to-Point Protocol)

      A widely used protocol for establishing direct connections over serial links, often utilized for
      dial-up and DSL connections. Supports authentication (PAP/CHAP), compression, and error detection.

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Link interfaces**                       Select one interface for normal PPP and least two interfaces for Multilink (MLPPP) connections.
      **Description**                           You may enter a description here for your reference. Description will appear in the "Interfaces Assign" select lists
      **Service Provider**                      Select the country, Provider and Plan for the PPP connection.
      **Username**                              Enter your username for CHAP authentication.
      **Password**                              Enter your password for CHAP authentication.
      **Phone Number**                          Typically ``*99#`` for GSM networks and ``#777`` for CDMA networks
      **Access Point Name (APN)**               Enter the APN for your service provider. E.g., ``internet.t-d1.de`` for T-Mobile.
      ========================================= ====================================================================================

      ========================================= ====================================================================================
      **Advanced Option**                       **Description**
      ========================================= ====================================================================================
      **APN number (optional)**                 Defaults to 1 if you set APN above. Ignored if you set no APN above.
      **SIM PIN**                               Enter the SIM PIN if your service provider requires it. Leave blank if not required.
      **SIM PIN wait**                          Time to wait for SIM to discover network after PIN is sent to SIM (seconds).
      **Init String**                           Enter the modem initialization string here. Do not include the "AT" string at the beginning of the command.
                                                Many modern USB 3G modems don't need an initialization string.
      **Connection Timeout**                    Enter timeout in seconds for connection to be established (sec.) Default is 45 sec.
      **Uptime Logging**                        This option causes cumulative uptime to be recorded and displayed on the Status Interfaces page.
      **Dial On Demand**                        This option causes the interface to operate in dial-on-demand mode.
                                                Do not enable if you want your link to be always up. The interface is configured, but the actual
                                                connection of the link is delayed until qualifying outgoing traffic is detected.
      **Idle Timeout**                          (seconds) Default is 0, which disables the timeout feature. If no incoming or outgoing packets are transmitted
                                                for the entered number of seconds the connection is brought down.
                                                When the idle timeout occurs, if the dial-on-demand option is enabled, mpd goes back into dial-on-demand mode.
                                                Otherwise, the interface is brought down and all associated routes removed.
      **Compression**                           This option enables Van Jacobson TCP header compression, which saves several bytes per TCP data packet.
                                                You almost always want this option. This compression ineffective for TCP connections with enabled modern extensions
                                                like time stamping or SACK, which modify TCP options between sequential packets.
      **TCPmssFix**                             This option causes mpd to adjust incoming and outgoing TCP SYN segments so that the requested maximum segment
                                                size is not greater than the amount allowed by the interface MTU. This is necessary in many setups to avoid problems
                                                caused by routers that drop ICMP Datagram Too Big messages. Without these messages, the originating machine sends data,
                                                it passes the rogue router then hits a machine that has an MTU that is not big enough for the data.
                                                Because the IP Don't Fragment option is set, this machine sends an ICMP Datagram Too Big message back to the originator
                                                and drops the packet. The rogue router drops the ICMP message and the originator never gets to discover that
                                                it must reduce the fragment size or drop the IP Don't Fragment option from its outgoing data.
      **ShortSeq**                              This option is only meaningful if multi-link PPP is negotiated. It proscribes shorter multi-link fragment headers,
                                                saving two bytes on every frame. It is not necessary to disable this for connections that are not multi-link.
      **ACFComp**                               Address and control field compression. This option only applies to asynchronous link types. It saves two bytes per frame.
      **ProtoComp**                             Protocol field compression. This option saves one byte per frame for most frames.
      ========================================= ====================================================================================


   .. tab:: PPPoE (Point-to-Point Protocol over Ethernet)

      Encapsulates PPP frames within Ethernet frames, enabling authentication and connection management
      over broadband connections like DSL. Typically used with ISPs for user authentication.

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Link interfaces**                       Select one parent interface for PPP encapsulation.
      **Description**                           You may enter a description here for your reference. Description will appear in the "Interfaces Assign" select lists
      **Username**                              Enter your username for CHAP authentication.
      **Password**                              Enter your password for CHAP authentication.
      **Service name**                          This field can usually be left empty unless specified by the provider.
      **Host-Uniq**                             This field can usually be left empty unless specified by the provider.
      ========================================= ====================================================================================

      .. Note:: Check the PPP tab for all advanced options.


   .. tab:: PPTP (Point-to-Point Tunneling Protocol)

      A VPN protocol that uses PPP to encapsulate network packets and secure data transmission.
      While widely supported, PPTP is considered insecure due to weak encryption mechanisms.

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Link interfaces**                       Select one parent interface for PPP encapsulation.
      **Description**                           You may enter a description here for your reference. Description will appear in the "Interfaces Assign" select lists
      **Username**                              Enter your username for CHAP authentication.
      **Password**                              Enter your password for CHAP authentication.
      ========================================= ====================================================================================

      .. Note:: Check the PPP tab for all advanced options.


   .. tab:: L2TP (Layer 2 Tunneling Protocol)

      An extension of PPTP that does not provide encryption on its own but was often paired with IPsec
      for secure tunneling. Used for VPN connections and remote access setups.

      .. Note:: Check the PPTP and PPP tab for all options.


.. Note:: The ``ppp`` log files can be found in :menuselection:`System --> Log Files --> General`.

Read `PPPoE ISP Setup </manual/how-tos/pppoe_isp_setup.html>`_ for an example configuration of PPPoE with VLAN Tag for an ISP connection.
