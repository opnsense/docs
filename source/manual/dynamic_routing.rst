======================
Dynamic Routing (FRR)
======================

.. contents::
   :local:
   :depth: 2

Dynamic Routing (using routing protocols) is supported via an external plugin.
Routing protocols support your network equipment in finding the best available path for your packets.
We use Free Range Routing (`FRR <https://frrouting.org/>`__) to implement the various available protocols for
dynamic routing.

These routing protocols are used to:

* Improve fault tolerance (if a connection breaks, a new route will be found if possible)
* Simplify administration (you have to add fewer routes manually)

It is not adviseable to use dynamic routing in the following scenarios:

* When your network is small (it would be simpler to use static routes)
* If you are working in a highly isolated environment, where you have to be in control of every route in your network

Routing Protocols supported by the plugin include:

* RIPv1 and RIPv2
* OSPFv2 and v3
* BGPv4

.. Warning::
    Not all routing protocols will work in any setup because they may have to be direct neighbors.
    Consider the limitations of a routing protocol before using it.

.. Warning::
    It's strongly advised to increase the kern.ipc.maxsockbuf value via **Tunables**. Go to :menuselection:`System --> Settings --> Tunables` and check if there
    is already a tunable for maxsockbuf and set it to 16777216 if it is lower. Otherwise add a new one with
    name above and the specified value.

.. Warning::
    Disabling a running routing daemon can be dangerous as it can lead to an inaccessible machine.
    If you want to disable a running routing daemon, make sure you do not lose routes which are
    required by your connection to this machine (for example when using SSH).


------------
Installation
------------

Go to :menuselection:`System --> Firmware --> Plugins` and select ``os-frr`` from the available plugins.


----------------
General setup
----------------

To use one or more of the protocols included, the plugin must be enabled in
:menuselection:`Routing --> General`. Without any other service enabled this makes sure the zebra service is being
configured, which is the coordinating master service which handles generic features such as logging and acccess to kernel
routing.

.. Tip::

    By default logging should be enabled, which sends messages to the local logging and offers remote logging over syslog.
    Always make sure to choose a sensible log level (default is Notifications) and check the log in
    :menuselection:`Routing --> Diagnostics -> Log`

.. Note::

    The plugins supports seamless reloads since version `os-frr-1.4.3`. When using older versions, there is no configuration reloading.
    This means there might be a temporary loss of service when saving settings. Normally this is only a small glitch, but in high traffic areas it might be
    something to take under consideration when performing maintenance.

------------------------------------------------
Dynamic routing and high availability
------------------------------------------------

In enterprise networks there is often a need to protect services against all sorts of failures. Dynamic
routing helps to always provide a valid path for packets to travel. These nodes themselved might
need to be configured more resilient to prevent single points of failures on the edges of your network.

In OPNsense high availability and failover is organised around :doc:`carp <hacarp>`, which makes it a logical choice to
combine both technologies here as well.

There are different strategies ranging from disabling the daemon when in carp mode,
to more fine grained control of route propagation when a machine is in backup mode.


.. Note::

    `Unicast CARP` is available to use the protocol across router boundaries. This can enable the use of CARP on WAN interfaces peering with eBGP neighbors if they are not connected to the same switch.


CARP failover mode
..............................

The most simple mode available. When a node becomes `Backup` it will stop the FRR services. When it returns to `Master`
it will start the FRR services.

.. Note::

    Due to the nature of this option, it cannot be combined with other available CARP options.


OSPF[6]: CARP demote
.............................

This option registers a :doc:`status monitor </development/backend/carp>` on top of the FRR logging feed to detect changes in link status.
If OSPF cannot find its neighbors, it will make this machine less attractive by increasing the demotion factor.

The feature is inspired by OpenBSD's handling of CARP demotion in ospfd (https://man.openbsd.org/ospfd.conf.5) and can be enabled
using the :code:`CARP demote` checkbox in :menuselection:`Routing: OSPF[v3]`.

.. Note::

    Since the relevant neighbor negotiation messages are only being logged when the log level (in :menuselection:`Routing --> General`) is configured to debug,
    the log will be more chatty when using this feature. When using a lower log level the status monitor is not expected
    to catch any relevant events.


OSPF[6]: Influence interface cost based on CARP status
......................................................................

FRR does not natively support interaction with CARP status as the variant in OpenBSD does
(carp note in “depend on” keyword https://man.openbsd.org/ospfd.conf.5), this is where our next option comes into play.

Using the interface settings of an OSPF interface you can choose to adjust costs for that interface based on the CARP status of the
selected virtual address. Go to :menuselection:`Routing --> OSPF[v3] -> Interface` and choose an interface, here you will find the
following options that influence behaviour:

* Depend on (carp):

  * Select a virtual address that this interface relies on. When this target is not in **MASTER** mode, the selected interface is considered **demoted**

* Cost (when demoted):

  * Adjust the cost to this value when going to demoted state, usually one would use a high value here to prefer other routes first

* Cost:

  * The standard cost, when provided will be used when in normal conditions. If it's left blank FRR defaults will be used, which it will also rollback to when going back to master mode.


------------------------------------------------
Dynamic Routing Protocols
------------------------------------------------

..
    TODO: Add Tutorials for each section in separate document pages.

For more detailed information, check out the `FRR documentation <https://docs.frrouting.org/en/latest/protocols.html>`_.

* :ref:`General <general-section>`
* :ref:`RIP <rip-section>`
* :ref:`OSPF <ospf-section>`
* :ref:`OSPFv3 <ospfv3-section>`
* :ref:`BGP <bgp-section>`
* :ref:`BFD <bfd-section>`
* :ref:`STATIC <static-section>`

.. _general-section:

:menuselection:`Routing --> General`

.. tabs::

   .. tab:: General

      =================================== =======================================================================================================================
      Options                             Description
      =================================== =======================================================================================================================
      **Enable**                          This will activate the routing service. Without enabling it globally, none of the individual services will run.
      **Profile**                         Control FRR's default profile: `traditional` reflects defaults adhering mostly to IETF standards or common practices
                                          in wide-area internet routing. `datacenter` reflects a single administrative domain with intradomain links
                                          using aggressive timers.
      **Enable CARP Failover**            This will activate the routing service only on the master device. The backup device will stop the service completely.
      **Enable SNMP AgentX Support**      This will activate support for Net-SNMP AgentX.
      **Enable logging**                  Sends logs to the OPNsense integrated syslog-ng service.
      **Log Level**                       This is the detail level of the log. A higher level means more data is logged.
      **Firewall Rules**                  Enable automatically created firewall rules, when additional policies are needed,
                                          disable this and define your own custom policies in the Firewall section.
      =================================== =======================================================================================================================

   .. tab:: Firewall Rules

      =================================== =======================================================================================================================
      Description                         Rule autogenerated by `Firewall Rules` option
      =================================== =======================================================================================================================
      **Pass OSPF**                       Allows OSPF traffic from configured network IP address ranges to multicast `224.0.0.0/24` (direction: in).
      **Pass OSPF UNICAST**               Allows OSPF unicast traffic from configured network IP address ranges to the local interface (direction: in).
      **Pass OSPF**                       Allows OSPF traffic from the local interface to multicast `224.0.0.0/24` (direction: out).
      **Pass OSPF UNICAST**               Allows OSPF unicast traffic from the local interface to configured network IP address ranges (direction: out).
      **Pass OSPF6 MULTICAST**            Allows OSPFv3 traffic from link-local IPv6 (`fe80::0/10`) to multicast address `ff02::5/128` (direction: in).
      **Pass OSPF6 MULTICAST DR**         Allows OSPFv3 traffic from link-local IPv6 (`fe80::0/10`) to multicast address `ff02::6/128` (direction: in).
      **Pass OSPF6 UNICAST**              Allows OSPFv3 unicast traffic from link-local IPv6 (`fe80::0/10`) to the local interface (direction: in).
      **Pass OSPF6 MULTICAST**            Allows OSPFv3 traffic from the local interface to multicast address `ff02::5/128` (direction: out).
      **Pass OSPF6 MULTICAST DR**         Allows OSPFv3 traffic from the local interface to multicast address `ff02::6/128` (direction: out).
      **Pass OSPF6 UNICAST**              Allows OSPFv3 unicast traffic from the local interface to link-local IPv6 (`fe80::0/10`) (direction: out).
      =================================== =======================================================================================================================


.. Attention::

   Any route received with dynamic routing protocols will only be installed if no similiar local route already exists. E.g., if a neighbor advertises
   a default gateway route, but a directly attached default gateway route already exists, the local route will be preferred and the advertised route will be discarded.


.. _rip-section:

RIP (Routing Information Protocol) - `legacy`
................................................

:menuselection:`Routing --> RIP`

.. tabs::

    .. tab:: General

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **enable**                          This will activate the RIP service.
       **Version**                         Choose your RIP version (1 or 2). 1 is classful, 2 supports CIDR.
       **Passive Interfaces**              Select the interfaces, where no RIP packets should be sent to, (e.g., WAN interface).
       **Route Redistribution**            Select other routing sources, which should be redistributed to the other nodes. A good choice is `Connected Routes` to
                                           automatically redistribute all locally attached routes to other routers with RIP.
                                           Otherwise use the `Networks` option to manually insert networks to distribute.
       **Networks**                        Enter your networks in CIDR notation like ``127.0.0.0/8``.
       **Default Metric**                  Set the default metric to a value between 1 and 16. Routes with lower metrics will be preferred, while higher metrics
                                           indicate less preferred or distant paths.
       =================================== =======================================================================================================================


The Routing Information Protocol (RIP) is a basic distance-vector routing protocol that determines the best path to a network destination based on hop count.
With a maximum limit of 15 hops, RIP is suitable only for smaller networks. 
To prevent routing loops, RIP employs techniques like split horizon, route poisoning, and holddown timers.
While easy to configure, RIP has slow convergence and limited scalability, making it less popular in modern networks compared to more efficient protocols like OSPF.
It should be considered a legacy protocol.

.. toctree::
   :maxdepth: 2

   how-tos/dynamic_routing_rip.rst


.. _ospf-section:
.. _ospfv3-section:

OSPF/OSPFv3 (Open Shortest Path First)
................................................

:menuselection:`Routing --> OSPF`
:menuselection:`Routing --> OSPFv3`

.. tabs::

    .. tab:: General

       ===================================== =======================================================================================================================
       Options                               Description
       ===================================== =======================================================================================================================
       **Enable**                            This will activate the OSPF service.
       **CARP demote**                       Register CARP status monitor. When no neighbors are found, consider this node less attractive. Requires syslog enabled
                                             with "Debugging" logging. Incompatible with "Enable CARP Failover".
       **Router ID**                         (OSPF) If you have a CARP setup, you may want to configure a router id in case of a conflict.
                                             (OSPFv3) Router ID as an IPv4 Address to uniquely identify the router.
       **Reference Cost**                    (OSPF only) Adjust the reference cost in Mbps for path calculation, useful when bundling interfaces for higher bandwidth.
       **Passive Interfaces**                Select the interfaces where no OSPF packets should be sent.
       **Redistribution Map**                Route Map to set for Redistribution, can be used to send a specific network as advertisement when it is defined in a
                                             `Prefix List` attached to a `Route Map`.
       **Log Adjacency Changes**             If it should be logged when the topology of the area changes.
       **Advertise Default Gateway**         This will send the information that we have a default gateway.
       **Always Advertise Default Gateway**  Always sends default gateway information, regardless of availability.
       **Advertise Default Gateway Metric**  Allows manipulation of the metric when advertising the default gateway.
       **Route Redistribution**              Select other routing sources to redistribute to other nodes. Can be combined with a Route Map per redistribution.
       ===================================== =======================================================================================================================

    .. tab:: Neighbors (OSPF only)

       =================================== =======================================================================================================================
       Options                               Description
       =================================== =======================================================================================================================
       **Enable**                            (OSPF only) Enable / Disable
       **Description**                       (OSPF only) Optional description for the neighbor.
       **Peer-IP**                           (OSPF only) Specify the IP address of the OSPF neighbor.
       **Poll-Interval**                     (OSPF only) The poll-interval specifies the rate for sending hello packets to neighbors that are not active.
                                             When the configured neighbor is discovered, hello packets will be sent at the rate of the hello-interval. 
                                             The default poll-interval is 60 seconds.
       **Priority**                          (OSPF only) The priority is used to for the Designated Router (DR) election on non-broadcast multi-access networks.
       =================================== =======================================================================================================================

    .. tab:: Networks

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable / Disable
       **Network Address**                 (OSPF) Specifies the network address (e.g., `192.168.1.0`) to include in OSPF.
                                           (OSPFv3) Specifies the IPv6 network address (e.g., `fe80::1234`) to include in OSPFv3.
       **Network Mask**                    (OSPF) Defines the network mask (e.g., `24`) for the specified network.
                                           (OSPFv3) Defines the network prefix length (e.g., `64`) for the specified IPv6 address range.
       **Area**                            Assigns the network to an OSPF area using an identifier like `0.0.0.0` (Backbone Area). The Backbone Area connects
                                           other areas, supporting inter-area communication, while additional areas (e.g., `0.0.0.1`, `0.0.0.255`) segment
                                           the network logically to limit routing updates.
       **Area Range**                      Summarizes multiple networks in the specified area, consolidating multiple networks into a single summarized route
                                           (OSPF) `192.168.0.0/23`, (OSPFv3) `fe80:1234::/64`.
       **Prefix-List In**                  Filters inbound route advertisements using a prefix list.
       **Prefix-List Out**                 Filters outbound route advertisements using a prefix list.
       =================================== =======================================================================================================================

       .. Note::

          Using a **Network** configuration with `0.0.0.0` as the Backbone Area is beneficial in larger networks, where defining broad network ranges streamlines OSPF
          configuration. This approach avoids the need to configure OSPF individually on each interface by including all subnets within the specified range.
          The Backbone Area serves as the primary route aggregation point, allowing inter-area communication which is essential in hierarchical OSPF networks.
          `Networks` and `Interfaces` cannot have the same `Area`, only one of them can be defined in the `Backbone Area`.

    .. tab:: Interfaces

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable / Disable
       **Interface**                       Select an interface where these settings apply.
       **Authentication Type**             (OSPF only) Defines security method for OSPF exchanges (None, plain, or MD5) to prevent unauthorized updates.
       **Authentication Key**              (OSPF only) Specifies a password or key used for plain or MD5 authentication.
       **Authentication Key ID**           (OSPF only) Numeric identifier for MD5 authentication, ensuring correct key selection.
       **Area**                            Assigns the network to an OSPF area using an identifier like `0.0.0.0` (Backbone Area). The Backbone Area connects
                                           other areas, supporting inter-area communication, while additional areas (e.g., `0.0.0.1`, `0.0.0.255`) segment
                                           the network logically to limit routing updates.
       **Passive Interface**               (OSPFv3 only) Disables OSPF Hello packets on the interface, preventing neighbor relationships (used for security or optimization).
       **Cost**                            Sets the OSPF metric for path selection; lower costs are preferred paths within the area.
       **Cost (when demoted)**             Specifies metric cost when interface is in backup mode via CARP, deprioritizing paths dynamically.
       **Depend on (carp)**                Links the interface cost to a CARP VHID, adjusting costs based on primary or backup status.
       **Hello Interval**                  Sets frequency (in seconds) of Hello packets to maintain OSPF neighbor relationships.
       **Dead Interval**                   Defines the timeout period for OSPF neighbors; after this period, the neighbor is marked as down.
       **Retransmission Interval**         Time (seconds) to wait before resending Link-State Advertisements (LSAs) if acknowledgment is delayed.
       **Retransmission Delay**            Configures the hold time before LSAs are resent, accommodating slow or high-latency links.
       **Priority**                        Determines the likelihood of becoming a Designated Router; higher values increase priority.
       **BFD**                             Activates Bidirectional Forwarding Detection for rapid link failure detection; peer configuration required.
       **Network Type**                    Defines the OSPF network type, impacting adjacency and LSA flooding methods.

                                           - **Broadcast Multi-Access**: Assumes networks supporting multiple routers with broadcast capability (e.g., Ethernet).
                                           - **Non-Broadcast Multi-Access (NBMA)**: For networks without broadcast support (e.g., Frame Relay); requires manual neighbor setup.
                                           - **Point-to-Multipoint**: Connects multiple routers over a single interface, treating each as a point-to-point link.
                                           - **Point-to-Point**: Directly connects two routers, simplifying adjacency and LSA transmission.
       =================================== =======================================================================================================================

       .. Note::

          **Interfaces** in OSPF are for defining how each interface participates in OSPF routing. Key settings include **Area**, **Hello Interval** and **Dead Interval**
          for neighbor relationships and **Cost** for path preference. `Networks` and `Interfaces` cannot have the same `Area`,
          only one of them can be defined in the `Backbone Area`. For simpler networks, using `Interfaces` is recommended.

    .. tab:: Prefix Lists

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable / Disable
       **Name**                            The name of your Prefix-List. If there should be multiple entries for the same prefix list, give them all the same name.
       **Number**                          The ACL sequence number (10-99).
       **Action**                          Set permit for match or deny to negate the rule.
       **Network**                         The network pattern you want to match.
       =================================== =======================================================================================================================

       .. Note::

          **Prefix Lists** in OSPF serve as a filter to control the distribution of specific IP ranges within the network. Though not as common as in BGP,
          prefix filtering can prevent or allow propagation of defined network routes.

    .. tab:: Route Maps

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable / Disable
       **Name**                            Route-map name for matching and setting patterns, enabled via redistribution.
       **Action**                          Set permit for match or deny to negate the rule.
       **ID**                              Route-map ID between 10 and 99. Entries added in order of insertion.
       **Prefix List**                     Allows for matching based on prefix lists, multiple selections enabled.
       **Set**                             Free text for setting options, e.g., "local-preference 300" or "community 1:1".
       =================================== =======================================================================================================================

       .. Note::

          **Route Maps** act like conditional filters, allowing you to set and modify OSPF route attributes based on match criteria.
          They can combine prefix lists for detailed route manipulation.


Open Shortest Path First (OSPF) is a widely used link-state routing protocol designed for IP networks within a single autonomous system (AS).
Operating as an interior gateway protocol (IGP), OSPF builds a network topology map by gathering link-state information from routers,
allowing it to create an optimal routing table for IP packet delivery. OSPFv2 (RFC 2328) supports IPv4, while v3 (RFC 5340) extends support to IPv6.

.. toctree::
   :maxdepth: 2

   how-tos/dynamic_routing_ospf.rst


.. _bgp-section:

BGP (Border Gateway Protocol)
................................................

:menuselection:`Routing --> BGP`

.. tabs::

    .. tab:: General

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enable**                          This will activate the BGP service.
       **BGP AS Number**                   Your AS Number here.
       **BGP AD Distance**                 Adjust BGP administrative distance, typically set to 20. Useful if you want to prefer OSPF-learned routes.
       **Router ID**                       Optional fixed router ID for BGP.
       **Graceful Restart**                Enable BGP graceful restart as per RFC 4724, allowing packet forwarding during protocol restoration.
       **Network**                         Defines connected networks to be advertised over BGP. Disable Network Import-Check to announce all networks.
       **Network Import-Check**            By default, only networks present in the routing table are advertised. Disable to announce all configured networks.
       **Log Neighbor Changes**            Enable extended logging of BGP neighbor changes.
       **Route Redistribution**            Select other routing sources to redistribute to other nodes. Can be combined with a Route Map per redistribution.
       =================================== =======================================================================================================================

    .. tab:: Neighbors

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable/Disable
       **Description**                     Optional description for the neighbor.
       **Peer-IP**                         Specify the IP address of the BGP neighbor.
       **Remote AS mode**                  "Use Remote AS Number" will use the number specified in the "Remote AS" field, while "External" or "Internal" will
                                           ignore it in favor of the alternative "remote-as internal" and "remote-as external" settings.
       **Remote AS**                       AS (Autonomous System) number of the neighbor, required for establishing a BGP session.
       **BGP MD5 Password**                Password used for MD5 authentication of BGP connections to enhance security.
       **Weight**                          Default weight for routes from this neighbor; higher weight increases path preference within the same AS.
       **Local Initiater IP**              Specify the local IP address used to establish connections with the neighbor. Only relevant for MD5 authentication.
       **Update-Source Interface**         Interface where BGP sessions are sourced from, typically required when using loopback addresses.
       **IPv6 link-local interface**       Interface for IPv6 link-local neighbors, used primarily for link-local IPv6 addressing.
       **Next-Hop-Self**                   Sets the local router as the next hop for routes advertised to the neighbor, commonly used in Route Reflector setups.
       **Next-Hop-Self All**               Extends `Next-Hop-Self` by applying the setting to all addresses, including multiple address families.
       **Multi-Hop**                       Enables connections to eBGP neighbors across multiple hops; often required for peering over loopback addresses.
       **Multi-Protocol**                  Enables multiprotocol BGP for support of additional address families like IPv6.
       **Route Reflector Client**          Marks the neighbor as a client for a route reflector; used to reduce the number of full BGP mesh connections.
       **Soft reconfiguration inbound**    Allows policy changes without resetting the session by storing inbound updates.
       **BFD**                             Enable Bidirectional Forwarding Detection (BFD) for rapid link failure detection with the neighbor.
       **Keepalive**                       Sets the interval (default 60 seconds) between keepalive messages to check the neighbor's availability.
       **Hold Down Time**                  Time (default 180 seconds) before declaring a neighbor down if no keepalive messages are received.
       **Connect Timer**                   Interval to attempt reconnecting with a neighbor after a disconnect.
       **Send Defaultroute**               Sends a default route to the neighbor, useful in small AS environments where a full routing table is not necessary.
       **Enable AS-Override**              Allows replacement of the neighbor's AS with the local AS, common in BGP confederations.
       **Allow AS In**                     Accept incoming routes with AS path containing AS number with the same value as the current system AS.
       **Disable Connected Check**         Allows eBGP connections over loopback addresses by bypassing checks for direct connections.
       **Attribute Unchanged**             Keeps specified attributes (like `MED`, `AS-Path`, etc.) unchanged in updates to the neighbor.
       **Prefix-List In**                  Prefix list to filter inbound prefixes from this neighbor.
       **Prefix-List Out**                 Prefix list to filter outbound prefixes sent to this neighbor.
       **Route-Map In**                    Route-map to apply to routes received from this neighbor.
       **Route-Map Out**                   Route-map to apply to routes advertised to this neighbor.
       **Peer Group**                      Groups neighbors with similar configurations to simplify management.
       =================================== =======================================================================================================================

       .. Note::

          **Neighbors** in BGP are external or internal peers with whom the router establishes BGP sessions. Neighbors exchange route information,
          and each neighbor can be configured individually or as part of a Peer Group.

       .. Note::

          A **Route Reflector** (RR) minimizes the need for a full mesh of BGP connections in the same AS by reflecting routes from its clients to other clients.
          In typical iBGP setups, all routers must directly peer with each other to avoid routing loops, but route reflectors allow clients to peer only with the RR.
          Clusters of RRs and clients prevent loops, and redundancy can be achieved with multiple RRs.
          This setup is crucial for scalability in large networks. For a small network, do not enable any of the RR specific options.

    .. tab:: AS-Path Lists

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable/Disable
       **Description**                     Optional description for the AS-Path list.
       **Number**                          ACL rule number (0-4294967294). No sequence numbers; removing the ACL is required to insert between entries.
       **Action**                          Set permit to match or deny to negate the rule.
       **AS**                              AS pattern to match, with regex allowed (e.g., ".$" or "_1$").
       =================================== =======================================================================================================================

       .. Note::

          An **AS-Path List** is used to filter routes based on their AS-Path attributes. By matching specific AS paths, you can control the acceptance or rejection
          of routes from particular AS sequences. This is useful for policy enforcement in multi-AS environments but not needed for small networks.

    .. tab:: Prefix Lists

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable/Disable
       **Description**                     Optional description for the Prefix-List.
       **Name**                            Name of the Prefix-List, descriptive of its purpose. If there should be multiple entries for the same prefix list,
                                           give them all the same name.
       **IP Version**                      IP version to use.
       **Number**                          ACL sequence number (1-4294967294).
       **Action**                          Set permit to match or deny to negate the rule.
       **Network**                         Specifies a network pattern to match, with optional `ge` (greater than or equal) and `le` (less than or equal)
                                           attributes to control the prefix length range. For example, a pattern like `192.168.0.0/16 ge 24 le 28` matches any
                                           route within the `192.168.0.0/16` block with prefix lengths from `/24` to `/28`.
       =================================== =======================================================================================================================

       .. Note::

          **Prefix Lists** are used to filter prefixes in BGP. They match prefixes and control the import/export of specific IP ranges, allowing for
          fine-grained network control. It is very important to filter routes, especially when peering between eBGP and iBGP. Leaking routes of RFC1918 addresses
          to eBGP peers or announcing wrong prefixes is bad practice and could result in peering bans from external providers.

    .. tab:: Community Lists

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable/Disable
       **Description**                     Optional description for the Community-List.
       **Number**                          Community-List number (1-99 for standard, 100-500 for expanded).
       **Sequence Number**                 ACL sequence number (10-99).
       **Action**                          Set permit to match or deny to negate the rule.
       **Community**                       Community pattern to match, with optional regex.
       =================================== =======================================================================================================================

       .. Note::

          **Community Lists** allow tagging and filtering routes based on community attributes. By assigning community tags, you can apply policies that
          influence route preference. Useful for large networks; not so much in small networks.

    .. tab:: Route Maps

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable/Disable
       **Description**                     Optional description for the route-map.
       **Name**                            Name of the route-map, used in neighbor configuration.
       **Action**                          Set permit to match or deny to negate the rule.
       **ID**                              Route-map ID (1-65535). Sorting is managed automatically.
       **AS-Path List**                    Select the AS-Path List. If multiples with the same name exist, selecting one is enough.
       **Prefix List**                     Select the Prefix List. If multiples with the same name exist, selecting one is enough.
       **Community List**                  Select the Community List. If multiples with the same name exist, selecting one is enough.
       **Set**                             Free text field for setting attributes, e.g., "local-preference 300" or "community 1:1".
       =================================== =======================================================================================================================

       .. Note::

          **Route Maps** act like conditional filters, allowing you to set and modify BGP route attributes based on match criteria.
          They can combine prefix lists, community lists, and AS-paths for detailed route manipulation.

    .. tab:: Peer Groups

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable/Disable
       **Name**                            Name of the peer group.
       **Remote AS mode**                  "Use Remote AS Number" will use the number specified in the "Remote AS" field, while "External" or "Internal" will
                                           ignore it in favor of the alternative "remote-as internal" and "remote-as external" settings.
       **Remote AS**                       Remote AS for the peer group.
       **Listen Ranges**                   Enter one or multiple IP networks in CIDR notation. Accept connections from any peers in the specified prefix.
       **Update-Source Interface**         Physical IPv4 interface facing the peer.
       **Next-Hop-Self**                   Sets the local router as the next hop for routes advertised to the peer group, commonly used in Route Reflector setups.
       **Send Defaultroute**               Enable sending of default routes to the peer group.
       **Prefix-List In**                  Prefix list to filter inbound prefixes from this peer group.
       **Prefix-List Out**                 Prefix list to filter outbound prefixes sent to this peer group.
       **Route-Map In**                    Route-map to apply to routes received from this peer group.
       **Route-Map Out**                   Route-map to apply to routes advertised to this peer group.
       =================================== =======================================================================================================================

       .. Note::

          A **Peer Group** in BGP simplifies configurations by grouping neighbors with similar settings. Another possibility is defining **Listen Ranges** to accept connections
          from multiple peers without configuring each of them as neighbor individually. This approach reduces management complexity and ensures uniform settings across peers.
          Peer Groups are especially useful in larger networks where multiple BGP peers require identical policy; not so much in small networks.

Border Gateway Protocol (BGP) is an exterior gateway protocol used to exchange routing information between autonomous systems (AS) on the Internet.
As a path-vector protocol, BGP makes routing decisions based on defined paths, network policies, or administrator-configured rules.
BGP has two main types: iBGP, used for routing within a single AS (using private AS numbers from 64512 to 65534), and eBGP, which operates between
different AS across the Internet (using public AS numbers 1 to 64511). BGP’s flexibility and scalability make it essential
for global Internet routing and large network infrastructures.

.. toctree::
   :maxdepth: 2

   how-tos/dynamic_routing_bgp.rst


------------------------------------------------
Supplemental Protocols
------------------------------------------------


.. _bfd-section:

BFD (Bidirectional Forward Detection)
................................................

:menuselection:`Routing --> BFD`

.. tabs::

    .. tab:: General

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enable**                          This will activate the BFD service.
       =================================== =======================================================================================================================

    .. tab:: BFD Neighbor

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable/Disable
       **Description**                     Set an optional description for this neighbor.
       **Peer-IP**                         Specify the IP of your neighbor.
       **Multihop**                        Enables multi-hop mode, allowing BFD to expect packets with TTL less than 254 and listen on the multihop port (4784).
                                           Note: Echo mode is not supported in multi-hop (see RFC 5883, section 3).
       =================================== =======================================================================================================================

       .. Note::

          A **BFD Neighbor** refers to a neighboring device configured to use BFD with BGP, OSPF or other protocols.
          BFD neighbors exchange small, frequent packets to rapidly detect link failures, reducing convergence time in routing;
          usually a whole lot faster than typical keepalive or hello mechanisms.


Bidirectional Forwarding Detection (BFD) is a lightweight protocol used to detect faults between routers or switches by sending periodic
Hello packets (asynchronous mode). BFD quickly identifies failing links, making it a useful companion to routing protocols like OSPF and BGP for faster convergence.

.. toctree::
   :maxdepth: 2

   how-tos/dynamic_routing_bfd.rst


.. _static-section:

STATIC (Static Routes Daemon)
................................................

:menuselection:`Routing --> STATIC`

.. tabs::

    .. tab:: Static General

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enable**                          This will activate the staticd service
       =================================== =======================================================================================================================

    .. tab:: Static Routes

       =================================== =======================================================================================================================
       Options                             Description
       =================================== =======================================================================================================================
       **Enabled**                         Enable/Disable
       **Network**                         Defines the target for the static route, in CIDR notation.
       **Gateway (optional)**              Optional gateway IP address for this route.
       **Interface**                       Select the interface where this setting applies.
       =================================== =======================================================================================================================


STATIC is a daemon that handles the installation and deletion of static routes. These routes can be used supplemental to dynamic routes. It is beneficial for
fine grained control over routes in more complex network environments, if redistributing directly attached routes is not an option.
