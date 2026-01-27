============================================
Dynamic Routing - BFD Tutorials
============================================

.. contents::
   :local:
   :depth: 2

For more details go to: `Dynamic Routing - BFD </manual/dynamic_routing.html#bfd-section>`_

----------------------------
BFD with OSPF or BGP
----------------------------

This guide provides a step-by-step setup to enable BFD for faster convergence times when link failures occur in the peering network.
It is mostly needed for high availability setups where up to a minute of convergence with conventional BGP or OSPF mechanisms is not acceptable.

BFD can bring routing convergence times down to a second.

Setting up BFD is additional to the `OSPF Tutorial </manual/how-tos/dynamic_routing_ospf.html>`_ or `BGP Tutorial </manual/how-tos/dynamic_routing_bgp.html>`_ steps.

.. tabs::

   .. group-tab:: Step 1

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
      **Destination**                                 Peering IP (Router IP)
      **Destination Port**                            3784 (Single-Hop BFD)
      **Description**                                 Allow BFD single-hop sessions
      ==============================================  ====================================================================

      .. Note::

         BFD is unidirectional, both sides need rules to send and receive BFD packets. We only use single hop in our simple setup so
         this is the only rule we need.


   .. group-tab:: Step 2

      **Configure BFD Neighbor**

      - :menuselection:`Routing --> BFD --> General`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BFD --> Neighbors`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Description**                                 ``Router B``
      **Peer-IP**                                     ``10.1.1.2``
      **Multihop**                                    Do not enable, it is needed for more complex setups only.
      ==============================================  ====================================================================

      .. Note::

         The next step is for either BGP or OSPF, choose the correct one for your setup.


   .. group-tab:: Step 3 BGP

      **Configure BGP Settings**

      - :menuselection:`Routing --> BGP --> Neighbor`

      Open the existing neighbor `Router B` and enable BFD.

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Peer IP**                                     ``10.1.1.2``
      **Remote AS**                                   ``65011``
      **Update-Source Interface**                     ``igc2``
      **BFD**                                         ``X`` (new)
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

   .. group-tab:: Step 3 OSPF

      **Configure OSPF Settings**

      - :menuselection:`Routing --> OSPF --> Interface`

      Open the existing peering interface to `Router B` and enable BFD.

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Interface**                                   ``Peering`` (igc2)
      **Area**                                        ``0.0.0.0``
      **BFD**                                         ``X`` (new)
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration


Setup Router B
------------------------------------------

.. tabs::

   .. group-tab:: Step 1

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
      **Destination**                                 Peering IP (Router IP)
      **Destination Port**                            3784 (Single-Hop BFD)
      **Description**                                 Allow BFD single-hop sessions
      ==============================================  ====================================================================

   .. group-tab:: Step 2

      **Configure BFD Neighbor**

      - :menuselection:`Routing --> BFD --> General`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      ==============================================  ====================================================================

      - :menuselection:`Routing --> BFD --> Neighbors`

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Description**                                 ``Router A``
      **Peer-IP**                                     ``10.1.1.1``
      **Multihop**                                    Do not enable, it is needed for more complex setups only.
      ==============================================  ====================================================================

   .. group-tab:: Step 3 BGP

      **Configure BGP Settings**

      - :menuselection:`Routing --> BGP --> Neighbor`

      Open the existing neighbor `Router A` and enable BFD.

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Peer IP**                                     ``10.1.1.1``
      **Remote AS**                                   ``65011``
      **Update-Source Interface**                     ``igc2``
      **BFD**                                         ``X`` (new)
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration

   .. group-tab:: Step 3 OSPF

      **Configure OSPF Settings**

      - :menuselection:`Routing --> OSPF --> Interface`

      Open the existing peering interface to `Router A` and enable BFD.

      ==============================================  ====================================================================
      **Enable**                                      ``X``
      **Interface**                                   ``Peering`` (igc2)
      **Area**                                        ``0.0.0.0``
      **BFD**                                         ``X`` (new)
      ==============================================  ====================================================================

      - Press ``Save`` to enable the new configuration


Verify the setup
------------------------------------------

Go to :menuselection:`Routing --> Diagnostics --> BFD` and look at the Summary tab to view the status of the BFD neighbors.

The real benefit of BFD can only be seen if there are multiple routes with different cost. When the BFD packets are interrupted, the route will quickly be discarded and the next best route will be installed and chosen. This will happen in just a ping or even faster.

An example for a setup that will benefit from BFD is `IPsec Failover with VTI and OSPF </manual/how-tos/dynamic_routing_ospf.html#ipsec-failover-with-vti-and-ospf>`_
