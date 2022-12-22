========================================
IPsec - Policy based public key setup
========================================

This example utilises the new options available in OPNsense 23.1 to setup a site to site tunnel in policy mode
between two OPNsense machines using key pairs.

.. contents:: Index

--------------------------------
Network topology
--------------------------------

The schema below describes the situation we are implementing. Two networks (A,B) and a transit network (10.10.1.0/24)
to peer both firewalls.

.. nwdiag::
  :scale: 100%

    nwdiag {

      span_width = 90;
      node_width = 180;
      network A {
          address = "10.1.0.0/24";
          pclana [label="PC Site A\n10.1.0.20",shape="cisco.pc"];
          fwa [shape = "cisco.firewall", address="10.1.0.1/24"];
      }
      network Ext {
          address = "10.10.1.0/24";
          label = "Ext";
          fwa [shape = "cisco.firewall", address="10.10.1.1/24"];
          fwb [shape = "cisco.firewall", address="10.10.1.2/24"];
      }
      network B {
          address = "192.168.1.0/24"
          fwb [shape = "cisco.firewall", address="192.168.1.20"];
          pclanb [label="PC Site B\n192.168.1.20",shape="cisco.pc"];
      }


    }


--------------------------------
Preparations
--------------------------------

Since our policy based setup doesn't require interfaces, gateways and routes, we only need to make sure the IPsec
module is enabled on the Connections tab and Key pairs are registered for both hosts.

..................................
Key pairs
..................................

Go to the :menuselection:`VPN->IPsec->Key Pairs` option in the menu and create a new key on both hosts, then copy the public part
from Site A to Site B and vise versa. Keys may easily be generated with the gear button in the Key type field.


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

.. Note::

    One may omit the local address if any address may be used to initiate the connection from, other valid options
    are also mentioned in the help text of the attribute.


.....................
Authentication
.....................

Next we will need to add local authentication (add a new record in the local grid):

===============================================================

======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Authentication          Public Key          Public Key
Id                      **hostA**           **hostB**
Public Keys             **hostA-key**       **hostB-key**
======================= =================== ===================

Then we need to set Pre-Shared Key for remote authentication as well:

===============================================================

======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Authentication          Public Key          Public Key
Id                      **hostB**           **hostA**
Public Keys             **hostB-key**       **hostA-key**
======================= =================== ===================


.. Note::

    On host A the private key for Host A should be known and only the public key of Host B, Host B is exactly the oposite.


.....................
Children
.....................

Finally we may add a child which will add security policies and kernel routes.


======================= =================== ===================
Property                site A              site B
======================= =================== ===================
Mode                    Tunnel              Tunnel
Policies                [checked]           [checked]
Local                   **192.168.1.0/24**  **10.0.1.0/24**
Remote                  **10.0.1.0/24**     **192.168.1.0/24**
======================= =================== ===================

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
