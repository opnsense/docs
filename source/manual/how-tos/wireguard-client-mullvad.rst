=======================================
WireGuard MullvadVPN Road Warrior Setup
=======================================

------------
Introduction
------------

MullvadVPN is a cloud-based VPN provider, offering secure tunneling that respects your privacy. 
To set up a WireGuard VPN to MullvadVPN we assume you are familiar with the concepts of WireGuard and that
you have read the basic howto :doc:`wireguard-client`.

----------------------------------
Step 1 - Setup WireGuard Instance
----------------------------------

Go to the **Instances** tab and create a new instance. Give it a **Name** and set a desired **Listen Port**.
If you have more than one server instance be aware that you can use the **Listen Port** only once. In 
the field **Tunnel Address** insert an unsused private IP address and subnet mask. We don't need it in
the first step, but it will be required later. Every other field can be left blank.

Hit **Save** and open your instance again to write down your public key. You will need it to get the rest
of the configuration from the Mullvad API servers.

Now change to your OPNsense CLI via SSH or Console and execute *either* of the curl strings below. Please replace
**YOURACCOUNTNUMBER** with your own ID you got from MullvadVPN and **YOURPUBLICKEY** with the one in your **Instances**

The command below is for Mullvad's standard API. DNS requests through a tunnel that uses tunnel IPs generated via this API are "hijacked", so that Mullvad's DNS servers are used to avoid leaks:

.. code-block:: sh

    curl -sSL https://api.mullvad.net/wg/ -d account=YOURACCOUNTNUMBER --data-urlencode pubkey=YOURPUBLICKEY

The alternative command below is for Mullvad's other API. DNS requests through the tunnel are not hijacked when using tunnel IPs generated via this API:

.. code-block:: sh

	curl -sSL https://api.mullvad.net/app/v1/wireguard-keys -H "Content-Type: application/json" -H "Authorization: Token YOURACCOUNTNUMBER" -d '{"pubkey":"YOURPUBLICKEY"}'
    
What you receive is what WireGuard calls **Allowed IP** for your WireGuard Instance. Edit your instance again and remove
the value of **Tunnel Address** that you used when setting it up and change it to the one received from the command above.

In the **Peers** tab, create a new Peer and give it a **Name**, set 0.0.0.0/0 in **Allowed IPs** and set
the **DNS** to 193.138.218.74. This is the one MulladVPN provides for privacy.

Now go to Mullvad's server list_, set the filter to only `Wireguard` instances, and choose the one you like to use as your breakout. Write down it's
public key and set it as **Public Key**.

Also do not forget **Endpoint Address** and **Endpoint Port**. The **Endpoint Port** is 51820. The **Endpoint Address** will depend on which Mullvad server you wish to use. For example, if you want to use the "nl1-wireguard" server, the **Endpoint Address** will be :code:`nl1-wireguard.mullvad.net`.

.. _list: https://www.mullvad.net/en/servers/

Go back to tab **Instances**, open the instance and choose the newly created peer in **Peers**.

Now we can **Enable** the VPN in tab **General** and continue with the setup.

--------------------------------
Step 2 - Assignments and Routing
--------------------------------

To let your internal clients go through the tunnel, you must add a NAT entry. Go to 
:menuselection:`Firewall --> NAT --> Outbound` and add a rule. Check that rule generation is set to manual
or hybrid. Add a rule and select Wireguard as **Interface**. **Source** should be your
LAN network and set **Translation / target** to **interface address**.

When assigning interfaces we can also add gateways to them. This would offer you the chance to 
balance traffic via different VPN providers or do more complex routing scenarios.

See the how-to on selective routing for further information :doc:`wireguard-selective-routing`
