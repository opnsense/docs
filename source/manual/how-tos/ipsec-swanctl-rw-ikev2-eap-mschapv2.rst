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

.. Warning::
    Don't copy security relevant configuration parameters like passwords into your configuration. Create your own!

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

.. Attention::
    In all following examples, parameters that should be empty or at default are **omitted**. *Don't change them without a good reason.*

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

Create a server certificate for your IPsec VPN. The lifetime of the certificate is 1 year, if it expires you have to renew the certificate on the OPNsense or your clients can't connect anymore.

    ==============================================  ====================================================================================================
    **Method:**                                     Create an internal Certificate
    **Descriptive name:**                           vpn1.example.com
    **Certificate authority:**                      IPsec CA
    **Type:**                                       Server Certificate
    **Key Type:**                                   RSA
    **Key lenght (bits):**                          2048
    **Digest Algorithm:**                           SHA256
    **Lifetime (days):**                            365
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

Create an IPv4 pool that all roadwarriors will share. This configuration will result in 256 usable IPv4 addresses. Please note that this is not a network, it's a pool of IP addresses that will be leased.

    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-ipv4
    **Network:**                                    172.16.203.0/24
    ==============================================  ====================================================================================================

Create an IPv6 pool that all roadwarriors will share. This configuration will result in 256 usable IPv6 addresses.
    
    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-ipv6
    **Network:**                                    2001:db8:1234:ec::/120
    ==============================================  ====================================================================================================

.. Note::
    The IPv6 pool is not a /64 Prefix, because it's used to define a pool of IPv6 addresses that can be used as leases. Prefix /120 means there are 256 IPv6 addresses available. The hard limit of strongswan pools is Prefix /97.


1.2 - VPN: IPsec: Pre-Shared Keys
---------------------------------

Create EAP Pre-Shared Keys. The local identifier is the username, and the Pre-Shared Key is the password for the VPN connection.

    ==============================================  ====================================================================================================
    **Local Identifier:**                           ``john@vpn1.example.com``
    **Pre-Shared Key:**                             48o72g3h4ro8123g8r
    **Type:**                                       EAP
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Local Identifier:**                           ``laura@vpn1.example.com``
    **Pre-Shared Key:**                             LIUAHSDq2nak!12
    **Type:**                                       EAP
    ==============================================  ====================================================================================================

.. Note::
    Instead of ``john@vpn1.example.com`` you can use any string as local identifier, for example only ``john``. If you have multiple VPN servers, the FQDN makes it easier to know which one the user is assigned to.
    
1.3 - VPN: IPsec: Connections
-----------------------------

- Enable IPsec with the checkbox at the bottom left and apply. If you forget to do this nothing will work.

- Press **+** to add a new Connection, enable **advanced mode** with the toggle.

**General Settings:**

    ==============================================  ====================================================================================================
    **Proposals:**                                  aes256-sha256-modp2048   (Disable default!)
    **Version:**                                    IKEv2
    **Local addresses:**                            ``vpn1.example.com``
    **UDP encapsulation:**                          X
    **Rekey time:**                                 2400
    **DPD delay:**                                  30
    **Pools:**                                      ``pool-roadwarrior-ipv4`` ``pool-roadwarrior-ipv6``
    **Keyingtries:**                                0
    **Description:**                                roadwarrior-eap-mschapv2-p1
    ==============================================  ====================================================================================================

**Save** to reveal the next options:

**Local Authentication:**

    ==============================================  ====================================================================================================
    **Round:**                                      0
    **Authentication:**                             Public Key
    **Id:**                                         vpn1.example.com
    **Certificates:**                               vpn1.example.com
    **Description:**                                local-vpn1.example.com
    ==============================================  ====================================================================================================

**Remote Authentication:**

    ==============================================  ====================================================================================================
    **Round:**                                      0
    **Authentication:**                             EAP-MSCHAPv2
    **EAP Id:**                                     ``%any``
    **Description:**                                remote-eap-mschapv2
    ==============================================  ====================================================================================================

**Children:**

.. Note::
    This is where you select the networks your roadwarrior should be able to access. In a split tunnel scenario, you would specify the example LAN nets ``192.168.1.0/24`` and  ``2001:db8:1234:1::/64`` as local traffic selectors. In a full tunnel scenario (all traffic forced through the tunnel) you would specify ``0.0.0.0/0`` and ``::/0`` as local traffic selectors. The following example child will use the full tunnel method. A full tunnel is generally more secure - especially with IPv6 involved - since no traffic can leak.

Press **+** to add a new Child, enable **advanced mode** with the toggle.

    ==============================================  ====================================================================================================
    **Start action:**                               Trap
    **ESP proposals:**                              aes256-sha256-modp2048  (Disable default!)
    **Local:**                                      ``0.0.0.0/0`` ``::/0``
    **Rekey time (s):**                             600
    **Description:**                                roadwarrior-eap-mschapv2-p2
    ==============================================  ====================================================================================================

**Save** and **Apply** the configuration.

Now you can skip to :ref:`Firewall rules, Outbound NAT and DNS <rw-swanctl-fw-nat-dns>`

.. _rw-swanctl-method2:

--------------------------------------------
Method 2 - Static IP address per roadwarrior
--------------------------------------------


2.1 - VPN: IPsec: Connections: Pools
------------------------------------

Create an individual IPv4 pool for each roadwarrior. This configuration will result in 1 usable IPv4 address.

    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-john-ipv4
    **Network:**                                    172.16.203.1/32
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-laura-ipv4
    **Network:**                                    172.16.203.2/32
    ==============================================  ====================================================================================================

Create an individual IPv6 pool for each roadwarrior. This configuration will result in 1 usable IPv6 address.
    
    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-john-ipv6
    **Network:**                                    2001:db8:1234:ec::1/128
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-laura-ipv6
    **Network:**                                    2001:db8:1234:ec::2/128
    ==============================================  ====================================================================================================

.. Note::
    If a roadwarrior has more than one device, you can provide them a larger pool. For example /31 would result in 2 IPv4 addresses, and /127 in 2 IPv6 addresses. You will have to keep track of this yourself though, don't configure pools that overlap.


2.2 - VPN: IPsec: Pre-Shared Keys
---------------------------------

Create EAP Pre-Shared Keys. The local identifier is the username, and the Pre-Shared Key is the password for the VPN connection.

    ==============================================  ====================================================================================================
    **Local Identifier:**                           ``john@vpn1.example.com``
    **Pre-Shared Key:**                             48o72g3h4ro8123g8r
    **Type:**                                       EAP
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Local Identifier:**                           ``laura@vpn1.example.com``
    **Pre-Shared Key:**                             LIUAHSDq2nak!12
    **Type:**                                       EAP
    ==============================================  ====================================================================================================

.. Note::
    Instead of ``john@vpn1.example.com`` you can use any string as local identifier, for example only ``john``. If you have multiple VPN servers, the FQDN makes it easier to know which one the user is assigned to.


2.3 - VPN: IPsec: Connections
-----------------------------

- Enable IPsec with the checkbox at the bottom left and apply. If you forget to do this nothing will work.

**2.3.1 Create connection for john@vpn1.example.com:**

- Press **+** to add a new Connection, enable **advanced mode** with the toggle.

**General Settings:**

    ==============================================  ====================================================================================================
    **Proposals:**                                  aes256-sha256-modp2048  (Disable default!)
    **Version:**                                    IKEv2
    **Local addresses:**                            ``vpn1.example.com``
    **UDP encapsulation:**                          X
    **Rekey time:**                                 2400
    **DPD delay:**                                  30
    **Pools:**                                      ``pool-roadwarrior-john-ipv4`` ``pool-roadwarrior-john-ipv6``
    **Keyingtries:**                                0
    **Description:**                                roadwarrior-john-eap-mschapv2-p1
    ==============================================  ====================================================================================================

**Save** to reveal the next options:

**Local Authentication:**

    ==============================================  ====================================================================================================
    **Round:**                                      0
    **Authentication:**                             Public Key
    **Id:**                                         vpn1.example.com
    **Certificates:**                               vpn1.example.com
    **Description:**                                local-vpn1.example.com
    ==============================================  ====================================================================================================

**Remote Authentication:**

    ==============================================  ====================================================================================================
    **Round:**                                      0
    **Authentication:**                             EAP-MSCHAPv2
    **EAP Id:**                                     ``john@vpn1.example.com``
    **Description:**                                remote-john-eap-mschapv2
    ==============================================  ====================================================================================================

**Children:**

.. Note::
    This is where you select the networks your roadwarrior should be able to access. In a split tunnel scenario, you would specify the example LAN nets ``192.168.1.0/24`` and  ``2001:db8:1234:1::/64`` as local traffic selectors. In a full tunnel scenario (all traffic forced through the tunnel) you would specify ``0.0.0.0/0`` and ``::/0`` as local traffic selectors. The following example child will use the full tunnel method. A full tunnel is generally more secure - especially with IPv6 involved - since no traffic can leak.

Press **+** to add a new Child, enable **advanced mode** with the toggle.

    ==============================================  ====================================================================================================
    **Start action:**                               Trap
    **ESP proposals:**                              aes256-sha256-modp2048  (Disable default!)
    **Local:**                                      ``0.0.0.0/0`` ``::/0``
    **Rekey time (s):**                             600
    **Description:**                                roadwarrior-john-eap-mschapv2-p2
    ==============================================  ====================================================================================================

**Save** and **Apply** the configuration.


**2.3.2 Create connection for laura@vpn1.example.com:**

- Press **+** to add a new Connection, enable **advanced mode** with the toggle.

**General Settings:**

    ==============================================  ====================================================================================================
    **Proposals:**                                  aes256-sha256-modp2048  (Disable default!)
    **Version:**                                    IKEv2
    **Local addresses:**                            ``vpn1.example.com``
    **UDP encapsulation:**                          X
    **Rekey time:**                                 2400
    **DPD delay:**                                  30
    **Pools:**                                      ``pool-roadwarrior-laura-ipv4`` ``pool-roadwarrior-laura-ipv6``
    **Keyingtries:**                                0
    **Description:**                                roadwarrior-laura-eap-mschapv2-p1
    ==============================================  ====================================================================================================

**Save** to reveal the next options:

**Local Authentication:**

    ==============================================  ====================================================================================================
    **Round:**                                      0
    **Authentication:**                             Public Key
    **Id:**                                         vpn1.example.com
    **Certificates:**                               vpn1.example.com
    **Description:**                                local-vpn1.example.com
    ==============================================  ====================================================================================================

**Remote Authentication:**

    ==============================================  ====================================================================================================
    **Round:**                                      0
    **Authentication:**                             EAP-MSCHAPv2
    **EAP Id:**                                     ``laura@vpn1.example.com``
    **Description:**                                remote-laura-eap-mschapv2
    ==============================================  ====================================================================================================

**Children:**

.. Note::
    This is where you select the networks your roadwarrior should be able to access. In a split tunnel scenario, you would specify the example LAN nets ``192.168.1.0/24`` and  ``2001:db8:1234:1::/64`` as local traffic selectors. In a full tunnel scenario (all traffic forced through the tunnel) you would specify ``0.0.0.0/0`` and ``::/0`` as local traffic selectors. The following example child will use the full tunnel method. A full tunnel is generally more secure - especially with IPv6 involved - since no traffic can leak.

Press **+** to add a new Child, enable **advanced mode** with the toggle.

    ==============================================  ====================================================================================================
    **Start action:**                               Trap
    **ESP proposals:**                              aes256-sha256-modp2048  (Disable default!)
    **Local:**                                      ``0.0.0.0/0`` ``::/0``
    **Rekey time (s):**                             600
    **Description:**                                roadwarrior-laura-eap-mschapv2-p2
    ==============================================  ====================================================================================================

**Save** and **Apply** the configuration.


.. Note::
    You have to repeat this workflow for each additional roadwarrior you create. They all need new pools and new connections.

.. _rw-swanctl-fw-nat-dns:

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

