=====
NPTv6
=====

Network Prefix Translation, shortened to NPTv6, is used to translate IPv6 addresses. A common usage for this
is to translate global ("WAN") IPs to local ones. In this regard, it is similar to NAT, although NPTv6 can only be
used to map addresses one-to-one, unlike NAT which typically translates one external IP to several internal ones.

NPTv6 routes are listed at :menuselection:`Firewall --> NAT --> NPTv6`. New rules can be added by clicking **Add** in the upper right
corner. A quick overview of the fields:

============================= =======================================================================================================================================================================
 Disabled                      Disables this rule without having to remove it.
 Interface                     Which interface this rule should apply to. Most of the time, this will be the WAN interface.
 Description                   A description to easily indentify the purpose of this rule in the overview.
 **Internal IPv6 Prefix**
 Source / Invert               Use this option to invert the sense of the source address match.
 Source / Address              The internal (LAN) ULA IPv6 Prefix for the Network Prefix Translation. The prefix size specified for the internal IPv6 prefix will be applied to the external prefix.
 **Destination IPv6 Prefix**
 Destination / Invert          Use this option to invert the sense of the destination address match.
 Destination / Address         The Global Unicast routable IPv6 prefix.
============================= =======================================================================================================================================================================
