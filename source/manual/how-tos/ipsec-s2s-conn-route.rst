====================================
IPsec - Route based (VTI) PSK setup
====================================

This example utilises the new options available in OPNsense 23.1 to setup a site to site tunnel in routed mode
between two OPNsense machines using a pre shared key.

.. contents:: Index

--------------------------------
Network topology
--------------------------------

The schema below describes the situation we are implementing. Two networks (A,B) and a transit network (10.10.1.0/24)
to peer both firewalls. We will create a tunnel network using :code:`192.168.123.1` [A] and :code:`192.168.123.2` [B].

.. nwdiag::
  :scale: 100%

    nwdiag {

      span_width = 90;
      node_width = 180;
      network A {
          address = "10.2.0.0/24";
          pclana [label="PC Site A\n10.2.0.20",shape="cisco.pc"];
          fwa [shape = "cisco.firewall", address="10.2.0.1/24"];
      }
      network Ext {
          address = "10.10.1.0/24";
          label = "Ext-VTI\n192.168.123.1 <--> 192.168.123.2";
          fwa [shape = "cisco.firewall", address="10.10.1.1/24"];
          fwb [shape = "cisco.firewall", address="10.10.1.2/24"];
      }
      network B {
          address = "192.168.2.0/24"
          fwb [shape = "cisco.firewall", address="192.168.2.20"];
          pclanb [label="PC Site B\n192.168.2.20",shape="cisco.pc"];
      }


    }



--------------------------------
Preparations
--------------------------------

.....................
Interface
.....................

In order to define our IPsec tunnel we do need to define a virtual tunnel interface (:menuselection:`VPN->IPsec->Virtual Tunnel Interfaces`) first.
The purpose of this device is to attach a tunnel to a security policy defined by its request id (:code:`reqid`).

On both sites A and B we will add VTIs using the following parameters:

===============================================================

======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Reqid                   10                  10
Local address           **10.10.1.1**       **10.10.1.2**
Remote address          **10.10.1.2**       **10.10.1.1**
Tunnel local address    **192.168.123.1**   **192.168.123.2**
Tunnel remote address   **192.168.123.2**   **192.168.123.1**
======================= =================== ===================


.. Note::

    Reqid should be a unique number within all configured :code:`if_ipsec(4)` tunnels. The number 10 is arbitrary


.....................
Gateways
.....................

Next step on both ends is to define a gateway (:menuselection:`System->Gateways->Single`) which reaches the other end of this channel, the
interface should be automatically created and is called :code:`ipsec10` in this example.

Both ends will need a gateway pointing at each other :
Site A will need the following gateway:

===============================================================

======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Name                    IPSEC10_GW          IPSEC10_GW
Interface               IPSEC10             IPSEC10
Address Family          IPv4                IPv4
IP address              **192.168.123.2**   **192.168.123.1**
======================= =================== ===================


.....................
Routes
.....................

We may already prepare the routes as the interfaces and gateways are available in :menuselection:`System->Routes->Configuration`.

On Site A we need to define a path to Site B and the other way around:

===============================================================

======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Network Address         **10.0.2.0/24**     **192.168.2.0/24**
Gateway                 IPSEC10_GW          IPSEC10_GW
======================= =================== ===================


.....................
Enable IPsec
.....................

Before configuring the connections, we enable the IPsec module. Just mark the "enable" checkbox on the connections tab.

--------------------------------
Setting up the IPsec connection
--------------------------------

In order to setup a simple (and common) IPsec connection, we go to :menuselection:`VPN->IPsec->Connections` and add
a new entry.


.....................
General settings
.....................

Side by side the following general settings need to be set in this case, which configures the first part of the security association between
both sites:

===============================================================

======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Local addresses         **10.10.1.1**       **10.10.1.2**
Remote addresses        **10.10.1.2**       **10.10.1.1**
======================= =================== ===================

Press <save> to go to the next step.

.....................
Authentication
.....................

Next we will need to add local authentication (add a new record in the local grid):

===============================================================

======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Authentication          Pre-Shared Key      Pre-Shared Key
Id                      **hostA**           **hostB**
======================= =================== ===================

Then we need to set Pre-Shared Key for remote authentication as well:

===============================================================

======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Authentication          Pre-Shared Key      Pre-Shared Key
Id                      **hostB**           **hostA**
======================= =================== ===================

.. Note::

    Secrets for both ends need to be added to ":menuselection:`VPN->IPsec->Pre-Shared Keys`", site A needs a secret
    set for local identifier :code:`hostB`. Optionally one may also set a second (remote) identifier in which case the secret
    belongs to these two identifiers.

.....................
Children
.....................

Finally we may add a child which will add security policies. Since our VTI tunnel matches on all traffic, both Site A and B
use the same configuration which looks like this:


===============================================================

====================== ========================================
Mode                   Tunnel
Policies               **[uncheck]**
Local                  0.0.0.0/0
Remote                 0.0.0.0/0
====================== ========================================

.. Warning::

    Make sure no policies are installed, when missing a passthrough and having policies installed one would not be able
    to access the firewall anymore as traffic will be trapped inside the tunnel.

.....................
Save and apply
.....................

Finally save the settings and hit apply on the connections page to establish the tunnel.

--------------------------------
Validate
--------------------------------

Now can check if the tunnel is active on both side using the status overview in :menuselection:`VPN->IPsec->Status Overview`

--------------------------------
Install firewall policies
--------------------------------

With the tunnel active, all that remains is to accept traffic on this tunnel using the :menuselection:`Firewall->Rules->IPsec`
menu option.
