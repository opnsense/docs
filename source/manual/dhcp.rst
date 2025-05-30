========================
DHCP
========================

DHCP is used to automatically provide clients with an IP address (instead of clients having to set one themselves).
DHCP is available for both IPv4 and IPv6 clients, referred to as DHCPv4 and DHCPv6, respectively.

---------------------------
Available Options
---------------------------

There are different DHCP servers to choose from:

    - `Dnsmasq <https://thekelleys.org.uk/dnsmasq/doc.html>`__ (since version 25.7)
    - `KEA <https://www.isc.org/kea/>`__ (since version 24.1)
    - `ISC <https://www.isc.org/dhcp/>`__ (EOL)

Additionally, there is a dedicated DHCP relay:

    - `Dhcrelay <https://man.freebsd.org/cgi/man.cgi?query=dhcrelay>`__ (since version 24.7)

.. Note::

    Dnsmasq is the new default DHCP server in version 25.7 and supersedes ISC. It is recommended for small and medium sized setups up to
    a thousand clients. Read more about the deployment differences between KEA and Dnsmasq here: `Dnsmasq </manual/dnsmasq.html#dhcp-service>`__

.. Note::

    KEA is the correct choice for large HA (High Availability) setups with more than a thousand clients in many different DHCP ranges.
    Dnsmasq can be used for smaller HA setups as alternative, though it does not offer lease synchronization like KEA.

...............................
Reservations
...............................

ISC, KEA and Dnsmasq offer the possibility to reserve an IP address for a specific client. This is useful when a client
needs to have the same IP address every time it connects to the network. All services also offer the ability to define reservations
inside and outside of the assigned pool of dynamic IP addresses. However, you should only define reservations outside of the pool.
Unless you can guarantee that this client is online at all times when the reservation is in the dynamic range, the DHCP server is
free to offer this IP address to a different client when the first client goes offline.

.. Note::

    In Dnsmasq static DHCPv4 pools can be configured for reservations.

--------------------
Dnsmasq DNS & DHCP
--------------------

Dnsmasq is a lightweight DNS, router advertisement and DHCP server.
It is intended to provide coupled DNS and DHCP service to a LAN.
Dnsmasq accepts DNS queries and either answers them from a small, local, cache or forwards them to a real, recursive, DNS server.

The dnsmasq DHCP server supports static address assignments and multiple networks.
It automatically sends a sensible default set of DHCP options, and can be configured to send any desired set of DHCP options, including vendor-encapsulated options.

The dnsmasq DHCPv6 server provides the same set of features as the DHCPv4 server, and in addition, it includes router advertisements and a
neat feature which allows naming for clients which use DHCPv4 and stateless autoconfiguration only for IPv6 configuration.
There is support for doing address allocation (both DHCPv6 and RA) from subnets which are dynamically delegated via DHCPv6 prefix delegation.

See manual: :doc:`Dnsmasq </manual/dnsmasq>`

-----------------
ISC DHCP
-----------------

...............................
Settings overview
...............................

DHCPv4 settings can be found at :menuselection:`Services --> ISC DHCPv4`. DHCPv6 settings can be found at :menuselection:`Services --> ISC DHCPv6`.

The DHCPv4 submenu further consists of:

* An entry per interface of general settings, like a toggle to enable/disable DHCPv4 for this interface, DHCP range, DNS servers…
* **Leases**: Shows all IP addresses that are handed out to clients.
* **Log File**: Shows the log file of the DHCPv4 server.

The DHCPv6 submenu further consists of:

* **Leases**: Shows all IP addresses that are handed out to clients.

...............................
Using DHCPv4
...............................

A typical DHCPv4 usage scenario is using it on your LAN with an IP range of 192.168.1.x, where x can be a number from 1
through 254. This means a subnet mask of 255.255.255.0. The range can also be written as 192.168.1.0/24. (The “1” in
the third group can also be another number, and there are also other ranges available for private use. These are
described in `RFC 1918 <https://tools.ietf.org/html/rfc1918#section-3>`_.)

The LAN IP of the OPNsense device that serves DHCP to the LAN should fall in the same DHCP IP range. Typically, it gets
the address ending in .1 (so 192.168.1.1 in this example).

To set the LAN IP, go to :menuselection:`Interfaces --> [LAN]`, set “IPv4 Configuration Type” to “Static”, and under
“Static IPv4 configuration”, set “IPv4 address” to ``192.168.1.1`` and the subnet dropdown to “24”. Then click Save.

To set the DHCP settings, go to :menuselection:`Services --> ISC DHCPv4 --> [LAN]`. Under “Gateway”, put ``192.168.1.1``. Under range,
put ``192.168.1.100`` as the start address and ``192.168.1.200`` as the end address. Then click Save. After saving,
click the “Apply Settings” button.


...............................
Using DHCPv6
...............................
.. _Using DHCPv6:

When IPv6 addresses should be provisioned over DHCPv6 the :menuselection:`Services--> ISC DHCPv6 -->[Interface]` is the place
to look at. Like in the IPv4 scenario, you can provide a range here, offer settings like default DNS servers and
create static assignments based on the clients unique DHCP identifier (`DUID <https://en.wikipedia.org/wiki/DHCPv6>`__).

Always make sure  :doc:`Router advertisements </manual/radvd>` are properly configured before debugging DHCPv6 issues, these two
daemons depend on eachother.

If a Prefix Delegation Range is specified, downstream routers may request prefixes (IA_PD). Routing a delegated prefix to a downstream
router requires OPNsense to be aware of the router's IPv6 WAN address. This can be achieved in two ways:

* **Dynamic DHCPv6 address lease**: If an address range is specified in the DHCPv6 service settings and the downstream router requests both an address (IA_NA) and prefix (IA_PD), the prefix will be routed to the leased address.
* **Static mapping**: If the DUID of an active prefix lease matches the DUID of a DHCPv6 static mapping, the delegated prefix will be unconditionally routed to the static mapping's IPv6 address. The DHCPv6 service doesn't have to be configured with an address range and the downstream router doesn't have to request an address. The address in the static mapping may be a GUA, ULA or link-local address. This allows downstream prefix delegation to routers which only request a prefix, not an address.

...............................
Advanced settings
...............................

To configure options that are not available in the GUI one can add custom configuration files on the firewall itself.
Files can be added in :code:`/usr/local/etc/dhcpd.opnsense.d/` for IPv4 and :code:`/usr/local/etc/dhcpd6.opnsense.d/`
for IPv6, these should use as extension .conf (e.g. custom-options.conf). When more files are placed inside the directory,
all will be included in alphabetical order.

.. Warning::
    It is the sole responsibility of the administrator which places a file in the extension directory to ensure that the configuration is
    valid.

...............................
Diagnostics
...............................

As mentioned in the settings overview, the current leased IP addresses can be seen in the **Leases** page for diagnostic
purposes. Both IPv4 and IPv6 have their own leases page. This page reflects the current facts as reported by DHCPd in the
`/var/dhcpd/var/db/dhcpd(6).leases` database. By default this page only shows the current active leases. To show
all configured leases, check the "inactive" box. You are also able to filter on interfaces by using the dropdown
showing "All Interfaces".

- All times are reported in local time as specified in `Administration <settingsmenu.html#general>`__
- Clients are considered online if they exist the ARP table for IPv4 or NDP table for IPv6.
- The different possible states a lease can be in is documented in the
  `dhcpd.leases <https://www.freebsd.org/cgi/man.cgi?query=dhcpd.leases>`__ page. If failover is enabled, checking the
  **inactive** box will reveal all IP addresses currently reserved by DHCPd with a **backup** state. These are leases that are
  available for allocation by the failover secondary. The amount shown will vary depending on the configured failover
  split value or range.
- The lease type can either by **dynamic** or **static**. This is provided for ease of sorting.
- A static mapping for a dynamic lease can be configured by clicking on the plus sign of a row.
- A lease can also be directly deleted from the leases database.
- for DHCPv4, a hostname for a client will be shown if the client specifies their hostname as part of the protocol.
- For DHCPv6, a MAC address will be shown if it exists in the NDP table or if the MAC address exists in the DUID, but only
  if this MAC address maps to a known vendor. This is because a MAC address cannot reliably be fetched from a DUID.
- The DHCPv6 leases page also shows the delegated prefixes in a separate tab.

-----------------
DHCRelay
-----------------

.. _dhcp-relaying:


DHCP relaying is the forwarding of DHCP requests received on one interface to the DHCP server of another. DHCP
relaying is available for both DHCPv4 and DHCPv6. The settings can be found at :menuselection:`Services --> DHCRelay`.

...............................
Destinations
...............................

+---------------+-----------------------------------------------------------------------------------------------------------+
| Setting       | Explanation                                                                                               |
+===============+===========================================================================================================+
| Name          | A descriptive name of the reusable relay destination                                                      |
+---------------+-----------------------------------------------------------------------------------------------------------+
| Server        | A comma separated list of IPs to which the requests should be forwarded. Can be IPv4 or IPv6 exclusively. |
+---------------+-----------------------------------------------------------------------------------------------------------+

...............................
Relays
...............................

+-----------------------+---------------------------------------------------------------------------------------------------+
| Setting               | Explanation                                                                                       |
+=======================+===================================================================================================+
| Enable                | Check to enable this entry                                                                        |
+-----------------------+---------------------------------------------------------------------------------------------------+
| Interface             | Which interface to apply relaying to. Only interfaces with an Ethernet address can be selected.   |
|                       | Only one interface per destination per address family is allowed.                                 |
+-----------------------+---------------------------------------------------------------------------------------------------+
| Destination           | The target destination of the relay from the pool of previously set up destinations.              |
+-----------------------+---------------------------------------------------------------------------------------------------+
| Agent Information     | If this is checked, the DHCP relay will append the circuit ID (interface number) and the          |
|                       | agent ID to the DHCP request.                                                                     |
+-----------------------+---------------------------------------------------------------------------------------------------+

-----------------
KEA DHCP
-----------------

Kea is the next generation of DHCP software, developed by Internet Systems Consortium (ISC).

...............................
Control Agent
...............................

The Kea Control Agent (CA) is a daemon which exposes a RESTful control interface for managing Kea servers.
When building a high available dhcp setup, the control agent is a requirement for these kind of setups.

========================================================================================================================================================

====================================  ==================================================================================================================
Enabled                               Enable control agent
Bind address                          Address on which the RESTful interface should be available, usually this is localhost (127.0.0.1)
Bind port                             Choose an unused port for communication here.
====================================  ==================================================================================================================

.. Note::

  Although the control agent is required to use high availability peers, it does not have to listen on
  a non loopback address. The peer configuration by default uses the so called "Multi-Threaded Configuration (HA+MT)",
  in which case it starts a separate listener for the HA communication.

...............................
Kea DHCPv4
...............................

This is the DHCPv4 service available in KEA, which offers the following tab sheets with their corresponding settings:

* Settings

  - Generic settings for this service

* Subnets

  - Subnets and associated pools

* Reservations

  - Machine static reservations

* HA Peers

  - Define HA peers for this cluster. All nodes should contain the exact same definitions (usually two hosts, a :code:`primary` and a :code:`standby` host)

========================================================================================================================================================

====================================  ==================================================================================================================
**Settings**
Service\\Enabled                      Enable DHCPv4 service
Service\\Manual config                Configure kea dhcp 4 manually, requires supplying your own :code:`/usr/local/etc/kea/kea-dhcp4.conf` file
                                      (advanced users only)
General\\Interfaces                   Interfaces to listen on for dhcp[v4] requests
General\\Valid lifetime               Defines how long the addresses (leases) given out by the server are valid (in seconds)
High Availability\\Enabled            Enable high availability setup, requires an active control agent.
High Availability\\This server name   This servername, when unspecified the hostname for this firewall is used.
**Subnets**
Subnet                                Subnet in cidr presentation (e.g. 192.168.1.0/24)
Pools                                 List of pools (available addresses) for this service
Auto collect option data              When set, collect primary address to be used as gateway and dns for the connected clients.
Routers (gateway)                     Default gateway to offer
DNS servers                           Default DNS servers to offer to the client
NTP servers                           Default NTP (time) servers to offer to the client
TFTP server                           TFTP (etherboot) location to offer the client
TFTP bootfile name                    TFTP boot filename to use
**Reservations**
Subnet                                Select a subnet to which this reservation belongs
IP address                            Address to offer the client
MAC address                           Hardware address which identifies this client
Hostname                              Hostname to offer the client
Description                           User friendly description for this reservation
**HA Peers**
Role                                  Choose if the selected host is a primary or a standby machine
Url                                   This specifies the URL of our server instance, which should use a different port than the control agent.
                                      For example http://192.0.2.1:8001/
====================================  ==================================================================================================================


.. Tip::
  When using a CARP / HA setup, you usually should specify gateways and dns entries manually. Make sure to disable "Auto collect option data"
  in that case.

To configure a server with a minimal setup on LAN (like offered on a default OPNsense using ISC-DHCP) using the :code:`192.168.1.0/24` network
offering addresses in the range :code:`192.168.1.100 - 192.168.1.199`. Follow the following steps:

1.  Enable the service (General\\Enabled)
2.  Choose LAN as listen interface (General\\Interfaces)
3.  Add a new subnet containing the following settings

  - Subnet : :code:`192.168.1.0/24`
  - Pools : :code:`192.168.1.100 - 192.168.1.199`
  - Auto collect option data: :code:`[x]`

4. Click on the **Apply** button.



...............................
Leases DHCPv4
...............................

This page offers an overview of the (non static) leases being offered by KEA DHCPv4.

