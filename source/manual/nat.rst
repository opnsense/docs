===========================
Network Address Translation
===========================

Network Address Translation (abbreviated to NAT) is a way to separate external and internal networks (WANs and LANs),
and to share an external IP between clients on the internal network. NAT can be used on IPv4 and IPv6. For IPv6,
:doc:`Network Prefix Translation <nptv6>` is also available.

Most of the options below use three different addresses: the source, destination and redirect address. These
addresses are used for the following:

============= ===========================================================================================================
 Source        Where the traffic comes from. This can often be left on “any”.
 Destination   Where the traffic is headed. For incoming traffic from outside, this is usually your external IP address.
 Redirect      Where the traffic should be redirected.
============= ===========================================================================================================

.. warning::

    - Network Address Translation should not be relied upon as a security measure.
    - Disabling pf will also disable NAT.

--------------------
Some terms explained
--------------------

**BINAT**: NAT generally works in one direction. However, if you have networks of equal size, you can also use BINAT, which is
bidirectional. This can simplify your set-up. If you don't have networks of equal size, you can only use regular NAT.

**NAT reflection**: When a client on the internal network tries to access another client, but using the *external* IP
instead of the internal one (which would the most logical), NAT reflection can rewrite this request so that it uses
the internal IP, in order to avoid taking a detour and applying rules meant for actual outside traffic.

.. Tip::
   There is a how-to section explaining :doc:`NAT Reflection <how-tos/nat_reflection>` in detail.

.. Note::
    The NAT rules generated with enabling **NAT reflection** only include networks directly connected to your
    Firewall. This means if you have a private network separated from your LAN you need to add this with a
    manual outbound NAT rule.

**Pool options**: When there are multiple IPs to choose from, this option will allow regulating which IP gets used.
The default, Round Robin, will simply distribute packets to one server after the other. If you only have one external
IP, this option has no effect.

---------------
Port forwarding
---------------

When multiple clients share an external IP address, any connection not initiated by one of the clients will not
succeed since the firewall will not know where to send the traffic. This can be addressed by creating port
forwarding rules. For example, for a web server behind the firewall to be accessible, ports 80 and 443 need to
be redirected to it.

Port forwarding is also referred to as “Destination NAT” or “DNAT”.

In OPNsense, port forwarding can be set up by navigating to :menuselection:`Firewall --> NAT --> Port Forward`. Here, you will see
an overview of port forwarding rules. New rules can be added by clicking **Add** in the upper right corner.

When adding a rule, the following fields are available:

========================= =========================================================================================================
Disabled                  Disable this rule without removing it.
No RDR (NOT)              Do not create a redirect rule. Leave this disabled unless you know what you are doing.
Interface                 Which interface this rule should apply to. Most of the time, this will be WAN.
TCP/IP version            IPv4, IPv6 or both.
Protocol                  In typical scenarios, this will be TCP.
Source                    Where the traffic comes from. Click “Advanced” to see the other source settings.
Source / Invert           Invert match in “Source” field.
Source port range         When applicable, the source port we should match on.
                          This is usually random and almost never equal to the destination port range (and should usually be 'any').
Destination / Invert      Invert match in “Destination” field.
Destination               Where the traffic is headed.
Destination port range    Service port(s) the traffic is using
Redirect target IP        Where to redirect the traffic to.
Redirect target port      Which port to use (when using tcp and/or udp)
Pool Options              See “Some terms explained”. The default is to use Round robin.
Description               A description to easily find the rule in the overview.
Set local tag             Set a tag that other NAT rules and filters can check for.
Match local tag           Check for a tag set by another rule.
No XMLRPC sync            Prevent this rule from being synced to a backup host. (Checking this on the backup host has no effect.)
NAT reflection            See “Some terms explained”. Leave this on the default unless you have a good reason not to.
Filter rule association   Associate this with a regular firewall rule.
========================= =========================================================================================================

.. Note:

   In OPNsense, this feature is also used to implement transparent proxies. A connection needs to be forwarded to a
   daemon (listening on localhost), which then tries to get the original destination IP from the `/dev/pf` device.

   For example, a transparent proxy that handles HTTP traffic needs a rule that forwards traffic from TCP port 80,
   IPv4 to 127.0.0.1:3128 (in the default configuration).


Filter rule association
-----------------------

This option controls the creation of linked filter rules in :menuselection:`Firewall --> Rules`.

.. tabs::

    .. tab:: Pass

       An linked filter rule will be automatically added and updated. This rule cannot be seen or edited in
       :menuselection:`Firewall --> Rules`.

       .. Tip::

          This option is recommended for simple setups.

    .. tab:: None

       Choose this if you want to create your own :menuselection:`Firewall --> Rules` manually. No linked filter rule is created.

    .. tab:: Add associated filter rule

       Adds a linked :menuselection:`Firewall --> Rules` rule that is automatically updated when the NAT rule is updated.
       The created filter rule cannot be manually edited. Ensure setting a `Description` in the NAT rule, the filter rule will share it.
       This option is the same as `Pass`, but makes the filter rule visible in :menuselection:`Firewall --> Rules`.

       .. Note::

          If multiple `Interfaces` are selected in the :menuselection:`Firewall --> NAT --> Port Forward` rule, the filter rule will
          appear in :menuselection:`Firewall --> Rules --> Floating`.

    .. tab:: Add unassociated filter rule

       Adds a filter rule **once** that is **not** linked to the NAT rule. The created filter rule can be edited manually, it will never
       be updated when changing the NAT rule. Ensure setting a `Description` in the NAT rule, the filter rule will set it once.

       .. Note::

          This option is recommended for more comple setups, like Port Forward rules on VPN interfaces.
          The rule can be edited and features like `reply-to` disabled.


----------
One-to-one
----------

One-to-one NAT will, as the name implies, translate two IPs one-to-one, rather than one-to-many as is most common.
In this respect, it is similar to what NPT does for IPv6.

In OPNsense, one-to-one NAT can be set up by navigating to :menuselection:`Firewall --> NAT --> One-to-one`. Here, you will see an
overview of one-to-one rules. New rules can be added by clicking **Add** in the upper right corner.

When adding a rule, the following fields are available:

====================== ===================================================================================================================
Disabled               Disable this rule without removing it.
Interface              Which interface this rule should apply to. Most of the time, this will be WAN.
Type                   BINAT (default) or NAT. See “Some terms explained”.
External network       Starting address of external network, which should be used to translate addresses to/from.
Source / invert        Invert match in “Source” field.
Source                 The internal network for this mapping, usually some `RFC 1918 <https://nl.wikipedia.org/wiki/RFC_1918>`_ range
Destination / invert   Invert match in “Destination” field.
Destination            The destination network packages should match, when used to map external networks, this is usually :code:`any`
Description            A description to easily find the rule in the overview.
NAT reflection         See “Some terms explained”. Leave this on the default unless you have a good reason not to.
====================== ===================================================================================================================


--------
Outbound
--------

When a client on an internal network makes an outbound request, the gateway will have to change the source IP to
the external IP of the gateway, since the outside server will not be able to send an answer back otherwise.

Outbound NAT is also referred to as “Source NAT” or “SNAT”.

If you only have one external IP, then you leave the Outbound NAT options on automatic. However, if you have
multiple IP addresses, you might want to change the settings and add some custom rules.

The main settings for outbound are as follows:

======================================== =====================================================================================================
 Automatic outbound NAT rule generation   The default. Follows the behaviour described above, and is good for most scenarios.
 Manual outbound NAT rule generation      No automatic rules are generated. They can be added manually.
 Hybrid outbound NAT rule generation      Automatic rules are added, but additional manual rules can be added as well.
 Disable outbound NAT rule generation     Disables outbound NAT. This is used for :doc:`transparent bridges <how-tos/transparent_bridge>`, for example.
======================================== =====================================================================================================

New rules can be added by clicking **Add** in the upper right corner.

When adding a rule, the following fields are available:

=====================  ==========================================================================================================
 Disabled               Disable this rule without removing it.
 Do not NAT             Disable NAT for all traffic matching this rule. Leave this disabled unless you know what you are doing.
 Interface              Which interface this rule should apply to. Most of the time, this will be WAN.
 TCP/IP version         IPv4 or IPv6
 Protocol               In typical scenarios, this will be TCP.
 Source invert          Invert match in “Source” field.
 Source                 The source network to match
 Source port            When applicable, the source port we should match on.
                        This is usually random and almost never equal to the destination port range (and should usually be 'any').
 Destination invert     Invert match in “Destination” field.
 Destination            Destination network to match
 Destination port       Service port the traffic is using
 Translation / target   What to translate matching packets to.
 Log                    Put packets matching this rule in the logs. Use this sparingly to avoid overflowing the logs.
 Translation / port     Which port to use on the target
 Static-port            Prevents pf(4) from modifying the source port on TCP and UDP packets.
 Pool options           See “Some terms explained”. The default is to use Round robin.
 Set local tag          Set a tag that other NAT rules and filters can check for.
 Match local tag        Check for a tag set by another rule.
 No XMLRPC sync         Prevent this rule from being synced to a backup host. (Checking this on the backup host has no effect.)
 Description            A description to easily find the rule in the overview.
=====================  ==========================================================================================================


--------------------
API access
--------------------


Partial API access, is available and described in more detail in the :doc:`firewall <../development/api/core/firewall>` api reference manual.

-------
How-tos
-------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   how-tos/nat_reflection
