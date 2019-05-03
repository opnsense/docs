=======================================
WireGuard MullvadVPN Road Warrior Setup
=======================================

.. Warning::
    WireGuard Plugin is still in development, use at your own risk!
    
------------
Introduction
------------

MullvadVPN is a cloud-based VPN provider, offering secure tunneling in respect to privacy. 
To set up a WireGuard VPN to MullvadVPN we assume you are familiar with the concepts of WireGuard you that
you have read the basic howto :doc:`wireguard-client`.

----------------------------------
Step 1 - Setup WireGuard Instance
----------------------------------

Go to tab **Local** and create a new instance. Give it a **Name** and set a desired **Listen Port**. 
If you have more than one server instance be aware that you can use the **Listen Port** only once. In 
the field **Tunnel Address** insert an unsused private IP address and subnet mask. We don't need it in
the first step, but as it is required we can't go on without it. Every other field can be left blank.

Hit **Save** and open your instance again to write down your public key. You need it to get the rest
of the configuration from the Mullvad API servers. 

Now change to your OPNsense CLI via SSH or Console and execute the curl string below. Please replace the
**account** data with your own ID you got from MullvadVPN and **pubkey** with the one in your **Local**

.. code-block:: sh

    curl -sSL https://api.mullvad.net/wg/ -d account=123 --data-urlencode pubkey=PUBKEY
    
What you receive it the **Tunnel Addres** for your server instance, so edit your instance again, remove
the **Tunnel Address** you used when setting up and change it to the one you got.

On **Endpoint** tab create a new Endpoint, give it a **Name**, set 0.0.0.0/0 in **Tunnel Address** and set
the **DNS** to 193.138.219.228. This is the one MulladVPN provides for privacy.

Now go to the WireGuard server list_ and choose the one you like to use as your breakout. Write down it's
public key and set it as **Public Key**. Also don't forget **Endpoint Address** and **Endpoint Port**.

.. _list: https://www.mullvad.net/en/servers/#wireguard

Go back to tab **Local**, open the instance and choose the newly created endpoint in **Peers**.

Now we can **Enable** the VPN in tab **General** and continue with the setup.

--------------------------------
Step 2 - Assignments and Routing
--------------------------------

To let you internal clients go through the tunnel you have to add a NAT entry. Go to 
:menuselection:`Firewall --> NAT --> Outbound` and add a rule. Check that rule generation is set to manual
or hybrid. Add a rule and select Wireguard as **Interface**. **Source** should be your
LAN network and set **Translation / target** to **interface address**.

When assigning interfaces we can also add gateways to them. This would  offer you the chance to 
balance traffic via different VPN providers or do more complex routing scenarios. 



