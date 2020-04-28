==========================
IPsec: Setup Remote Access
==========================

.. contents:: Index

-----
Intro
-----

Remate adccess to the company's infrastructure is one of most important and critical services exposed
to the internet. IPsec Mobile Clients offer mobile users (formerly known as Road Warriors) a solution
that is easy to setup and comptabile with most current devices.

With this guide we will show you how to configure the server side on OPNsense with the different
authentication methods e.g.

* EAP-MSCHAPv2
* Mutual-PSK + XAuth
* Mutual-RSA + XAuth
* ...


.. Note::

   For the sample we will use a private ip for our WAN connection.
   This requires us to disable the default block rule on WAN to allow private traffic.
   To do so, go to :menuselection:`Interfaces --> [WAN]` and uncheck “Block private networks”.
   *(Don't forget to save and apply)*

   .. image:: images/block_private_networks.png

------------
Sample Setup
------------
All configuration examples are based on the following setup, please read this carefully
as all guides depend on it.

**Company Network with Remote Client**

.. nwdiag::
  :scale: 100%

    nwdiag {

      span_width = 90;
      node_width = 180;
      Internet [shape = "cisco.cloud"];
      fileserver [label="File Server",shape="cisco.fileserver",address="192.168.1.10"];
      fileserver -- switchlan;

      network LAN {
        switchlan [label="",shape = "cisco.workgroup_switch"];
        label = " LAN";
        address ="192.168.1.1.x/24";
        fw1 [address="192.168.1.1/24"];
      }

      network WAN  {
        label = " WAN";
        fw1 [shape = "cisco.firewall", address="172.18.0.164"];
        Internet;
      }

      network Remote {
          Internet;
          laptop [address="172.10.10.55 (WANIP),10.10.0.1 (IPsec)",label="Remote User",shape="cisco.laptop"];
      }
    }

Company Network
---------------
==================== =============================
 **Hostname**         fw1
 **WAN IP**           172.18.0.164
 **LAN IP**           192.168.1.0/24
 **LAN DHCP Range**   192.168.1.100-192.168.1.200
 **IPsec Clients**    10.10.0.0/24
==================== =============================


---------------------------
Firewall Rules Mobile Users
---------------------------
To allow IPsec Tunnel Connections, the following should be allowed on WAN.

* Protocol ESP
* UDP Traffic on Port 500 (ISAKMP)
* UDP Traffic on Port 4500 (NAT-T)

.. image:: images/ipsec_wan_rules.png
    :width: 100%

To allow traffic passing to your LAN subnet you need to add a rule to the IPsec
interface.

.. image:: images/ipsec_ipsec_lan_rule.png
    :width: 100%

-----------------
VPN compatibility
-----------------

In the next table you can see the existing VPN authentication mechanisms and which client 
operating systems support it, with links to their configurations.
For Linux testing was done with Ubuntu 18.4 Desktop and *network-manager-strongswan* and
*libcharon-extra-plugins* installed. 
As Andoid does not support IKEv2 yet we added notes for combinations with strongSwan
app installed to have a broader compatibility for all systems.
Mutual RSA and PSK without XAuth requires L2TP, since this legacy technology is 
very error prone we will not cover it here.

.. csv-table:: VPN combinations
   :header: "VPN Method", "Win7", "Win10", "Linux", "Mac OS X", "IOS", "Android", "OPNsense config"
   :widths: 40, 20, 20, 20, 20, 20, 20, 20

   "IKEv1 Hybrid RSA + XAuth","N","N","N","tbd","tbd","N",":doc:`/manual/how-tos/ipsec-rw-srv-ikev1xauth`"
   "IKEv1 Mutual RSA + XAuth","N","N","N","tbd","tbd","Y :doc:`/manual/how-tos/ipsec-rw-android`",":doc:`/manual/how-tos/ipsec-rw-srv-ikev1xauth`"
   "IKEv1 Mutual PSK + XAuth","N","N","N","tbd","tbd","Y :doc:`/manual/how-tos/ipsec-rw-android`",":doc:`/manual/how-tos/ipsec-rw-srv-ikev1xauth`"
   "IKEv2 EAP-TLS","N","N","N","tbd","tbd","Y :doc:`/manual/how-tos/ipsec-rw-android`",":doc:`/manual/how-tos/ipsec-rw-srv-eaptls`"
   "IKEv2 RSA local + EAP remote","N","N","N","tbd","tbd","Y :doc:`/manual/how-tos/ipsec-rw-android`",":doc:`/manual/how-tos/ipsec-rw-srv-eaptls`"
   "IKEv2 EAP-MSCHAPv2","Y :doc:`/manual/how-tos/ipsec-rw-w7`","Y :doc:`/manual/how-tos/ipsec-rw-w7`","Y :doc:`/manual/how-tos/ipsec-rw-linux`","Y","Y","Y :doc:`/manual/how-tos/ipsec-rw-android`",":doc:`/manual/how-tos/ipsec-rw-srv-mschapv2`"
   "IKEv2 Mutual RSA + EAP-MSCHAPv2","N","N","N","tbd","tbd","Y :doc:`/manual/how-tos/ipsec-rw-android`",":doc:`/manual/how-tos/ipsec-rw-srv-rsamschapv2`"
   "IKEv2 EAP-RADIUS","Y :doc:`/manual/how-tos/ipsec-rw-w7`","Y :doc:`/manual/how-tos/ipsec-rw-w7`","Y :doc:`/manual/how-tos/ipsec-rw-linux`","Y","Y","Y :doc:`/manual/how-tos/ipsec-rw-android`",":doc:`/manual/how-tos/ipsec-rw-srv-eapradius`"
