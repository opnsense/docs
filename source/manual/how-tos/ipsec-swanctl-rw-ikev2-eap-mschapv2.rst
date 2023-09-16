=======================================
IPsec - Roadwarriors IKEv2 EAP-MSCHAPv2
=======================================

.. contents:: Index

The following roadwarrior configuration is universally usable between different clients and easy to setup.

EAP-MSCHAPv2 via IKEv2 is based on a server certificate and an EAP Pre-Shared Key (username + password).
The CA certificate has to be installed on the users device.

------------------------------------
Networks used in this How-To section
------------------------------------

=========  ===================  =========================
Interface  Network IPv4         Network IPv6
=========  ===================  =========================
WAN        ``203.0.113.0/24``   ``2001:db8:1234::/48``
LAN        ``192.168.1.0/24``   ``2001:db8:1234:1::/64``
IPsec      ``172.16.203.0/24``  ``2001:db8:1234:ec::/64``
=========  ===================  =========================

The example users are ``John`` and ``Laura``.

-----------------------------
Methods for Roadwarrior Setup
-----------------------------

:ref:`Method 1 - Shared IP pool for all roadwarriors <rw-swanctl-method1>`
--------------------------------------------------------------------------

- Benefit: Easy configuration and works with most clients out of the box.
- Drawback: All configured EAP Identities can authenticate with this connection, so you can't have tight access control. Roadwarriors don't have unique IP addresses.

:ref:`Method 2 - Static IP address per roadwarrior <rw-swanctl-method2>`
------------------------------------------------------------------------

- Benefit: Tight security because every user can be controlled individually with firewall rules. The whole configuration is stored in one file (swanctl.conf). There are no other dependencies, so it won't break suddenly in the future.
- Drawback: Configuration needs more time and might not scale with large user counts. Windows native VPN client doesn't like this configuration very much because it demands the eap identity exchange method.


-------------
Prerequisites
-------------

System: Trust: Authorities
--------------------------


System: Trust: Certificates
---------------------------


External DNS A-Record
---------------------



.. _rw-swanctl-method1:

----------------------------------------------
Method 1 - Shared IP pool for all roadwarriors
----------------------------------------------


1.1 - VPN: IPsec: Connections: Pools
------------------------------------


1.2 - VPN: IPsec: Pre-Shared Keys
---------------------------------


1.3 - VPN: IPsec: Connections
-----------------------------



.. _rw-swanctl-method2:

---------------------------------------------
Method 2: Shared IP pool for all roadwarriors
---------------------------------------------


2.1 - VPN: IPsec: Connections: Pools
------------------------------------


2.2 - VPN: IPsec: Pre-Shared Keys
---------------------------------


2.3 - VPN: IPsec: Connections
-----------------------------


------------------------------------
Firewall rules, Outbound NAT and DNS
------------------------------------


Firewall: Aliases
-----------------


Firewall: Rules: IPsec
----------------------


Firewall: NAT: Outbound
-----------------------


Services: Unbound DNS
---------------------


--------------------
Client configuration
--------------------


Windows native VPN client
-------------------------


Windows NCP Secure Entry client
-------------------------------


iOS (iPhone, iPad) native VPN client
------------------------------------


Android StrongSwan VPN client
-----------------------------


Linux Strongswan swanctl.conf
-----------------------------

