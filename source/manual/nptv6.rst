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
 Interface                     Which interface this rule should apply to. Most of the time, this will be a WAN interface.
 Internal IPv6 Prefix          The internal IPv6 prefix used in the LAN(s). This will replace the prefix of the destination address in inbound packets. The prefix size specified here will also be applied to the external prefix.
 External IPv6 Prefix          The external IPv6 prefix. This will replace the prefix of the source address in outbound packets.
 Category                      The category this rule belongs to, can be used as a filter in the overview.
 Description                   A description to easily indentify the purpose of this rule in the overview.
============================= =======================================================================================================================================================================
