============================
WireGuard Road Warrior Setup
============================

.. Warning::
    **IMPORTANT NOTE** :
    WireGuard Plugin is still in development, use at your own risk!
    
------------
Introduction
------------

WireGuard is a simple and fast modern VPN. It aims to be faster and simpler than IPSec. It intends to be
considerably more performant than OpenVPN. Initially released for the Linux kernel, it is now cross-platform
and widely deployable. It is currently under heavy development. We will describe here how to set up
WireGuard as a central server or just as a client.

---------------------
Step 1 - Installation
---------------------

Since WireGuard Plugin is still in development you have to switch via **System->Firmware->Settings** 
the **Release Type** to **Development**. After this go to **System->Firmware->Plugins->** and search 
for **os-wireguard-devel**.  Install the plugin as usual, refresh and page and the you'll find the client 
via **VPN->WireGuard**.

--------------------------------
Step 2a - Setup WireGuard Server
--------------------------------

The setup of a central VPN server is very simple. Just go to tab **Server** and create a new instance.
Give it a **Name** and set a desired **Listen Port**. If you have more than one server instance be 
aware that you can use the **Listen Port** only once. For **Tunnel Address** choose a new virtual 
network to run communication over it, just like with OpenVPN or GRE (e.g. 192.168.0.1/24).
**Peers** can not be chosen yet since we have not created them yet. 
After hitting **Save changes** you can reopen the newly created instance, write down your new public
key and give it to the other side. 

Now go to tab **Endpoints** and add the fist road warrior, give it a **Name**, insert the **Public
Key** and the **Tunnel Address** (e.g. 192.168.0.2/24). **Endpoint Address** and  **Endpoint Port**
can be left empty since they are mostly dynamic, now hit **Save changes**.

Go back to tab **Server**, open the instance and choose the newly created endpoint in **Peers**.

Now we can **Enable** the VPN in tab **General** and go on with the setup.

If you want to add more users just add them in **Endpoints** and link them via **Peers**.

------------------------
Step 2b - Setup Firewall
------------------------

On **Firewall->Rules** add a new rule on your WAN interface allowing the port you set in your
instance (Protocol UDP). You also have a new interace **Wireguard** in rules, where you can 
set granular rules on connection inside your tunnel.

Your tunnel is now up and running.

---------------------------------
Step 2c - Assignments and Routing
---------------------------------

With this setup your clients can reach your internal networks when they add it vial **Tunnel Address**.
But what if you want to push all traffic via VPN in order to filter some streams out of it?
Then we have to assign the interface via **Interface->Assignments**, choose our instance (e.g. instance
0 is interface wg0), enable it, hit **Prevent Interface Removal** and don't configure an IP address.

After ths we can go to **Firewall->NAT->Outbound** and add a rule. Check that rule generation is set
to manual or hybrid. Add a rule and select your WAN as **Interface**. **Source** should be the Tunnel
Network you use and **Translation / target** set to WAN address.

Now when you add 0.0.0.0/0 on your road warrior, outgoing packets are translated and reach the 
Internet via your VPN. 

When assigning interfaces we can also add gateways to them. This would  offer you the chance to 
balance traffic via different VPN providers or do more complex routing scenarios. 
To do this, go to **System->Gateways->Single** and add a new gateway. Choose your WireGuard interface
and set the Gateway to **dynamic**.

-------------------------
Step 4 - Routing networks
-------------------------

If you want to route your internal networks via this VPN just add the network in the 
**Tunnel Address** in **Endpoints** tab (e.g. 10.0.1.0/24). 

That's it!
