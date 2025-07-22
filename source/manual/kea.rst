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

    .. tab:: Subnets (DHCPv4/v6)

        .. Note:: Subnets and associated pools

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
