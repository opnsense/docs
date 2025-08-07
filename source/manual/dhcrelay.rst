==================
DHCrelay
==================

.. contents:: Index

DHCP relaying is the forwarding of DHCP requests received on one interface to the DHCP server of another. DHCP
relaying is available for both DHCPv4 and DHCPv6. The settings can be found at :menuselection:`Services --> DHCRelay`.

DHCrelay binds to port 67 like other available DHCP servers. To run multiple servers side by side, use strict interface binding if available.

-------------------------
Destinations
-------------------------

+---------------+-----------------------------------------------------------------------------------------------------------+
| Setting       | Explanation                                                                                               |
+===============+===========================================================================================================+
| Name          | A descriptive name of the reusable relay destination                                                      |
+---------------+-----------------------------------------------------------------------------------------------------------+
| Server        | A comma separated list of IPs to which the requests should be forwarded. Can be IPv4 or IPv6 exclusively. |
+---------------+-----------------------------------------------------------------------------------------------------------+

-------------------------
Relays
-------------------------

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
