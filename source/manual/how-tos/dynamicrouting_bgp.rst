====================
Dynamic Routing: BGP
====================

.. Note::
    Since OPNsense version 20.7 the frr package was updated to version 7,
    which requires an eBGP outbound policy by default. The requirement was
    disabled but it is strongly advised to use a prefix-list and filter 
    your networks to your outbound neighbors.

-------------
Configuration
-------------

The following tables describe the most used configurations. 


General:

====================== =======================================================================
 Setting                Description
====================== =======================================================================
 Enable                 Enables the BGP daemon
 BGP AS Number          The internal AS number
 Router ID              Router ID this system is uses for communication with other peers
 Network                A list of local networks to announce. With frr version 6 this setting 
                        and an additional Null-Route was enough to announce the networks
                        Now it is advised to add a prefix-list and link it in neighbor config
 Route Redistribution   Allows to redistribute additional routes (static, kernel, OSPF etc.)
                        into the BGP process. Usually this is only used with OSPF but also 
                        available here
====================== =======================================================================

Neighbors:

========================= ===================================================================
 Setting                   Description
========================= ===================================================================
 Enable                    Enables the neighbor config
 Description               Give a description for documentation when many neighbors are used
 Peer IP                   The IP address of the neighbor
 Remote AS                 Remote AS where this neighbor belongs to. For iBGP this has to be 
                           the same number as in General tab 
 Update-Source Interface   Interface name nearest to the peer, usually WAN for eBGP and LAN 
                           for iBGP
 Next-Hop-Self             Enable this option if this is an iBGP neighbor
 Multi-Hop                 When the neighbor is not directly connected enable this option
                           BGP packets usually have a TTL of 1 and would get lost otherwise
 Send Defaultroute         Enable this option to send the neighbor itself as default gateway
 Prefix-List               Match against linked prefix-list and direction of in and out
                           To advertise a network to neighbor it would be direction out
                           To filter out specific networks advertised by peer it would be in
 Route-Map                 Same as prefix-list but used with route-maps. Route-maps are more 
                           powerful compared to prefix-list but also more complex
========================= ===================================================================

AS Path Lists:

============= ===================================================================
 Setting       Description
============= ===================================================================
 Enable        Enables the list entry
 Description   Give a description for documentation when many entries are used
 Number        The ACL rule number (10-99); keep in mind that there are no 
               sequence numbers with AS-Path lists. When you want to add a 
               new line between you have to completely remove the ACL
 Action        Permit or Deny for this list. This can also be done via route-map
 AS            A regular expression to match for AS Paths like *.$*. This is
               typically used for path prepending
============= ===================================================================

Prefix Lists:

================= ===================================================================
 Setting           Description
================= ===================================================================
 Enable            Enables the list entry
 Name              Prefix Lists are named lists so they are not grouped by a number
 Description       Give a description for documentation when many entries are used
 Sequence Number   Multiple rules can belong to a named list. With the squence 
                   number the ordering is done (top to bottom)
 Action            Permit or Deny for this list. This can also be done via route-map
 Network           The network pattern to match. It is also possible to add "ge" or 
                   "le" additions after the network statement. Usually this is used
                   to announce the local network or maybe to decline specific routes
                   from a neighbor      
================= ===================================================================

Community Lists:

================= ===================================================================
 Setting           Description
================= ===================================================================
 Enable            Enables the list entry
 Number            Prefix Lists are numbered lists so they are not grouped by a name
 Description       Give a description for documentation when many entries are used
 Sequence Number   Multiple rules can belong to a named list. With the squence 
                   number the ordering is done (top to bottom)
 Action            Permit or Deny for this list. This can also be done via route-map
 Community         The BGP communities attribute is widely used for implementing 
                   policy routing. Network operators can manipulate BGP communities 
                   attribute based on network policy          
================= ===================================================================

Route Maps:

============= =================================================================
 Setting       Description
============= =================================================================
 Enable        Enables the list entry
 Description   Give a description for documentation when many entries are used
 Name          Route Maps are named lists so they are not grouped by a number
 Action        Permit or Deny for this list
 ID            Multiple rules can belong to a route-map. With the ID the 
               ordering is done (top to bottom)
 AS Path       A linked AS Path to match against
 Prefix List   A linked Prefix List to match against
 Community     A linked Community List to match against
 Set           Via the set statement the specified matches can be manipulated.
               There are many options to set communities, change the local
               preference for gateway selection or use metrics for MED (Multi
               Exit Descriminator)
============= =================================================================

Here you can find a couple of examples:
http://docs.frrouting.org/en/latest/bgp.html#miscellaneous-configuration-examples
