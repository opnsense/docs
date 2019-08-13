===========================
Rules
===========================

OPNsense contains a stateful packet filter, which can be used to restrict or allow traffic from and/or to specific networks
as well as influence how traffic should be forwarded (see also policy based routing in ":doc:`/manual/how-tos/multiwan`").

The rules section shows all policies that apply on your network, grouped by interface.


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

The use of states can also improve security particularly in case of tcp type traffic, since packet sequence numbers and timestamps are also checked in order
to pass traffic, it's much harder to spoof traffic.

.. Note::
    When changing rules, sometimes its necessary to reset states to assure the new policies are used for existing traffic.
    You can do this in :menuselection:`Firewall --> Diagnostics --> States Reset` or :menuselection:`Firewall --> Diagnostics --> States Dump`
    to reset specific states.


.. Note::
    In order to keep states, the system need to reserve memory. By default 10% of the system memory is reserved for states,
    this can be configured in :menuselection:`Firewall --> Settings --> Firewall Maximum States`.
    (The help text shows the default number of states on your platform)


....................
Action
....................

Rules can be set to three different action types:

* Pass --> allow traffic
* Block --> deny traffic and don't let the client know it has been dropped (which is usually advisable for untrusted networks)
* Reject --> deny traffic and let the client know about it. (only tcp and udp support rejecting packets, which in case of TCP means a :code:`RST` is returned, for UDP :code:`ICMP UNREACHABLE` is returned).

For internal networks it can be practical to use reject, so the client does not have to wait for a time-out when access is not allowed.
When receiving packets from untrusted networks, you usually don't want to communicate back if traffic is not allowed.

....................
Processing order
....................

Firewall rules are processed in sequence, first evaluating the **Floating** rules section followed by all rules which
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

.. Tip::

    The interface should show all rules that are used, when in doubt, you can always inspect the raw output of the ruleset in :code:`/tmp/rules.debug`


......................
Direction
......................

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
