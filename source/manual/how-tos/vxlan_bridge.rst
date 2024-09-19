============
VXLAN Bridge
============

.. contents:: Index


-------
Summary
-------


This guide covers the configuration of a VXLAN tunnel between two OPNsense firewalls connected via VPN. This enables Layer 2 communication over Layer 3, which can introduce challenges such as DHCP conflicts and network traffic routing issues. Layer 2 tunneling should only be used when necessary, as routing is usually the best option for Layer 3 networks.

.. Attention:: 

    - | A large broadcast domain will create more broadcast and multicast traffic. This can quickly saturate WAN links since it will be exchanged over the internet with Layer 2 tunneling. 
    - | Switches need special attention. Layer 2 protocols like STP will now be shared over the VXLAN tunnel. The Switch should filter specific Layer 2 protocols to prevent improper STP convergence. DHCP could also be filtered with the Switch, so different DHCP servers can be used.
    - | Bridges, VXLAN and VPN introduce overhead, which can increase CPU usage and limit bandwidth. This configuration is not suitable for high-throughput environments where gigabits of traffic are required.
    - | If e.g., `Site B` uses the bridged LAN as their main network, all traffic will be sent to `Site A` for routing and breakout to the internet. Please be aware of the implications.

See the section on `VXLAN </manual/other-interfaces.html#vxlan>`_ for more details.


--------------
Setup Overview
--------------

There are two OPNsense - Site A and Site B - that should communicate over the internet via Layer2.

Since VXLAN is not encrypted, a VPN should be used to secure the connection. IPsec or Wireguard are recommended, since they can create simple point to point VPNs between the loopback interfaces for the VXLAN source and remote addresses.

===============  ================
**Interface**    **IP Address**
===============  ================
**Site (A)**
WAN              203.0.113.1/32
lo1              172.16.88.1/32
bridge0          192.168.10.1/24
vxlan1           IPv4 None
LAN              IPv4 None
**Site (B)**
WAN              198.51.100.2/32
lo1              172.16.88.2/32
bridge0          192.168.10.2/24
vxlan1           IPv4 None
LAN              IPv4 None
===============  ================


--------------
Configuration
--------------


1. Loopback Interface Setup
---------------------------
   
- | Go to :menuselection:`Interfaces --> Other Types --> Loopback` and add ``lo1`` on both `Sites`
- | Go to :menuselection:`Interfaces --> Assignments` and assign ``lo1``
- | Enable ``lo1`` and set a static IPv4 configuration:
       
    - Site A: `172.16.88.1/32`
    - Site B: `172.16.88.2/32`
     
.. Note:: These loopback interfaces will be used for the VXLAN source and remote addresses. This will ensure that the VXLAN interfaces can be created during boot, since loopback interfaces are always available.


2. VPN Setup
------------

The ``lo1`` interfaces on both firewalls must be connected via VPN. In this example, the VPN will span between the WAN IPs 203.0.113.1/32 (Site A) and 198.51.100.2/32 (Site B). This can be achieved with:
        
    - | A policy-based IPsec tunnel, including the loopback IPs in Phase 2 `Children` (`172.16.88.1/32` on Site B, `172.16.88.2/32` on Site A) or
    - | A WireGuard tunnel with no interface IPs, including the loopback IPs (`172.16.88.1/32` on Site B, `172.16.88.2/32` on Site A) in the `Allowed IPs` or
    - | Any other VPN protocol since VXLAN is VPN agnostic.

The tunnel should now route traffic between the two loopback interfaces. Test connectivity by pinging the loopback interfaces across the tunnel; use the loopback as source interface. 

Allowing `VXLAN` (UDP/4789) and `ICMP` traffic in :menuselection:`Firewall --> Rules --> Loopback` and :menuselection:`Firewall --> Rules --> IPsec` is required. 


3. VXLAN Interface
------------------

- | Go to :menuselection:`Interfaces --> Other Types --> VXLAN` and create vxlan1 interfaces:
       
    - Site A: VNI: `1`, Source address: `172.16.88.1`, Destination address: `172.16.88.2`
    - Site B: VNI: `1`, Source address: `172.16.88.2`, Destination address: `172.16.88.1`
- | Go to :menuselection:`Interfaces --> Assignments` and assign ``vxlan1``. Do not assign interface IPs.


4. Bridging VXLAN and LAN
-------------------------

.. Attention:: Connecting Layer2 broadcast domains can cause service interruptions. 


- | Remove the IP configuration from `LAN`, it will be set directly on the bridge later. 
- | Go to :menuselection:`Interfaces --> Other Types --> Bridge`
- | Create a `bridge0` with `vxlan1` and the respective `LAN` interface on both `Sites`
- | Bridge specific tunables should be set for the packet filter: `LAN Bridge </manual/how-tos/lan_bridge.html#step-six>`_
- | Assign both bridges and set IPv4 addresses in the same subnet to both bridge interfaces:

       - Site A: `192.168.10.1/24`
       - Site B: `192.168.10.2/24`
- | Create firewall rules to allow traffic between the bridged interfaces. These rules must allow LAN to LAN traffic, e.g., source `192.168.10.0/24` to destination `192.168.10.0/24`. Starting with an any allow rule and restricting it after logging the traffic is recommended.
- | Only one firewall should be the DHCP server on the bridge
- | Set MTU to 1380 and MSS to 1320 on the bridge interfaces. This ensures packets are appropriately sized for the combined overhead from VXLAN and the VPN tunnel

5. Testing & Finalizing
-----------------------

- Test connectivity by pinging between the bridged networks amd from hosts connected to the bridge via LAN interface