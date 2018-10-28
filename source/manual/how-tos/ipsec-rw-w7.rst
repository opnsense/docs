====================================
IPsec: Setup Windows 7 Remote Access
====================================

Here you can see the configuration options for all compatible VPN types.
We assume that you are familiar with adding a new VPN connection.

All screenshot were taken from **Network and Sharing Center->Change adapter settings**.

---------------------------
Step 1 - Install Certificte
---------------------------

Since Windows 7 also supports IKEv2 we need to install your Root Certificate Authority.
Hit the Windows Start button and type *mmc* in search box. Go to **File->Add/Remove Snap-In**.
Choose **Certificates->Add->Computer account**.
Open **Certificate** and navigate to **Trusted Root Certificate Authorities**, right click,
**All taks** and import. Select the Root CA and install. 

If you are using client certificates for authentication (e.g EAP-TLS) use a PKCS12/PFX and install 
it under **Personal** instead of **Trusted Root Certificate Authorities**. All included certificates 
will be installed in the correct folders.

screenshot 

---------------------------
Step 2 - Add VPN Connection
---------------------------

Add a new VPN connection via **Network and Sharing Center** and choose as **Internet Address**
the correct FQDN. This is imporatant when using certificates since the FQDN of your connection
and the one in the certificate has to match!
Then set a **Username** and **Password** and leave **Domain** emtpy.

-------------------
Step 3 - Finetuning
-------------------

Via **Network and Sharing Center** go to **Change adapter settings** and open the properties
of your newly created adapter. Check that the FQDN is correct:

picture1

On tab **Networking** in IPv4 configuration under **Advanced** is the option **Use defaut gateway on remote network**.
If this option is enabled, all traffic will be send through the VPN (if IPsec SA matches). When unchecked, you have
to set specific routes sent via VPN. 

picture2



IKE Extensions
--------------
========================= ================ ================================================
**Enable**                 checked          *check to enable mobile clients*
**User Authentication**    Local Database   *For the example we use the Local Database*
**Group Authentication**   none             *Leave on none*
**Virtual Address Pool**   10.10.0.0/24      *Enter the IP range for the remote clients*
========================= ================ ================================================

You can select other options, but we will leave them all unchecked for this
example.

**Save** your settings and select **Create Phase1** when it appears.
Then enter the Mobile Client Phase 1 setting.

-------------------------------
Step 3 - Phase 1 Mobile Clients
-------------------------------

Phase 1 General information
---------------------------
========================= ============= ================================================
**Connection method**      default       *default is 'Start on traffic'*
**Key Exchange version**   V2            *only V2 is supported for EAP-TLS*
**Internet Protocol**      IPv4
**Interface**              WAN           *choose the interface connected to the internet*
**Description**            MobileIPsec   *freely chosen description*
========================= ============= ================================================

Phase 1 proposal (Authentication)
---------------------------------
=========================== ====================== ============================================
 **Authentication method**   EAP-TLS                *This is the method we want here*
 **My identifier**           Distinguished Name     *Set the FQDN you used within certificate*
 **My Certificate**          Certificate            *Choose the certificate from dropdown list*
=========================== ====================== ============================================

.. Note::

   Some clients require RSA as remote like Strongswan Android App. If you encounter problem with 
   your client devices replace **Authentication method** to **RSA (local) + EAP-TLS (remote)**

Phase 1 proposal (Algorithms)
-----------------------------
========================== ============= ===========================================================
 **Encryption algorithm**   AES           *For our example we will use AES/256 bits*
 **Hash algoritm**          SHA1,SHA256   *SHA1 and SHA256 for compatibility*
 **DH key group**           1024,2048 bit *1024 and 2048 bit for compatibility*
 **Lifetime**               28800 sec     *lifetime before renegotiation*
========================== ============= ===========================================================

Advanced Options are fine by default.

**Save** your setting.

-------------------------------
Step 3 - Phase 2 Mobile Clients
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
======================= ================== =============================
 **Mode**                Tunnel IPv4        *Select Tunnel mode*
 **Description**         MobileIPsecP2      *Freely chosen description*
======================= ================== =============================

Local Network
-------------
======================= ================== ==============================
 **Local Network**       LAN subnet        *Route the local LAN subnet*
======================= ================== ==============================

Phase 2 proposal (SA/Key Exchange)
----------------------------------
=========================== ============ ====================================================
**Protocol**                 ESP           *Choose ESP for encryption*
**Encryption algorithms**    AES / 256     *For this example we use AES 256*
**Hash algorithms**          SHA1,SHA256   *Same as before, mix SHA1 and SHA256*
**PFS Key group**            off           *Most mobile systems do not support PFS in Phase2*
**Lifetime**                 3600 sec
=========================== ============ ====================================================

**Save** your setting **Enable IPsec**, Select:

.. image:: images/ipsec_s2s_vpn_p1a_enable.png
    :width: 100%

.. Note::

   If you already had IPsec enabled and added Road Warrior setup, it's important to 
   restart the whole service via services widget in the upper right corner of IPSec pages
   or via **System->Diagnostics->Services->Strogswan** since applying configuration only
   reloads it, but a restart also loads the required modules of strongswan.

------------------------
Step 4 - Add IPsec Users
------------------------

Go to **System->Trust->Certificates** and create a new client certificate.
Just click **Add**, choose your CA and probably increase the lifetime. Everything else besides
the CN can be left default. Give a **Common Name** and **Save**. Download the newly created
certificate as PKCS12 and export it to you enduser device.

----------------------
