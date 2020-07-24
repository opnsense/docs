============================
WireGuard Road Warrior Setup
============================

------------
Introduction
------------

WireGuard is a simple, fast VPN using modern `cryptography <https://www.WireGuard.com/protocol>`__. It aims to be faster and simpler than IPsec whilst also being a considerably more performant alternative to OpenVPN. Initially released for the Linux kernel, it is now cross-platform and widely deployable. It is under heavy development and was included in the Linux kernel v5.6 in `March 2020 <https://arstechnica.com/gadgets/2020/03/WireGuard-vpn-makes-it-to-1-0-0-and-into-the-next-linux-kernel>`__. 

.. Warning::

    WireGuard is still experimental and should be used with caution.

This article describes setting up a central WireGuard server, running on OPNsense and configuring a client. 

---------------------
Step 1 - Installation
---------------------

Install the plugin via :menuselection:`System --> Firmware --> Plugins` and selecting the package **os-WireGuard**.

Once the plugin is installed, refresh the page and you will find the WireGuard configuration menu via :menuselection:`VPN --> WireGuard`.

--------------------------------
Step 2a - Setup WireGuard Server
--------------------------------

First, create a WireGuard VPN server via :menuselection:`VPN --> WireGuard` under the **Local** tab. Create a new instance using the **+** button and customizing the following values as neccessary:

====================== =================== =====================================================================
 **Enabled**            Checked            *Check to enable the server*
 **Name**               WireGuard          *The name of the server instance*
 **Instance**           (auto populated)   *Automatically generated server instance number*
 **Public Key**         (empty)            *Leave empty, keys will be automatically generated*
 **Private key**        (empty)            *Leave empty, keys will be automatically generated*
 **Listen Port**        51820              *Server listen port. If multiple servers exist, this port must be unique*
 **DNS Server**         192.168.1.254      *Populate as required with DNS server*
 **Tunnel Address**     10.10.10.1/24      *Use CIDR notation and avoid subnet overlap with regularly used networks*
 **Peers**              (empty)            *List of peers for this server, leave blank on initial configuration*
 **Disable Routes**     Unchecked          *This will prevent installing routes*
====================== =================== =====================================================================

.. Warning::

    Ensure that **Tunnel Address** is a /24 or the desired CIDR notated subnet mask, do not use /32.

Once the tunnel is created after clicking **Save**, reopen the newly created instance and take note of the public key that was just generated. This key will be required when setting up any client that wishes to connect to this server. Make sure to protect it and use secure transmission methods to clients (e.g. PGP encrypted or via SMS).

Use the **Endpoints** tab to add the first client. Use the **+** button and configure the following:

====================== =================== =====================================================================
 **Enabled**            Checked            *Check to enable the server*
 **Name**               client1            *The name of the client*
 **Public Key**         PubKey             *Provide public key from client*
 **Shared Secret**      (empty)            *optional - shared secret (PSK) for this peer*
 **AllowedIPs**         10.10.10.2/32      *IP address of client (peer) - ensure to use /32 with multiple clients*
 **Endpoint Address**   (empty)            *Not required for inbound connections - dynamic*
 **Endpoint Port**      (empty)            *Not required for inbound connections - dynamic*
 **Keepalive**          (empty)            *optional - sets persistent keepalive interval*
====================== =================== =====================================================================

Click **Save** and return to the **Local** tab. Now select the newly created peer under **Peers**. Click **Save**.

Next, enable WireGuard under the **General** tab and continue with the setup. Add further clients under **Endpoints** and allow them to access the **Wireguard** server by selecting them under **Peers**. 

.. Hint:: 

    Pressing **Save** effectively executes :code:`wg-quick down wg0` followed by :code:`wg-quick up wg0` (with 0 being the **Instance ID** of the server). Though not often required, sometimes it is useful to debug a tunnel not starting via the CLI using :code:`wg show`. Configuration files are stored at :code:`/usr/local/etc/wireguard/wgX.conf`.

------------------------------
Step 2b - Setup Firewall rules
------------------------------

To accept connections from clients which are outside the LAN firewall rules must be created to permit that traffic to flow from WAN to LAN. Select :menuselection:`Firewall --> NAT --> Port Forward` and click **+Add** creating a rule with the following information:

=========================== ================ =====================================================================
 **Interface**               WAN              *The interface this rule applies to*
 **TCP/IP Version**          IPv4             *Select the Internet Protocol version this rule applies to*
 **Protocol**                UDP              *WireGuard works over UDP*
 **Source**                  *                *Accept traffic from any source*
 **Source Port**             *                *Accept traffic on any port*
 **Destination**             WAN address      *Traffic destination*
 **Destination Port**        51820            *Specify the port or port range required*
 **Redirect target IP**      192.168.1.254    *The LAN IP of the firewall*
 **Redirect target port**    51820            *The listen port for WireGuard server*
 **Description**             WG WAN to LAN    *Optional - provide a description*
=========================== ================ ===================================================================== 

If more granular rules are required note there is a new interface **wg0** where these may be configured.

The final piece is to allow traffic from the Wireguard network. Do this via :menuselection:`Firewall --> Rules --> WireGuard` and click **+Add** with the following information (if an item is not specified, leave it set to the default value):

=========================== ================ =====================================================================
 **Interface**               WireGuard        *The interface this rule applies to*
 **Source**                  WireGuard net    *Source subnet*
 **Destination**             any              *Traffic destination*
 **Description**             WG WAN to LAN    *Optional - provide a description*
=========================== ================ =====================================================================

.. Hint::

    Rules defined under :menuselection:`Firewall --> Rules --> WireGuard` take precedence over rules individually configured for each tunnel.

Connect to the tunnel from a client and verify connection via :menuselection:`VPN --> WireGuard` using the **List Configuration** and **Handshakes** tabs where peers are identified by their public keys. At this point the tunnel should be up and running but the client will have limited access.

---------------------------------
Step 2c - Assignments and Routing
---------------------------------

Thus far, the setup documented here permits your clients to reach the internal networks configured via **Allowed IPs**. However, a common use case is that users wish to push all traffic through a VPN tunnel. To do this assign WireGuard an interface via :menuselection:`Interfaces --> Assignments` and select the wgX instance from the **New interface** dropdown menu. Click **+** to assign the interface. Once assigned, click **Save**.

Rename the interface as required and select **Prevent Interface Removal** by selecting the interface from the :menuselection:`Interfaces -> [wgX]` list. Do not assign the interface an IP address.

The next step is to configure Outbound NAT. Go to :menuselection:`Firewall --> NAT --> Outbound` and add a rule. First, ensure that rule generation is set to manual or hybrid (if unsure, select hybrid). Add a rule (via **+Add** in the top right) with the following values (unless explictly mentioned below, leave as default):

=========================== ================ =====================================================================
 **Interface**               WAN              *The interface the rule applies to*
 **Source address**          wg0 net          *Tunnel Network configured previously*
 **Translation / target**    WAN address      *Packets matching this rule will be mapped to the IP address given here*
=========================== ================ ===================================================================== 

To reach the Internet from a client via the VPN configure configure **AllowedIPs** to 0.0.0.0/0.

When assigning interfaces, gateways can be added to them. This is useful if balancing traffic across multiple VPNs is required or in more complex routing scenarios.
 
To do this, go to :menuselection:`System --> Gateways --> Single` and add a new gateway. Choose the relevant WireGuard interface
and set the Gateway to **dynamic**.

-------------------------------
Step 3 - Setup WireGuard Client
-------------------------------

.. Tip::

    Key generation can be performed on any device with `WireGuard client tools <https://www.wireguard.com/install>`__ installed. A one-liner for generating a matching private and public keypair is :code:`wg genkey | tee private.key | wg pubkey > public.key`.

Client configuration is largely beyond the scope of this article since there is such a wide array of possible targets. However, the key pieces of information required to configure a client are: 

* Address - *Server side this is referred to as **Tunnel Address***
* DNS - *DNS server*
* Endpoint - *DNS entry or IP supported, include the port here*
* Public Key - *Refers to Public Key of the WireGuard server*
* AllowedIPs - *Configure which traffic (by subnet) is sent via the tunnel*

-------------------------------
Appendix A - Example configurations
-------------------------------

.. Warning::

    Note that WireGuard is still under heavy development and these configurations may change without warning. They are provided for guidance only. 
    
    **Do not reuse these example keys!**

An example Client configuration file:

.. code-block:: none

    [Interface]
    PrivateKey = 8GboYh0YF3q/hJhoPFoL3HM/ObgOuC8YI6UXWsgWL2M=
    Address = 10.10.10.2/32
    DNS = 192.168.1.254

    [Peer]
    PublicKey = OwdegSTyhlpw7Dbpg8VSUBKXF9CxoQp2gAOdwgqtPVI=
    AllowedIPs = 0.0.0.0/0
    Endpoint = vpn.example.com:51820


An example Server configuration file:

.. code-block:: none

    [Interface]
    Address = 10.10.10.1/24
    DNS = 192.168.1.254
    ListenPort = 51820
    PrivateKey = YNqHwpcAmVj0lVzPSt3oUnL7cRPKB/geVxccs0C0kk0=
    [Peer]
    PublicKey = CLnGaiAfyf6kTBJKh0M529MnlqfFqoWJ5K4IAJ2+X08=
    AllowedIPs = 10.10.10.2/32