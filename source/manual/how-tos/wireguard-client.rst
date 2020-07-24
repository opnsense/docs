============================
WireGuard Road Warrior Setup
============================

------------
Introduction
------------

WireGuard is a simple, fast and modern VPN using modern `cryptography <https://www.WireGuard.com/protocol/>`. It aims to be faster and simpler then IPsec whilst also being considerably more performant OpenVPN. Initially released for the Linux kernel, it is now cross-platform and widely deployable. It is under heavy development and was included in the Linux kernel v5.6 in `March 2020 <https://arstechnica.com/gadgets/2020/03/WireGuard-vpn-makes-it-to-1-0-0-and-into-the-next-linux-kernel/>`. WireGuard is still experimental and should be used with caution.

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
 **Public Key**         (empty)            *Leave empty, keys will be automatically generated on save*
 **Private key**        (empty)            *Leave empty, keys will be automatically generated on save*
 **Listen Port**        51820              *Server listen port. If multiple servers exist, this port must be unique*
 **DNS Server**         1.1.1.1            *Populate as required with DNS server*
 **Tunnel Address**     10.10.10.1/24      *Use CIDR notation and avoid subnet overlap with regularly used networks*
 **Peers**              (empty)            *List of peers for this server, leave blank on initial configuration*
 **Disable Routes**     Unchecked          *This will prevent installing routes*
====================== =================== =====================================================================

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

Note - pressing **Save** effectively executes **wg-quick down wg0** followed by **wg-quick up wg0** (with 0 being the **Instance ID** of the server). Though not often required, sometimes it is useful to debug a tunnel not starting via the CLI using **wg show**. Configuration files are stored at **/usr/local/etc/wireguard/wgX.conf**.

------------------------
Step 2b - Setup Firewall
------------------------

To accept traffic from the internet, add a new rule on the WAN interface using :menuselection:`Firewall --> Rules` and allowing the server listen port configured previously (Protocol UDP). If more granular rules are required note there is a new interface **wg0** where these may be configured.

Connect to the tunnel from a client and verify connection via :menuselection:`VPN --> WireGuard` using the **List Configuration** and **Handshakes** tabs where peers are identified by their public keys. At this point the tunnel should be up and running but the client will have limited access.

---------------------------------
Step 2c - Assignments and Routing
---------------------------------

With this setup your clients can reach your internal networks when they add it via **Allowed IPs**.
But what if you want to push all traffic via VPN in order to filter some streams out of it?
Then we have to assign the interface via :menuselection:`Interface --> Assignments`, choose our instance (e.g. instance
0 is interface wg0), enable it, hit **Prevent Interface Removal** and don't configure an IP address.

After this we can go to :menuselection:`Firewall --> NAT --> Outbound` and add a rule. Check that rule generation is set
to manual or hybrid. Add a rule and select your WAN as **Interface**. **Source** should be the Tunnel
Network you use and **Translation / target** set to WAN address.

Now when you add 0.0.0.0/0 on your road warrior, outgoing packets are translated and reach the 
Internet via your VPN. 

When assigning interfaces we can also add gateways to them. This would offer you the chance to
balance traffic via different VPN providers or do more complex routing scenarios. 
To do this, go to :menuselection:`System --> Gateways --> Single` and add a new gateway. Choose your WireGuard interface
and set the Gateway to **dynamic**.

-------------------------------
Step 3 - Setup WireGuard Client
-------------------------------

The development of WireGuard is very dynamic so this howto won't include any screenshots since 
features are added rapidly or naming might change. 
If we have OPNsense also at the client side the configuration is similar to step 3a but you have to
choose **Allowed IPs** within the range of the server side and exchange public keys after 
the creation of a new instance. Then networks which should be routed via WireGuard have to be 
added to your **Allowed IPs** in the endpoint configuration of your client (e.g. 192.168.0.0/24 
when this is the LAN of the WireGuard server). For pushing all network traffic via VPN you can add
0.0.0.0/0. If you do this it's important to also specify a DNS server which will be added to your
interface. Therefore go to **Local**, edit your instance and fill in one or more IP addresses in
the **DNS** field. 



That's it!
