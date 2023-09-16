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

The example users are ``John`` and ``Laura``. The example FQDN is ``vpn1.example.com``.

.. Hint::
    Any IPv6 functionality is optional. If you don't want to use IPv4+IPv6 dual stack, just skip all IPv6 addresses/networks and focus on IPv4. Its also possible to skip IPv4 and create native IPv6 tunnels.


-----------------------------
Methods for Roadwarrior Setup
-----------------------------

:ref:`Method 1 - Shared IP pool for all roadwarriors <rw-swanctl-method1>`
--------------------------------------------------------------------------

- **Benefit:** Easy configuration and works with most clients out of the box.
- **Drawback:** All configured EAP Identities can authenticate with this connection, so you can't have tight access control. Roadwarriors don't have unique IP addresses.


:ref:`Method 2 - Static IP address per roadwarrior <rw-swanctl-method2>`
------------------------------------------------------------------------

- **Benefit:** Tight security because every user can be controlled individually with firewall rules. The whole configuration is stored in one file (swanctl.conf). There are no other dependencies, so it won't break suddenly in the future.
- **Drawback:** Configuration needs more time and might not scale with large user counts. Windows native VPN client doesn't like this configuration very much because it demands the eap identity exchange method.


-------------
Prerequisites
-------------

System: Trust: Authorities
--------------------------

Create a certificate authority which will be used to create server certificates for your IPsec VPN. The lifetime of the CA is 10 years, if it expires you have to deploy new CA certificates to all clients.

    ==============================================  ====================================================================================================
    **Descriptive name:**                           IPsec CA
    **Method:**                                     Create an internal Certificate Authority
    **Key Type:**                                   RSA
    **Key length (bits):**                          2048
    **Digest Algorithm:**                           SHA256
    **Lifetime (days):**                            3650
    **Country Code:**                               Enter your Country Code
    **State or Province:**                          Enter Your State
    **City:**                                       Enter your City
    **Organization:**                               Enter your Organization
    **Email Address:**                              Enter your Email address
    **Common Name:**                                IPsec CA
    ==============================================  ====================================================================================================


System: Trust: Certificates
---------------------------

Create a server certificate for your IPsec VPN. The lifetime of the certificate is around 1 year, if it expires you have to renew the certificate on the OPNsense or your clients can't connect anymore.

    ==============================================  ====================================================================================================
    **Method:**                                     Create an internal Certificate
    **Descriptive name:**                           vpn1.example.com
    **Certificate authority:**                      IPsec CA
    **Type:**                                       Server Certificate
    **Key Type:**                                   RSA
    **Key lenght (bits):**                          2048
    **Digest Algorithm:**                           SHA256
    **Lifetime (days):**                            397
    **Country Code:**                               Enter your Country Code
    **State or Province:**                          Enter Your State
    **City:**                                       Enter your City
    **Organization:**                               Enter your Organization
    **Email Address:**                              Enter your Email address
    **Common Name:**                                vpn1.example.com
    **Alternative Names:**                          **Type DNS:** vpn1.example.com
    ==============================================  ====================================================================================================


External DNS Records
--------------------

Your OPNsense Firewall has the example IP Subnets ``203.0.113.0/24`` and ``2001:db8:1234::/48``. The FQDN can point to any bindable IPv4 and IPv6 address in those subnets. It will be used by clients to connect to the IPsec VPN Server - and by the OPNsense to bind the local listen address.

- Create an A-Record with your external DNS provider, for example ``vpn1.example.com in A 203.0.113.1``
- Create an AAAA-Record, for example ``vpn1.example.com in AAAA 2001:db8:1234::1``


Firewall: Aliases
-----------------

Create an alias for the IP addresses of your FQDN. That way you can create a combined IPv4/IPv6 rule to allow incoming connections to your IPsec VPN server.

    ==============================================  ====================================================================================================
    **Name:**                                       ``host_vpn1_example_com``
    **Type:**                                       Host(s)
    **Content:**                                    ``203.0.113.1`` ``2001:db8:1234::1``
    **Description:**                                Host vpn1.example.com
    ==============================================  ====================================================================================================

Create an alias for the UDP ports used by IPsec. Port 500 is ISAKMP and port 4500 is IPsec NAT-T.
    
    ==============================================  ====================================================================================================
    **Name:**                                       ``port_ipsec_500_4500``
    **Type:**                                       Port(s)
    **Content:**                                    ``500`` ``4500``
    **Description:**                                Ports IPsec 500 and 4500
    ==============================================  ====================================================================================================

    
Firewall: Rules: WAN
--------------------

Since this roadwarrior configuration will use UDP encapsulation, the ESP packets will be encapsulated inside UDP packets. That's why you don't need a rule to allow the ESP protocol. You only need a firewall rule to allow UDP 500 and UDP 4500. Use the aliases you created in the prior step.

    ==============================================  ====================================================================================================
    **Action**                                      Pass
    **Interface**                                   WAN
    **Direction**                                   In
    **TCP/IP Version**                              IPv4+IPv6
    **Protocol**                                    UDP
    **Source**                                      Any
    **Source port**                                 Any
    **Destination**                                 ``host_vpn1_example_com``
    **Destination port**                            ``port_ipsec_500_4500``
    **Description**                                 Allow IPsec UDP ports from ANY source to this firewall 
    ==============================================  ====================================================================================================

    
Update your Firewall
--------------------

Update your OPNsense at least to Version 23.7.4, that's the version that introduced ``EAP id: %any`` which is used in Method 1. If you stay on a lower Version, you can only configure Method 2.


.. Note::
    - Now that the Prerequisites have been met, you can choose where to continue:
    - :ref:`Method 1 - Shared IP pool for all roadwarriors <rw-swanctl-method1>`
    - :ref:`Method 2 - Static IP address per roadwarrior <rw-swanctl-method2>`

.. Attention::
    - Don't create both methods on your OPNsense at the same time, it's a potential security risk.
    - Only create **one connection** where you use ``EAP id: %any`` (Method 1). If you create multiple connections with ``EAP id: %any``, any roadwarrior can connect to any of them.


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

--------------------------------------------
Method 2 - Static IP address per roadwarrior
--------------------------------------------


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

