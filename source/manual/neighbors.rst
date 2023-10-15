===========================
Neighbors
===========================

The neighbors section (available as of 24.1) allows the definition of static IPv4 and IPv6 addresses
on your network.

For IPv4 entries will be saved into the :code:`ARP` table, IPv6 uses :code:`NDP` to register machines mac addresses
to IP addresses.

These tables determine to which (physcal) machine an IP address is connected, which can be practical when arp
messages are not being received or we want to force the ip/mac combination for specific clients.

When opening the page it will show a grid containing all static entries defined, these may also originate from
other components (such as dhcp), in which case you cannot edit them. Entries defined here do contain the following
options:

==============================================================================================================================================

=========================== ==================================================================================================================
Ether Address               Hardware MAC address of the cllient (format xx:xx:xx:xx:xx:xx)
IP address                  IP address to assign to the provided MAC address, which will either end up in the arp (IPv4) or ndp (IPv6) table
Description                 Description for internal use
=========================== ==================================================================================================================


.. Tip::

    To analyse the current contents of the ARP or NDP tables, use the interface diagnostics menu detailed in
    the :doc:`diagnostics </manual/diagnostics_interfaces>` document.

