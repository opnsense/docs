================
Other interfaces
================

Besides wired, wireless and VPN interfaces, there are also some other, virtual interfaces, as well as some
miscellaneous interface-related. These options can be found under :menuselection:`Interfaces --> Other types`.
This document briefly explains these options.

------
Bridge
------

Bridging allows to create a connection between separate networks, allow traffic on network A destined for network B
(where both networks are connected to your OPNsense device) to reach it via this bridge. Note that this does not
include DHCP services—this needs to set using :ref:`DHCP relaying <dhcp-relaying>`.

---
GIF
---

GIF (``gif(4)``, Generic Tunnel Interface) can be used to tunnel IPv6 via IPv4 connections. A common use for this are the
IPv6 tunnel of Hurricane Electric (he.net).

---
GRE
---

GRE (``gre(4)``, Generic Routing Encapsulation) is used to create a virtual point-to-point connection, through which
encapsulated packages can be sent. This can be used to utilise protocols between devices over a connection that
does not normally support these protocols.

----
LAGG
----

LAGG (``lagg(4)``) allows for link aggregation, bonding and fault tolerance. This works best if your network switches
support. Only unassigned interfaces can be added to LAGG. More information about LAGG can be found in
`the FreeBSD manual <https://www.freebsd.org/doc/handbook/network-aggregation.html>`_.

----
VLAN
----

VLANs (Virtual LANs) can be used to segment a single physical network into multiple virtual networks. This can be
done for QoS purposes, among other things. For this reason, most ISP-issued IPTV devices utilise VLANs.
