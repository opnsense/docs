===========================
(Advanced) Settings
===========================

In some circumstances people might want to change how our system handles traffic by default, in which case
the advanced settings section is a good place to look.



IPv6 Options
------------------------------------

Allow IPv6
.....................................

By default selected, when deselected a firewall rule will be generated blocking all IPv6 traffic on this machine.
The floating firewall section will display this rule when "Automatically generated rules" is expanded.


Network Address Translation
------------------------------------

.. Warning::

    Although the options below might look interesting to ease setup, we do not advise to use them. Since automatic rules
    always contain assumptions about the situation they try to solve, it's not guaranteed they will fit your use-case at all
    times. They merely exist for historical reasons, if possible better add manual rules nat rules to make sure the intend is
    very explicit when one inspects your setup.

Reflection for port forwards
.....................................

Disabled by default, when enabled the system will generate rules to reflect port forwards on non external interfaces
automatically (interfaces without a gateway set).
If for example you create a portforward on your :code:`wan` interface to a webserver which is hosted internally, a similar
rule will be generated on the :code:`lan` interface.

.. Note::

    This marker only adds a redirect for the same target the source address is not influenced. (:code:`rdr`)


Reflection for 1:1
.....................................

Disabled by default, when enabled the system will generate redirect (:code:`rdr`) rules for 1to1 nat rules similar to
the portforward option.


Automatic outbound NAT for Reflection
......................................

Since both reflection rules only redirect traffic on other nets, quite often they are used in conjunction with this option.
When enabled, source addresses are translated so returning traffic is always pushed through the firewall for these automatic rules.

.. Note::

    The disadvantage of reflecting traffic back in using one of the firewalls internal addresses is that the receiving side
    looses visibility of the actual client.


Bogon Networks
------------------------------------

Update Frequency
.....................................

Configure the frequency of updating the lists of IP addresses that are reserved (but not RFC 1918) or not yet assigned by IANA.



Gateway Monitoring
------------------------------------

Skip rules
.....................................

By default, when a rule has a specific gateway set, and this gateway is down,
rule is created and traffic is sent to default gateway.
This option overrides that behavior and the rule is not created when gateway is down


Multi-WAN
------------------------------------

Sticky connections
.....................................

When using a gateway group the firewall will use the same gateway for the same source address, by default as long as there's a state
active, optionally this can be configured with a different timeout.

Shared forwarding
.....................................

Using policy routing in the packet filter rules causes packets to skip processing for the traffic shaper and captive portal tasks.
Using this option enables the sharing of such forwarding decisions between all components to accomodate complex setups.


Disable force gateway
.....................................

By default OPNsense enforces a gateway on "Wan" type interfaces (those with a gateway attached to it), although the default usually
is the desired behaviour, it does influence the routing decisions made by the system (local traffic bound to an address will use the associated gateway).

.. Note::

    This rule is responsible for the :code:`let out anything from firewall host itself (force gw)` rule visible in the floating section,
    it forces a route to (:code:`route-to`) on all non local traffic for the "Wan" type interface.


Schedules
------------------------------------

Schedule States
.....................................

By default schedules clear the states of existing connections when the expiration time has come. This option overrides that behavior by not clearing states for existing connections.


Miscellaneous
------------------------------------

Firewall Optimization
.....................................

Firewall state table optimization to use, influences the number of active states in the system, only to be changed in specfic implementation scenarios.

* [normal] (default)As the name says, it is the normal optimization algorithm
* [high-latency] Used for high latency links, such as satellite links. Expires idle connections later than default
* [aggressive] Expires idle connections quicker. More efficient use of CPU and memory but can drop legitimate idle connections
* [conservative] Tries to avoid dropping any legitimate idle connections at the expense of increased memory usage and CPU utilization.

Bind states to interface
.....................................

Set behaviour for keeping states, by default states are floating, but when this option is set they should match the interface.
The default option (unchecked) matches states regardless of the interface, which is in most setups the best choice.


Disable Firewall
.....................................

Disable all firewall (including NAT) features of this machine.


Firewall Adaptive Timeouts
.....................................

Timeouts for states can be scaled adaptively as the number of state table entries grows.

* [start] When the number of state entries exceeds this value, adaptive scaling begins. All timeout values are scaled linearly with factor (adaptive.end - number of states) / (adaptive.end - adaptive.start).
* [end] When reaching this number of state entries, all timeout values become zero, effectively purging all state entries immediately. This value is used to define the scale factor, it should not actually be reached (set a lower state limit, see below).

Firewall Maximum States
.....................................

Maximum number of connections to hold in the firewall state table, usually the default is fine,
when serving a lot of connections you may consider increasing the default size which is mentioned in the help text.


Firewall Maximum Fragments
.....................................

Sets the maximum number of entries in the memory pool used for fragment reassembly.

Firewall Maximum Table Entries
.....................................
Maximum number of table entries for systems such as aliases, sshlockout, bogons, etc, combined.
When using a lot of large aliases, you may consider increasing the default. The configured default is mentioned in the help text.


Static route filtering
.....................................

This option only applies if you have defined one or more static routes.
If it is enabled, traffic that enters and leaves through the same interface will not be checked by the firewall.
This may be desirable in some situations where multiple subnets are connected to the same interface.

.. Note::

    Although these rules will be visible in the "automatic" rule section of each interface, we generally advice to add the rules actually
    recquired on a per net basis manually.


Disable reply-to
.....................................

With Multi-WAN you generally want to ensure traffic leaves the same interface it arrives on, hence :code:`reply-to` is added automatically by default.
When using bridging, you must disable this behavior if the WAN gateway IP is different from the gateway IP of the hosts behind the bridged interface.

.. Warning::

    Although our default is to enable this rule for historic reasons, there are side-affects when adding :code:`reply-to`
    to every "wan" type rule. When allowing traffic originating from the same network as the interface is attached to, it will
    still reply the packet to the configured gateway.

    To prevent this behvior, you can either disable :code:`reply-to` here and configure the desired behaviour on a per-rule basis or
    add a rule for local traffic above the one for outbound traffic disabling :code:`reply-to` (in rule advanced).

Disable anti-lockout
.....................................

When this is unchecked, access to the web GUI or SSH on the LAN interface is always permitted, regardless of the user-defined firewall rule set.
Check this box to disable the automatically added rule, so access is controlled only by the user-defined firewall rules. Ensure you have a firewall rule in place that allows you in, or you will lock yourself out.

Aliases Resolve Interval
.....................................

Interval, in seconds, that will be used to resolve hostnames configured on aliases.


Check certificate of aliases URLs
.....................................

Make sure the certificate is valid for all HTTPS addresses on aliases. If it's not valid or is revoked, do not download it.


Anti DDOS
------------------------------------

Enable syncookies
.....................................


This option is quite similar to the `syncookies <https://www.freebsd.org/cgi/man.cgi?syncookies>`__ kernel setting,
preventing memory allocation for local services before a proper handshake is made.

In this case pf will be protected agains state table exhaustion.

The following modes are available:

* never (default)
* always
* adaptive - in which case a lower and upper percentage should be specified referring to the usage of the state table.
