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

Go to the **Instances** tab and create a new instance. Give it a **Name** and set a desired **Listen port**.
If you have more than one server instance be aware the **Listen port** must be unique for each instance. In
the field **Tunnel address** insert an unused private IP address and subnet mask. We don't need it in
the first step, but it will be required later. Every other field can be left blank.

Click **Save** and open your instance again to get your public key. You will need it to get the rest
of the configuration from the Mullvad API servers.

Now open the OPNsense CLI via SSH or the console and execute *either* of the curl commands below. Please replace
**YOURACCOUNTNUMBER** with your own ID you got from MullvadVPN and **YOURPUBLICKEY** with the one in your **Instances**

The command below is for Mullvad's standard API. DNS requests through a tunnel that uses tunnel IPs generated via this API are "hijacked", so that Mullvad's DNS servers are used to avoid leaks:

.. code-block:: sh

    curl -sSL https://api.mullvad.net/wg/ -d account=YOURACCOUNTNUMBER --data-urlencode pubkey=YOURPUBLICKEY

The alternative command below is for Mullvad's other API. DNS requests through the tunnel are not hijacked when using tunnel IPs generated via this API:

.. code-block:: sh

	curl -sSL https://api.mullvad.net/app/v1/wireguard-keys -H "Content-Type: application/json" -H "Authorization: Token YOURACCOUNTNUMBER" -d '{"pubkey":"YOURPUBLICKEY"}'
    
The response is the **Allowed IP** for your WireGuard Instance. Edit your instance again and remove
the value of **Tunnel address** that you used when setting it up and change it to the one received from the command above.

--------------------------------
Step 2 - Setup WireGuard Peer
--------------------------------

In the **Peers** tab, create a new Peer and give it a **Name**, then set 0.0.0.0/0 in **Allowed IPs**.

Now go to Mullvad's server list_, set the filter to only `WireGuard` instances, and choose the one you like to use as your breakout. Set the server's public key and as **Public key**.

Set **Endpoint address** with the "Domain name" value in the server list and **Endpoint port** to 51820, WireGuard's default listening port.
As an example: for the "nl1-wireguard" server, the **Endpoint Address** will be :code:`nl1-wireguard.mullvad.net`.
In the **Instances** dropdown, select the instance created previously and click **Save**.

.. _list: https://www.mullvad.net/en/servers/

Now we **Enable** WireGuard in the **General** tab and continue with the setup.

--------------------------------
Step 3 - Configure NAT
--------------------------------

To allow your internal clients through the tunnel, you must add a NAT entry. Go to 
:menuselection:`Firewall --> NAT --> Outbound`, ensure that rule generation is set to either manual
or hybrid. Add a new rule and select WireGuard as **Interface**. Set **Source** to your
LAN network and **Translation / target** to **Interface address**.

When assigning interfaces we can also add gateways to them. This would offer you the chance to 
balance traffic via different VPN providers or do more complex routing scenarios.

See the how-to on selective routing for further information :doc:`wireguard-selective-routing`

--------------------------------
Step 4 - Conclusion
--------------------------------

At this point, you should have a working connection and be able to pass the Mullvad connection test found on their website.
If your configuration does not work or does not pass, a good place to start investigating is `VPN --> WireGuard --> Log file`.
