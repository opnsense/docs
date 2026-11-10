===========================
Neighbors
===========================

.. contents:: Index


--------------------
Overview
--------------------

Neighbors are hosts with a hardware address that are connected to the same OSI layer 2 broadcast domain.

Hosts maintain their own local neighbor table, independent of other hosts in the same broadcast domain.

Whenever a host sends a packet to an IP address, it first tries to resolve if the target can be found in the same
broadcast domain. If the destination is not on-link, the packet will be sent to the default gateway.

A central host like a firewall will automatically learn most neighbors since it will be the default gateway.

For automatic host discovery and its logs, see :doc:`hostwatch`.


--------------------
Static Assignments
--------------------

Static assignments can be configured in :menuselection:`Interfaces --> Neighbors`.

This page allows the definition of static IPv4/IPv6 to MAC address mappings on your network.

IPv4 entries will be saved into the ARP table, IPv6 into the NDP table.

These tables define which hardware address is associated with which IP address. This can be practical when ARP/NDP
messages are not being received or we want to force the IP/MAC combination for specific clients.

When opening the page it will show a grid containing all static entries defined:

==============================================================================================================================================

=========================== ==================================================================================================================
**Ether Address**           Hardware MAC address of the client (format xx:xx:xx:xx:xx:xx)
**IP address**              IP address to assign to the provided MAC address, which will either end up in the ARP (IPv4) or NDP (IPv6) table
**Description**             Description for internal use
=========================== ==================================================================================================================

.. Attention::

    Some entries can be from other sources like DHCP and cannot be edited.

.. Tip::

    To analyse the current contents of the ARP or NDP tables, use the interface diagnostics menu detailed in
    the :doc:`diagnostics </manual/diagnostics_interfaces>` document.
