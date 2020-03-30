:orphan:

============================
WireGuard Site-to-Site Setup
============================
    
------------
Introduction
------------

WireGuard is a simple and fast modern VPN. It aims to be faster and simpler than IPSec. It intends to be
considerably more performant than OpenVPN. Initially released for the Linux kernel, it is now cross-platform
and widely deployable. It is currently under heavy development.

---------------------
Step 1 - Installation
---------------------

Install the plugin as usual, refresh and page and the you will find the client 
via :menuselection:`VPN --> WireGuard`.

------------------------
Step 2 - Setup WireGuard
------------------------

The setup of a Site-2-Site VPN is very simple. Just go to tab **Local** and create a new instance.
Give it a **Name** and set a desired **Listen Port**. If you have more than one service instance be 
aware that you can use the **Listen Port** only once. For **Tunnel Address** choose a new virtual 
network to run communication over it, just like with OpenVPN or GRE (e.g. 192.168.0.1/24).
**Peers** can not be chosen yet since we have not created them yet. 
After hitting **Save changes** you can reopen the newly created instance, write down your new public
key and give it to the other side. 

When this VPN is set up on OPNsense only do the same on the second machine and exchange the public
keys. Now go to tab **Endpoints** and add the remote site, give it a **Name**, insert the **Public
Key** and the **Allowed IPs** e.g. *192.168.0.2/32, 10.10.10.0/24*. This will set the remonte tunnel
IP address (/32 is important when using multiple endpoints) and route 10.10.10.0/24 via the tunnel. 
**Endpoint Address** is the public IP of the remote site and you can also set optionally the 
**Endpoint Port**, now hit **Save changes**.

Go back to tab **Local**, open the instance and choose the newly created endpoint in **Peers**.

Now we can **Enable** the VPN in tab **General** and go on with the setup.

-----------------------
Step 3 - Setup Firewall
-----------------------

On :menuselection:`Firewall --> Rules` add a new rule on your WAN interface allowing the port you set in your
instance (Protocol UDP). You also have a new interface **Wireguard** in rules, where you can
set granular rules on connections inside your tunnel.

Your tunnel is now up and running.

-------------------------
Step 4 - Routing networks
-------------------------

If you want to route your internal networks via this VPN just add the network in the field 
**Allowed IPs** in **Endpoints** tab (e.g. 10.0.1.0/24). 

That's it!
