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
OPNsense offers a wide range of VPN technologies ranging from modern SSL VPN's to
well known IPsec as well as older (now considered insecure) legacy options such as
L2TP and PPTP.

.. image:: images/vpn.png
    :width: 100%

.. Note::

  VPN technologies displayed with an open lock are considered to be insecure.

Integrated VPN options
----------------------
Integrated solutions are those that are available within the GUI without installing
any additional package or plugin. These include:

* **IPsec**
* **OpenVPN (SSL VPN)**


Plugin VPN options
------------------
Via plugins additional VPN technologies are offered, including:

* **Legacy L2TP & PPTP**
* **Tinc** - Automatic Full Mesh Routing
* **Zerotier** - seamlessly connect everything, requires account from zerotier.com, free for up to 100 devices.


-------------
Configuration
-------------
Please read our how-to's for configuration examples and more detailed information.

IPsec Road Warrior
-------------------
:doc:`how-tos/ipsec-road`

IPsec Site-to-Site
-----------------------
:doc:`how-tos/ipsec-s2s`

IPsec Site-to-Site with BINAT
-----------------------------
:doc:`how-tos/ipsec-s2s-binat`

OpenVPN/SSL Road Warrior
------------------------
:doc:`how-tos/sslvpn_client`

OpenVPN/SSL Site-to-Site
------------------------
:doc:`how-tos/sslvpn_s2s`

OpenConnect Client
------------------
:doc:`how-tos/openconnect`

Zerotier
--------
:doc:`how-tos/zerotier`
