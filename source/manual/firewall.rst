===========================
Rules
===========================

OPNsense contains a stateful packet filter, which can be used to restrict or allow traffic from and/or to specific networks
as well as influence how traffic should be forwarded (see also policy based routing in ":doc:`/manual/how-tos/multiwan`").

The rules section shows all policies that apply on your network, grouped by interface.


--------------------
Overview
--------------------

Our overview shows all the rules that apply to the selected interface (group) or floating section.
For every rule some details are provided and when applicable you can perform actions, such as move, edit, copy, delete.


.. image:: images/Firewall_overview.png
    :width: 600px
    :align: center

Below you will find some highlights about this screen.

1.  Interface name
      The name of the interface is part of the normal menu breadcrumb
2.  Category
      If categories are used in the rules, you can select which one you will show here.
3.  Toggle inspection
      You can toggle between inspection and rule view here, when in inspection mode, statistics of the rule are shown.
      (such as packet counters, number of active states, ...)
4.  Show / hide automatic rules
      Some rules are automatically generated, you can toggle here to show the details. If a magnifying glass
      is shown you can also browse to its origin (The setting controlling this rule).
5.  Automatic rules
      The contents of the automatic rules
6.  User rules
      All user defined rules



--------------------
The basics
--------------------

Before creating rules, it's good to know about some basics which apply to all rules.

....................
States
....................

By default rules are set to stateful (you can change this, but it has consequences), which means that the state of
a connection is saved into a local dictionary which will be resolved when the next packet comes in.
The consequence of this is that when a state exists, the firewall doesn't need to process all its rules again to determine
the action to apply, which has huge performance advantages.

Another advantage of stateful packet filtering is that you only need to allow traffic in one direction to automatically
allow related packets for the same flow back in. Below diagram shows a tcp connection from a client to a server for https
traffic, when not using stateful rules, both the client should be permitted to send traffic to the server at port 443
as the server back to the client (usually a port >=1024).

.. _Firewall_States:

.. blockdiag::
   :desctable:

   blockdiag {
        group {
            color = "#eee";
            label = "Client [tcp:1024]";
            client_req [label="request"];
            client_res [label=""];
        }

        group {
            color = "#eee";
            label = "Firewall";
            firewall_req [label=""];
            firewall_res [label=""];
        }

        group {
            color = "#eee";
            label = "Server [tcp:443]";
            server_req [label=""];
            server_res [label="reply"];
        }
        client_req -> firewall_req -> server_req [color=green];
        client_res <- firewall_res <- server_res [color=red];
    }


The use of states can also improve security particularly in case of tcp type traffic, since packet sequence numbers and timestamps are also checked in order
to pass traffic, it's much harder to spoof traffic.

.. Note::
    When changing rules, sometimes its necessary to reset states to assure the new policies are used for existing traffic.
    You can do this in :menuselection:`Firewall --> Diagnostics --> States`.


.. Note::
    In order to keep states, the system need to reserve memory. By default 10% of the system memory is reserved for states,
    this can be configured in :menuselection:`Firewall --> Settings --> Firewall Maximum States`.
    (The help text shows the default number of states on your platform)

States can also be quite convenient to find the active top users on your firewall at any time, we added
an easy to use "session" browser for this purpose. You can find it under :menuselection:`Firewall --> Diagnostics --> Sessions`.

.. Tip::

    States also play an important rule into protecting services against (distributed) denial of service attacks (DDOS).
    Relevant topics available in our documentation are "synproxy" states, connection limits and `syncookies <firewall_settings.html#enable-syncookies>`__


....................
Action
....................

.. _Firewall_Rule_Action:

Rules can be set to three different action types:

* Pass --> allow traffic
* Block --> deny traffic and don't let the client know it has been dropped (which is usually advisable for untrusted networks)
* Reject --> deny traffic and let the client know about it. (only tcp and udp support rejecting packets, which in case of TCP means a :code:`RST` is returned, for UDP :code:`ICMP UNREACHABLE` is returned).

For internal networks it can be practical to use reject, so the client does not have to wait for a time-out when access is not allowed.
When receiving packets from untrusted networks, you usually don't want to communicate back if traffic is not allowed.

....................
Processing order
....................

.. _Firewall_Rule_Processing_Order:

Firewall rules are processed in sequence per section, first evaluating the **Floating** rules section followed by all rules which
belong to **interface groups** and finally all **interface** rules.

Internal (automatic) rules are usually registered first.

.. blockdiag::
   :desctable:

   blockdiag {
      System [label="System defined", style = dotted];
      Floating [label="Floating rules"];
      Groups [label="Interface groups"];
      Interfaces [label="Interfaces"];
      System -> Floating -> Groups -> Interfaces;
   }


Rules can either be set to :code:`quick` or not set to quick, the default is to use quick. When set to quick, the rule is
handled on "first match" basis, which means that the first rule matching the packet will take precedence over rules following in sequence.

When :code:`quick` is not set, last match wins. This can be useful for rules which define standard behaviour.
Our default deny rule uses this property for example (if no rule applies, drop traffic).


.. Note::
    Internally rules are registered using a priority, floating uses :code:`200000`,
    groups use :code:`300000` and interface rules land on :code:`400000` combined with the order in which they appear.
    Automatic rules are usually registered at a higher priority (lower number).

.. Warning::

    **NAT rules are always processed before filter rules!**
    So for example, if you define a `NAT : port forwarding rules <nat.html#port-forwarding>`__  *without a associated rule*, i.e. **Filter rule association** set to **Pass**, this has the consequence, that no other rules will apply!

.. Tip::

    The interface should show all rules that are used, when in doubt, you can always inspect the raw output of the ruleset in :code:`/tmp/rules.debug`

....................
Rule sequence
....................

.. _Firewall_Rule_Sequence:

The sequence in which the rules are displayed and processed can be customized per section:

* Select one or more rules using the checkbox on the left side of the rule.
* Use the arrow button in the action menu on the right side of a rule in order to move selected rules before the rule where the action button is pressed.
* Or you can use the arrow button on the top in the heading row to move the selected rules to the end.

......................
Direction
......................

.. _Firewall_Rule_Direction:

.. blockdiag::
   :desctable:

   blockdiag {
      source [label="Source"];
      firewall [label="Firewall"];
      destination [label="Destination"];
      source -> firewall [label="in"]
      firewall -> destination [label="out"];
   }


Traffic can be matched on :code:`in[coming]` or :code:`out[going]`  direction, our default is to filter on incoming direction.
In which case you would set the policy on the interface where the traffic originates from.

For example, if you want to allow :code:`https` traffic coming from any host on the internet,
you would usually set a policy on the WAN interface allowing port :code:`443` to the host in question.


.. Note::
    Traffic leaving the firewall is accepted by default (using a non-quick rule), when **Disable force gateway** in
    :menuselection:`Firewall --> Settings --> Advanced` is not checked, the connected gateway would be enforced as well.


--------------------
Settings
--------------------

Traffic that is flowing through your firewall can be allowed or denied using rules, which define policies.
This section of the documentation describe the different settings, grouped by usage.

.......................
Descriptive settings
.......................

Some settings help to identify rules, without influencing traffic flow.

=====================================================================================================================

====================================  ===============================================================================
Category                              The category this rule belongs to, can be used as a filter in the overview
Description                           Descriptive text
====================================  ===============================================================================


.................
Basic settings
.................

Below are the settings most commonly used:

=====================================================================================================================

====================================  ===============================================================================
Action                                The :ref:`action <Firewall_Rule_Action>` to perform.
Disabled                              Disable a rule without removing it, can be practical for testing purposes and
                                      to support easy enablement of less frequently used policies.
Interface                             Interface[s] this rule applies on. You can easily copy rules between interfaces
                                      and change this field to the new target interface.
                                      (remember to check the order before applying)
TCP/IP Version                        Does this rule apply on IPv4, IPv6 or both.
Protocol                              Protocol to use, most common are TCP and UDP
Source                                Source network or address, when combining IPv4 and IPv6 in one rule, you can use
                                      aliases which contain both address families.
                                      You can select multiple sources per rule.
Source / Invert                       Invert source selection (for example not 192.168.0.0/24)
                                      You can only invert single sources.
Destination                           Destination network or address, like source you can use aliases here as well.
                                      You can select multiple destinations per rule.
Destination / Invert                  When the filter should be inverted, you can mark this checkbox.
                                      You can only invert single destinations.
Destination port range                For TCP and/or UDP you can select a service by name (http, https)
                                      or number (range), you can also use aliases here to simplify management.
Log                                   Create a log entry when this rule applies, you can use
                                      :menuselection:`Firewall --> Log Files --> Live View` to monitor if your rule
                                      applies.
====================================  ===============================================================================


.. Tip::

    The use of descriptive names help identify traffic in the live log view easily.

.. Tip::

  .. raw:: html

      <i class="fa fa-eye"></i>
    With the use of the eye button in the right top corner of the screen you can find statistics about the rule in
    question (number of evaluations, number of active states and traffic counters).

.. Tip::

    You can select multiple sources or destinations per rule, yet keep in mind that a nested alias might be the better choice.
    This feature is most useful if you plan to create `security zones </manual/how-tos/security-zones.html>`_.

..........................
Traffic shaping (QoS)
..........................

When a firewall rule needs to be constrained in terms of the number of packets it may process over time,
it's possible to combine the rule with the traffic shaper.

The process of shaping is explained in the :doc:`/manual/shaping` section of our documentation. Below you will find the
relevant properties for the firewall rule.


=====================================================================================================================

====================================  ===============================================================================
Traffic shaping/rule direction        Force packets being matched by this rule into the configured queue or pipe
Traffic shaping/reverse direction     Force packets being matched in the opposite direction
                                      into the configured queue or pipe
====================================  ===============================================================================


.. Tip::

    Filter rules are more flexible than the ones specified in the shaper section itself as these can be combined with
    aliases as well. Although this feature is quite new, it's certainly worth looking at when in need of a traffic shaper.



.....................
Less commonly used
.....................

Some settings are usually best left default, but can also be set in the normal rule configuration.

=====================================================================================================================

====================================  ===============================================================================
Source port range                     In case of TCP and/or UDP, you can also filter on the source port (range) that is
                                      used by the client. Since in most cases you can't influence the source port,
                                      this setting is usually kept default (:code:`any`).
Quick                                 If a packet matches a rule specifying quick, the first matching rule wins.
                                      When not set to quick the last matching rule wins. When not sure, best use
                                      quick rules and interpret the ruleset from top to bottom.
Direction                             Direction of the traffic,
                                      see also :ref:`Direction <Firewall_Rule_Direction>`.
====================================  ===============================================================================

...................
High Availability
...................

The following options are specifically used for HA setups.

=====================================================================================================================

====================================  ===============================================================================
No XMLRPC Sync                        Disable configuration sync for this rule, when **Firewall Rules** sync is
                                      enabled in :menuselection:`System --> High Availability --> Settings`
State Type / NO pfsync                Prevent states created by this rule to be synced to the other node
====================================  ===============================================================================



....................
Schedule
....................

Rules can also be scheduled to be active at specific days or time ranges, you can create schedules in
:menuselection:`Firewall --> Advanced --> Schedules` and select one in the rule.


......................
Policy based routing
......................

This feature can be used to forward traffic to another gateway based on more fine grained filters than static routes
could (`OSI layer 4 verses OSI layer 3 <https://en.wikipedia.org/wiki/OSI_model>`__) and can be used to build multi-wan scenario's using gateway groups.

More information about Multi-Wan can be found in the ":doc:`/manual/how-tos/multiwan`" chapter.

=====================================================================================================================

====================================  ===============================================================================
Gateway                               When a gateway is specified, packets will use policy based routing using
                                      the specified gateway or gateway group. Usually this option is set on the
                                      receiving interface (LAN for example), which then chooses the gateway
                                      specified here. (This ignores default routing rules). Only packets flowing in
                                      the same direction of the rule are affected by this parameter, the opposite
                                      direction (replies) are not affected by this option.
reply-to                              By default traffic is always send to the connected gateway on the interface.
                                      If for some reason you don't want to force traffic to that gateway, you
                                      can disable this behaviour or enforce an alternative target here.
====================================  ===============================================================================


.. Note::

      When using policy based routing, don't forget to exclude local traffic which shouldn't be forwarded.
      You can do so by creating a rule with a higher priority, using a :code:`default` gateway.


.. Tip::

    In our experience the packet capture function (:menuselection:`Interfaces --> Diagnostics --> Packet capture`) can
    be a valuable tool to inspect if traffic is really heading the direction you would expect it to go, just
    choose a host to monitor and try to exchange some packets. When selecting all interfaces, it's easy to see
    where traffic headed.

....................
Connection limits
....................


The advanced options contains some settings to limit the use of a rule or specify specific timeouts for
the it. Most generic (default) settings for these options can be found under :menuselection:`Firewall --> Settings --> Advanced`

=====================================================================================================================

====================================  ===============================================================================
Max states                            Limits the number of concurrent states the rule may create.
                                      When this limit is reached, further packets that would create state will
                                      not match this rule until existing states time out.
Max source nodes                      Limits the maximum number of source addresses which can simultaneously
                                      have state table entries.
Max established                       Limits the maximum number of simultaneous TCP connections which have
                                      completed the 3-way handshake that a single host can make.
Max source states                     Limits the maximum number of simultaneous state entries that
                                      a single source address can create with this rule.
Max new connections                   Limit the rate of new connections over a time interval.  The
                                      connection rate is an approximation calculated as a moving average.
                                      (number of connections / seconds) Only applies on TCP connections
State timeout                         State Timeout in seconds (applies to TCP only)
====================================  ===============================================================================


....................
Advanced
....................

Some less common used options are defined below.

=====================================================================================================================

====================================  ===============================================================================
Source OS                             Operating systems can be fingerprinted based on some tcp fields from
                                      the originating connection. These fingerprints can be used as well
                                      to match traffic on. (more detailed information can be found in the
                                      `pf.os <https://www.freebsd.org/cgi/man.cgi?query=pf.os>`__ man page)
allow options                         By default the firewall blocks IPv4 packets with IP options or IPv6
                                      packets with routing extension headers set.
                                      If you have an application that requires such packets
                                      (such as multicast or IGMP)
                                      you can enable this option.
TCP flags                             If specific TCP flags need to be set or unset, you can specify those here.
Set priority                          Packets matching this rule will be assigned a specific queueing priority.
                                      If the packet is transmitted on a VLAN interface, the queueing priority
                                      will be written as the priority code point in the 802.1Q VLAN
                                      header.  If two priorities are given, packets which have a TOS of
                                      lowdelay and TCP ACKs with no data payload will be assigned to the second one.
Match priority                        Only match packets which have the given queueing priority assigned.
Set local tag                         Packets matching this rule will be tagged with the specified string.
                                      The tag acts as an internal marker that can be used to identify these
                                      packets later on. This can be used, for example, to provide trust between
                                      interfaces and to determine if packets have been processed by translation rules.
                                      Tags are “sticky”, meaning that the packet will be tagged even
                                      if the rule is not the last matching rule.
                                      Further matching rules can replace the tag with a new one but will not
                                      remove a previously applied tag. A packet is only ever assigned
                                      one tag at a time.
Match local tag                       Match packets that are tagged earlier (using set local tag)
State Type                            Influence the state tracking mechanism used, the following options are available.
                                      When in doubt, it's usually best to preserve the default :code:`keep state`

                                      * Keep state :menuselection:`-->` is used for stateful connection tracking.
                                      * Sloppy state :menuselection:`-->` works like keep state,
                                        but it does not check sequence numbers.
                                        Use it when the firewall does not see all packets.
                                      * Synproxy state :menuselection:`-->` proxies incoming TCP connections to help
                                        protect servers from spoofed TCP SYN floods.
                                        This option includes the functionality of keep state
                                        and modulate state combined.
                                      * None :menuselection:`-->` Do not use state mechanisms to keep track.
====================================  ===============================================================================

--------------------
Troubleshooting
--------------------

While building your ruleset things can go wrong, it's always good to know where to look for signs of an issue.
One of the most common mistakes is traffic doesn't match the rule and/or the order of the rule doesn't make sense
for whatever reason.

With the use of the "inspect" button, one can easily see if a rule is being evaluated and traffic did pass using
this rule. It's also possible to jump directly into the attached states to see if your host is in the list
as expected.

Another valuable tool is the live log viewer, in order to use it, make sure to provide your rule with an easy to
read description and enable the "log" option.

If your using source routing (policy based routing), debugging can sometimes get a bit more complicated. Since the normal
system routing table may not apply, it helps to know which flow the traffic actually followed. The packet capture is a useful
tool in that case.

Common issues in this area include return traffic using a different interface than the one it came into, since traffic
follows the normal routing table on it's way out (reply-to issue), or traffic leaving the wrong interface due to overselection
(matching internal traffic and forcing a gateway).

Inspecting used netmasks is also a good idea, intending to match a host but providing a subnet is a mistake easily made
(e.g. :code:`192.168.1.1/32` vs :code:`192.168.1.1/24` is in reality all of :code:`192.168.1.x`).

Last but not least, remember rules are matched in order and the default (inbound) policy is :code:`block` if nothing else
is specified, since we match traffic on :code:`inbound`, make sure to add rules where traffic originates from
(e.g. :code:`lan` for traffic leaving your network, the return should normally be allowed by state).

--------------------
API access
--------------------


Partial API access is described in more detail in the :doc:`firewall <../development/api/core/firewall>` api reference manual.
