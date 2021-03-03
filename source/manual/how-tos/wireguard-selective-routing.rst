=================================================================
Set up WireGuard for selective routing to external VPN provider
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
     **Name**               *Call it whatever you want (eg :code:`VPNProviderName_Location`)*
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
     **Name**              *Call it whatever you want (eg :code:`VPNProviderName`)*
     **Public Key**        *This will initially be blank; it will be populated once the configuration is saved*
     **Private Key**       *This will initially be blank; it will be populated once the configuration is saved*
     **Listen Port**       *51820 or a higher numbered unique port*
     **DNS Server**        *Leave this blank or specify the DNS servers provided by your VPN provider*
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

    ==================== ============================================================================================
     **Name**             *Call it whatever you want, easiest to name it the same as the interface*
     **Description**      *Add one if you wish to*
     **Interface**        *Select your newly created interface in the dropdown*
     **Address Family**   *Select IPv4 in the dropdown*
     **IP address**       *Insert the gateway IP that you configured under the WireGuard local peer configuration*
     **Far Gateway**      *Checked*
     **Monitor IP**       *Insert an external IP to monitor the gateway, such as 1.1.1.1 or 8.8.8.8*
    ==================== ============================================================================================

- **Save** the gateway configuration and then click **Apply changes**

---------------------------------------------------------------------------------
Step 7 - Create an Alias for the relevant local hosts that will access the tunnel
---------------------------------------------------------------------------------

- Go to :menuselection:`Firewall --> Aliases`
- Click **+** to add a new Alias
- Configure the Alias as follows (if an option is not mentioned below, leave it as the default):

    ================= ==================================================================================================
     **Enabled**       *Checked*
     **Name**          *Call it whatever your want, eg :code:`WG_VPN_Hosts`*
     **Type**          *Select either Host(s) or Network(s) in the dropdown, depending on whether you want specific host IPs to use the tunnel, or an entire local network (such as a VLAN)*
     **Content**       *Enter the host IPs, or the network in CIDR format*
     **Description**   *Add one if you wish to*
    ================= ==================================================================================================

- **Save** the Alias, and then click **Apply**

-------------------------------
Step 8 - Create a firewall rule
-------------------------------

This will involve two steps - first creating a second Alias for all local (private) networks, and then creating the firewall rule itself. The ultimate effect of these two steps is that only traffic from the relevant hosts that is destined for **non-local** destinations will be sent down the tunnel. This will ensure that the relevant hosts can still access local resources

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
     **Source**                   *Select the relevant hosts Alias you created above in the dropdown (eg :code:`WG_VPN_Hosts`)*
     **Destination / Invert**     *Checked*
     **Destination**              *Select the :code:`RFC1918_Networks` Alias you created above in the dropdown*
     **Destination port range**   *any*
     **Description**              *Add one if you wish to*
     **Gateway**                  *Select the gateway you created above (eg :code:`WAN_VPNProviderName`)*
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
     **Interface**              *Select the interface for your WireGuard VPN (eg :code:`WAN_VPNProviderName`)*
     **TCP/IP Version**         *IPv4*
     **Protocol**               *any*
     **Source invert**          *Unchecked*
     **Source address**         *Select the Alias for the hosts/networks that are intended to use the tunnel (eg :code:`WG_VPN_Hosts`)*
     **Source port**            *any*
     **Destination invert**     *Unchecked*
     **Destination address**    *any*
     **Destination port**       *any*
     **Translation / target**   *Interface address*
     **Description**            *Add one if you wish to*
    ========================== =========================================================================================================

- **Save** the rule, and then click **Apply changes**
