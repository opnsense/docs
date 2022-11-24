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

OPNsense offers a wide range of VPN technologies ranging from modern SSL VPNs to
well known IPsec as well as WireGuard and Zerotier via the use of plugins.

.. image:: images/vpn.png
    :width: 30%

--------------------------
IPsec
--------------------------

Since IPsec is used in many different scenario's and sometimes has the tendency to be a bit complicated, we
will describe different usecases and provide some examples in this chapter.

.................................
Site 2 Site policy based
.................................

Probably one of the oldest and most used scenarios is the policy based one.

Like all IPsec configurations, a standard site to site setup starts with a so called "Phase 1" entry to establish the
communication between both peers defined in :menuselection:`VPN -> IPsec -> Tunnel Settings`. After the phase 1
is configured, the "Phase 2" defines which policies traffic should match on.

Since the kernel traps traffic matching defined policies, no additional routing need to be configured in order to
communicate between both ends of a tunnel.

.. Note::

  Using Network Address Translation in these types of setups is different, due to the fact that the installed IPsec policy
  should accept the traffic in order to encapsulate it. The `IPSec BINAT` document will explain how to apply translations.

.. Tip::

  When matching overlapping networks in a policy, make sure to exclude your own network segments in the
  :code:`Passthrough networks` option in :menuselection:`VPN -> IPsec -> Advanced Settings` to prevent traffic being blackholed.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/ipsec-s2s
   how-tos/ipsec-s2s-binat


.................................
Site 2 Site route based (VTI)
.................................

Unlike the policy based setup described in the previous chapter, the route based variant depends on custom routes being installed
on both ends of the tunnel. When adding a route based tunnel, the system will add an interface for you which you can use in normal
routing operations.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/ipsec-s2s-route
   how-tos/ipsec-s2s-route-azure


.................................
Road Warriors / Mobile users
.................................

For people working from home IPsec is also an option, althouh a bit more complicated in comparison to OpenVPN due
to the many different implementation types.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/ipsec-rw


.................................
Diagnostics
.................................

In order to keep track of the connected tunnels, you can use the :menuselection:`VPN -> IPsec -> Status Overview`
to browse through the configured tunnels.

The :menuselection:`VPN -> IPsec -> Security Policy Database` is also practical to gain insights in the registered policies,
when NAT is used, the additional SPD entries should be visible here as well.


When troubleshooting problems with your firewall, it is very likely you have to check
the logs available on your system. In the UI of OPNsense, the log files are generally grouped
with the settings of the component they belong to. The log files can be found in the "Log file" menu item.

.. Tip::

    When trying to debug various issues, the amount of log information gathered can be configured using the settings
    in :menuselection:`VPN -> IPsec -> Advanced Settings`.



--------------------------
OpenVPN (SSL VPN)
--------------------------

One of the main advantages of OpenVPN in comparison to IPsec is the ease of configuration, there are less settings involved
and it's quite simple to export settings for clients.

.................................
Site 2 Site
.................................

OpenVPN on OPNsense can also be used to create a tunnel between two locations, similar to what IPsec offers, generally
the performance of IPsec is higher which usually makes this a less common choice.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/sslvpn_s2s


.. Note::

    When using the site to site example with :code:`SSL/TLS` instead of a shared key, make sure to configure "client specific overrides"
    as well to correctly bind the remote networks to the correct client.

.................................
Road Warriors / Mobile users
.................................

Mobile usage is really where OpenVPN excells, with various (multifactor) authentication options and a high flexibility in available network options.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/sslvpn_client


.................................
Client Specific Overrides
.................................

The mechanism of client overrides utilises OpenVPN :code:`client-config-dir` option, which offer the ability to use
specific client configurations based on the client's X509 common name.

It is possible to specify the contents of these configurations in the gui under :menuselection:`VPN -> OpenVPN -> Client Specific Overrides`.
Apart from that, an authentication server (:menuselection:`System -> Access -> Servers`) can also provide client details in special cases when returning
:code:`Framed-IP-Address`, :code:`Framed-IP-Netmask` and :code:`Framed-Route` properties.

.. Tip::

      Radius can be used to provisioning tunnel and local networks.

A selection of the most relevant settings can be found in the table below.

.. csv-table:: Client Specific Overrides
   :header: "Parameter", "Purpose"
   :widths: 30, 40

   "Disabled", "Set this option to disable this client-specific override without removing it from the list"
   "Servers", "Select the OpenVPN servers where this override applies to, leave empty for all"
   "Common name", "The client's X.509 common name, which is where this override matches on"
   "IPv[4|6] Tunnel Network", "The tunnel network to use for this client per protocol family, when empty the servers will be used"
   "IPv[4|6] Local Network", "The networks that will be accessible from this particular client per protocol family."
   "IPv[4|6] Remote Network", "These are the networks that will be routed to this client specifically using iroute, so that a site-to-site VPN can be established."
   "Redirect Gateway", "Force the clients default gateway to this tunnel"

.. Note::

      When configuring tunnel networks, make sure they fit in the network defined on the server tunnel itself to allow the server to send data back to the client.
      For example in a :code:`10.0.0.0/24` network you are able to define a client specific one like :code:`10.0.0.100/30`.

      To reduce the chances of a collision, also make sure to reserve enough space at the server as the address might already be assigned to a dynamic client otherwise.



--------------------------
Plugin VPN options
--------------------------

Via plugins additional VPN technologies are offered, including:

* **OpenConnect** - SSL VPN client, initially build to connect to commercial vendor appliances like Cisco ASA or Juniper.
* **Stunnel** - Provides an easy to setup universal TLS/SSL tunneling service, often used to secure unencrypted protocols.
* **Tinc** - Automatic Full Mesh Routing
* **WireGuard** - Simple and fast VPN protocol working with public and private keys.
* **Zerotier** - seamlessly connect everything, requires account from zerotier.com, free for up to 100 devices.


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
