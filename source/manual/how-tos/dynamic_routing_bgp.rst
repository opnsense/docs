============================================
Dynamic Routing - BGP Tutorials
============================================

.. contents::
   :local:
   :depth: 2

For more details go to: `Dynamic Routing - BGP </manual/dynamic_routing.html#bgp-section>`_

---------------------------------------------------
Peering with Routers in internal AS (iBGP)
---------------------------------------------------

This guide provides a step-by-step setup for iBGP between two routers. Each router has a WAN connection,
a unique LAN network, and a shared internal peering network. The routes of the unique LAN networks and any new networks
should be automatically shared between the two routers.

iBGP is the internal variant of BGP for use in one internal Autonomous System (AS). Using a private AS numbers from 64512 to 65534
automatically enables iBGP. Each iBGP neighbor in your internal AS can share the same private AS number.

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
      **Protocol**                                    TCP
      **Source**                                      Peering Network
      **Source Port**                                 Any
      **Destination**                                 Peering Network
      **Destination Port**                            179 (BGP)
      **Description**                                 Allow inbound BGP traffic from peer
      ==============================================  ====================================================================

      .. Note::

         Rules allowing traffic from `LAN Router A` to `LAN Router B` must be created in their respective LAN rulesets.
         Since traffic from LAN A to LAN B will use the peering connection, additional rules must be created in the Peering ruleset.
         Create rules to allow traffic entering `Peering Router A` from `LAN Router B`, and vice versa.


   .. group-tab:: Step 3

      **Configure General Settings**

      - :menuselection:`Routing --> General`
      - Select **Enable**
      - Deselect **Firewall rules** since we created a custom rule for BGP
      - Press `Save`

      .. Note::

         Deactivating the automatic firewall rules is optional. If multiple dynamic routing protocols are used concurrently,
         the automatic rules will ease configuration.


   .. group-tab:: Step 4

      **Configure General BGP Settings**

      - :menuselection:`Routing --> BGP --> General`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **BGP AS Number*                                ``65011`` (or any other private AS number)
      **Route Redistribution**                        ``Connected routes (directly attached subnet or host)``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BGP --> Neighbors`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Peer IP**                                     ``10.1.1.2`` (Peering IP Router B)
      **Remote AS**                                   ``65011``
      **Update-Source Interface**                     ``igc2`` (Peering interface Router A)
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

      .. Note::

         This sets up our peering interface igc2, which will send and receive BGP unicasts
         for advertising and receiving route updates. Since BGP is unicast, OSPF with multicasts can be easier to set up and maintain
         if there is a large number of peering routers in the internal AS.


   .. group-tab:: Step 5

      **Filter redistributed Routes with a Prefix List (Optional)**

      - :menuselection:`Routing --> BGP --> Prefix Lists`

      ==============================================  ====================================================================
      **Name**                                        ``Permit_Prefix``
      **IP Version**                                  ``IPv4``
      **Number**                                      ``1``
      **Action**                                      ``Permit``
      **Network**                                     ``192.168.1.0/24``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BGP --> Route Maps`

      ==============================================  ====================================================================
      **Name**                                        ``Permit_Map``
      **Action**                                      ``Permit``
      **ID**                                          ``1``
      **Prefix List**                                 ``Permit_Prefix``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BGP --> Neighbor`

      ==============================================  ====================================================================
      **Route-Map Out**                               ``Permit_Map``
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

      .. Note::

         With the Permit_Map attached, only the network 192.168.1.0/24 will be advertised from this router.
         Any other networks that will exist as connected routes will not be advertised to BGP neighbors.


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
      **Protocol**                                    TCP
      **Source**                                      Peering Network
      **Source Port**                                 Any
      **Destination**                                 Peering Network
      **Destination Port**                            179 (BGP)
      **Description**                                 Allow inbound BGP traffic from peer
      ==============================================  ====================================================================

      .. Note::

         Rules allowing traffic from `LAN Router A` to `LAN Router B` must be created in their respective LAN rulesets.
         Since traffic from LAN A to LAN B will use the peering connection, additional rules must be created in the Peering ruleset.
         Create rules to allow traffic entering `Peering Router A` from `LAN Router B`, and vice versa.


   .. group-tab:: Step 3

      **Configure General Settings**

      - :menuselection:`Routing --> General`
      - Select **Enable**
      - Deselect **Firewall rules** since we created a custom rule for BGP
      - Press `Save`

   .. group-tab:: Step 4

      **Configure General BGP Settings**

      - :menuselection:`Routing --> BGP --> General`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **BGP AS Number*                                ``65011`` (or any other private AS number)
      **Network**                                     leave empty (we use Route Redistribution)
      **Route Redistribution**                        ``Connected routes (directly attached subnet or host)``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BGP --> Neighbors`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Peer IP**                                     ``10.1.1.1`` (Peering IP Router A)
      **Remote AS**                                   ``65011``
      **Update-Source Interface**                     ``igc2`` (Peering interface Router B)
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

   .. group-tab:: Step 5

      **Filter redistributed Routes with a Prefix List (Optional)**

      - :menuselection:`Routing --> BGP --> Prefix Lists`

      ==============================================  ====================================================================
      **Name**                                        ``Permit_Prefix``
      **IP Version**                                  ``IPv4``
      **Number**                                      ``1``
      **Action**                                      ``Permit``
      **Network**                                     ``192.168.1.0/24``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BGP --> Route Maps`

      ==============================================  ====================================================================
      **Name**                                        ``Permit_Map``
      **Action**                                      ``Permit``
      **ID**                                          ``1``
      **Prefix List**                                 ``Permit_Prefix``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BGP --> Neighbor`

      ==============================================  ====================================================================
      **Route-Map Out**                               ``Permit_Map``
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
    - Ping from 192.168.1.1 (Router A) to 192.168.200.1 (Router B) and vice versa
    - Ping from 192.168.1.201 (Device LAN A) to 192.168.200.201 (Device LAN B) and vice versa
    - If the ping does not work, look at the installed routes and verify the Firewall rules


-------------------------------------------
Peering with ISP for Internet Access (eBGP)
-------------------------------------------

This guide will focus on the most simple eBGP peering scenario. An ISP provides internet access through their autonomous system (AS) by peering with your router as neighbor.
They are your only upstream provider and will push a default route; you will not receive an internet routing table. The ISP will announce the IP address space for you, since it is provider dependent.

Your main task is configuring your neighbor correctly, employing a prefix list so that none of your local RFC1918 routes leak to the provider, and the provider can only
announce the default route to you. If unsure, ask your provider what they expect from you as neighbor. Be mindful of a correct configuration, since an invalid one could get your neighbor
temporarly disabled by the ISP.

.. Attention::

   More complex setups like announcing provider independant address spaces or using the Router as ISP router are out of scope for this setup guide. These setups
   must be created and maintained by BGP experts. Since BGP has no built-in automatic safety mechanisms, an invalid configuraton can disrupt global internet
   routing (e.g., announcing the wrong networks or subnet masks).

Network Diagram
------------------------------------------

::

        +-----------------+     Peering Network      +-----------------+
        |                 |      203.0.113.0/30      |                 |
        |    Router A     |--------------------------|    ISP Router   |
        |     AS65011     | WAN A                ISP |     AS64496     |
        |                 | 203.0.113.1  203.0.113.2 |                 |
        +-----------------+                          +-----------------+
      192.168.1.1 |                                             |
                  |                                             |
        LAN A: 192.168.1.0/24                               Public AS
                  |                                             |
                  |                                             |
        Device A: 192.168.1.201                                 |


Setup Router A
------------------------------------------

.. tabs::

   .. tab:: Step 1

      **Configure Network Interfaces**

      =============================  ================================
      **Interface**                  **Configuration**
      =============================  ================================
      **LAN**                        ``igc0`` - IP: `192.168.1.1/24`
      **WAN**                        ``igc1`` - IP: `203.0.113.1/30`
      =============================  ================================

      #. Configure the **LAN** Interface with IP `192.168.1.1/24` on `igc0`.
      #. Assign the **WAN** Interface on `igc1` with IP `203.0.113.1/30` for the peering network between Router A and the ISP Router.

   .. tab:: Step 2

      **Create Firewall rules on Peering Interface**

      - :menuselection:`Firewall --> Rules --> Peering (igc1)`

      ==============================================  ====================================================================
      **Action**                                      Pass
      **Interface**                                   WAN (igc1)
      **Direction**                                   In
      **TCP/IP Version**                              IPv4
      **Protocol**                                    TCP
      **Source**                                      WAN network
      **Source Port**                                 Any
      **Destination**                                 WAN network
      **Destination Port**                            179 (BGP)
      **Description**                                 Allow inbound BGP traffic from ISP Router
      ==============================================  ====================================================================

   .. tab:: Step 3

      **Configure General Settings**

      - :menuselection:`Routing --> General`
      - Select **Enable**
      - Deselect **Firewall rules** since we created a custom rule for BGP
      - Press `Save`

      .. Note::

         Deactivating the automatic firewall rules is optional. If multiple dynamic routing protocols are used concurrently,
         the automatic rules will ease configuration.


   .. tab:: Step 4

      **Configure General BGP Settings**

      - :menuselection:`Routing --> BGP --> General`

      ==============================================  =======================================================================
      **Enable**                                      ``X``
      **BGP AS Number**                               ``65011`` (or any other private AS number)
      **Network**                                     leave empty (we do not want to advertise any networks)
      **Route Redistribution**                        ``None`` (we do not want to advertise any networks)
      ==============================================  =======================================================================

      - :menuselection:`Routing --> BGP --> Neighbors`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Peer IP**                                     ``203.0.113.2`` (Peering IP ISP Router)
      **Remote AS**                                   ``64496``
      **Update-Source Interface**                     ``igc1`` (Peering interface Router A)
      ==============================================  ====================================================================

   .. tab:: Step 5

      **Filter redistributed Routes with a Prefix List**

      - :menuselection:`Routing --> BGP --> Prefix Lists`

      ==============================================  ====================================================================
      **Name**                                        ``Filter_Prefix_RFC1918``
      **IP Version**                                  ``IPv4``
      **Number**                                      ``1``
      **Action**                                      ``Deny``
      **Network**                                     ``192.168.0.0/16``
      ==============================================  ====================================================================

      ==============================================  ====================================================================
      **Name**                                        ``Filter_Prefix_RFC1918``
      **IP Version**                                  ``IPv4``
      **Number**                                      ``2``
      **Action**                                      ``Deny``
      **Network**                                     ``172.16.0.0/12``
      ==============================================  ====================================================================

      ==============================================  ====================================================================
      **Name**                                        ``Filter_Prefix_RFC1918``
      **IP Version**                                  ``IPv4``
      **Number**                                      ``3``
      **Action**                                      ``Deny``
      **Network**                                     ``10.0.0.0/8``
      ==============================================  ====================================================================

      ==============================================  ====================================================================
      **Name**                                        ``Filter_Prefix_RFC1918``
      **IP Version**                                  ``IPv4``
      **Number**                                      ``4``
      **Action**                                      ``Permit``
      **Network**                                     ``0.0.0.0/0``
      ==============================================  ====================================================================

      ==============================================  ====================================================================
      **Name**                                        ``Filter_Prefix_Default``
      **IP Version**                                  ``IPv4``
      **Number**                                      ``5``
      **Action**                                      ``Deny``
      **Network**                                     ``0.0.0.0/0``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BGP --> Route Maps`

      ==============================================  ====================================================================
      **Name**                                        ``Filter_Map_RFC1918``
      **Action**                                      ``Permit``
      **ID**                                          ``1``
      **Prefix List**                                 ``Filter_Prefix_RFC1918``
      ==============================================  ====================================================================

      ==============================================  ====================================================================
      **Name**                                        ``Filter_Map_Default``
      **Action**                                      ``Deny``
      **ID**                                          ``2``
      **Prefix List**                                 ``Filter_Prefix_Default``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BGP --> Neighbor`

      ==============================================  ====================================================================
      **Route-Map In**                                ``Filter_Map_RFC1918``
      **Route-Map Out**                               ``Filter_Map_Default``
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

      .. Note::

         `Route-Map In` will deny all RFC1918 routes that the ISP could accidentally advertise to us. Only 0.0.0.0/0 is allowed as advertisement from the ISP.
         `Route-Map Out` will prevent any false advertisements from us to the ISP.


Verify the setup
------------------------------------------

- | :menuselection:`Routing --> Diagnostics --> General`
- `IPv4 Routes Tab`:
    - Router A must have a route to 0.0.0.0/0 via 203.0.113.2 installed

- Test connectivity with ICMP:
    - Ping from 203.0.113.1 (Router A) to 203.0.113.2 (ISP)
    - Ping from 203.0.113.1 to a destination on the internet
    - If the ping does not work, look at the installed routes and verify the Firewall rules
