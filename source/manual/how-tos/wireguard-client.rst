============================
WireGuard Road Warrior Setup
============================

.. Warning::
    WireGuard Plugin is still in development, use at your own risk!
    
------------
Introduction
------------

WireGuard is a simple, fast and modern VPN. It aims to be faster and simpler than IPSec. It intends to be
considerably more performant than OpenVPN. Initially released for the Linux kernel, it is now cross-platform
and widely deployable. It is currently under heavy development. We will describe here how to set up
WireGuard as a central server or just as a client.

---------------------
Step 1 - Installation
---------------------

Since WireGuard Plugin is still in development you have to switch via :menuselection:`System --> Firmware --> Settings`
the **Release Type** to **Development**. After this go to :menuselection:`System --> Firmware --> Plugins` and search
for **os-wireguard-devel**.  Install the plugin as usual, refresh the page and you'll find the client 
via :menuselection:`VPN --> WireGuard`. If you do not want to switch to **Development** you can also go to console 
and type 

.. code-block:: sh

    pkg install os-wireguard-devel

--------------------------------
Step 2a - Setup WireGuard Server
--------------------------------

The setup of a central VPN server is very simple. Just go to tab **Local** and create a new instance.
Give it a **Name** and set a desired **Listen Port**. If you have more than one service instance be 
aware that you can use the **Listen Port** only once. For **Tunnel Address** choose an unused network
to tunnel all clients just like with OpenVPN or GRE (e.g. 192.168.0.1/24).
**Peers** can not be chosen yet since we have not created them yet. 
After hitting **Save changes** you can reopen the newly created instance, write down your new public
key and give it to the other side in a secure way (e.g. PGP encrypted or via SMS). 

Now go to tab **Endpoints** and add the fist road warrior, give it a **Name**, insert the **Public
Key** and the **Tunnel Address** (e.g. 192.168.0.2/24). **Endpoint Address** and  **Endpoint Port**
can be left empty since they are mostly dynamic, now hit **Save changes**.

Go back to tab **Local**, open the instance and choose the newly created endpoint in **Peers**.

Now we can **Enable** the VPN in tab **General** and continue with the setup.

If you want to add more users just add them in **Endpoints** and link them via **Peers**.

------------------------
Step 2b - Setup Firewall
------------------------

On :menuselection:`Firewall --> Rules` add a new rule on your WAN interface allowing the port you set in your
instance (Protocol UDP). You also have a new interace **Wireguard** in rules, where you can 
set granular rules on connection inside your tunnel.

Your tunnel is now up and running.

---------------------------------
Step 2c - Assignments and Routing
---------------------------------

With this setup your clients can reach your internal networks when they add it vial **Tunnel Address**.
But what if you want to push all traffic via VPN in order to filter some streams out of it?
Then we have to assign the interface via :menuselection:`Interface --> Assignments`, choose our instance (e.g. instance
0 is interface wg0), enable it, hit **Prevent Interface Removal** and don't configure an IP address.

After this we can go to :menuselection:`Firewall --> NAT --> Outbound` and add a rule. Check that rule generation is set
to manual or hybrid. Add a rule and select your WAN as **Interface**. **Source** should be the Tunnel
Network you use and **Translation / target** set to WAN address.

Now when you add 0.0.0.0/0 on your road warrior, outgoing packets are translated and reach the 
Internet via your VPN. 

When assigning interfaces we can also add gateways to them. This would  offer you the chance to 
balance traffic via different VPN providers or do more complex routing scenarios. 
To do this, go to :menuselection:`System --> Gateways --> Single` and add a new gateway. Choose your WireGuard interface
and set the Gateway to **dynamic**.

-------------------------------
Step 3 - Setup WireGuard Client
-------------------------------

The development of WireGuard is very dynamic so this howto won't include any screenshots since 
features are added rapidly or naming might change. 
If we have OPNsense also at the client side the configuration is similar to step 3a but you have to
choose a **Tunnel Address** within the range of the server side and exchange public keys after 
the creation of a new instance. Then networks which should be routed via WireGuard have to be 
added to your **Tunnel Address** in the endpoint configuration of your client (e.g. 192.168.0.0/24 
when this is the LAN of WireGuard server). For pushing all network traffic via VPN you can add 
0.0.0.0/0. If you do this it's important to also specifiy a DNS server which will be added to your
interface. Therefore go to **Local**, edit your instance and fill in one or more IP addresses to 
the **DNS** field. 



That's it!
