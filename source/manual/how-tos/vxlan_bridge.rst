============================
VXLAN Bridge
============================

.. contents:: Index


----------------------------
Summary
----------------------------

This guide covers the configuration of a VXLAN tunnel between two OPNsense firewalls connected via VPN. This enables Layer 2 communication over Layer 3 networks and can introduce various challenges. Layer 2 tunneling should only be used when necessary, as routing is usually the best option for Layer 3 networks.

Here are some general use cases:

- Use the same IP addresses and internet breakout on multiple sites
- Provide external IP addresses to a different site without routing
- Connect devices that communicate via broadcasts
- Share Layer 2 protocols such as STP and DHCP
- Transmit routing protocols like OSPF


.. Attention:: 

    - | A large broadcast domain will create more broadcast and multicast traffic. This can quickly saturate WAN links since it will be exchanged over the internet with Layer 2 tunneling
    - | Switches need special attention. Layer 2 protocols like STP will now be shared over the VXLAN tunnel. The Switch should filter specific Layer 2 protocols to prevent improper STP convergence. DHCP could also be filtered with the Switch, so different DHCP servers can be used
    - | Bridges, VXLAN and VPN introduce overhead, which can increase CPU usage and limit bandwidth. This configuration is not suitable for high-throughput environments where gigabits of traffic are required
    - | If e.g., `Site B` uses the bridged LAN as their main network, all traffic will be sent to `Site A` for routing and breakout to the internet. Please be aware of the implications

See the section on `VXLAN </manual/other-interfaces.html#vxlan>`_ for more details.


----------------------------
Setup Overview
----------------------------

In this setup example, there are two OPNsense firewalls - Site A and Site B - that should communicate over the internet via Layer2.

Since VXLAN is not encrypted, a VPN should be used to secure the connection. IPsec or Wireguard are recommended, since they can create simple point to point VPNs between loopback interfaces.

===============  ================  ================
**Interface**    **Site A**        **Site B**
===============  ================  ================
WAN              203.0.113.1/32    198.51.100.2/32
lo1              172.16.88.1/32    172.16.88.2/32
bridge0          192.168.10.1/24   192.168.10.2/24
vxlan1           IPv4 None         IPv4 None
LAN              IPv4 None         IPv4 None
===============  ================  ================


----------------------------
Configuration
----------------------------


1. Loopback Interface Setup
----------------------------
   
- | Go to :menuselection:`Interfaces --> Devices --> Loopback` and add ``lo1`` on both `Sites`
- | Go to :menuselection:`Interfaces --> Assignments` and assign ``lo1``
- | Enable ``lo1`` and set a static IPv4 configuration:
       
    - Site A: `172.16.88.1/32`
    - Site B: `172.16.88.2/32`
     
.. Note:: These loopback interfaces will be used for the VXLAN source and remote addresses. Loopback interfaces are always available for service binding during boot.


2. VPN Setup
----------------------------

The ``lo1`` interfaces on both firewalls must be connected via VPN. In this example, the VPN will use the endpoint IPs `203.0.113.1/32 (Site A)` and `198.51.100.2/32 (Site B)`. This can be achieved with:

    - | A policy-based IPsec tunnel, including the loopback IPs in Phase 2 `Children`:
        
        - `172.16.88.1/32` on Site B
        - `172.16.88.2/32` on Site A
    - | A WireGuard tunnel without a `Tunnel address`, including the loopback IPs in `Allowed IPs`:

        - `172.16.88.1/32` on Site B
        - `172.16.88.2/32` on Site A
    - | Any other VPN protocol since VXLAN is VPN agnostic

Create Firewall rules that allow `VXLAN` (UDP/4789) and `ICMP` traffic for:

    - :menuselection:`Firewall --> Rules --> Loopback`
    - :menuselection:`Firewall --> Rules --> IPsec` (or Wireguard)

The tunnel should now route traffic between the two loopback interfaces:

    - Go to :menuselection:`Interfaces --> Diagnostics --> Ping`
    - Test connectivity by pinging the loopback interfaces across the tunnel. Use the ``lo1`` interface address as source address.


3. VXLAN Interface
----------------------------

- | Go to :menuselection:`Interfaces --> Devices --> VXLAN` and create ``vxlan1`` interfaces:
       
===============  ================  ================
**Option**       **Site A**        **Site B**
===============  ================  ================
VNI              1                 1
Source address   172.16.88.1/32    172.16.88.2/32
Remote address   172.16.88.2/32    172.16.88.1/32
Multicast group  `leave empty`     `leave empty`
Device           None              None
===============  ================  ================

- Go to :menuselection:`Interfaces --> Assignments` and assign ``vxlan1``.

.. Note:: Do not assign IP addresses to the ``vxlan1`` interfaces.


4. Bridging VXLAN and LAN
----------------------------

.. Attention:: Connecting Layer2 broadcast domains can cause service interruptions.


- | Remove the IP configuration from ``LAN``, it will be moved to ``bridge0``
- | Go to :menuselection:`Interfaces --> Devices --> Bridge` and create ``bridge0`` interfaces:

==================  =====================  =====================
**Option**          **Site A**             **Site B**
==================  =====================  =====================
Member interfaces   ``LAN, vxlan1``        ``LAN, vxlan1``
Description         ``bridge0``            ``bridge0``
Link-local address  `Check if using IPv6`  `Check if using IPv6`
==================  =====================  =====================

- | Bridge specific tunables must set for the packet filter: `LAN Bridge </manual/how-tos/lan_bridge.html#step-six>`_
- | Assign and enable ``bridge0`` and set IPv4 addresses in the same subnet:

       - Site A: `192.168.10.1/24`
       - Site B: `192.168.10.2/24`
- | Create firewall rules to allow traffic between the bridged interfaces:

    - These rules must allow LAN to LAN traffic, e.g., source `192.168.10.0/24` to destination `192.168.10.0/24`.
    - Starting with an any allow rule and restricting it after logging is recommended.
- | If experiencing packet fragmentation issues, set the MTU to 1380 and MSS to 1320 on the ``bridge0`` interfaces. This ensures packets are appropriately sized for the combined overhead from VXLAN and the VPN tunnel. This should not be needed if PMTU (Path MTU Discovery) works correctly. It is essential that ICMP is allowed.

.. Note:: Only the main `Site` should be the DHCP server on ``bridge0``. If you want to use different DHCP servers per `Site`, use external ones and block the DHCP packets on your managed switch before they enter the OPNsense ``LAN`` interface. Ensure that no IP address conflicts emerge with seperate pools in the same IP address space.


5. Testing & Finalizing
----------------------------

.. Tip:: For this step, using `Packet Capture </manual/diagnostics_interfaces.html#packet-capture>`_ is recommended.

#. | Test connectivity by pinging between the IP addresses of ``bridge0``
#. | Use `Packet Capture` to see if the `ARP protocol` has the same broadcasts on both ``bridge0`` interfaces
#. | Go to :menuselection:`Interfaces --> Diagnostics --> ARP Table` and check if `MAC addresses` from both `Sites` have been learned
#. | Ping directly between hosts through the VXLAN tunnel. Check with `Packet Capture` if `ARP` resolves the `MAC addresses` of these hosts and adds them into their `ARP tables`
#. | Test the maximum packet size when pinging through the tunnel by specifying custom packet sizes and setting the `do not fragment` flag
#. | Use tools like `tcpdump` or `Wireshark` directly on the hosts and initiate traffic to and from destinations to either `Site`
#. | Test the performance between `Site A` and `Site B` with `iperf3`. If it is very slow, check the MTU/MSS settings, WAN link speed and CPU usage

.. Note:: These are some of the basic tests. If there are issues revisit each step of this setup guide. Since Layer 2 over Layer 3 tunnels can be brittle, there are a multitude of issues that often need to be resolved by network experts. When issues can not be resolved, using Layer 3 VPN routing between `Sites` is the best and most stable alternative.
