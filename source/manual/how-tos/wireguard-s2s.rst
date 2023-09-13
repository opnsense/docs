============================
WireGuard Site-to-Site Setup
============================
    
------------
Introduction
------------

WireGuard is a simple and fast modern VPN protocol. It aims to be less complicated than IPSec, working more like ssh with private and public keys.
It has fewer lines of code and is more easily audited than other VPN protocols. Initially released for the Linux kernel, it is now cross-platform and widely deployable.

.. Attention::
    Wireguard is useful for simple routed site to site tunnels and roadwarrior setups. To this date, it doesn't play too nicely with high availability setups. That's because the peer may keep polling a stale interface and misinterpret the other instance as being the one that is down and keep sending traffic there. Also, because Wireguard is bound to all interfaces (and not explicitely the CARP VIP), both High Availability firewalls will send handshakes and fight against each other for the remote Wireguard peer. This behavior will probably be mitigated in 24.1 with Wireguard CARP vhid tracking. Using the protocol for critical workloads and high availability should be avoided in favor of IPsec.
    
.. Note::
    The following example covers an IPv4 Site to Site Wireguard Tunnel between two OPNsense Firewalls with public IPv4 addresses on their WAN interfaces. You will connect *Site A LAN Net* ``172.16.0.0/24`` to *Site B LAN Net* ``192.168.0.0/24`` using the *Wireguard Transfer Net* ``10.2.2.0/24``. *Site A Public IP* is ``203.0.113.1`` and *Site B Public IP* is ``203.0.113.2``.
    
.. Tip::
    You can also easily expand this Site to Site tunnel with IPv6 Global Unicast addresses (GUA) or Unique Local Addresses (ULA) to create a Dual Stack tunnel. Just add these IPv6 Networks (usually with /64 Prefix) to the *allowed IPs* and create Firewall rules to allow the traffic.

---------------------
Step 1 - Installation
---------------------

Install the os-wireguard plugin in :menuselection:`System --> Firmware --> Plugins`, refresh the GUI and you will soon find :menuselection:`VPN --> WireGuard`.

--------------------------------------------------
Step 2a - Setup WireGuard Local on OPNsense Site A
--------------------------------------------------

Go to tab **Local** and press **+** to create a new instance.

Enable the *advanced mode* toggle.

    ====================== ====================================================================================================
     **Enabled**            *Checked*
     **Name**               *wgopn-site-a*
     **Public Key**         *Generate with "Generate new keypair" button*
     **Private Key**        *Generates automatically*
     **Listen Port**        *51820*
     **MTU**                *1420 (default) or 1412 if you use PPPoE*
     **Tunnel Address**     *10.2.2.1/24*
     **Peers**              *Populated in later step*
    ====================== ==================================================================================================== 

Press **Save** and **Apply**.

--------------------------------------------------
Step 2b - Setup WireGuard Local on OPNsense Site B
--------------------------------------------------

Go to tab **Local** and press **+** to create a new instance.

Enable the *advanced mode* toggle.

    ====================== ====================================================================================================
     **Enabled**            *Checked*
     **Name**               *wgopn-site-b*
     **Public Key**         *Generate with "Generate new keypair" button*
     **Private Key**        *Generates automatically*
     **Listen Port**        *51820*
     **MTU**                *1420 (default) or 1412 if you use PPPoE*
     **Tunnel Address**     *10.2.2.2/24*
     **Peers**              *Populated in later step*
    ====================== ==================================================================================================== 

Press **Save** and **Apply**.

------------------------------------------------------
Step 3a - Setup WireGuard Endpoints on OPNsense Site A
------------------------------------------------------

Go to tab **Endpoints** and press **+** to create a new endpoint. 

Enable the *advanced mode* toggle.

    ====================== ====================================================================================================
     **Enabled**            *Checked*
     **Name**               *wgopn-site-b*
     **Public Key**         *Insert the public key of the local instance from wgopn-site-b*
     **Shared Secret**      *Leave empty*
     **Allowed IPs**        *10.2.2.2/32 192.168.0.0/24*
     **Endpoint Address**   *203.0.113.2*
     **Endpoint Port**      *51820*
    ====================== ==================================================================================================== 

Press **Save** and **Apply**.

Go to tab **Local** and edit *wgopn-site-a*.

    ====================== ====================================================================================================
     **Peers**              *wgopn-site-b*
    ====================== ==================================================================================================== 

Press **Save** and **Apply**.

------------------------------------------------------
Step 3b - Setup WireGuard Endpoints on OPNsense Site B
------------------------------------------------------

Go to tab **Endpoints** and press **+** to create a new endpoint. 

Enable the *advanced mode* toggle.

    ====================== ====================================================================================================
     **Enabled**            *Checked*
     **Name**               *wgopn-site-a*
     **Public Key**         *Insert the public key of the local instance from wgopn-site-a*
     **Shared Secret**      *Leave empty*
     **Allowed IPs**        *10.2.2.1/32 172.16.0.0/24*
     **Endpoint Address**   *203.0.113.1*
     **Endpoint Port**      *51820*
    ====================== ==================================================================================================== 

Press **Save** and **Apply**.

Go to tab **Local** and edit *wgopn-site-b*.

    ====================== ====================================================================================================
     **Peers**              *wgopn-site-a*
    ====================== ==================================================================================================== 

Press **Save** and **Apply**.

------------------------------
Step 4a - Setup Firewall Site A
------------------------------

Go to :menuselection:`Firewall --> Rules --> WAN` add a new rule to allow incoming wireguard traffic from Site B.

    ====================== ====================================================================================================
     **Action**             *Pass*
     **Interface**          *WAN*
     **Direction**          *In*
     **TCP/IP Version**     *IPv4*
     **Protocol**           *UDP*
     **Source**             *203.0.113.2*
     **Source port**        *51820*
     **Destination**        *203.0.113.1*
     **Destination port**   *51820*
     **Description**        *Allow Wireguard from Site B to Site A*    
    ====================== ==================================================================================================== 

Press **Save** and **Apply**.
    
Go to :menuselection:`Firewall --> Settings --> Normalization` and add a new rule to prevent fragmentation of traffic going through the wireguard tunnel.

    ============================ ==================================================================================================
     **Interface**                *WireGuard (Group)*
     **Direction**                *Any*
     **Protocol**                 *any*
     **Source**                   *any*
     **Destination**              *any*
     **Destination port**         *any*
     **Description**              *Wireguard MSS Clamping Site A*
     **Max mss**                  *1380 or lower, subtract at least 40 bytes from the Wireguard MTU*
    ============================ ==================================================================================================

.. Note::
    By creating the normalization rules, you ensure that IPv4 TCP can pass through the Wireguard tunnel without being fragmented. Otherwise you could get working ICMP and UDP, but some encrypted TCP sessions will refuse to work. If you want to use IPv6 TCP, lower the MSS by 60 bytes instead of 40 bytes.

-------------------------------
Step 4b - Setup Firewall Site B
-------------------------------

Go to :menuselection:`Firewall --> Rules --> WAN` add a new rule to allow incoming wireguard traffic from Site A.

    ====================== ====================================================================================================
     **Action**             *Pass*
     **Interface**          *WAN*
     **Direction**          *In*
     **TCP/IP Version**     *IPv4*
     **Protocol**           *UDP*
     **Source**             *203.0.113.1*
     **Source port**        *51820*
     **Destination**        *203.0.113.2*
     **Destination port**   *51820*
     **Description**        *Allow Wireguard from Site A to Site B*    
    ====================== ====================================================================================================
    
Press **Save** and **Apply**.

Go to :menuselection:`Firewall --> Settings --> Normalization` and add a new rule to prevent fragmentation of traffic going through the wireguard tunnel.

    ============================ ==================================================================================================
     **Interface**                *WireGuard (Group)*
     **Direction**                *Any*
     **Protocol**                 *any*
     **Source**                   *any*
     **Destination**              *any*
     **Destination port**         *any*
     **Description**              *Wireguard MSS Clamping Site B*
     **Max mss**                  *1380 or lower, subtract at least 40 bytes from the Wireguard MTU*
    ============================ ==================================================================================================

-----------------------------------------------
Step 4c - Enable Wireguard on Site A and Site B
-----------------------------------------------

Go to :menuselection:`VPN --> WireGuard --> Settings` on both Sites and **Enable WireGuard**

Press **Apply** and check :menuselection:`VPN --> WireGuard --> Diagnostics`. You should see *Send* and *Received* traffic and *Handshake* should be populated by a number.

Your tunnel is now up and running.

----------------------------------------------------------------
Step 5 - Allow traffic between Site A LAN Net and Site B LAN Net
----------------------------------------------------------------

Go to OPNsense Site A :menuselection:`Firewall --> Rules --> LAN A` add a new rule.

    ====================== ====================================================================================================
     **Action**             *Pass*
     **Interface**          *LAN A*
     **Direction**          *In*
     **TCP/IP Version**     *IPv4*
     **Protocol**           *Any*
     **Source**             *172.16.0.0/24*
     **Source port**        *Any*
     **Destination**        *192.168.0.0/24*
     **Destination port**   *Any*
     **Description**        *Allow LAN Site A to LAN Site B*    
    ====================== ====================================================================================================

Press **Save** and **Apply**.
    
Go to OPNsense Site A :menuselection:`Firewall --> Rules --> Wireguard (Group)` add a new rule.

    ====================== ====================================================================================================
     **Action**             *Pass*
     **Interface**          *Wireguard (Group)*
     **Direction**          *In*
     **TCP/IP Version**     *IPv4*
     **Protocol**           *Any*
     **Source**             *192.168.0.0/24*
     **Source port**        *Any*
     **Destination**        *172.16.0.0/24*
     **Destination port**   *Any*
     **Description**        *Allow LAN Site B to LAN Site A*    
    ====================== ====================================================================================================

Press **Save** and **Apply**.    Allowed IPs

Go to OPNsense Site B :menuselection:`Firewall --> Rules --> LAN A` add a new rule.

    ====================== ====================================================================================================
     **Action**             *Pass*
     **Interface**          *LAN B*
     **Direction**          *In*
     **TCP/IP Version**     *IPv4*
     **Protocol**           *Any*
     **Source**             *192.168.0.0/24*
     **Source port**        *Any*
     **Destination**        *172.16.0.0/24*
     **Destination port**   *Any*
     **Description**        *Allow LAN Site B to LAN Site A*    
    ====================== ====================================================================================================

Press **Save** and **Apply**.    

Go to OPNsense Site B :menuselection:`Firewall --> Rules --> Wireguard (Group)` add a new rule.

    ====================== ====================================================================================================
     **Action**             *Pass*
     **Interface**          *Wireguard (Group)*
     **Direction**          *In*
     **TCP/IP Version**     *IPv4*
     **Protocol**           *Any*
     **Source**             *172.16.0.0/24*
     **Source port**        *Any*
     **Destination**        *192.168.0.0/24*
     **Destination port**   *Any*
     **Description**        *Allow LAN Site A to LAN Site B*    
    ====================== ====================================================================================================

Press **Save** and **Apply**.

.. Note::
    Now both Sites have full access to the LAN of the other Site through the Wireguard Tunnel. For additional networks just add more **Allowed IPs** to the Wireguard Endpoints and adjust the firewall rules to allow the traffic.
