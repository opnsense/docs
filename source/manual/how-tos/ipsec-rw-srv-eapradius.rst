==========================================
IPsec: Setup OPNsense for IKEv2 EAP-RADIUS
==========================================

.. contents:: Index

EAP-RADIUS via IKEv2 is nearly the same as EAP-MSCHAPv2, but authentication is agains a Radius instance.
We assume you have read the first part at 
:doc:`how-tos/ipsec-rw`

----------------------------
Step 1 - Create Certificates
----------------------------

For EAP-RADIUS with IKEv2 you need to create a Root CA and a server certificate
for your Firewall. 

Go to **System->Trust->Authorities** and click **Add**. Give it a **Descriptive Name** and as **Method**
choose **Create internal Certificate Authority**. Increase the **Lifetime** and fill in the fields 
matching your local values. Now go to **System->Trust->Certificates** and create a new certificate for 
the Firewall itself. Important is to change the **Type** to server. The Common Name can be the hostname
of the Firewall and set as **Alternative Name** the FQDN your Firewall how it is known to the WAN side.
This is most important as your VPN will drop when the FQDN does not match the ones of the certificate.

If you already have a CA roll out a server certificate and import 
the CA itself via **System->Trust->Authorities** and the certificate with the key in 
**System->Trust->Certificates**.

---------------------
Step 2 - Setup Radius
---------------------

If you already have a local Radius server, add a new client with the IP address of your Firewall,
set a shared secret, go to OPNsense UI to **System->Access->Servers** and add a new instance:

============================ ================ ====================================
 **Descriptive Name**         Name             *Give it a name*
 **Type**                     Radius           *This is what we want*
 **Hostname or IP Address**   Radius IP        *Set the IP of your Radius server*
 **Shared Secret**            s3cureP4ssW0rd   *Choose a secure password*
============================ ================ ====================================

When you do not have an own Radius instance just use the OPNsense plugin and follow this guide:
:doc:`how-tos/freeradius`

-----------------------
Step 3 - Mobile Clients
-----------------------
First we will need to setup the mobile clients network and authentication source.
Go to **VPN->IPsec->Mobile Clients**

For our example will use the following settings:

IKE Extensions
--------------
========================== ============== ================================================
 **Enable**                 checked        *check to enable mobile clients*
 **User Authentication**    Nothing        *As we use Radius, no need to select anything*
 **Group Authentication**   none           *Leave on none*
 **Virtual Address Pool**   10.10.0.0/24   *Enter the IP range for the remote clients*
========================== ============== ================================================

You can select other options, but we will leave them all unchecked for this
example.

**Save** your settings and select **Create Phase1** when it appears.
Then enter the Mobile Client Phase 1 setting.

-------------------------------
Step 4 - Phase 1 Mobile Clients
-------------------------------

Phase 1 General information
---------------------------
========================== ============= ==================================================
 **Connection method**      default       *default is 'Start on traffic'*
 **Key Exchange version**   V2            *only V2 is supported for EAP-RADIUS*
 **Internet Protocol**      IPv4
 **Interface**              WAN           *choose the interface connected to the internet*
 **Description**            MobileIPsec   *freely chosen description*
========================== ============= ==================================================

Phase 1 proposal (Authentication)
---------------------------------
=========================== ==================== =============================================
 **Authentication method**   EAP-RADIUS           *This is the method we want here*
 **My identifier**           Distinguished Name   *Set the FQDN you used within certificate*
 **My Certificate**          Certificate          *Choose the certificate from dropdown list*
=========================== ==================== =============================================


Phase 1 proposal (Algorithms)
-----------------------------
========================== ================ ============================================
 **Encryption algorithm**   AES              *For our example we will use AES/256 bits*
 **Hash algoritm**          SHA1, SHA256     *SHA1 and SHA256 for compatibility*
 **DH key group**           1024, 2048 bit   *1024 and 2048 bit for compatibility*
 **Lifetime**               28800 sec        *lifetime before renegotiation*
========================== ================ ============================================

Advanced Options are fine by default.

**Save** your settings.

-------------------------------
Step 5 - Phase 2 Mobile Clients
-------------------------------
Press the button that says '+ Show 0 Phase-2 entries'

.. image:: images/ipsec_s2s_vpn_p1a_show_p2.png
    :width: 100%

You will see an empty list:

.. image:: images/ipsec_s2s_vpn_p1a_p2_empty.png
    :width: 100%

Now press the *+* at the right of this list to add a Phase 2 entry.

General information
-------------------
================= =============== =============================
 **Mode**          Tunnel IPv4     *Select Tunnel mode*
 **Description**   MobileIPsecP2   *Freely chosen description*
================= =============== =============================

Local Network
-------------
=================== ============ ==============================
 **Local Network**   LAN subnet   *Route the local LAN subnet*
=================== ============ ==============================

Phase 2 proposal (SA/Key Exchange)
----------------------------------
=========================== ============== ====================================================
 **Protocol**                ESP            *Choose ESP for encryption*
 **Encryption algorithms**   AES / 256      *For this example we use AES 256*
 **Hash algorithms**         SHA1, SHA256   *Same as before, mix SHA1 and SHA256*
 **PFS Key group**           off            *Most mobile systems do not support PFS in Phase2*
 **Lifetime**                3600 sec
=========================== ============== ====================================================

**Save** your settings and **Enable IPsec**, Select:

.. image:: images/ipsec_s2s_vpn_p1a_enable.png
    :width: 100%

.. Note::

   If you already had IPsec enabled and added Road Warrior setup, it is important to 
   restart the whole service via services widget in the upper right corner of IPSec pages
   or via **System->Diagnostics->Services->Strogswan** since applying configuration only
   reloads it, but a restart also loads the required modules of strongSwan.

------------------------
Step 6 - Add IPsec Users
------------------------

Go to your Radius Management Console and start adding users!
If you are using our FreeRADIUS Plugin follow the official guide:
:doc:`how-tos/freeradius`
