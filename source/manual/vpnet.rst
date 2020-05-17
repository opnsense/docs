==========================
Virtual Private Networking
==========================

A virtual private network secures public network connections and in doing so it
extends the private network into the public network such as internet. With a VPN
you can create large secure networks that can act as one private network.

.. image:: images/Virtual_Private_Network_overview.png
    :width: 100%

(picture from `wikipedia <https://en.wikipedia.org/wiki/File:Virtual_Private_Network_overview.svg>`__)

Companies use this technology for connecting branch offices and remote users
(road warriors).

OPNsense supports VPN connections for branch offices as well as remote users.

Creating a single secured private network with multiple branch offices connecting
to a single site can easily be setup from within the graphical user interface.
For remote users, certificates can be created and revoked and a simple to use export
utility makes the client configuration a breeze.

--------------------------
Supported VPN technologies
--------------------------
OPNsense offers a wide range of VPN technologies ranging from modern SSL VPNs to
well known IPsec as well as older (now considered insecure) legacy options such as
L2TP and PPTP.

.. image:: images/vpn.png

.. Note::

  VPN technologies displayed with an open lock are considered to be insecure.

.................................
Integrated VPN options
.................................

Integrated solutions are those that are available within the GUI without installing
any additional package or plugin. These include:

* **IPsec**
* **OpenVPN (SSL VPN)**


.................................
Plugin VPN options
.................................

Via plugins additional VPN technologies are offered, including:

* **Legacy L2TP & PPTP**
* **OpenConnect** - SSL VPN client, initially build to connect to commercial vendor appliances like Cisco ASA or Juniper.
* **Stunnel** - Provides an easy to setup universal TLS/SSL tunneling service, often used to secure unencrypted protocols.
* **Tinc** - Automatic Full Mesh Routing
* **WireGuard** - Very simple and fast VPN working with public and private keys.
* **Zerotier** - seamlessly connect everything, requires account from zerotier.com, free for up to 100 devices.


-------------
Log Files
-------------

When troubleshooting problems with your firewall, it is very likely you have to check
the logs available on your system. In the UI of OPNsense, the log files are generally grouped
with the settings of the component they belong to. The log files can be found here:

================= =============================================== =====================================
 **IPsec Log**     :menuselection:`VPN --> IPsec --> Log File`     *Everything around IPsec goes here*
 **OpenVPN Log**   :menuselection:`VPN --> OpenVPN --> Log File`   *OpenVPN logs everything here*
================= =============================================== =====================================

.. Note::
   Log files on file system:
   /var/log/ipsec.log (clog)
   /var/log/openvpn.log (clog)


-------------
Configuration
-------------
Please read our how-tos for configuration examples and more detailed information.

..............
IPsec
..............


.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/ipsec-road
   how-tos/ipsec-s2s
   how-tos/ipsec-s2s-route
   how-tos/ipsec-s2s-binat
   how-tos/ipsec-rw
   how-tos/ipsec-rw-android
   how-tos/ipsec-rw-linux
   how-tos/ipsec-rw-srv-eapradius
   how-tos/ipsec-rw-srv-eaptls
   how-tos/ipsec-rw-srv-ikev1xauth
   how-tos/ipsec-rw-srv-mschapv2
   how-tos/ipsec-rw-srv-rsamschapv2
   how-tos/ipsec-rw-w7
   how-tos/ipsec-s2s-route-azure


..............
OpenVPN
..............


.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/sslvpn_client
   how-tos/sslvpn_s2s


..............
Other
..............

.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/openconnect
   how-tos/stunnel
   how-tos/wireguard-s2s
   how-tos/wireguard-client
   how-tos/wireguard-client-azire
   how-tos/wireguard-client-mullvad
   how-tos/zerotier
