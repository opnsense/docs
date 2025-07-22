==================
KEA DHCP
==================

.. contents:: Index

Kea is the next generation of DHCP software, developed by Internet Systems Consortium (ISC).

It is considered the replacement for `ISC-DHCP` in larger HA enabled setups
and synergizes well with `radvd` for HA enabled router advertisements.

Currently it is not possible to register hostnames dynamically between KEA and Unbound, only static reservations will be
synchronized on an Unbound service restart.

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
Kea DHCPv4/v6
...............................

This is the DHCPv4/v6 service available in KEA, which offers the following tab sheets with their corresponding settings:

.. tabs::

    .. tab:: Settings (DHCPv4/v6)

        .. Note:: Generic settings for this service

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

        .. Note:: Subnets and associated pools

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

    .. tab:: PD Pools (DHCPv6)

        .. Note:: Prefix delegation pools for IPv6

    .. tab:: Reservations (DHCPv4/v6)

        .. Note:: Machine static reservations

    .. tab:: HA Peers (DHCPv4/DHCPv6)

        .. Note:: Define HA peers for this cluster. All nodes should contain the exact same definitions (usually two hosts, a :code:`primary` and a :code:`standby` host)
    

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
Leases DHCPv4/v6
...............................

This page offers an overview of the (non static) leases being offered by KEA DHCPv4.
