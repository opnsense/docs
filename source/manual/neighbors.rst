===========================
Neighbors
===========================

.. contents:: Index


--------------------
Overview
--------------------

Neighbors are devices with an ethernet address that are connected to the same OSI layer 2 broadcast domain.

Devices maintain their own local neighbor table, independent of other devices in the same broadcast domain.

Whenever a device sends a packet to an IP address, it first tries to resolve if the target can be found in the same
broadcast domain. If the destination is not on-link, the packet will be sent to the default gateway.

A central device like a firewall will automatically learn most neighbors since it will be the default gateway.


--------------------
Automatic Discovery
--------------------

The host discovery service offers a way to discover most neighbors on the network via their ARP and NDP messages.
When the daemon is activated, it builds a database of known neighbors and logs when IP address to MAC mappings change.

This can be useful to see how volatile a network is and if unknown new devices appear.

Running the daemon improves some services that currently directly consume the ARP and NDP tables. The database has a persistent state,
can be queried faster, and for IPv6 will have a better picture of RFC 4941 addresses.


Settings
--------------------

Settings can be found in :menuselection:`Interfaces --> Neighbors --> Automatic Discovery`

==============================================================================================================================================

=========================== ==================================================================================================================
**Enable**                  Enable the "hostwatch" service to discover network hosts.
**Interfaces**              Limit host discovery to the interfaces selected here.
**Promiscuous mode**        Listening for network packets not targeted directly at us.
**Verbose logging**         Verbosity mode, send more detailed information to the log.
**Ignore networks**         Ignore the selected networks.
=========================== ==================================================================================================================

.. Attention::

    The service will only listen on ethernet interfaces. Tunnel, loopback and similar interfaces are skipped since there is no ARP/NDP traffic.

.. Tip::

    Promiscuous mode is rarely needed. The firewall is in a central position and routes traffic between networks. The setting makes sense in a network
    where it would only be an observer.


Discovered Hosts
--------------------

If the host discovery service is enabled, you can see the contents of the database in this table. Otherwise, it will show the current contents of the
kernel ARP and NDP tables.

An interesting metric can be the "Last Seen" column, which shows devices that have recently joined or not seen for a while.


Discovery Log
--------------------

In the discovery log, you can find entries for new stations (devices) and movements of devices.

These logs have a simple structure, and could be consumed by an external syslog server for further processing (e.g., alerts for new stations.)

If the log is busy with a lot of movements that look like flapping, something could be wrong in your network. Most common would be MAC address duplication,
or multiple devices fighting for the same IP address.


--------------------
Static Assignments
--------------------
This section allows the definition of static IPv4/IPv6 to MAC address mappings on your network.

IPv4 entries will be saved into the :code:`ARP` table, IPv6 into the :code:`NDP` table.

These tables define which hardware address is associated with which IP address. This can be practical when ARP/NDP
messages are not being received or we want to force the IP/MAC combination for specific clients.

When opening the page it will show a grid containing all static entries defined:

==============================================================================================================================================

=========================== ==================================================================================================================
Ether Address               Hardware MAC address of the client (format xx:xx:xx:xx:xx:xx)
IP address                  IP address to assign to the provided MAC address, which will either end up in the ARP (IPv4) or NDP (IPv6) table
Description                 Description for internal use
=========================== ==================================================================================================================

.. Attention::

    Some entries can be from other sources like DHCP and cannot be edited.

.. Tip::

    To analyse the current contents of the ARP or NDP tables, use the interface diagnostics menu detailed in
    the :doc:`diagnostics </manual/diagnostics_interfaces>` document.

