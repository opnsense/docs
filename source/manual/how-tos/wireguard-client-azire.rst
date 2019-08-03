=====================================
WireGuard AzireVPN Road Warrior Setup
=====================================
    
------------
Introduction
------------

AzireVPN is an international VPN provider, co-locating in multiple datacenters and offering secure
tunneling in respect to privacy. To set up a WireGuard VPN to AzireVPN we assume you are familiar
with the concepts of WireGuard you that you have read the basic howto :doc:`wireguard-client`.

-----------------------------------
Step 1 - Get AzireVPN configuration
-----------------------------------

For an automated rollout of configuration, AzireVPN will create a private key in your browser and send
the public key via an API call to their servers.
To get a configuration login to your account_

.. _account: https://www.azirevpn.com/cfg/wireguard

Via **Options** you can select the country where you want to break out, choose a port (default ist fine),
and set the protocol to tunnel (we only cover IPv4).

Hit **Download** at the end of the page to get the preconfigured text file and open it in your
favorite text editor. 

----------------------------------
Step 2 - Setup WireGuard Instance
----------------------------------

Go to tab **Local** and create a new instance. Give it a **Name** and set a desired **Listen Port**. 
If you have more than one server instance be aware that you can use the **Listen Port** only once. In 
the field **Private Key** insert the value from your text file and leave **Public Key** empty. **DNS** 
and **Tunnel Address** has also to be taken from the configuration. Hit **Save** and go to **Endpoint** 
tab.

On **Endpoint** tab create a new Endpoint, give it a **Name**, set 0.0.0.0/0 in **Allowed IPs** and set
the DNS name from your configuration in **Endpoint Address**. Don't forget to do this also for the port.

Go back to tab **Local**, open the instance and choose the newly created endpoint in **Peers**.

Now we can **Enable** the VPN in tab **General** and continue with the setup.

--------------------------------
Step 3 - Assignments and Routing
--------------------------------

To let you internal clients go through the tunnel you have to add a NAT entry. Go to 
:menuselection:`Firewall --> NAT --> Outbound` and add a rule. Check that rule generation is set to manual
or hybrid. Add a rule and select Wireguard as **Interface**. **Source** should be your
LAN network and set **Translation / target** to **interface address**.

When assigning interfaces we can also add gateways to them. This would  offer you the chance to 
balance traffic via different VPN providers or do more complex routing scenarios. 



