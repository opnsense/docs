====================================
Netbird Plugin Setup Guide
====================================

Introduction
============

This guide explains how to install and configure the **Netbird** plugin on OPNsense. 
Netbird is a peer-to-peer VPN that simplifies secure networking between devices. 
The plugin allows OPNsense to join a Netbird network, providing routing, DNS resolution, 
and firewalling capabilities.

Limitations
===========

- **Netbird Policies Do Not Create Firewall Rules on OPNsense**  
  - The policies set in the Netbird management console **do not** automatically create firewall rules on OPNsense.  
  - You need to manually configure the required firewall rules on the assigned ``wt0`` interface in OPNsense to allow or restrict traffic as needed.

Installation
============

The Netbird plugin can be installed directly from the official OPNsense repository.

Installing via Web UI
---------------------

1. Navigate to **System** → **Firmware** → **Plugins**.
2. Locate ``os-netbird`` in the list.
3. Click the **+** button to install the plugin.

Configuration
=============

After installation, navigate to **VPN** → **Netbird** to configure the plugin.

Required Settings
-----------------

- **Management Server URL**
  - The URL of the Netbird management server (self-hosted or Netbird Cloud).  
  - Example: ``https://netbird.example.com``.

- **Setup Key**
  - Generated in the Netbird management server.
  - Used to register OPNsense as a Netbird peer.

- **Optional Hostname**
  - Defines how OPNsense appears in the Netbird management console.  
  - Example: ``opnsense-router``.

General Settings
----------------

- **Port (Default: 51820)**  
  - The default WireGuard port.
  - Change this if another WireGuard server is already using the port.
  - Ensure this port is open on the **WAN interface** (Firewall rules required), otherwise only a relayed connection will be possible.

- **Disable Server Routes**  
  - When enabled, OPNsense **will not act as a routing peer**, preventing other Netbird peers from accessing networks behind OPNsense.

- **Disable Client Routes**  
  - When enabled, OPNsense **will not use Netbird routes** to reach remote networks.

- **Disable Netbird DNS Lookups**  
  - When enabled, OPNsense **will not resolve Netbird hostnames** (e.g., ``demo.netbird.selfhosted``) to IP addresses.

- **Enable Rosenpass**  
  - Enables **post-quantum encryption** using Rosenpass on top of WireGuard for enhanced security.  
  - When enabled, this OPNsense peer will attempt to use Rosenpass for encrypted connections.

- **Rosenpass Permissive Mode**  
  - When enabled, this peer will **prefer** Rosenpass for connections to other Rosenpass-enabled peers but will also allow connections to peers **without** Rosenpass.  
  - When disabled, this peer will **only** connect to other peers that support Rosenpass, rejecting connections from non-Rosenpass peers.

- **CARP Interface**  
  - Defines how Netbird behaves in a high-availability (HA) setup using CARP.  
  - **None**: If set to "None", Netbird will execute ``netbird up`` automatically and enable auto-connect.  
  - **Specific Interface**: If an interface is selected, auto-connect is **disabled**, and Netbird must be manually started on the **MASTER** node by triggering a CARP event or executing ``netbird up`` manually.

- **CARP VHID**  
  - Sets the **Virtual Host ID (VHID)** for CARP when using Netbird in a high-availability (HA) setup.  
  - This ID helps distinguish multiple CARP instances on the same network.  
  - It should match the **VHID** used in the OPNsense HA configuration for proper failover behavior.

After configuring the required settings, click **Save** and restart the Netbird service.

Assigning the Interface
=======================

To enable firewalling, NAT, or routing, you need to assign the **wt0** interface.

1. Go to **Interfaces** → **Assignments**.
2. Locate the unassigned ``wt0`` interface.
3. Enter a name in the description field (e.g., **Netbird**).
4. Click **Add** to assign it.
5. Click on the **Netbird** interface to configure it.
6. Check "Enable Interface"
7. optionally but recommended: Check "Prevent interface removal"
8. don't set any IP address or gateway
9. Click **Save**
10. Click on **Apply changes**

Why Assign ``wt0``?
-------------------

- Allows **incoming traffic from Netbird peers** (e.g., access to the OPNsense Web UI).
- Required for **firewalling, NAT, or advanced routing**.

Network Address Translation (NAT)
=================================

If you want OPNsense to act as an **exit node** for Netbird peers:

1. Go to **Firewall** → **NAT** → **Outbound**.
2. Set the mode to **Hybrid NAT**.
3. Add a rule to **translate traffic from Netbird (``wt0``) to the WAN interface**.
4. Save and apply changes.

Firewall Rules
==============

Firewall rules depend on your use case.  
However, some considerations:

- If **Rosenpass** is enabled, you may need to allow **incoming UDP traffic** on high ports (30,000–65,535).
- Define rules on the ``wt0`` interface to control peer access.

Accessing Logs
==============

Netbird logs can be accessed via the Web UI:

1. Navigate to **VPN** → **Netbird** → **Log File**.
2. Use logs to troubleshoot connection or routing issues.

Conclusion
==========

The Netbird plugin for OPNsense provides a powerful way to integrate Netbird’s VPN capabilities. 
By assigning ``wt0``, setting up NAT, and configuring firewall rules, OPNsense can serve as a routing peer 
or an exit node for Netbird networks.
