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
* **Leases**: Shows all IP addresses that are handed out to clients (can be filtered to only show active and static leases).
* **Log File**: Shows the log file of the DHCPv4 server.

The DHCPv6 submenu further consists of:

* **Relay**: DHCP requests can be “forwarded” to a DHCP server on another interface. This is called relaying.
* **Leases**: Shows all IP addresses that are handed out to clients (can be filtered to only show active and static leases).

------------
Using DHCPv4
------------

A typical DHCPv4 usage scenario is using it on your LAN with an IP range of 192.168.1.x, where x can be a number from 1
through 254. This means a subnet mask of 255.255.255.0. The range can also be written as 192.168.1.0/24. (The “1” in
the third group can also be another number, and there are also other ranges available for private use. These are
described in `RFC 1918 <https://tools.ietf.org/html/rfc1918#section-3>`_.)

The LAN IP of the OPNsense device that serves DHCP to the LAN should fall in the same DHCP IP range. Typically, it gets
the address ending in .1 (so 192.168.1.1) in this example.

To set the LAN IP, go to :menuselection:`Interfaces --> [LAN]`, set “IPv4 Configuration Type” to “Static”, and under
“Static IPv4 configuration”, set “IPv4 address” to ``192.168.1.1`` and the subnet dropdown to “24”. Then click Save.

To set the DHCP settings, go to :menuselection:`Services  -->  DHCPv4  -->  [LAN]`. Under “Gateway”, put ``192.168.1.1``. Under range,
put ``192.168.1.100`` as the start address and ``192.168.1.200`` as the end address. Then click Save. After saving,
click the “Apply Settings” button.

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
