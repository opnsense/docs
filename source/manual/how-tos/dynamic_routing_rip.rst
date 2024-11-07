============================================
Dynamic Routing - RIP Tutorials
============================================

.. contents::
   :local:
   :depth: 2

For more details go to: `Dynamic Routing - RIP </manual/dynamic_routing.html#rip-section>`_

------------------------------------------
Setup RIP between Routers
------------------------------------------

This guide provides a step-by-step setup for RIP between two routers. Each router has a WAN connection,
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
      **Protocol**                                    UDP
      **Source**                                      Peering Network
      **Source Port**                                 Any
      **Destination**                                 ``224.0.0.9`` (RIP v2 Multicast)
      **Destination Port**                            ``520``
      **Description**                                 Allow RIP v2 multicast traffic on UDP port 520 for routing updates
      ==============================================  ====================================================================

      .. Note::

         Rules allowing traffic from `LAN Router A` to `LAN Router B` must be created in their respective LAN rulesets.
         Since traffic from LAN A to LAN B will use the peering connection, additional rules must be created in the Peering ruleset.
         Create rules to allow traffic entering `Peering Router A` from `LAN Router B`, and vice versa.


   .. group-tab:: Step 3

      **Configure General Settings**

      - :menuselection:`Routing --> General`
      - Select **Enable**
      - Deselect **Firewall rules** since we created a custom rule for RIPv2
      - Press `Save`

      .. Note::

         Deactivating the automatic firewall rules is optional. If multiple dynamic routing protocols are used concurrently,
         the automatic rules will ease configuration.


   .. group-tab:: Step 4

      **Configure RIP Settings**

      - :menuselection:`Routing --> RIP`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Version**                                     ``2`` (to support CIDR and Multicast)
      **Passive Interfaces**                          ``LAN``, ``WAN`` (only the peering network shares routes)
      **Route Redistribution**                        ``Connected routes (directly attached subnet or host)``
      **Network**                                     leave empty since we use Connected routes
      **Default Metric**                              ``1`` (for high priority)
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration


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
      **Protocol**                                    UDP
      **Source**                                      Peering Network
      **Source Port**                                 Any
      **Destination**                                 ``224.0.0.9`` (RIP v2 Multicast)
      **Destination Port**                            ``520``
      **Description**                                 Allow RIP v2 multicast traffic on UDP port 520 for routing updates
      ==============================================  ====================================================================

   .. group-tab:: Step 3

      **Configure General Settings**

      - :menuselection:`Routing --> General`
      - Select **Enable**
      - Deselect **Firewall rules** since we created a custom rule for RIPv2
      - Press `Save`

   .. group-tab:: Step 4

      **Configure RIP Settings**

      - :menuselection:`Routing --> RIP`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Version**                                     ``2`` (to support CIDR and Multicast)
      **Passive Interfaces**                          ``LAN``, ``WAN`` (only the peering network shares routes)
      **Route Redistribution**                        ``Connected routes (directly attached subnet or host)``
      **Network**                                     leave empty since we use Connected routes
      **Default Metric**                              ``1`` (for high priority)
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
