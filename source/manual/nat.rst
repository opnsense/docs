===========================
Network Address Translation
===========================

Network Address Translation (abbreviated to NAT) is a way to separate external and internal networks (WANs and LANs),
and to share an external IP between clients on the interal network. NAT only works on IPv4. For IPv6,
:doc:`Network Prefix Translation <nptv6>` can be used instead.

Most of the options below use three different addresses: the source, destination and redirect address. These
addresses are used for the following:

============= ===========================================================================================================
 Source        Where the traffic comes from. This can often be left on “any”.
 Destination   Where the traffic is headed. For incoming traffic from outside, this is usually your external IP address.
 Redirect      Where the traffic should be redirected.
============= ===========================================================================================================

--------------------
Some terms explained
--------------------

**BINAT**: NAT generally works in one direction. However, if you have networks of equal size, you can also use BINAT, which is
bidirectional. This can simplify your set-up. If you don't have networks of equal size, you can only use regular NAT.

**NAT reflection**: When a client on the internal network tries to access another client, but using the *external* IP
instead of the internal one (which would the most logical), NAT reflection can rewrite this request so that it uses
the internal IP, in order to avoid taking a detour and applying rules meant for actual outside traffic.

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

In OPNsense, port forwarding can be set up by navigating to **Firewall->NAT->Port Forward**. Here, you will see
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
 Source port range
 Destination / Invert      Invert match in “Destination” field.
 Destination               Where the traffic is headed.
 Destination port range
 Redirect target IP        Where to redirect the traffic to.
 Redirect target port
 Pool Options              See “Some terms explained”. The default is to use Round robin.
 Description               A description to easily find the rule in the overview.
 Set local tag             Set a tag that other NAT rules and filters can check for.
 Match local tag           Check for a tag set by another rule.
 No XMLRPC sync            Prevent this rule from being synced to a backup host. (Checking this on the backup host has no effect.)
 NAT reflection            See “Some terms explained”. Leave this on the default unless you have a good reason not to.
 Filter rule association   Associate this with a regular firewall rule.
========================= =========================================================================================================

----------
One-to-one
----------

One-to-one NAT will, as the name implies, translate two IPs one-to-one, rather than one-to-many as is most common.
In this respect, it is similar to what NPT does for IPv6.

In OPNsense, one-to-one NAT can be set up by navigating to **Firewall->NAT->One-to-one**. Here, you will see an
overview of one-to-one rules. New rules can be added by clicking **Add** in the upper right corner.

When adding a rule, the following fields are available:

====================== =================================================================================================
 Disabled               Disable this rule without removing it.
 Interface              Which interface this rule should apply to. Most of the time, this will be WAN.
 Type                   BINAT (default) or NAT. See “Some terms explained”.
 External network       Starting address of external network.
 Source / invert        Invert match in “Source” field.
 Source
 Destination / invert   Invert match in “Destination” field.
 Destination
 Description            A description to easily find the rule in the overview.
 NAT reflection         See “Some terms explained”. Leave this on the default unless you have a good reason not to.
====================== =================================================================================================

--------
Outbound
--------

When a client on an internal network makes an outbound request, the gateway will have to change the source IP to
the external IP of the gateway, since the outside server will not be able to send an answer back otherwise.

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
 Source
 Source port
 Destination invert     Invert match in “Destination” field.
 Destination
 Destination port
 Translation / target   What to translate matching packets to.
 Log                    Put packets matching this rule in the logs. Use this sparingly to avoid overflowing the logs.
 Translation / port
 Static-port            Prevents pf(4) from modifying the source port on TCP and UDP packets.
 Pool options           See “Some terms explained”. The default is to use Round robin.
 Set local tag          Set a tag that other NAT rules and filters can check for.
 Match local tag        Check for a tag set by another rule.
 No XMLRPC sync         Prevent this rule from being synced to a backup host. (Checking this on the backup host has no effect.)
 Description            A description to easily find the rule in the overview.
=====================  ==========================================================================================================
