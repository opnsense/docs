=======================================
IPsec - Roadwarriors IKEv2 EAP-MSCHAPv2
=======================================

.. contents:: Index

The following roadwarrior configuration is universally usable for many different clients and easy to setup.

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
    Any IPv6 functionality is optional. If you don't want to use IPv4+IPv6 dual stack, just skip all IPv6 addresses/networks and focus on IPv4.

.. Note::
    - IPv6 transport with UDP encapsulation of ESP packets is supported by OPNsense 24.7 with the FreeBSD 14 kernel.
    - When using OPNsense 24.1 or below it is currently not possible to use IPv6 as outer tunnel transport address. IPsec requires UDP encapsulation of ESP packets for most mobile clients. UDP encapsulation and decapsulation for IPv6 is unsupported by the FreeBSD 13 Kernel.

.. Warning::
    - Don't copy security relevant configuration parameters like passwords into your configuration. Create your own! 
    - Change all IP addresses, usernames and DNS Records to your own usecase.

-----------------------------
Methods for Roadwarrior Setup
-----------------------------

:ref:`Method 1 - Shared IP pool for all roadwarriors <rw-swanctl-method1>`
--------------------------------------------------------------------------

- **Benefit:** Easy configuration and works with most clients out of the box.
- **Drawback:** All configured EAP Identities can authenticate with this connection, so you can't have tight access control. Roadwarriors don't have unique IP addresses.


:ref:`Method 2 - Static IP address per roadwarrior <rw-swanctl-method2>`
------------------------------------------------------------------------

- **Benefit:** Tight security because every user can be controlled individually with firewall rules.
- **Drawback:** Configuration needs more time and might not scale with large user counts. Windows native VPN client doesn't like this configuration since it demands the eap identity exchange method ``eap id = %any``.


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

Download this CA certificate and save it for later, it's needed for client setup.
    

System: Trust: Certificates
---------------------------

Create a server certificate for your IPsec VPN. The lifetime of the certificate is 1 year, if it expires you have to renew the certificate on the OPNsense or your clients can't connect anymore.

    ==============================================  ====================================================================================================
    **Method:**                                     Create an internal Certificate
    **Descriptive name:**                           vpn1.example.com
    **Certificate authority:**                      IPsec CA
    **Type:**                                       Server Certificate
    **Key Type:**                                   RSA
    **Key length (bits):**                          2048
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
    - Only create **one connection** where you use ``EAP id: %any`` (Method 1). If you create multiples of these connections, any roadwarrior can connect to any of them.


.. _rw-swanctl-method1:

----------------------------------------------
Method 1 - Shared IP pool for all roadwarriors
----------------------------------------------


1.1 - VPN: IPsec: Connections: Pools
------------------------------------

Create an IPv4 pool that all roadwarriors will share. This configuration will result in 256 usable IPv4 addresses. Please note that this is not a network, it's a pool of IP addresses that will be leased. The DNS Server(s) will be pushed as *Configuration Payload* (RFC4306 and RFC7296 3.15). In this example they represent the Unbound Server of the OPNsense.

    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-ipv4
    **Network:**                                    ``172.16.203.0/24``
    **DNS:**                                        ``192.168.1.1``
    ==============================================  ====================================================================================================

Create an IPv6 pool that all roadwarriors will share. This configuration will result in 256 usable IPv6 addresses.
    
    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-ipv6
    **Network:**                                    ``2001:db8:1234:ec::/120``
    **DNS:**                                        ``2001:db8:1234:1::1``
    ==============================================  ====================================================================================================

.. Note::
    The IPv6 pool is not a /64 Prefix, because it's used to define a pool of IPv6 addresses that can be used as leases. Prefix /120 means there are 256 IPv6 addresses available. The hard limit of StrongSwan pools is Prefix /97.

.. Note::
    You can skip the DNS field if you don't want to push DNS Servers to your clients.

1.2 - VPN: IPsec: Pre-Shared Keys
---------------------------------

Create EAP Pre-Shared Keys. The local identifier is the username, and the Pre-Shared Key is the password for the VPN connection.

    ==============================================  ====================================================================================================
    **Local Identifier:**                           ``john@vpn1.example.com``
    **Pre-Shared Key:**                             ``48o72g3h4ro8123g8r``
    **Type:**                                       EAP
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Local Identifier:**                           ``laura@vpn1.example.com``
    **Pre-Shared Key:**                             ``LIUAHSDq2nak!12``
    **Type:**                                       EAP
    ==============================================  ====================================================================================================

.. Note::
    Instead of ``john@vpn1.example.com`` you can use any string as local identifier, for example only ``john``. If you have multiple VPN servers, the FQDN makes it easier to know which one the user is assigned to.
    
1.3 - VPN: IPsec: Connections
-----------------------------

- Enable IPsec with the checkbox at the bottom right and apply.
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

Press **+** to add a new Child, enable **advanced mode** with the toggle.

    ==============================================  ====================================================================================================
    **Start action:**                               Trap
    **ESP proposals:**                              aes256-sha256-modp2048  (Disable default!)
    **Local:**                                      ``0.0.0.0/0`` ``::/0``
    **Rekey time (s):**                             600
    **Description:**                                roadwarrior-eap-mschapv2-p2
    ==============================================  ====================================================================================================

**Save** and **Apply** the configuration.

.. Note::
    With children you select the networks your roadwarrior should be able to access. In a split tunnel scenario, you would specify the example LAN nets ``192.168.1.0/24`` and  ``2001:db8:1234:1::/64`` as local traffic selectors. In a full tunnel scenario (all traffic forced through the tunnel) you would specify ``0.0.0.0/0`` and ``::/0`` as local traffic selectors. The following example child will use the full tunnel method. A full tunnel is generally more secure - especially with IPv6 involved - since no traffic can leak.


Now you can skip to :ref:`Firewall rules, Outbound NAT and DNS <rw-swanctl-fw-nat-dns>`

.. _rw-swanctl-method2:

--------------------------------------------
Method 2 - Static IP address per roadwarrior
--------------------------------------------


2.1 - VPN: IPsec: Connections: Pools
------------------------------------

Create an individual IPv4 pool for each roadwarrior. This configuration will result in 1 usable IPv4 address. The DNS Server(s) will be pushed as *Configuration Payload* (RFC4306 and RFC7296 3.15). In this example they represent the Unbound Server of the OPNsense.

    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-john-ipv4
    **Network:**                                    ``172.16.203.1/32``
    **DNS:**                                        ``192.168.1.1``
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-laura-ipv4
    **Network:**                                    ``172.16.203.2/32``
    **DNS:**                                        ``192.168.1.1``
    ==============================================  ====================================================================================================

Create an individual IPv6 pool for each roadwarrior. This configuration will result in 1 usable IPv6 address.
    
    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-john-ipv6
    **Network:**                                    ``2001:db8:1234:ec::1/128``
    **DNS:**                                        ``2001:db8:1234:1::1``
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Name:**                                       pool-roadwarrior-laura-ipv6
    **Network:**                                    ``2001:db8:1234:ec::2/128``
    **DNS:**                                        ``2001:db8:1234:1::1``
    ==============================================  ====================================================================================================

.. Note::
    If a roadwarrior has more than one device, you can provide them a larger pool. For example /31 would result in 2 IPv4 addresses, and /127 in 2 IPv6 addresses. You will have to keep track of this yourself though, don't configure pools that overlap.

.. Note::
    You can skip the DNS field if you don't want to push DNS Servers to your clients.

2.2 - VPN: IPsec: Pre-Shared Keys
---------------------------------

Create EAP Pre-Shared Keys. The local identifier is the username, and the Pre-Shared Key is the password for the VPN connection.

    ==============================================  ====================================================================================================
    **Local Identifier:**                           ``john@vpn1.example.com``
    **Pre-Shared Key:**                             ``48o72g3h4ro8123g8r``
    **Type:**                                       EAP
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Local Identifier:**                           ``laura@vpn1.example.com``
    **Pre-Shared Key:**                             ``LIUAHSDq2nak!12``
    **Type:**                                       EAP
    ==============================================  ====================================================================================================

.. Note::
    Instead of ``john@vpn1.example.com`` you can use any string as local identifier, for example only ``john``. If you have multiple VPN servers, the FQDN makes it easier to know which one the user is assigned to.


2.3 - VPN: IPsec: Connections
-----------------------------

- Enable IPsec with the checkbox at the bottom right and apply.

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

Press **+** to add a new Child, enable **advanced mode** with the toggle.

    ==============================================  ====================================================================================================
    **Start action:**                               Trap
    **ESP proposals:**                              aes256-sha256-modp2048  (Disable default!)
    **Local:**                                      ``0.0.0.0/0`` ``::/0``
    **Rekey time (s):**                             600
    **Description:**                                roadwarrior-john-eap-mschapv2-p2
    ==============================================  ====================================================================================================

**Save** and **Apply** the configuration.

.. Note::
    With children you select the networks your roadwarrior should be able to access. In a split tunnel scenario, you would specify the example LAN nets ``192.168.1.0/24`` and  ``2001:db8:1234:1::/64`` as local traffic selectors. In a full tunnel scenario (all traffic forced through the tunnel) you would specify ``0.0.0.0/0`` and ``::/0`` as local traffic selectors. The following example child will use the full tunnel method. A full tunnel is generally more secure - especially with IPv6 involved - since no traffic can leak.


**2.3.2 Create connection for laura@vpn1.example.com:**

- Press **+** to add a new Connection, enable **advanced mode** with the toggle. You could also **clone** the connection you already configured.

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

Now that you have configured split or full tunnel mode, you need rules to allow the traffic into your LAN and to the WAN (Internet). For IPv4 connection to the WAN (Internet) you need an Outbound NAT rule for IP-Masquerading. If you want the OPNsense to handle DNS, you can to configure Unbound so your roadwarriors use it as DNS server to prevent DNS leaks.

.. Tip::
    If you have internal IPv4 services (like a mailserver) that have external IPs in their DNS A-Records, you should configure Reflection NAT. There is a tutorial in the How-To section of Network Address Translation. If you follow it, add the ``ipsec`` interface in the Port Forward rules you create.

Firewall: Aliases
-----------------

Create the following aliases:

    ==============================================  ====================================================================================================
    **Name:**                                       ``InternetIPv4``
    **Type:**                                       Network(s)
    **Content:**                                    ``10.0.0.0/8``  ``172.16.0.0/12``  ``192.168.0.0/16``  ``127.0.0.0/8``
    **Description:**                                Internet IPv4 - use inverted
    ==============================================  ====================================================================================================

    .. Note::
        The ``InternetIPv6`` alias needs to be your own IPv6 network.
    
    ==============================================  ====================================================================================================
    **Name:**                                       ``InternetIPv6``
    **Type:**                                       Network(s)
    **Content:**                                    ``2001:db8:1234::/48``
    **Description:**                                Internet IPv6 - use inverted
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Name:**                                       ``net_pool_roadwarrior``
    **Type:**                                       Network(s)
    **Content:**                                    ``172.16.203.0/24``  ``2001:db8:1234:ec::/64``
    **Description:**                                Network pool-roadwarrior-ipv4 and ipv6
    ==============================================  ====================================================================================================


Additionally, if you created seperate IP pools for individual roadwarriors (Method 2), create the following aliases so you are able to create individual firewall rules per roadwarrior:

    ==============================================  ====================================================================================================
    **Name:**                                       ``host_pool_roadwarrior_john``
    **Type:**                                       Host(s)
    **Content:**                                    ``172.16.203.1/32``  ``2001:db8:1234:ec::1/128``
    **Description:**                                ``john@vpn1.example.com``
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Name:**                                       ``host_pool_roadwarrior_laura``
    **Type:**                                       Host(s)
    **Content:**                                    ``172.16.203.2/32``  ``2001:db8:1234:ec::2/128``
    **Description:**                                ``laura@vpn1.example.com``
    ==============================================  ====================================================================================================


Firewall: Rules: IPsec
----------------------

Here you use the aliases you created in the prior step in order to create firewall rules on the ``IPsec`` interface in order to allow traffic from the roadwarrior networks to your LAN and to the WAN (Internet).

As **first** rule it's a good idea to allow ICMP for troubleshooting purposes. With that rule, roadwarriors can ping the OPNsense firewall. Please note that they can only ping those IPs that are included in the local traffic selectors of the children.

    ==============================================  ====================================================================================================
    **Action**                                      Pass
    **Interface**                                   IPsec
    **Direction**                                   In
    **TCP/IP Version**                              IPv4+IPv6
    **Protocol**                                    ICMP
    **Source**                                      Any
    **Source port**                                 Any
    **Destination**                                 ``This Firewall``
    **Destination port**                            Any
    **Description**                                 Allow ICMP to this firewall 
    ==============================================  ====================================================================================================

As **second** rule, you should allow LAN access from the IPsec roadwarrior networks. If you created individual aliases, you can create multiples of those rules with the aliases of the individuals added instead of the whole network.

- Example for a rule that allows the whole IPsec roadwarrior network to the LAN. ``LAN net`` is a predefined alias if you have an interface called LAN:

    ==============================================  ====================================================================================================
    **Action**                                      Pass
    **Interface**                                   IPsec
    **Direction**                                   In
    **TCP/IP Version**                              IPv4+IPv6
    **Protocol**                                    TCP/UDP
    **Source**                                      ``net_pool_roadwarrior``
    **Source port**                                 Any
    **Destination**                                 ``LAN net``
    **Destination port**                            Any
    **Description**                                 Allow ICMP to this firewall 
    ==============================================  ====================================================================================================
    
- Example for an individual allow rule to the LAN:

    ==============================================  ====================================================================================================
    **Action**                                      Pass
    **Interface**                                   IPsec
    **Direction**                                   In
    **TCP/IP Version**                              IPv4+IPv6
    **Protocol**                                    TCP/UDP
    **Source**                                      ``host_pool_roadwarrior_john``
    **Source port**                                 Any
    **Destination**                                 ``LAN net``
    **Destination port**                            Any
    **Description**                                 Allow ``john@vpn1.example.com`` access to LAN net
    ==============================================  ====================================================================================================

The **last matching** rules can allow Internet access if you have configured a full tunnel. Just as the example above, you can also create individual rules to restrict Internet access to some roadwarriors:

    ==============================================  ====================================================================================================
    **Action**                                      Pass
    **Interface**                                   IPsec
    **Direction**                                   In
    **TCP/IP Version**                              IPv4
    **Protocol**                                    Any
    **Source**                                      ``net_pool_roadwarrior``
    **Source port**                                 Any
    **Destination / Invert**                        X
    **Destination**                                 ``InternetIPv4``
    **Destination port**                            Any
    **Description**                                 Allow Internet Access IPv4
    ==============================================  ====================================================================================================
    
    ==============================================  ====================================================================================================
    **Action**                                      Pass
    **Interface**                                   IPsec
    **Direction**                                   In
    **TCP/IP Version**                              IPv6
    **Protocol**                                    Any
    **Source**                                      ``net_pool_roadwarrior``
    **Source port**                                 Any
    **Destination / Invert**                        X
    **Destination**                                 ``InternetIPv6``
    **Destination port**                            Any
    **Description**                                 Allow Internet Access IPv6
    ==============================================  ====================================================================================================

.. Note::
    By setting **Destination / Invert** you invert the match of the alias. Don't use "Any" as Destination to the Internet, since it also includes all networks that are locally attached to your firewall.

Firewall: NAT: Outbound
-----------------------

For IPv4 Internet access to work, you need to set up an Outbound NAT rule for IP-Masquerading. Start by enabling at least **Hybrid outbound NAT rule generation** and **Save**. Otherwise you can't add your new manual NAT rule.

    ==============================================  ====================================================================================================
    **Interface**                                   WAN
    **Direction**                                   In
    **TCP/IP Version**                              IPv4
    **Protocol**                                    any
    **Source**                                      ``net_pool_roadwarrior``
    **Source port**                                 any
    **Destination**                                 any
    **Destination port**                            any
    **Translation / target**                        ``WAN address``
    **Description**                                 IPsec MASQ
    ==============================================  ====================================================================================================


Services: Unbound DNS
---------------------

.. Note::
    If you don't serve internal DNS records (Split DNS) or don't have an Active Directory you can skip the DNS configuration.


For full control over DNS, you should either use Unbound on the OPNsense or the DNS servers in your own network. If you provide your roadwarriors with external DNS servers (like ``8.8.8.8``), they can't resolve your internal ressources and will send those requests to external DNS servers, thus exposing your internal DNS records. (DNS Leak)

.. Attention::
    If you created a full tunnel for IPv4 only (``0.0.0.0/0`` without ``::/0``), and your roadwarriors are in IPv4+IPv6 dual stack networks, their devices will prefer the link local IPv6 DNS servers provided by SLAAC or DHCPv6 over your IPv4 VPN DNS server.

**Enable** Unbound and leave the *Network Interfaces* on *All (recommended)*. Next go to *Query Forwarding* and input your *Custom forwarding* servers. For example your Samba or Microsoft Active Directory Domain Controllers.

Unbound listens on port 53 UDP/TCP on all network interfaces of the OPNsense. If you followed all prior steps, access to your LAN is already permitted from the IPsec Network. You can use the IP addresses of the OPNsense in that network as target for the DNS queries.

In this example they are: ``192.168.1.1`` and ``2001:db8:1234:1::1``.

--------------------
Client configuration
--------------------

In this section there are a few example configurations of different clients. All configurations here are tuned to the exact settings above. If you change anything in the server configuration, make sure you change it here too.

All clients are configured to use the *Configuration Payload* for virtual IP address, traffic selectors and DNS Server(s). They are pushed by the VPN server to the client.

.. Note::
    Import the CA certificate to clients, not the server certificate.


Windows 10/11 native VPN client
-------------------------------

.. Note::
    - Windows 10/11 native VPN client works best with Method 1, which connects right away on the first authentication round. 
    - If you use Method 2 you should rather use the NCP client. The Windows VPN client doesn't send it's local ID on the first authentication round. That means that users have to type their passwords twice before the connection establishes. You can mitigate one authentication round by saving the username and password into the vpn profile. Attention: If they press cancel or click outside of the authentication window, it will vanish and trying to connect again will fail until the PC is rebooted!

- Open Powershell as user (for userspace import) or as admin (for computer wide import) and apply the following commands:

.. code-block::
    
    Add-VpnConnection -Name "vpn1.example.com" -ServerAddress "vpn1.example.com" -TunnelType "Ikev2"

    Set-VpnConnectionIPsecConfiguration -ConnectionName "vpn1.example.com" -AuthenticationTransformConstants SHA256 -CipherTransformConstants AES256 -EncryptionMethod AES256 -IntegrityCheckMethod SHA256 -PfsGroup PFS2048 -DHGroup Group14 -PassThru -Force


- Only set this parameter if you want a split tunnel:

.. code-block::
    
    Set-VpnConnection -Name "vpn1.example.com" -SplitTunneling $true

.. Note::
    If you use Split Tunneling, you have to set all routes manually. For users without admin rights, they have to be added to the "Network Configuration Operators" built-in group.
    Example Route (can be batched): ``route add 192.168.1.0 mask 255.255.255.0 172.16.203.254``

- Import the CA certificate into the Windows certificate store, please note that you have to be admin for this action:

    - Open MMC: Windows + R > Type mmc > Enter.
    - Add Certificates Snap-In: File > Add/Remove Snap-in > Certificates > Add > Computer account > Local computer > Finish.
    - Install Certificate: Go to Trusted Root Certification Authorities > Certificates > Right-click > All Tasks > Import > Select your CA certificate > Ensure it's set to Trusted - Root Certification Authorities > Finish.
    - Confirm: Check the certificate appears under Trusted Root Certification Authorities.
    - Close MMC. Choose 'No' if asked to save console settings.

- Connect the new VPN connection and use the following credentials, you can also save them prior to connecting:

    - Username: ``john@vpn1.example.com``
    - Password: ``48o72g3h4ro8123g8r``
    
**Optional** if DNS Server provisioning via *Configuration Payload* doesn't work:
- Set up DNS for the VPN:
    
    - Open Network Connections: Windows + R > Type ncpa.cpl > Enter.
    - Locate VPN adapter (e.g. "vpn1.example.com").
    - Right-click VPN adapter > Properties.
    - For IPv4:
    
        - Select Internet Protocol Version 4 (TCP/IPv4) > Properties.
        - Set DNS: ``192.168.1.1``
    - For IPv6:
    
        - Select Internet Protocol Version 6 (TCP/IPv6) > Properties.
        - Set DNS: ``2001:db8:1234:1::1``
    - Click OK to apply changes.


iOS native VPN client
---------------------

- Import the self-signed CA certificate into the iOS certificate store.
- Go to Settings > General > VPN.
- Tap on Add VPN Configuration....
- Select the type of VPN you are using. For this example, it's IKEv2.
- In the fields provided, enter:
    
    - Description: ``vpn1.example.com``
    - Server: ``vpn1.example.com``
    - Remote ID: ``vpn1.example.com``
    - Local ID: ``john@vpn1.example.com``
- In the Authentication section, select Username.
    
    - Username: ``john@vpn1.example.com``
    - Password: ``48o72g3h4ro8123g8r``
- Tap Done in the top right corner.
- To connect to the VPN, go back to Settings > VPN, then turn the VPN toggle switch to the ON position next to the profile you just created.

.. Note::
    iOS doesn't allow setting a DNS Server for the VPN, and it ignores the DNS *Configuration Payload*. The only workaround would be to change the DNS Server manually in the Wi-Fi settings each time the tunnel is brought up, and change them back when it's turned off.


Android StrongSwan VPN client
-----------------------------

- Import the self-signed CA certificate into the Android certificate store.
- Install the StrongSwan app from the Google Play Store
- Open the StrongSwan app and create a new VPN profile.
    
    - Server: ``vpn1.example.com``
    - VPN Typ: IKEv2 EAP
    - Username: ``john@vpn1.example.com``
    - Password: ``48o72g3h4ro8123g8r``
    - CA-Certificate: choose the imported CA certificate
    - Activate advanced mode:
    - IKEv2 Algorithms: aes256-sha256-modp2048
    - IPsec/ESP Algorithms: aes256-sha256-modp2048

- You can start the new profile and it should connect. If not, check the Logfile for the error message.

Windows/macOS NCP Secure Entry client
-------------------------------------

.. Attention::
    This is a commercial client and needs to be licensed. It is not affiliated with Deciso B.V. or OPNsense®.

- Install the NCP Secure Entry Client
- Save the following code as **example.ini**

.. code-block::
    
    [GENERAL]
    Export=1
    Product=NCP Secure Entry Client
    Version=13.14 Build 29669
    Date=11.09.2023 09:30:42
    [PROFILE1]
    Name=vpn1.example.com
    ConnMedia=21
    UseForAuto=0
    SeamRoaming=1
    NotKeepVpn=0
    BootProfile=0
    UseRAS=0
    SavePw=0
    PhoneNumber=
    DialerPhone=
    ScriptFile=
    HttpName=
    HttpPw=
    HttpScript=
    Modem=
    ComPort=1
    Baudrate=57600
    RelComPort=1
    InitStr=
    DialPrefix=
    3GApnSrc=2
    3GProvider=
    APN=
    3GPhone=
    3GAuth=0
    GprsATCmd=AT+CPIN=
    GprsPin=""
    BiometricAuth=0
    PreAuthEap=0
    PreAuthHttp=0
    ConnMode=0
    Timeout=0
    TunnelTrafficMonitoring=0
    TunnelTrafficMonitoringAddr=0.0.0.0
    QoS=none
    PkiConfig=
    ExchMode=34
    TunnelIpVersion=1
    IKEv2Auth=3
    IKE-Policy=automatic mode
    IKEv2Policy=aes256-sha256
    IkeDhGroup=14
    IkeLTSec=000:00:40:00
    IPSec-Policy=aes256-sha256
    PFS=14
    IPSecLTType=1
    IpsecLTSec=000:00:10:00
    IPSecLTKb=50000
    UseComp=0
    IkeIdType=3
    IkeIdStr=john@vpn1.example.com
    Gateway=vpn1.example.com
    ConnType=1
    UsePreShKey=0
    XAUTH-Src=0
    SplitOptionV4=1
    UseTunnel=1
    SplitOptionV6=1
    VpnBypass=none
    UseXAUTH=1
    UseUdpEnc=500
    UseUdpEncTmp=4500
    DisDPD=0
    DPDInterval=30
    DPDRetrys=8
    AntiReplay=0
    PathFinder=0
    UseRFC7427=1
    RFC7427Padding=2
    Ikev2AuthPrf=0
    CertReqWithData=0
    IpAddrAssign=0
    IPAddress=
    SubnetMask=
    DNS1=
    DNS2=
    DomainName=
    DomainInTunnel=
    SubjectCert=
    IssuerCert=
    FingerPrint=
    UseSHA1=0
    Firewall=0
    OnlyTunnel=0
    RasOnlyTunnel=0
    DNSActiv=1
    DNS1Tmp=
    DNS2Tmp=
    [IKEV2POLICY1]
    Ikev2Name=aes256-sha256
    Ikev2Crypt=6
    Ikev2PRF=5
    Ikev2IntAlgo=12
    [IPSECPOLICY1]
    IPSecName=aes256-sha256
    IpsecCrypt=6
    IpsecAuth=5

- For other users edit ``IkeIdStr=john@vpn1.example.com``. Change ``Name=vpn1.example.com`` and ``Gateway=vpn1.example.com`` to your vpn gateway.
- Import the example.ini Profile:
    
    - Launch the NCP Secure Entry Client.
    - Navigate to the Profile menu.
    - Select the option to Import Profile.
    - Browse to the location where your example.ini profile is saved.
    - Select the profile and click Open or Import (whichever option appears).
    - You can enter the username and password of the user when importing the profile.
    
        - Username: ``john@vpn1.example.com``
        - Password: ``48o72g3h4ro8123g8r``
- Import the self-signed CA certificate into the NCP certificate store. Go to ``C:\ProgramData\NCP\SecureClient\cacerts`` and copy your the .pem file in there.
- The profile should now be loaded into the NCP Secure Entry Client. You can start it and it should connect. If not, check the Logfile in "Help" for the error message.

.. Note::
    There is also a version for macOS, which works with the same configuration as above. The only challenge is finding the right folder for the *cacerts*. You can find it by going into the *terminal* and using the command ``sudo find / -name cacerts``. Then you can pinpoint the path and copy the CA certificates there.


---------------
Troubleshooting
---------------

If the VPN connection doesn't establish right away there are several steps you can take to troubleshoot the connection. Here's a short summary where to start. Debugging an IPsec connection takes time, don't get discouraged if you can't solve the problem right away.

- If it's your first IPsec connection, don't forget to enable IPsec and apply.
- Use tcpdump on the OPNsense to look for incoming packets on port 500 and port 4500 when you connect your VPN client. If you can't see any, your firewall blocks them, or the remote client can't send them due to a remote firewall. There could also be a wrong IP Address the packets are sent to.
- If there are packets received, but no packets sent, look into the VPN log files.
- Check /var/logs/ipsec/latest.log or :menuselection:`VPN --> IPsec --> Log File` for the connection being processed. Most of the time you can see errors in there you can search on the internet.
- The easiest tool to troubleshoot the connection is the Android StrongSwan Client or the Windows NCP Secure Entry Client. They have powerful inbuild logging so you can check both sides of the connection. In IPsec, you need the log of the server and the client to find the true cause of a connection error.
