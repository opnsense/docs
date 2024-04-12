===========================
Virtual IPs
===========================

When using additional addresses for features like NAT or binding services to different interfaces, you can
add extra addresses to already defined interfaces using **Virtual IPs**.


.. Note::

    Virtual IPs also play a vital role in :doc:`high availability </manual/hacarp>` setups


--------------------------
Types and their usage
--------------------------

.. _Firewall_VIP_Types:

OPNsense supports different types of virtual addresses all with their specific purposes, which we will explain below.


..................
IP Alias
..................

A standard extra address, which you can use to bind services to or use in
NAT rules.

The address will act like a normal interface address, which means
it will respond to ICMP ping requests and will generate ARP traffic
(OSI layer 2).

Additionally you can add an alias into an existing CARP group
(by setting its VHID). See the CARP VIP type below for more information.

Usually the subnet mask should match the interfaces or be defined as a single address (/32 or /128).

..................
CARP
..................


Specifies an address for use in a high availability cluster, acts like a
regular address when the node is in MASTER state.

A VHID Group number must be specified. The "Select an unassigned VHID" button allows you to
automatically select an available VHID number. The usual approach to selecting a VHID is to use a different
number per interface, but this is not a strict requirement, since the underlying protocol only
requires a VHID to be unique within the broadcast domain of the specified interface. However, to ease
management and debugging it is recommended to keep a separate VHID per interface.

Internally a custom mac address is generated needed for the protocol.
More information about CARP can be found in our :doc:`high availability </manual/hacarp>` section.

.. Note::
    The virtual MAC address of a CARP interface is :code:`00:00:5e:00:01:XX`, where the last two digits will be
    populated by its vhid.

.. Note::
    CARP uses IP protocol number 112 (0x70), to detect priority it will send out advertisements using
    :code:`224.0.0.18` or :code:`FF02::12`.

**Combining CARP virtual IP types with IP aliases**

In cases where there is a need for multiple IP aliases on a single interface which should be shared by a CARP cluster,
you can assign a single CARP VIP with a specific VHID in combination with regular IP alias types,
setting the VHID field to the same number as the initial CARP VIP VHID:

- The entire set of configured virtual IP addresses are now considered a single host (VHID).
- Only this VHID will send out advertisement packets.
- The set of IP addresses for this VHID are hashed and inserted in the advertisement packets.
  This hash is compared to the same VHID hash on the peer on reception of CARP advertisements. If they do not match,
  the peer will assume the master role as the configuration is out of sync.

.. Note::
    See `Adding multiple CARP IPs <how-tos/carp.html#adding-multiple-carp-ips>`__ for more information and the
    proper procedure to add IP aliases to a running CARP cluster.

.. Warning::
    While technically it is possible to assign multiple CARP VIPs on the same interface, but with separate VHIDs,
    this has no benefit and is not recommended. The CARP traffic and system procedures for failover will increase
    linearly in noise per virtual IP. Since the primary purpose of CARP is to react to link state changes, a single
    VHID acting for a single interface is the most efficient way to use the protocol.

.. Tip::
    If you're debugging a CARP setup, consider raising the CARP system logging verbosity. This can be done by
    adding the :code:`net.inet.carp.log` with value :code:`2` tunable in System -> Settings -> Tunables.
    The logs can be seen in System -> Log Files -> General (kernel process) or by using :code:`dmesg`.

..................
Proxy ARP
..................

Does not add a real address to an interface, instead it will use `choparp <https://www.freebsd.org/cgi/man.cgi?query=choparp>`__ to reply to
arp requests on the network. This can sometimes be practical in situations where clients should be let to believe an address is local.


..................
Other
..................

The **other** type won't respond to ICMP ping messages or reply to ARP requests, it merely is a definition of an
address (or range) which can be used in NAT rules. This is convenient when the firewall has a public IP block routed
to its WAN IP address, IP Alias, or a CARP VIP.


--------------------
Settings
--------------------

The interface should validate suitable combinations of settings, below you will find a detailed explanation for
everyone of them.

=====================================================================================================================

====================================  ===============================================================================
Mode                                  The type of address, as defined in :ref:`Types <Firewall_VIP_Types>`.
Interface                             The interface this address belongs to.
Type                                  Either Network or Single address, only has affect when creating NAT rules,
                                      where **Proxy ARP** and **Other** combined with **Expansion** will generate
                                      separate addresses for all items in the netmask.
Expansion                             When applicable, expand netmask to separate addresses.
Address                               The address and netmask to assign, when assigning multiple addresses in the
                                      same network, the masks usually should match.
Gateway                               Only applies to **IP Alias** types, usually this field should be empty, except
                                      some tunnel devices (ppp/pppoe/tun) expect the gateway address to be defined.
Virtual IP Password                   The password used to encrypt CARP packets over the network, should be the
                                      same on preferred master and backup node(s).
VHID Group                            The Virtual Host ID. This is a unique number that is used to
                                      identify the redundancy group to other nodes in the group,
                                      and to distinguish between groups on the same network.
                                      Acceptable values are from 1 to 255.
                                      This must be the same on all members of the group.
Advertising Frequency                 Defines how often is advertised that this interface is part of a group
                                      (:code:`Base` defined in seconds) and how much to **skew** when sending
                                      advertisements. A higher :code:`skew` means less preferred.
Description                           User friendly description of this VIP
====================================  ===============================================================================


--------------------
Status
--------------------

The status page shows all configured carp VHID groups and their active status.
Our status screen also offers some buttons to disable carp or force a node into maintenance mode.

All different statuses are detailed below.

................
INIT
................

Usually this indicates there is an issue with the interface, often this relates to not disconnected interfaces
or other technical problems.


................
BACKUP
................

In backup state this interface is part of a cluster and listening to advertisements.
If for some reason it won't receive advertisements for a short period of time, it will transition to master.

................
MASTER
................

Marks the active node, while listening to advertisements seen on the network. If another node is seen with a better
advertisement it might transition to backup
(depending on :code:`preempt` setting, found on the :menuselection:`System --> High Availability --> Settings` page).

................
DISABLED
................

Displayed when **Temporarily Disable CARP** is clicked on this page.
