=================================================================
WireGuard Selective Routing to External VPN Provider
=================================================================

------------
Introduction
------------

This how-to is designed to assist with setting up WireGuard on OPNsense to use selective routing to an external VPN provider.

These circumstances may apply where only certain local hosts are intended to use the VPN tunnel. Or it could apply where multiple connections to the VPN provider are desired, with each connection intended to be used by different specific local hosts.

This how-to focuses on the configuration of OPNsense. You will also have to configure the peer at your VPN provider - consult your VPN provider’s documentation as to how to do that.

Your OPNsense local public key will need to be registered with your VPN provider, and you will need to get your VPN provider’s endpoint public key and the VPN tunnel IP provided for your local peer by your VPN provider. In some cases, you will not be able to get the endpoint public key and VPN tunnel IP until you register your local public key. In that case, create the OPNsense local configuration first, using a dummy tunnel IP and no peer selected, so that the public key is generated, and then update the configuration later once the other information is known.

For an example of configuring the peer at a VPN provider (Mullvad), see Step 1 of the how-to :doc:`wireguard-client-mullvad`.

This how-to discusses IPv4 configuration only. It can be readily adapted for IPv6 as well.

-------------------------------
Step 1 - Configure the endpoint
-------------------------------

- Go to :menuselection:`VPN --> WireGuard --> Endpoints`
- Click **+** to add a new Endpoint
- Configure the Endpoint as follows (if an option is not mentioned below, leave it as the default):

    ====================== ====================================================================================================
     **Enabled**            *Checked*
     **Name**               *Call it whatever you want (eg* :code:`VPNProviderName_Location` *)*
     **Public Key**         *Insert the public key from your VPN provider*
     **Allowed IPs**        *0.0.0.0/0*
     **Endpoint Address**   *Insert the public IP address (desirably) or domain name of your VPN provider, as provided by it*
     **Endpoint Port**      *Insert the port of your VPN provider, as provided by it*
     **Keepalive**          *25*
    ====================== ====================================================================================================

- **Save** the Endpoint configuration, and then click **Save** again

---------------------------------
Step 2 - Configure the local peer
---------------------------------

- Go to :menuselection:`VPN --> WireGuard --> Local`
- Click **+** to add a new Local configuration
- Turn on “advanced mode"
- Configure the Local configuration as follows (if an option is not mentioned below, leave it as the default):

    ===================== ===============================================================================================
     **Enabled**           *Checked*
     **Name**              *Call it whatever you want (eg* :code:`VPNProviderName` *)*
     **Public Key**        *This will initially be blank; it will be populated once the configuration is saved*
     **Private Key**       *This will initially be blank; it will be populated once the configuration is saved*
     **Listen Port**       *51820 or a higher numbered unique port*
     **DNS Server**        *Leave this blank*
     **Tunnel Address**    *Insert the VPN tunnel IP provided by your VPN provider, in CIDR format, eg 10.24.24.10/32*
     **Peers**             *In the dropdown, select the Endpoint you configured above*
     **Disable Routes**    *Checked*
     **Gateway**           *Specify an IP that is 1 number below your VPN tunnel IP, eg 10.24.24.9 - see note below*
    ===================== ===============================================================================================

.. Note::

    The IP you choose for the Gateway is essentially arbitrary; pretty much any unique IP will do. The suggestion here is for convenience and to avoid conflicts

- **Save** the local peer configuration, and then click **Save** again

--------------------------
Step 3 - Turn on WireGuard
--------------------------

Turn on WireGuard under :menuselection:`VPN --> WireGuard --> General` if it is not already on

-------------------------------------------------------
Step 4 - Assign an interface to WireGuard and enable it
-------------------------------------------------------

- Go to :menuselection:`Interfaces --> Assignments`
- In the dropdown next to “New interface:”, select the WireGuard device (:code:`wg0` if this is your first one)
- Add a description (eg :code:`WAN_VPNProviderName`)
- Click **+** to add it, then click **Save**
- Then select your new interface under the Interfaces menu
- Configure it as follows (if an option is not mentioned below, leave it as the default):

    ============================= ===================================================================
     **Enable**                    *Checked*
     **Lock**                      *Checked if you wish to*
     **Description**               *Same as under Assignments, if this box is not already populated*
     **IPv4 Configuration Type**   *None*
     **IPv6 Configuration Type**   *None*
    ============================= ===================================================================

- **Save** the interface configuration and then click **Apply changes**

--------------------------
Step 5 - Restart WireGuard
--------------------------

Now restart WireGuard - you can do this from the Dashboard (if you have the services widget) or by turning it off and on under :menuselection:`VPN --> WireGuard --> General`

-------------------------
Step 6 - Create a gateway
-------------------------

- Go to :menuselection:`System --> Gateways --> Single`
- Click **Add**
- Configure the gateway as follows (if an option is not mentioned below, leave it as the default):

    ================================ ============================================================================================
     **Name**                         *Call it whatever you want, easiest to name it the same as the interface*
     **Description**                  *Add one if you wish to*
     **Interface**                    *Select your newly created interface in the dropdown*
     **Address Family**               *Select IPv4 in the dropdown*
     **IP address**                   *Insert the gateway IP that you configured under the WireGuard local peer configuration*
     **Far Gateway**                  *Checked*
     **Disable Gateway Monitoring**   *Unchecked*
     **Monitor IP**                   *Insert the endpoint VPN tunnel IP (NOT the public IP) of your VPN provider - see note below*
    ================================ ============================================================================================

.. Note::

    Specifying the endpoint VPN tunnel IP is preferable. As an alternative, you could include an external IP such as 1.1.1.1 or 8.8.8.8, but be aware that this IP will *only* be accessible through the VPN tunnel (OPNsense creates a static route for it), and therefore will not accessible from local hosts that are not using the tunnel

- **Save** the gateway configuration and then click **Apply changes**

---------------------------------------------------------------------------------
Step 7 - Create an Alias for the relevant local hosts that will access the tunnel
---------------------------------------------------------------------------------

- Go to :menuselection:`Firewall --> Aliases`
- Click **+** to add a new Alias
- Configure the Alias as follows (if an option is not mentioned below, leave it as the default):

    ================= ==================================================================================================
     **Enabled**       *Checked*
     **Name**          *Call it whatever your want, eg* :code:`WG_VPN_Hosts`
     **Type**          *Select either Host(s) or Network(s) in the dropdown, depending on whether you want specific host IPs to use the tunnel, or an entire local network (such as a VLAN)*
     **Content**       *Enter the host IPs, or the network in CIDR format*
     **Description**   *Add one if you wish to*
    ================= ==================================================================================================

- **Save** the Alias, and then click **Apply**

-------------------------------
Step 8 - Create a firewall rule
-------------------------------

This will involve two steps - first creating a second Alias for all local (private) networks, and then creating the firewall rule itself. The ultimate effect of these two steps is that only traffic from the relevant hosts that is destined for **non-local** destinations will be sent down the tunnel. This will ensure that the relevant hosts can still access local resources

It should be noted, however, that if the hosts that will use the tunnel are configured to use local DNS servers (such as OPNsense itself or another local DNS server), then this configuration will likely result in DNS leaks - that is, DNS requests for the hosts will continue to be processed through the normal WAN gateway, rather than through the tunnel. See the section at the end of this how-to for a discussion of potential solutions to this

- First go to :menuselection:`Firewall --> Aliases`
- Click **+** to add a new Alias
- Configure the Alias as follows (if an option is not mentioned below, leave it as the default):

    ================= ================================================
     **Enabled**       *Checked*
     **Name**          *RFC1918_Networks*
     **Type**          *Select Network(s) in the dropdown*
     **Content**       *192.168.0.0/16 10.0.0.0/8 172.16.0.0/12*
     **Description**   *All local (RFC1918) networks*
    ================= ================================================

- **Save** the Alias, and then click **Apply**
- Then go to :menuselection:`Firewall --> Rules --> [Name of interface for network in which hosts/network resides, eg LAN for LAN hosts]`
- Click **Add** to add a new rule
- Configure the rule as follows (if an option is not mentioned below, leave it as the default):

    ============================ ==================================================================================================
     **Action**                   *Pass*
     **Quick**                    *Checked*
     **Interface**                *Whatever interface you are configuring the rule on*
     **Direction**                *in*
     **TCP/IP Version**           *IPv4*
     **Protocol**                 *any*
     **Source / Invert**          *Unchecked*
     **Source**                   *Select the relevant hosts Alias you created above in the dropdown (eg* :code:`WG_VPN_Hosts` *)*
     **Destination / Invert**     *Checked*
     **Destination**              *Select the* :code:`RFC1918_Networks` *Alias you created above in the dropdown*
     **Destination port range**   *any*
     **Description**              *Add one if you wish to*
     **Gateway**                  *Select the gateway you created above (eg* :code:`WAN_VPNProviderName` *)*
    ============================ ==================================================================================================

- **Save** the rule, and then click **Apply Changes**
- Then make sure that the new rule is **above** any other rule on the interface that would otherwise interfere with its operation. For example, you want your new rule to be above the “Default allow LAN to any rule”

------------------------------------
Step 9 - Create an outbound NAT rule
------------------------------------

- Go to :menuselection:`Firewall --> NAT --> Outbound`
- Select "Hybrid outbound NAT rule generation” if it is not already selected, and click **Save** and then **Apply changes**
- Click **Add** to add a new rule
- Configure the rule as follows (if an option is not mentioned below, leave it as the default):

    ========================== =========================================================================================================
     **Interface**              *Select the interface for your WireGuard VPN (eg* :code:`WAN_VPNProviderName` *)*
     **TCP/IP Version**         *IPv4*
     **Protocol**               *any*
     **Source invert**          *Unchecked*
     **Source address**         *Select the Alias for the hosts/networks that are intended to use the tunnel (eg* :code:`WG_VPN_Hosts` *)*
     **Source port**            *any*
     **Destination invert**     *Unchecked*
     **Destination address**    *any*
     **Destination port**       *any*
     **Translation / target**   *Interface address*
     **Description**            *Add one if you wish to*
    ========================== =========================================================================================================

- **Save** the rule, and then click **Apply changes**

----------------------
Dealing with DNS leaks
----------------------

As noted in Step 8, if your network is configured to use a local DNS server - for example, unbound on OPNsense or on another local host - this how-to is likely to result in DNS requests from the hosts using the tunnel to be routed through the normal WAN gateway, rather than through the tunnel. This will result in the WAN IP being exposed.

If you wish to avoid that, there are several possible solutions. Obviously what solution works best will depend on your network configuration and desired outcomes.

The solutions include:

1. Force the local DNS server to use the tunnel as well. For a local DNS server that is not OPNsense, include the local IPs of that server in the Alias created in Step 7 for the relevant VPN hosts. For OPNsense itself, configure the DNS server to use the tunnel gateway. Implementing this solution will mean that all DNS traffic for your network will go through the tunnel, not just the DNS traffic for the hosts that are in the Alias (and, indeed, for a local DNS server that is not OPNsense, all traffic from that server, not just DNS traffic, will be forced through the tunnel). This may not be desirable for your circumstances

2. If possible, intercept DNS traffic coming from the relevant hosts using the tunnel, and forward that traffic (by using a port forward rule in OPNsense) to a DNS server supplied by your VPN provider (see note below), or to a public DNS server. Note that this will not always be possible to do - if the local DNS server that is configured generally for your network is not OPNsense itself and is on the same subnet as the hosts using the tunnel, then DNS requests will not be routed through OPNsense and so a port forward on OPNsense will not work

3. Assuming you have configured DHCP static mappings in OPNsense for the hosts using the tunnel, specify in that configuration either the DNS servers supplied by your VPN provider (see note below), or public DNS servers. This will override the network-wide DNS settings for those hosts

4. Configure public DNS servers for your whole local network, rather than local DNS servers

5. Manually override the DNS settings on the relevant hosts themselves (assuming that is possible) so that the DNS servers provided by DHCP are ignored, and either the DNS servers supplied by your VPN provider (see note below), or public DNS servers, are used instead

.. Note::

    If the DNS servers supplied by your VPN provider are local IPs (ie, within the scope of the :code:`RFC1918_Networks` Alias created in Step 8), then you will need to create an additional firewall rule in OPNsense to ensure that requests to those servers use the tunnel gateway rather than the normal WAN gateway. This rule would be similar to that created in Step 8, except that the destination would be your VPN provider's DNS server IPs and the destination invert box would be unchecked. This rule would also need to be placed *above* the rule created in Step 8
