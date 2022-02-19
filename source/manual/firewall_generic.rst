===========================
Generic info
===========================

This chapter explains some of the concepts that are being used in different modules of our firewall system and
therefore don't belong to a specific section of this topic.


-----------------------------------------
Address types
-----------------------------------------

When choosing source and or destination addresses, the user can choose several options depending on the context.
To explain what the different options mean when being presented, we will sum them up below:

========================================================================================================================================================

====================================  ==================================================================================================================
Alias                                 Flexible type of network or address definition for easy reuse, expained in
                                      :doc:`aliases </manual/aliases>`
Single host or network                Standard host or network in `CIDR notation <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__
any                                   All IPv4 and/or IPv6 addresses (in the world)
This Firewall                         All IPv4 and/or IPv6 addresses assigned to this firewall
[Interface] Network                   All networks assigned to the physical interface, this will include networks of virtual addresses assigned as well
                                      ([Interface] is explained in the :doc:`interfaces </manual/interfaces>` topic). Normally used to allow traffic
                                      from or to clients connected to a specific interface.
[Interface] Address                   All addresses configured on an interface, this includes all virtual (alias) addresses as well.
Virtual IPs                           Explicit selection for addresses defined in :doc:`Virtual IPs </manual/firewall_vip>`
====================================  ==================================================================================================================
