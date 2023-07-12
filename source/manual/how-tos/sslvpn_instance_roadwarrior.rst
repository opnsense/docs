=================================
Setup SSL VPN Road Warrior
=================================

.. image:: images/sslvpn_image_new.png
   :width: 100%

Road Warriors are remote users who need secure access to the companies infrastructure.
OPNsense uses OpenVPN for its SSL VPN Road Warrior setup and offers OTP (One Time Password)
integration with standard tokens and Googles Authenticator.

.. Tip::

  Did you know that OPNsense offers two-factor authentication throughout the entire
  system? See for more information: :doc:`/manual/two_factor`

.. Note::

   For the sample we will use a private IP for our WAN connection.
   This requires us to disable the default block rule on wan to allow private traffic.
   To do so, go to :menuselection:`Interfaces --> [WAN]` and uncheck "Block private networks".
   *(Dont forget to save and apply)*

   .. image:: images/block_private_networks.png


.. contents:: Index

----------------
Before you start
----------------
Before starting with the configuration of an OpenVPN SSL tunnel you need to have a
working OPNsense installation with a unique LAN IP subnet for each side of your
connection (your local network needs to be different than that of the remote
network).

.. Note::

   For the sample we will use a private IP for our WAN connection.
   This requires us to disable the default block rule on WAN to allow private traffic.
   To do so, go to :menuselection:`Interfaces --> [WAN]` and uncheck "Block private networks".
   *(Don't forget to save and apply)*

   .. image:: images/block_private_networks.png


--------------------------------
Network topology
--------------------------------

The schema below describes the situation we are implementing. One client using an "external" ip address of :code:`10.0.8.2/24`
a firewall we are connecting to at :code:`10.0.8.1/24` constructing a tunnel using  :code:`10.2.8.0/24` to reach :code:`192.168.8.0/24`.

.. nwdiag::
  :scale: 100%

    nwdiag {

      span_width = 90;
      node_width = 180;
      network {
          address = "10.0.8.0/24";
          pclana [label="Roadwarrior\n10.2.8.2",shape="cisco.pc"];
          fw [shape = "cisco.firewall", address="10.0.8.1/24"];
      }
      network Ext {
          address = "192.168.8.0/24";
          fw [shape = "cisco.firewall", address="192.168.8.1/24"];
          pclanb [label="Server\n192.168.8.20",shape="cisco.pc"];
      }

    }



--------------------------------
Preparations
--------------------------------

.....................
Trust
.....................


In order to setup a tunnel on both ends, we need to configure certificates to warrant trust between the client and this server.

* First we need an **Authority** which we are going to create in :menuselection:`System --> Trust --> Authorities`

   * Select `Create an internal Certificate Authority`
   * Choose cryptographic settings and a lifetime (you may want to increase the default as after this time you do need to redistribute certificates to both server and client).
   * Add descriptive information for this CA (`Descriptive name`, `City`, `Email`, ..`)
   * Set the `Common Name` to something descriptive for this certificate, like "Office-ovpn"


*  Next generate a **Certficate** for the server using :menuselection:`System --> Trust --> Certificates`

   * Select  `Create an internal Certificate`
   * Choose the just created authority in `Certificate authority`
   * Add descriptive information for this CA (`Descriptive name`, whereabouts are copied from the CA)
   * Set Type to `Server`
   * Choose cryptographic settings, lifetime determines the validaty of the server certificate (you do need to track this yourself), it's allow to choose a longer period here
   * Set the `Common Name` to the fqdn of this machine.

* For the client pc we will create a user and a certificate, from the :menuselection:`System --> Access --> Users` menu.

   * Hit the [+] sign to create a new user, for this test we will call it :code:`test1`
   * Check the "Certificate -> Click to create a user certificate" option and hit "save"
   * Next step in the certificate window, select "`Create an internal Certificate`" and "save"


.. Note::

      It's a best practice to offer each user it's own certificate using the same common name as the username, although
      it is also possible to clients to share a certificate. When adding a certificate from the user manager the CN is automatically
      set to its name. In this example we will only authenticate using the certificate, no additional user or password will be required.


.....................
Static keys
.....................

We create a static key and define it's use in :menuselection:`VPN --> OpenVPN --> Instances --> Static Keys`,  for this example
select `auth` as mode and click the gear button to generate one. Provide a description for this key.



------------------------------------
Create a server instance
------------------------------------

Now the generic setup is done, we can configure a new server type instance via :menuselection:`VPN --> OpenVPN --> Instances`

===============================================================

======================= =======================================
Property                site B
======================= =======================================
Role                    Server
Description             MyServer
Protocol                UDP (IPv4)
Port number             1194
Bind address            10.10.8.1 :sup:`1`
Server (IPv4)           10.1.8.0/24 (the tunnel network used)
Certificate             choose the prepared server certificate
TLS static key          choose the prepared static key
Authentication          Local Database  :sup:`2`
Strict User/CN Matching [V]  :sup:`3`
Local Network           192.168.8.0/24
======================= =======================================

.. admonition:: Note  :sup:`1`

   Leave empty to bind to all addresses assigned to this machine or use a loopback address combined with a port forward when
   the external address is not static.

.. admonition:: Note  :sup:`2`

   When users are also required to use a one-time-password, just select an authentication server that supports the additional
   token.

.. admonition:: Note  :sup:`3`

   Selecting the "Strict User/CN Matching" option warrants only matching user/certificate can login, when sharing a single
   vertificate between clients this option needs to be deselected.


Next go to :menuselection:`Firewall --> Rules --> WAN` and add a rule to allow traffic on port :code:`1194/UDP` from the other
host. At minimum we should add a rule similar to this one:

===============================================================

======================= =======================================
Property                site B
======================= =======================================
Interface               WAN
Protocol                UDP
Destination port range	1194
======================= =======================================

Finally we are going to allow traffic on the tunnel itself by adding a rule to :menuselection:`Firewall --> Rules --> OpenVPN`,
for this example we keep it simple and add one to allow all, in which case we can save the defaults when adding a rule.


------------------------------------
Export client profile
------------------------------------

With the server in place it's time to setup the client on OPNsense, for this we go to :menuselection:`VPN --> OpenVPN --> Client Export`
and export a profile for the remote client.

===================================================================

======================= ===========================================
Property                Value
======================= ===========================================
Remote Access Server    select the Roadwarrior server "MyServer"
Export type             File Only :sup:`1`
Hostname                10.10.8.1
======================= ===========================================

.. admonition:: Note  :sup:`1`

   Most clients support the standard :code:`ovpn` format, when using a tool like Viscosity from Sparklabs (https://www.sparklabs.com/viscosity/)
   you can also choose the proper type here.

Next client on the certificate with link user in the grid below and install the certificate on the client.


--------------------------------
Test connectivity
--------------------------------

After connecting the client, use the :menuselection:`VPN: OpenVPN: Connection Status` page to watch the status of the connected
client. It should show the client with byte counters.

Now try to ping from Site A (:code:`10.0.8.20`) to Site B (:code:`192.168.8.20`).
