==============================================
Dynamic Routing - OSPF Tutorials
==============================================

.. contents::
   :local:
   :depth: 2

For more details go to: `Dynamic Routing - OSPF </manual/dynamic_routing.html#ospf-section>`_

------------------------------------------
Setup OSPF between Routers
------------------------------------------

This guide provides a step-by-step setup for OSPF between two OPNsenses. Each router has a WAN connection,
a unique LAN network, and a shared internal peering network. The routes of the unique LAN networks and any new networks
should be automatically shared between the two routers.

.. Note::

   Peering network means that the OPNsenses are directly attached to each other via these interfaces. This can be done either
   by connecting a network cable directly between these ports, or ensure they are connected to the same switch in the same Layer 2
   Broadcast Domain.


Network Diagram
------------------------------------------

::

            +-----------------+     Peering Network      +-----------------+
      WAN A |                 |       10.1.1.0/30        |                 | WAN B
  ----------|   OPNsense A    |--------------------------|   OPNsense B    |----------
       DHCP |                 | 10.1.1.1        10.1.1.2 |                 | DHCP
            +-----------------+                          +-----------------+
                   | 192.168.1.1                   192.168.200.1 |
                   |                                             |
            LAN A: 192.168.1.0/24                       LAN B: 192.168.200.0/24
                   |                                             |
                   |                                             |
            Device A: 192.168.1.201                     Device B: 192.168.200.201


Setup OPNsense A
------------------------------------------

.. tabs::

   .. group-tab:: Step 1

      **Configure Network Interfaces**

      =============================  ================================
      **Interface**                  **Configuration**
      =============================  ================================
      **LAN**                        ``igc0`` - IP: `192.168.1.1/24`
      **WAN**                        ``igc1`` - IP: `DHCP`
      **Peering**                    ``igc2`` - IP: `10.1.1.1/30`
      =============================  ================================

      #. Configure the **LAN** Interface with IP `192.168.1.1/24` on `igc0`.
      #. Assign the **Peering** Interface on `igc2` with IP `10.1.1.1/30` for the peering network between OPNsense A and OPNsense B.

      .. Note::

         Since we do not use the **WAN** Interface for peering, it does not need any specific configuration.

   .. group-tab:: Step 2

      **Create Firewall rules on Peering Interface**

      - :menuselection:`Firewall --> Rules --> Peering (igc2)`

      ==============================================  ====================================================================
      **Action**                                      Pass
      **Interface**                                   Peering (igc2)
      **Direction**                                   In
      **TCP/IP Version**                              IPv4
      **Protocol**                                    OSPF (Protocol 89)
      **Source**                                      Peering Network
      **Source Port**                                 Any
      **Destination**                                 224.0.0.5, 224.0.0.6 (OSPF Multicast)
      **Destination Port**                            Any
      **Description**                                 Allow OSPF multicast traffic for routing updates
      ==============================================  ====================================================================

      .. Note::

         Rules allowing traffic from `LAN OPNsense A` to `LAN OPNsense B` must be created in their respective LAN rulesets.
         Since traffic from LAN A to LAN B will use the peering connection, additional rules must be created in the Peering ruleset.
         Create rules to allow traffic entering `Peering OPNsense A` from `LAN OPNsense B`, and vice versa.


   .. group-tab:: Step 3

      **Configure General Settings**

      - :menuselection:`Routing --> General`
      - Select **Enable**
      - Deselect **Firewall rules** since we created a custom rule for OSPF
      - Press `Save`

   .. group-tab:: Step 4

      **Configure General OSPF Settings**

      - :menuselection:`Routing --> OSPF --> General`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Passive Interfaces**                          ``LAN``, ``WAN`` (only the peering network shares routes)
      **Route Redistribution**                        ``Connected routes (directly attached subnet or host)``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> OSPF --> Interfaces`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Interface**                                   ``Peering`` (igc2)
      **Area**                                        ``0.0.0.0``
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

      .. Note::

         This sets up our peering interface igc2 in the Backbone Area 0.0.0.0 where it will send and receive OSPF multicasts
         for advertising and receiving route updates.


   .. group-tab:: Step 5

      **Filter redistributed Routes with a Prefix List (Optional)**

      - :menuselection:`Routing --> OSPF --> Prefix Lists`

      ==============================================  ====================================================================
      **Name**                                        ``Permit_Prefix``
      **Number**                                      ``10``
      **Action**                                      ``Permit``
      **Network**                                     ``192.168.1.0/24``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> OSPF --> Route Maps`

      ==============================================  ====================================================================
      **Name**                                        ``Permit_Map``
      **Action**                                      ``Permit``
      **ID**                                          ``10``
      **Prefix List**                                 ``Permit_Prefix``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> OSPF --> General`

      ==============================================  ====================================================================
      **Redistribution Map**                          ``Permit_Map``
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

      .. Note::

         With the Permit_Map attached, only the network 192.168.1.0/24 will be advertised from this router.
         Any other networks that will exist as connected routes will not be advertised to other routers in the 0.0.0.0 Backbone Area.


Setup OPNsense B
------------------------------------------

.. tabs::

   .. group-tab:: Step 1

      **Configure Network Interfaces**

      =============================  ================================
      **Interface**                  **Configuration**
      =============================  ================================
      **LAN Interface**              ``igc0`` - IP: `192.168.200.1/24`
      **WAN Interface**              ``igc1`` - IP: `DHCP`
      **Peering Interface**          ``igc2`` - IP: `10.1.1.2/30`
      =============================  ================================

      #. Configure the **LAN Interface** with IP `192.168.200.1/24` on `igc0`.
      #. Assign the **Peering Interface** on `igc2` with IP `10.1.1.2/30` for the peering network between OPNsense A and OPNsense B.

   .. group-tab:: Step 2

      **Create Firewall rules on Peering Interface**

      - :menuselection:`Firewall --> Rules --> Peering (igc2)`

      ==============================================  ====================================================================
      **Action**                                      Pass
      **Interface**                                   Peering (igc2)
      **Direction**                                   In
      **TCP/IP Version**                              IPv4
      **Protocol**                                    OSPF (Protocol 89)
      **Source**                                      Peering Network
      **Source Port**                                 Any
      **Destination**                                 224.0.0.5, 224.0.0.6 (OSPF Multicast)
      **Destination Port**                            Any
      **Description**                                 Allow OSPF multicast traffic for routing updates
      ==============================================  ====================================================================

   .. group-tab:: Step 3

      **Configure General Settings**

      - :menuselection:`Routing --> General`
      - Select **Enable**
      - Deselect **Firewall rules** since we created a custom rule for OSPF
      - Press `Save`

   .. group-tab:: Step 4

      **Configure General OSPF Settings**

      - :menuselection:`Routing --> OSPF --> General`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Passive Interfaces**                          ``LAN``, ``WAN`` (only the peering network shares routes)
      **Route Redistribution**                        ``Connected routes (directly attached subnet or host)``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> OSPF --> Interfaces`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Interface**                                   ``Peering`` (igc2)
      **Area**                                        ``0.0.0.0``
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

   .. group-tab:: Step 5

      **Filter redistributed Routes with a Prefix List (Optional)**

      - :menuselection:`Routing --> OSPF --> Prefix Lists`

      ==============================================  ====================================================================
      **Name**                                        ``Permit_Prefix``
      **Number**                                      ``10``
      **Action**                                      ``Permit``
      **Network**                                     ``192.168.200.0/24``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> OSPF --> Route Maps`

      ==============================================  ====================================================================
      **Name**                                        ``Permit_Map``
      **Action**                                      ``Permit``
      **ID**                                          ``10``
      **Prefix List**                                 ``Permit_Prefix``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> OSPF --> General`

      ==============================================  ====================================================================
      **Redistribution Map**                          ``Permit_Map``
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration


Verify the setup
------------------------------------------

- | :menuselection:`Routing --> Diagnostics --> General`
- `IPv4 Routes Tab`:
    - Verify if the routes to LAN OPNsense A and LAN OPNsense B exist
    - OPNsense A must have a route to 192.168.200.0/24 installed
    - OPNsense B must have a route to 192.168.1.0/24 installed

- Test connectivity with ICMP:
    - Ping from 192.168.1.1 (OPNsense A) to 192.168.200.1 (OPNsense B) and in reverse
    - Ping from 192.168.1.201 (Device LAN A) to 192.168.200.201 (Device LAN B) and vice versa
    - If the ping does not work, look at the installed routes and verify the Firewall rules


------------------------------------
IPsec VTI Failover with OSPF
------------------------------------

This guide will enhance what has been introduced in the previous section, introducing two WAN connections and
two VPN tunnels for seamless failover in case a connection goes down.

OPNsense A has one WAN connection and will initiate two IPsec VTI tunnels to OPNsense B which has two WAN connections. Both sides
should have static public IP addresses for the most stable setup.

Network Diagram
------------------------------------------

::

                                             Peering Networks
                                            ipsec1: 10.0.0.0/30
                     +-----------------+ 10.1.1.1        10.1.1.2 +-----------------+ WAN A: 198.51.100.2
    WAN A: 192.0.2.1 |                 |--------------------------|                 |-----------------------
    -----------------|   OPNsense A    |    ipsec2: 10.0.0.4/30   |   OPNsense B    | WAN B: 203.0.113.2
                     |                 |--------------------------|                 |-----------------------
                     +-----------------+ 10.1.1.5        10.1.1.6 +-----------------+
                            | 192.168.1.1                   192.168.200.1 |
                            |                                             |
                   LAN A: 192.168.1.0/24                       LAN B: 192.168.200.0/24
                            |                                             |
                            |                                             |
                   Device A: 192.168.1.201                     Device B: 192.168.200.201

Setup OPNsense A
------------------------------------------

Follow the steps as the `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_ with a few differences:

.. tabs::

   .. group-tab:: Step 1

      IPsec VTI tunnels have to be established for ``ipsec1`` and ``ipsec2``. Use the following guide to set them up: `IPsec - Route based (VTI) PSK setup </manual/how-tos/ipsec-s2s-conn-route.html>`_. Do not set up Gateways or Routes, since we will use dynamic routing.

   .. group-tab:: Step 2

      The Firewall rules have to be set up depending on `system tunables </manual/vpnet.html#route-based-vti>`_. It can be either
      the ``ipsec1`` and ``ipsec2`` interfaces, or the ``IPsec`` interface group.

   .. group-tab:: Step 3

      Same as `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_

   .. group-tab:: Step 4

      - :menuselection:`Routing --> OSPF --> Interfaces`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Interface**                                   ``ipsec1``
      **Area**                                        ``0.0.0.0``
      **Cost**                                        ``10``
      ==============================================  ====================================================================

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Interface**                                   ``ipsec2``
      **Area**                                        ``0.0.0.0``
      **Cost**                                        ``20``
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

      .. Note::

         The lower cost of ``ipsec1`` will make this interface prefered as route as long as it is available.

   .. group-tab:: Step 5

      Same as `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_

Setup OPNsense B
------------------------------------------

.. tabs::

   .. group-tab:: Step 1

      IPsec VTI tunnels have to be established for ``ipsec1`` and ``ipsec2``.

   .. group-tab:: Step 2

      The Firewall rules have to be set up.

   .. group-tab:: Step 3

      Same as `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_

   .. group-tab:: Step 4

      - :menuselection:`Routing --> OSPF --> Interfaces`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Interface**                                   ``ipsec1``
      **Area**                                        ``0.0.0.0``
      **Cost**                                        ``10``
      ==============================================  ====================================================================

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Interface**                                   ``ipsec2``
      **Area**                                        ``0.0.0.0``
      **Cost**                                        ``20``
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

   .. group-tab:: Step 5

      Same as `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_


Verify the setup
------------------------------------------

In addition to the setup verification steps of the previous setup guide:

- Disconnect ipsec1:
    - The traffic between 192.168.1.0/24 and 192.168.200.0/24 should automatically route over ipsec2
- Reconnect ipsec1:
    - The traffic should route back over ipsec1

.. Note::

    This failover can take as long as the `Dead Interval` of OSPF needs to mark the route as down.
    Follow the steps in `Dynamic Routing - BFD </manual/dynamic_routing.html#bfd-section>`_ to speed up convergence time.

.. Note::

    IPsec VTI interfaces natively support the multicasts of routing protocols like OSPF or BGP. If you want to do the same setup with policy based
    IPsec tunnels, these tunnels should connect loopback interfaces. On these loopback interfaces, GRE tunnels can be established. The peering
    should then be configured with the GRE tunnel interfaces. This setup introduces more complexity and processing overhead; the VTI setup
    should be prefered.
