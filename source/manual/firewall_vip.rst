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
(by setting its VHID).

Usually the subnet mask should match the interfaces or be defined as a single address (/32 or /128).

..................
CARP
..................


Specifies an address for use in a high availability cluster, acts like a
regular address when the node is in MASTER state.

Internally a custom mac address is generated needed for the protocol.
More information about CARP can be found in our :doc:`high availability </manual/hacarp>` section.

.. Note::
    The virtual MAC address of a CARP interface is :code:`00:00:5e:00:01:XX`, where the last two digits will be
    populated by its vhid.

.. Note::
    CARP uses IP protocol number 112 (0x70), to detect priority it will send out advertisements using
    :code:`224.0.0.18` or :code:`FF02::12`.


..................
Proxy ARP
..................

Does not add a real address to an interface, instead it will use `choparp <https://www.freebsd.org/cgi/man.cgi?query=choparp>`__ to reply to
arp requests on the network. This can sometimes be practical in situations where clients should be let to believe an address is local.


..................
Other
..................

The **other** type won't respond to ICMP ping messages or reply to ARP requests, it merely is a definition of an
address (or range) which can be used in NAT rules.


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
