==============================================
Dynamic Routing - OSPF Tutorials
==============================================

.. contents::
   :local:
   :depth: 2

For more details go to: `Dynamic Routing - OSPF </manual/dynamic_routing.html#ospf-section>`_

.. Note::

   OSPFv2 supports IPv4. For IPv6 use OSPFv3 instead.


------------------------------------------
Setup OSPF between Routers
------------------------------------------

This guide provides a step-by-step setup for OSPF between two routers. Each router has a WAN connection,
a unique LAN network, and a shared internal peering network. The routes of the unique LAN networks and any new networks
should be automatically shared between the two routers.

.. Note::

   Peering network means that the routers are directly attached to each other via these interfaces. This can be done either
   by connecting a network cable directly between these ports, or ensuring they are connected to the same switch in the same Layer 2
   Broadcast Domain.


Network Diagram
------------------------------------------

::

            +-----------------+     Peering Network      +-----------------+
      WAN A |                 |       10.1.1.0/30        |                 | WAN B
  ----------|    Router A     |--------------------------|    Router B     |----------
       DHCP |                 | 10.1.1.1        10.1.1.2 |                 | DHCP
            +-----------------+                          +-----------------+
                   | 192.168.1.1                   192.168.200.1 |
                   |                                             |
            LAN A: 192.168.1.0/24                       LAN B: 192.168.200.0/24
                   |                                             |
                   |                                             |
            Device A: 192.168.1.201                     Device B: 192.168.200.201


Setup Router A
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
      #. Assign the **Peering** Interface on `igc2` with IP `10.1.1.1/30` for the peering network between Router A and Router B.

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

         Rules allowing traffic from `LAN Router A` to `LAN Router B` must be created in their respective LAN rulesets.
         Since traffic from LAN A to LAN B will use the peering connection, additional rules must be created in the Peering ruleset.
         Create rules to allow traffic entering `Peering Router A` from `LAN Router B`, and vice versa.


   .. group-tab:: Step 3

      **Configure General Settings**

      - :menuselection:`Routing --> General`
      - Select **Enable**
      - Deselect **Firewall rules** since we created a custom rule for OSPF
      - Press `Save`

      .. Note::

         Deactivating the automatic firewall rules is optional. If multiple dynamic routing protocols are used concurrently,
         the automatic rules will ease configuration.


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


Setup Router B
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
      #. Assign the **Peering Interface** on `igc2` with IP `10.1.1.2/30` for the peering network between Router A and Router B.

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
    - Verify if the routes to LAN Router A and LAN Router B exist
    - Router A must have a route to 192.168.200.0/24 installed
    - Router B must have a route to 192.168.1.0/24 installed

- Test connectivity with ICMP:
    - Ping from 192.168.1.1 (Router A) to 192.168.200.1 (Router B) and in reverse
    - Ping from 192.168.1.201 (Device LAN A) to 192.168.200.201 (Device LAN B) and vice versa
    - If the ping does not work, look at the installed routes and verify the Firewall rules


------------------------------------
IPsec Failover with VTI and OSPF
------------------------------------

This guide will enhance what has been introduced in the previous section, introducing two WAN connections and
two VPN tunnels for seamless failover in case a connection goes down.

Router A has one WAN connection and will initiate two IPsec VTI tunnels to Router B which has two WAN connections. Both sides
should have static public IP addresses for the most stable setup.

Network Diagram
------------------------------------------

::

                                          Peering Networks
                                         ipsec1: 10.0.0.0/30
                  +-----------------+ 10.1.1.1        10.1.1.2 +-----------------+ WAN A: Static
    WAN A: Static |                 |--------------------------|                 |---------------
    --------------|    Router A     |    ipsec2: 10.0.0.4/30   |    Router B     | WAN B: Static
                  |                 |--------------------------|                 |---------------
                  +-----------------+ 10.1.1.5        10.1.1.6 +-----------------+
             192.168.1.1 |                                             | 192.168.200.1
                         |                                             |
                  LAN A: 192.168.1.0/24                       LAN B: 192.168.200.0/24
                         |                                             |
                         |                                             |
                  Device A: 192.168.1.201                     Device B: 192.168.200.201

Setup Router A and B
------------------------------------------

Follow the steps as the `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_ with a few differences:

.. tabs::

   .. group-tab:: Step 1

      - :menuselection:`VPN --> IPsec --> Connections`: IPsec VTI tunnels must be established for ``ipsec1`` and ``ipsec2``.
      - Use the following guide to set them up: `IPsec - Route based (VTI) PSK setup </manual/how-tos/ipsec-s2s-conn-route.html>`_.

      .. Note::

         Do not set up gateways or routes for the VTI interfaces, since we will use dynamic routing. If there are local routes the dynamic
         routes will not be installed.

   .. group-tab:: Step 2

      The Firewall rules must be set up depending on `system tunables </manual/vpnet.html#route-based-vti>`_. It can be either
      for the ``ipsec1`` and ``ipsec2`` interfaces, or the ``IPsec`` interface group.

   .. group-tab:: Step 3

      Same as `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_

   .. group-tab:: Step 4

      Add ``ipsec1`` with cost 10 and ``ipsec2`` with cost 20.

      .. Note::

         The lower cost of ``ipsec1`` will make this interface prefered as route as long as it is available.

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
    IPsec tunnels, follow the next guide.

------------------------------------------------------
IPsec Failover with Policy Based Tunnels, GRE and OSPF
------------------------------------------------------

This guide will use policy based IPsec tunnels for dynamic routing instead of VTI.
These do not natively support multicasts from routing protocols such as OSPF. To mitigate this, GRE over IPsec will be used as peering
connection.

GRE over IPsec introduces another layer of complexity, each tunnel creates header overhead that reduces the possible MTU. ICMP should be allowed for clients
to automatically discover the correct packet size through the tunnel via `Path MTU Discovery`. Otherwise, MTU and MSS must be adjusted manually.

Router A has one WAN connection and will initiate two IPsec policy based tunnels to Router B which has two WAN connections. Both sides
should have static public IP addresses for the most stable setup. Dynamic IPs for one endpoint can also be a valid choice.

Network Diagram
------------------------------------------

::

                                        Peering Networks
                                       gre1: 10.0.0.0/30
                +-----------------+ 10.1.1.1        10.1.1.2 +-----------------+ WAN A: Static
    WAN A: DHCP | lo1:10.2.2.1/32 |--------------------------| lo1:10.2.2.2/32 |--------------
    ------------|    Router A     |    gre2: 10.0.0.4/30     |    Router B     | WAN B: Static
                | lo2:10.2.2.5/32 |--------------------------| lo2:10.2.2.6/32 |--------------
                +-----------------+ 10.1.1.5        10.1.1.6 +-----------------+
            192.168.1.1 |                                             | 192.168.200.1
                        |                                             |
                LAN A: 192.168.1.0/24                       LAN B: 192.168.200.0/24
                        |                                             |
                        |                                             |
                Device A: 192.168.1.201                     Device B: 192.168.200.201

Setup Router A and B
------------------------------------------

Follow the steps as the `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_ with a few differences:

.. tabs::

   .. group-tab:: Step 1

      #. :menuselection:`Interfaces --> Devices --> Loopback`: Create two loopback interfaces on each firewall, use the network diagram for reference.
      #. :menuselection:`VPN --> IPsec --> Connections`: Create two policy based IPsec tunnels that each connect a pair of loopback interfaces as children, e.g., ``10.2.2.1/32`` with ``10.2.2.2/32``.
      #. :menuselection:`Interfaces --> Devices --> GRE`: Create two GRE tunnels on each firewall that each use a loopback interface of the other side as `Remote address`. The tunnel local and remote address can be referenced from the network diagram.

      .. Note::

         The GRE tunnels will be the peering networks, all traffic from LAN A to LAN B and vice versa will flow through there. GRE should not be used without IPsec in public networks since its payload is not encrypted.

   .. group-tab:: Step 2

      #. :menuselection:`Firewall --> Rules --> IPsec`: Create Firewall rules to allow GRE to establish over the policy based IPsec tunnel.
      #. :menuselection:`Firewall --> Rules --> gre1/gre2`: Create Firewall rules to allow OSPF multicasts and the peering traffic of LAN A and LAN B through the GRE tunnels.

   .. group-tab:: Step 3

      Same as `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_

   .. group-tab:: Step 4

      Add ``gre1`` with cost 10 and ``gre2`` with cost 20.

      .. Note::

         The lower cost of ``gre1`` will make this interface prefered as route as long as it is available.

   .. group-tab:: Step 5

      Same as `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#setup-ospf-between-routers>`_


Verify the setup
------------------------------------------

For setup verification follow the same steps as in the `previous setup guide </manual/how-tos/dynamic_routing_ospf.html#verify-the-setup>`_
