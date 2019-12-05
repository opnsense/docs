================
Other Types
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

--------------
Loopback
--------------

Loopbacks are logical virtual interfaces which emulate real interfaces and can be used for different setup scenario's,
which require always-on interfaces. Below you will find some scenario's for which these types of interfaces are used.

*   Administrative access to services on your machine, which can bind to an address configured on top of the loopback.
*   Using loopback addresses as router IDs for OSPF or BGP, which helps to identify your nodes and eases administration

----
VLAN
----

VLANs (Virtual LANs) can be used to segment a single physical network into multiple virtual networks. This can be
done for QoS purposes, among other things. For this reason, most ISP-issued IPTV devices utilise VLANs.


------
VXLAN
------

Virtual eXtensible Local Area Networks (VXLANs) are used to overlay virtualized layer 2 networks over layer 3 networks
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
