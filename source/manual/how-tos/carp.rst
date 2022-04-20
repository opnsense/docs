
==============
Configure CARP
==============


--------
Overview
--------

One of the more powerful features of OPNsense is to set-up a redundant
firewall with automatic fail-over option. This chapter describes step by
step how to create a set-up based on two networks. The 192.168.1.0/24
will be used for the internal network and 172.18.0.0/24 will be used to
route our traffic to the internet.

.. image:: ./images/900px-Carp_setup_example.png
  :width: 100%

When using CARP ( `FreeBSD handbook on CARP <https://www.freebsd.org/doc/handbook/carp.html>`__ ), all
fail-safe interfaces should have a dedicated IP address which will be
combined with one shared virtual IP address to communicate to both
networks. In the picture above the dashed lines are used to mark the
virtual addresses.

The configuration file (XML) for both firewalls can be downloaded from
the wiki.

-----------
Terminology
-----------

There is some terminology involved in setting up a CARP cluster, which
we will explain briefly first:

.. rubric:: CARP
    :name: carp

Common Address Redundancy Protocol uses IP protocol 112, is derived from
OpenBSD and uses multicast packets to signal its neighbours about its
status. Always make sure that each interface can receive CARP packets.
Every virtual interface must have a unique Virtual Host ID (vhid), which
is shared across the physical machines. To determine which physical
machine has a higher priority, the advertised skew is used. A lower skew
means a higher score. (our master firewall uses 0).


.. rubric:: pfSync
    :name: pfsync

Together with CARP, we can use pfSync to replicate our firewalls state.
When failing over you need to make sure both machines know about all
connections to make the migration seamless. It's highly advisable to use
a dedicated interface for pfSync packets between the hosts, both for
security reasons (state injection) as for performance.

.. Warning::
    When using different network drivers on both machines, like running a HA 
    setup with one physical machine as master and a virtual machine as slave, 
    states can not be synced as interface names differ. The only workaround
    would be to set up a LAGG.

.. rubric:: XMLRPC sync
    :name: xmlrpc-sync

OPNsense includes a mechanism to keep the configuration of the backup
server in sync with the master. This mechanism is called XMLRPC sync and
can be found under :menuselection:`System --> High Availability --> Settings`.

-----------------------------------------
Setup interfaces & basic firewall rules
-----------------------------------------

.. Warning::
    Make sure the interface assignments on both systems are identical!
    Via :menuselection:`Interfaces --> Overview` you can check if e.g. DMZ is opt1 on
    both machines. When the assignments differ you will have mixed
    Master and Backup IPs on both machines.

Our example uses three interfaces, which all have a rather basic setup.

.. rubric:: Master
    :name: master


Go to interfaces, make sure you have all three interfaces assigned and
setup the following addresses and subnets:

+-----------------------+
| LAN 192.168.1.10/24   |
+-----------------------+
| WAN 172.18.0.101/24   |
+-----------------------+
| PFSYNC 10.0.0.1       |
+-----------------------+

Next we need to make sure the appropriate protocols can be used on the
different interfaces, go to :menuselection:`Firewall --> Rules` and make sure both LAN and
WAN accept at least CARP packets (see protocol selection). Because we're
connecting both firewalls using a direct cable connection, we will add a
single rule to accept all traffic on all protocols for that specific
interface. Another option is to only accept traffic to the GUI port and
pfSync protocol.

.. rubric:: Backup
    :name: backup

The backup server needs its own dedicated addresses, we will use these:

+----------+-------------------+
| LAN      | 192.168.1.20/24   |
+----------+-------------------+
| WAN      | 172.18.0.102/24   |
+----------+-------------------+
| PFSYNC   | 10.0.0.2          |
+----------+-------------------+

.. Note::
    Per default the dropdown menu for subnet mask only fits for IPv4
    addresses (up to 32). If you want to add an IPv6 CARP address,
    write you v6 address and the dropdown list will auto-update to  
    itself up to 128.
    
Because we are going to synchronize firewall settings between both
hosts, we only need to make sure that the pfSync interface can accept
data from the master for the initial setup. Use the same rule as used
for the master on this interface.

-----------------
Setup Virtual IPs
-----------------

On the master node we are going to setup our Virtual IP addresses, which
will also be added to the backup node with a higher skew after synchronisation. 
Go to :menuselection:`Interfaces --> Virtual IPs` and add a new one with the following
characteristics:

+-------------------------+------------------------------------+
| Type                    | Carp                               |
+-------------------------+------------------------------------+
| Interface               | WAN                                |
+-------------------------+------------------------------------+
| IP addresses            | 172.18.0.100 / 24                  |
+-------------------------+------------------------------------+
| Virtual password        | opnsense (the example uses this)   |
+-------------------------+------------------------------------+
| VHID Group              | 1                                  |
+-------------------------+------------------------------------+
| Advertising Frequency   | Base 1 / Skew 0                    |
+-------------------------+------------------------------------+
| Description             | VIP WAN                            |
+-------------------------+------------------------------------+

And another using the following:

+-------------------------+------------------------------------+
| Type                    | Carp                               |
+-------------------------+------------------------------------+
| Interface               | LAN                                |
+-------------------------+------------------------------------+
| IP addresses            | 192.168.1.1 / 24                   |
+-------------------------+------------------------------------+
| Virtual password        | opnsense (the example uses this)   |
+-------------------------+------------------------------------+
| VHID Group              | 3                                  |
+-------------------------+------------------------------------+
| Advertising Frequency   | Base 1 / Skew 0                    |
+-------------------------+------------------------------------+
| Description             | VIP LAN                            |
+-------------------------+------------------------------------+

------------------
Setup outbound NAT
------------------

When traffic is going out of the firewall it should also use the virtual
IP address on the WAN interface to make seamless transitions possible. The 
default NAT configuration is for OPNsense is to use Automatic outbound NAT 
rule generation using the WAN interface's IP address for outgoing connections. 
This will not allow seamless transitions and needs to be changed to the WAN 
VIP.

Go to :menuselection:`Firewall --> NAT --> Outbound`. Choose manual outbound
nat rule generation. On this page create the a rule originating from the
192.168.1.0/24 network to use the CARP virtual interface (172.18.0.100).
The rule should contain the following:

+-------------------------+------------------------------------+
| Interface               | WAN                                |
+-------------------------+------------------------------------+
| Source addresss         | LAN net (192.168.1.0/24)           |
+-------------------------+------------------------------------+
| Translation / target    | 172.18.0.100 (CARP virtual IP)     |
+-------------------------+------------------------------------+

----------------------------
(optional) Setup DHCP server
----------------------------

When using DHCP for the local area network, there are some things to
consider. All clients should use the virtual address instead of the
physical address it's normally propagating. Next thing to consider is
there will be two servers active at the same time, which should know of
each others pools. If DNS requests are also forwarded by OPNsense, make
sure the DHCP server sends the right IP address. These are settings used
in our example (on the master server):

+--------------------+----------------+
| DNS servers        | 192.168.1.1    |
+--------------------+----------------+
| Gateway            | 192.168.1.1    |
+--------------------+----------------+
| Failover peer IP   | 192.168.1.20   |
+--------------------+----------------+

---------------------------------
Setup pfSync and HA sync (xmlrpc)
---------------------------------

First we should configure pfSync to synchronize the connection state tables and
HA sync (xmlrpc) on the master firewall. Go to
:menuselection:`System --> High Availability --> Settings` and enable pfSync by
activating the `Synchronize States` checkbox, selecting PFSYNC for the
`Synchronize Interface` and enter the peer IP (10.0.0.2) in the field
`Synchronize Peer IP`.

To synchronize the configuration settings from the master to the backup
firewall, we setup the XMLRPC sync. In the `Synchronize Config to IP` field
we enter the peer IP (10.0.0.2) of the PFSYNC interface again to keep this
traffic on the direct connection between the two firewalls. Now we need to
enter the remote user name and password and configure the settings we want to
duplicate to the backup server. For our setup we will enable the following:

+---------------------------+
| Synchronize rules         |
+---------------------------+
| Synchronize NAT           |
+---------------------------+
| Synchronize DHCPD         |
+---------------------------+
| Synchronize Virtual IPs   |
+---------------------------+

After this we configure pfSync on the backup firewall. Go to
:menuselection:`System --> High Availability --> Settings` and enable pfSync by
activating the `Synchronize States` checkbox, selecting PFSYNC for the
`Synchronize Interface` and enter the master IP (10.0.0.1) in the field
`Synchronize Peer IP`. Do not configure XMLRPC sync on the backup firewall.

--------------
Finalize setup
--------------

Just to make sure all settings are properly applied, reboot both
firewalls before testing.

-------------
Testing setup
-------------

First go to :menuselection:`System --> High availability --> Status` in the OPNsense webinterface and check if
both machines are properly initialized.

To test our setup, we will connect a client to the local area network
and open a ssh connection to a host behind both firewalls. Now when
connected you should be able to look at the state table on both OPNsense
firewalls (:menuselection:`Firewall --> Diagnostics --> States Dump`) and they should both display the same
connection. Next try to pull the network plug from the master firewall
and it should move over to the backup without loosing (or freezing) the
ssh connection.

------------------------
Adding multiple CARP IPs
------------------------

If your provider offers you a subnet of public IP addresses and you 
want to expose them for NAT or different services running on your 
Firewall, you will also have to add them to your HA setup. 
Since adding a VHID for every IP would make the CARP traffic very noisy,
you can also add a new IP Alias and choose the correct VHID where the
first CARP IP is configured. 

.. Note::
   IP Alias is not synchronized to slave, be sure to also add it to your
   second machine.

-----------------------------------
Example: Updating a CARP HA Cluster
-----------------------------------

Running a redundant Active/Passive cluster leads to the expectation to have zero 
downtime. To keep the downtime at a minimum when running updates just follow
these steps:

- Update your secondary unit and wait until it is online again
- On your primary unit go to :menuselection:`Interfaces --> Virtual IPs --> Status` and click **Enter Persistent CARP Maintenance Mode**
- You secondary unit is now *MASTER*, check if all services like DHCP, VPN, NAT are working correctly
- If you ensured the update was fine, update your primary unit and hit **Leave Persistent CARP Maintenance Mode**

With these steps you will not lose too many packets and your existing connection will be transferred as well.
Also note that entering persistent mode survives a reboot.

---------
Resources
---------

#. Configuration for master server ( :download:`Carp_example_master.xml <resources/Carp_example_master.xml>` )
#. Configuration for backup server ( :download:`Carp_example_backup.xml <resources/Carp_example_backup.xml>` )
