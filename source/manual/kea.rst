==================
KEA DHCP
==================

.. contents:: Index

Kea is the next generation of DHCP software, developed by Internet Systems Consortium (ISC).

It is considered the replacement for `ISC-DHCP` in larger HA enabled setups
and synergizes well with `radvd` for HA enabled router advertisements.

Currently it is not possible to register hostnames dynamically between KEA and Unbound, only static reservations will be
synchronized on an Unbound service restart.

-------------------------
Control Agent
-------------------------

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

-------------------------
Kea DHCPv4/v6
-------------------------

This is the DHCPv4/v6 service available in KEA, which offers the following tab sheets with their corresponding settings:

.. tabs::

    .. tab:: Settings (DHCPv4/v6)

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **//Service**
        **Enabled**                               Enable DHCPv4/v6 server.
        **Manual config**                         Disable configuration file generation and manage the file
                                                  (/usr/local/etc/kea/kea-dhcp4.conf) or
                                                  (/usr/local/etc/kea/kea-dhcp6.conf) manually.
        **//General settings**
        **Interfaces**                            Select interfaces to listen on.
        **Valid lifetime**                        Defines how long the addresses (leases) given out by the server are valid (in seconds)
        **Firewall rules**                        Automatically add a basic set of firewall rules to allow dhcp traffic, more fine grained
                                                  controls can be offered manually when disabling this option.
        **Socket type** (DHCPv4 only)             Socket type used for DHCP communication.
        **//High Availability**
        **Enabled**                               Enable High availability hook, requires the Control Agent to be enabled as well.
        **This server name**                      The name of this server, should match with one of the entries in the HA peers.
                                                  Leave empty to use this machines hostname
        **Max Unacked clients**                   This specifies the number of clients which send messages to the partner but appear to
                                                  not receive any response. A higher value needs a busier environment in order to consider
                                                  a member down, when set to 0, any network disruption will cause a failover to happen.
        ========================================= ====================================================================================

    .. tab:: Subnets (DHCPv4/v6)

        **DHCPv4**

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Subnet**                                Subnet to use, should be large enough to hold the specified pools and reservations
        **Description**                           You may enter a description here for your reference (not parsed).
        **Pools**                         	      List of pools, one per line in range or subnet format (e.g. 192.168.0.100 - 192.168.0.200 , 192.0.2.64/26)
        **Match client-id**                       By default, KEA uses client-identifiers instead of MAC addresses to locate clients,
                                                  disabling this option changes back to matching on MAC address which is used by most dhcp implementations.
        **//DHCP option data**
        **Auto collect option data**              Automatically update option data for relevant attributes as routers,
                                                  dns servers and ntp servers when applying settings from the gui.
        **Routers (gateway)**                     Default gateways to offer to the clients
        **Static routes**                         Static routes that the client should install in its routing cache, defined as dest-ip1,router-ip1,dest-ip2,router-ip2
        **DNS servers**                           DNS servers to offer to the clients
        **Domain name**                           The domain name to offer to the client, set to this firewall's domain name when left empty
        **Domain search**                         The domain search list to offer to the client
        **NTP servers**                           Specifies a list of IP addresses indicating NTP (RFC 5905) servers available to the client.
        **Time servers**                          Specifies a list of RFC 868 time servers available to the client.
        **Next server**                           Next server IP address
        **TFTP server**                           TFTP server address or FQDN
        **TFTP bootfile name**                    Boot filename to request
        **IPv6-only Preferred (Option 108)**      The number of seconds for which the client should disable DHCPv4. The minimum value is 300 seconds.
        ========================================= ====================================================================================

        **DHCPv6**

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Subnet**                                Subnet to use, should be large enough to hold the specified pools and reservations
        **Interface**                             Select which interface this subnet belongs to
        **Allocator**                             Select allocator method to use when offering leases to clients.
        **PD Allocator**                          Select allocator method to use when offering prefix delegations to clients
        **Description**                           You may enter a description here for your reference (not parsed).
        **Pools**                         	      List of pools, one per line in range or subnet format (e.g. 2001:db8:1::-2001:db8:1::100, 2001:db8:1::/80
        **//DHCP option data**
        **DNS servers**                           DNS servers to offer to the clients
        **Domain search**                         The domain search list to offer to the client
        ========================================= ====================================================================================

    .. tab:: PD Pools (DHCPv6)

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Subnet**                                Subnet this reservation belongs to
        **Prefix**
        **Prefix length**
        **Delegated length**
        **Description**                           You may enter a description here for your reference (not parsed).
        ========================================= ====================================================================================

        .. Attention::

            Currently the delegated prefix will not create an automatic static route in the system routing table.

    .. tab:: Reservations (DHCPv4/v6)

        **DHCPv4**

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Subnet**                                Subnet this reservation belongs to
        **IP address**                            IP address to offer to the client
        **MAC address**                           MAC/Ether address of the client in question
        **Hostname**                              Offer a hostname to the client
        **Description**                           You may enter a description here for your reference (not parsed).
        **//DHCP option data**
        **Auto collect option data**              Automatically update option data for relevant attributes as routers,
                                                  dns servers and ntp servers when applying settings from the gui.
        **Routers (gateway)**                     Default gateways to offer to the clients
        **Static routes**                         Static routes that the client should install in its routing cache, defined as dest-ip1,router-ip1,dest-ip2,router-ip2
        **DNS servers**                           DNS servers to offer to the clients
        **Domain name**                           The domain name to offer to the client, set to this firewall's domain name when left empty
        **Domain search**                         The domain search list to offer to the client
        **NTP servers**                           Specifies a list of IP addresses indicating NTP (RFC 5905) servers available to the client.
        **Time servers**                          Specifies a list of RFC 868 time servers available to the client.
        **Next server**                           Next server IP address
        **TFTP server**                           TFTP server address or FQDN
        **TFTP bootfile name**                    Boot filename to request
        ========================================= ====================================================================================

        **DHCPv6**

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Subnet**                                Subnet this reservation belongs to
        **IP address**                            IP address to offer to the client
        **DUID**                           	      DUID of the client in question
        **Hostname**                              Offer a hostname to the client
        **Domain search**                         The domain search list to offer to the client
        **Description**                           You may enter a description here for your reference (not parsed).
        ========================================= ====================================================================================

    .. tab:: HA Peers (DHCPv4/DHCPv6)

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Name**                                  Peer name, there should be one entry matching this machines "This server name"
        **Role**                                  This peers role
        **Url**                           	      This specifies the URL of our server instance, which should use a different port than
                                                  the control agent. For example http://my-host:8001/
        ========================================= ====================================================================================

        .. Note:: Define HA peers for this cluster. All nodes should contain the exact same definitions (usually two hosts, a :code:`primary` and a :code:`standby` host)
    

-------------------------
Configuration examples
-------------------------


DHCPv4 for medium/large HA setups
------------------------------------------

KEA DHCPs main strength is its ability to synchronize leases between multiple servers,
which makes it ideal for medium to large HA setups (more than 1000 unique clients) where you cannot use Dnsmasq DHCP.

As example we configure a network with two KEA DHCP instances on a master and backup OPNsense.

To configure KEA with a minimal HA setup for LAN using the :code:`192.168.1.0/24` network follow these steps:

LAN Network:
    - CARP IPv4 address: ``192.168.1.1/24``
    - Master IPv4 address: ``192.168.1.2/24``
    - Backup IPv4 address: ``192.168.1.3/24``

.. Attention::

    All configuration must be done on the master, and afterwards synchronized to the backup via :menuselection:`System: --> High Availability --> Status`

- Go to :menuselection:`Services --> KEA DHCP --> Control Agent`:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enabled**                         ``X``
**Bind address**                    ``127.0.0.1``
**Bind port**                       ``8000``
==================================  =======================================================================================================

- **Apply** then go to :menuselection:`Services --> KEA DHCP --> KEA DHCPv4` and follow through these tabs:

.. tabs::

    .. tab:: Settings

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **//Service**
        **Enabled**                         ``X``

        **//General settings**
        **Interfaces**                      ``LAN``
        **Firewall rules**                  ``X``

        **//High Availability**
        **Enabled**                         ``X``
        **This server name**                (It is highly recommended to use the offered default value)
        ==================================  =======================================================================================================

        **Apply** and go to **Subnets**

    .. tab:: Subnets

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Subnet**                          ``192.168.1.0/24``
        **Pools**                           ``192.168.1.100 - 192.168.1.199``

        **//DHCP option data**
        **Auto collect option data**        (This must be unchecked for HA)
        **Routers (gateway)**               ``192.168.1.1`` (use the LAN CARP IP address)
        **DNS servers**                     ``192.168.1.1`` (use the LAN CARP IP address)
        ==================================  =======================================================================================================

        **Save** and go to **HA Peers**

    .. tab:: HA Peers

        - First entry:

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Name**                            (Use the name that is displayed in the settings Tab for "This server name" on the master)
        **Role**                            ``primary``
        **URL**                             ``http://192.168.1.2:8001/`` (Use the LAN interface IP of the master,
                                            the port must be different than the control agent)
        ==================================  =======================================================================================================

        - Second entry:

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Name**                            (Use the name that is displayed in the settings Tab for "This server name" on the backup)
        **Role**                            ``standby``
        **URL**                             ``http://192.168.1.3:8001/`` (Use the LAN interface IP of the backup,
                                            the port must be different than the control agent)
        ==================================  =======================================================================================================

        **Save** and **Apply**

Now the initial configuration is finished, and we synchronize it with the backup server. Both servers will always share the exact same configuration.

Go to :menuselection:`System: --> High Availability --> Settings` and ensure that KEA is selected in `Services to synchronize`.

Then go to :menuselection:`System: --> High Availability --> Status` and press `Synchronize and reconfigure all`.

Immediately afterwards, KEA will be active on both master and backup, and a bidirectional lease synchronization will be configured.


-------------------------
Leases DHCPv4/v6
-------------------------

This page offers an overview of the (non static) leases being offered by KEA DHCPv4/v6.
