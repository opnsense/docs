=========
Routes
=========

Routing is one of the core features of your firewall, which is responsible for forwarding packets over the network
based on (predefined) paths.

Within the routing section of your firewall you can keep track of configured routes and define static routes
yourself to teach your firewall which path it should take when forwarding packets to a specific network.



.. blockdiag::
   :desctable:

   blockdiag {
      client [shape="cisco.pc", label="[1]"];
      OPNsense [shape="cisco.firewall", label=""];
      internet [shape="cisco.cloud"];
      private_net [shape="cisco.cloud", label=""];
      private_net2 [shape="cisco.cloud", label="[2]"];
      Gateway1 [shape="cisco.router", label=""];
      Gateway2 [shape="cisco.router", label="[3]"];
      client -> OPNsense;
      OPNsense -> Gateway1 -> internet;
      OPNsense -> Gateway2 -> private_net;
      OPNsense -> Gateway2 -> private_net2;

      group {
          label = "Client";
          color = none;

          client;
      }

      group {
        label = "OPNsense";
        color = none;

        OPNsense;
      }

      group {
          label = "Gateways";
          color = none;

          Gateway1 ;
          Gateway2 ;
      }

      group {
          label = "Networks";
          color = none;

          internet;
          private_net;
          private_net2;
      }
   }


When a client sends a packet to the firewall for a network not directly attached to it, the firewall would
normally check its routing table to determine to which gateway (see :doc:`/manual/gateways`) it should be send.


.. Tip::
    Use traceroute (:menuselection:`Interfaces --> Diagnostics --> Trace Route`) to verify which path traffic would
    follow to reach its destination.

----------------------
Configuration
----------------------

This is where you can setup static routes, looking at the diagram in the previous chapter, here you would define how
:code:`[1]` would access :code:`[2]` using router :code:`[3]`.

The number of settings are obviously limited, we need to know the gateway and the target network.

===========================================================================================================

============================= =============================================================================
Disabled                      (temporary) disable this item
Network Address               Destination network to reach
Gateway                       The gateway to use.
Description                   Optional description for this item
============================= =============================================================================


.. Note::
    Some services are known to update the routing table themselves, in which case you shouldn't add static routes
    manually (OpenVPN manages its own routes for example).


................................
Equal-Cost Multipath (ECMP)
................................

ECMP distributes traffic to the same destination network across multiple gateways with equal routing priority.
It is supported for static routes and for dynamic routing via the FRR plugin (see :doc:`/manual/dynamic_routing`).

To configure ECMP:

1. Set :code:`net.route.multipath` to :code:`1` in :menuselection:`System --> Settings --> Tunables` and apply the change.
   Alternatively, select **Enable ECMP routing** in the configuration wizard.
2. In :menuselection:`System --> Routes --> Configuration`, add an enabled static route for each gateway,
   using the same **Network Address** (including prefix length) and a different **Gateway** for each entry.
   The gateways must already be configured under :menuselection:`System --> Gateways --> Configuration`.
3. Apply the routes and check :menuselection:`System --> Routes --> Status` to verify the installed paths.

For example, two routes for :code:`192.0.2.0/24` via different gateways provide two equal-cost paths to that network.
The configuration page groups routes by destination and displays **ECMP routing disabled** when multiple routes
share a destination while :code:`net.route.multipath` is disabled (the default).

.. Warning::

    ECMP static routes currently do not support path monitoring. Failures that leave a route installed must be
    handled by clients using that route. UDP-based protocols with recovery mechanisms, such as QUIC, may recover
    seamlessly, while TCP connections may stall until they time out or the client retries.
    Initial connections can also be sticky: repeated attempts may select the same failed path, making a failed
    link appear to be a permanent loss of connectivity even when another path is available.


----------------------
Status
----------------------


The status page shows the current active content of the routing table.

ECMP routes can be expanded to show their individual next hops.

===========================================================================================================

============================= =============================================================================
Proto                         Protocol (IPv4 or IPv6)
Destination                   Destination network
Gateway                       Where to send the packet for this destination network
Flags                         Routes have associated flags which influence operation of the protocols
                              when sending to destinations matched by the routes.
                              See the **Flags** table below for details.
Use                           Counts the number of packets sent via this route
MTU                           The MTU set for this route
Netif                         Interface to use for this route
Netif (name)                  Name of the interface if found
Expire                        The time at which this route should expire, or zero if it should	never expire.
                              It is the responsibility of individual protocol suites to	ensure that routes are
                              actually deleted once they expire.
============================= =============================================================================


.............
Flags
.............


The following flags are supported by the kernel.

============================= =============================================================================
Letter / Flag                 Description
============================= =============================================================================
1 [RTF_PROTO1]                Protocol specific routing flag
2 [RTF_PROTO2]                Protocol specific routing flag
3 [RTF_PROTO3]                Protocol specific routing flag
B [RTF_BLACKHOLE]             Just discard pkts (during updates)
b [RTF_BROADCAST]             The route represents a broadcast address
C [RTF_CLONING]               Generate new routes on use
c [RTF_PRCLONING]             Protocol-specified generate new routes on use
D [RTF_DYNAMIC]               Created dynamically (by redirect)
d [RTF_DONE]                  Message confirmed
G [RTF_GATEWAY]               Destination is a gateway
H [RTF_HOST]                  Host entry (net otherwise)
L [RTF_LLINFO]                Valid protocol to link address translation
M [RTF_MODIFIED]              Modified dynamically (by redirect)
R [RTF_REJECT]                Host or net unreachable
S [RTF_STATIC]                Manually added
U [RTF_UP]                    Route usable
X [RTF_XRESOLVE]              External daemon resolves name
============================= =============================================================================

----------------------
Logs
----------------------

Route related logging, like :code:`radvd` and :code:`rtsold` for IPv6 write messages to this logging section
which can be used for debugging purposes.
