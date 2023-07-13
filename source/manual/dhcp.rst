====
DHCP
====

DHCP is used to automatically provide clients with an IP address (instead of clients having to set one themselves).
DHCP is available for both IPv4 and IPv6 clients, referred to as DHCPv4 and DHCPv6, respectively.

-----------------
Settings overview
-----------------

DHCPv4 settings can be found at :menuselection:`Services --> DHCPv4`. DHCPv6 settings can be found at :menuselection:`Services --> DHCPv6`.

The DHCPv4 submenu further consists of:

* An entry per interface of general settings, like a toggle to enable/disable DHCPv4 for this interface, DHCP range, DNS servers…
* **Relay**: DHCP requests can be “forwarded” to a DHCP server on another interface. This is called relaying.
* **Leases**: Shows all IP addresses that are handed out to clients.
* **Log File**: Shows the log file of the DHCPv4 server.

The DHCPv6 submenu further consists of:

* **Relay**: DHCP requests can be “forwarded” to a DHCP server on another interface. This is called relaying.
* **Leases**: Shows all IP addresses that are handed out to clients.

------------
Using DHCPv4
------------

A typical DHCPv4 usage scenario is using it on your LAN with an IP range of 192.168.1.x, where x can be a number from 1
through 254. This means a subnet mask of 255.255.255.0. The range can also be written as 192.168.1.0/24. (The “1” in
the third group can also be another number, and there are also other ranges available for private use. These are
described in `RFC 1918 <https://tools.ietf.org/html/rfc1918#section-3>`_.)

The LAN IP of the OPNsense device that serves DHCP to the LAN should fall in the same DHCP IP range. Typically, it gets
the address ending in .1 (so 192.168.1.1 in this example).

To set the LAN IP, go to :menuselection:`Interfaces --> [LAN]`, set “IPv4 Configuration Type” to “Static”, and under
“Static IPv4 configuration”, set “IPv4 address” to ``192.168.1.1`` and the subnet dropdown to “24”. Then click Save.

To set the DHCP settings, go to :menuselection:`Services --> DHCPv4 --> [LAN]`. Under “Gateway”, put ``192.168.1.1``. Under range,
put ``192.168.1.100`` as the start address and ``192.168.1.200`` as the end address. Then click Save. After saving,
click the “Apply Settings” button.


------------
Using DHCPv6
------------
.. _Using DHCPv6:

When IPv6 addresses should be provisioned over DHCPv6 the :menuselection:`Services-->DHCPv6-->[Interface]` is the place
to look at. Like in the IPv4 scenario, you can provide a range here, offer settings like default DNS servers and
create static assignments based on the clients unique DHCP identifier (`DUID <https://en.wikipedia.org/wiki/DHCPv6>`__).

Always make sure  :doc:`Router advertisements </manual/radvd>` are properly configured before debugging DHCPv6 issues, these two
daemons depend on eachother.

-------------------------
Advanced settings
-------------------------

To configure options that are not available in the GUI one can add custom configuration files on the firewall itself.
Files can be added in :code:`/usr/local/etc/dhcpd.opnsense.d/` for IPv4 and :code:`/usr/local/etc/dhcpd6.opnsense.d/`
for IPv6, these should use as extension .conf (e.g. custom-options.conf). When more files are placed inside the directory,
all will be included in alphabetical order.

.. Warning::
    It is the sole responsibility of the administrator which places a file in the extension directory to ensure that the configuration is
    valid.

.. _dhcp-relaying:

-------------
DHCP relaying
-------------

DHCP relaying is the forwarding of DHCP requests received on one interface to the DHCP server on another. DHCP
relaying is available for both DHCPv4 and DHCPv6. The DHCPv4 settings can be found at
:menuselection:`Services --> DHCPv4 --> Relay`. The DHCPv6 settings can be found at
:menuselection:`Services --> DHCPv6 --> Relay`.

When setting up DHCP relaying (both DHCPv4 and DHCPv6 relaying have the same settings), the following options are
available:

+-----------------------+----------------------------------------------------------------------------------------------+
| Setting               | Explanation                                                                                  |
+=======================+==============================================================================================+
| Enable                |                                                                                              |
+-----------------------+----------------------------------------------------------------------------------------------+
| Interface(s)          | Which interfaces to apply relaying to. Only interfaces with an IP can be selected.           |
+-----------------------+----------------------------------------------------------------------------------------------+
| Append circuit ID and | If this is checked, the DHCP relay will append the circuit ID (interface number) and the     |
| agent ID to requests  | agent ID to the DHCP request.                                                                |
+-----------------------+----------------------------------------------------------------------------------------------+
| Destination servers   | A comma separated list of IPs to which the requests should be forwarded.                     |
+-----------------------+----------------------------------------------------------------------------------------------+

-----------
Diagnostics
-----------

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
