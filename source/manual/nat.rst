===========================
Network Address Translation
===========================

.. contents:: Index


Network Address Translation (abbreviated to NAT) is a way to separate external and internal networks (WANs and LANs),
and to share an external IP between clients on the internal network. NAT can be used on IPv4 and IPv6.

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
    manual Source NAT (Outbound) rule.

**Pool options**: When there are multiple IPs to choose from, this option will allow regulating which IP gets used.
The default, Round Robin, will simply distribute packets to one server after the other. If you only have one external
IP, this option has no effect.

------------------------------
Destination NAT (Port Forward)
------------------------------

When multiple internal clients share one external IP address, any inbound connection targeting the external IP address
will not succeed, since the firewall will not know where to send the traffic. This can be addressed by creating port
forwarding rules. For example, for a web server behind the firewall to be accessible, ports 80 and 443 need to
be redirected to it.

Destination NAT (Port Forward) can be set up by navigating to :menuselection:`Firewall --> NAT --> Destination NAT (Port Forward)`.
Here, you will see an overview of Destination NAT (Port Forward) rules.

When adding a rule, the following fields are available:

.. tabs::

   .. tab:: Organization

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Disabled**                              Disable this rule so it will not be used.
      **Sequence**                              Rules are evaluated in sequence order.
      **Categories**                            Assign categories for rule organization.
      **Description**                           Enter a description to identify this rule.
      ========================================= ====================================================================================

   .. tab:: Interface

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Interface**                             Choose the interface(s) on which the traffic originates.
      **Version**                               Select IPv4, IPv6 or both.
      **Protocol**                              Assign categories for rule organization.
      **Description**                           Select the protocol this rule should match.
      ========================================= ====================================================================================

   .. tab:: Source

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Invert Source**                         Match everything except the specified source.
      **Source Address**                        Specify the source network or alias to match.
      **Source Port**                           Source port or port range.
      ========================================= ====================================================================================

   .. tab:: Destination

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Invert Destination**                    Match everything except the specified destination.
      **Destination Address**                   Destination address or alias to match.
      **Destination Port**                      Destination port or port range.
      ========================================= ====================================================================================

   .. tab:: Translation

      .. Tip:: This translates the original destination (e.g., the external IP address of the firewall) to a new target (e.g., an internal host).

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Redirect Target IP**                    The internal IP address to forward traffic to.
      **Redirect Target Port**                  The port on the internal host to forward traffic to.
      **Pool Options**                          Choose how traffic is distributed when multiple target IPs are used.
      ========================================= ====================================================================================

   .. tab:: Options

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **No XMLRPC Sync**                        Exclude this rule from synchronizing to HA peers.
      **NAT Reflection**                        Control NAT reflection for this rule.
      **Set Tag**                               Assign a tag to packets matching this rule.
      **Match Tag**                             Only match packets that have this tag.
      **Firewall rule**                         By default, firewall rules need to be created manually, which is also the advised
                                                option. Alternatively you can use Pass, which passes traffic on the nat rule
                                                (not visible in the rules tab) or generate interface rules which can be overruled
                                                via rules with a higher priority. Please keep in mind the destination for the rule
                                                should match the target defined in this NAT rule.
      ========================================= ====================================================================================


.. Note::

   This feature is also used to implement transparent proxies. A connection can to be forwarded to a
   daemon (listening on localhost), which then tries to get the original destination IP from the `/dev/pf` device.

   For example, a transparent proxy that handles HTTP traffic needs a rule that forwards traffic from TCP port 80,
   IPv4 to 127.0.0.1:3128 (in the default configuration).

.. Attention::

   You cannot NAT to [::1] (the IPv6 localhost) or any other link-local addresses. IPv6 requires routable addresses
   for NAT, at least an ULA (Unique Local Address) is required as target.

Filter rule association
-----------------------

This option controls the creation of linked filter rules in :menuselection:`Firewall --> Rules [new]`.

.. tabs::

   .. tab:: Manual

      Choose this if you want to create your own :menuselection:`Firewall --> Rules [new]` manually. No linked filter rule is created.

      .. Note::

         This option is recommended for more comple setups, like Destination NAT (Port Forward) rules on VPN interfaces.
         The filter rule can be edited and features like `reply-to` disabled.

   .. tab:: Pass

      A filter rule will be automatically added and updated. This rule cannot be seen or edited in :menuselection:`Firewall --> Rules [new]`.

      .. Note::

         Recommended choice for most setups.

   .. tab:: Register rule

      Adds a linked filter rule in :menuselection:`Firewall --> Rules [new]` that is automatically updated when the NAT rule is updated.
      The created filter rule cannot be manually edited.


----------
One-to-one
----------

One-to-one NAT will translate two IPs one-to-one, rather than one-to-many as is most common in other NAT types.
In this respect, it is similar to what NPT does for IPv6.

One-to-one NAT can be set up by navigating to :menuselection:`Firewall --> NAT --> One-to-one`.

When adding a rule, the following fields are available:

.. tabs::

   .. tab:: Organization

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Enable**                                Enable this rule
      **Sequence**                              Rules are evaluated in sequence order.
      **Categories**                            Assign categories for rule organization.
      **Description**                           Enter a description to identify this rule.
      ========================================= ====================================================================================

   .. tab:: Interface

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Interface**                             Choose the interface(s) on which the traffic originates.
      ========================================= ====================================================================================

   .. tab:: Mapping

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Type**                                  Select BINAT (default) or NAT here, when nets are equally sized binat is usually the
                                                best option.Using NAT we can also map unequal sized networks. A BINAT rule specifies
                                                a bidirectional mapping between an external and internal network and can be used from
                                                both ends, nat only applies in one direction.
      **External network**                      Enter the external subnet's starting address for the 1:1 mapping or network.
                                                This is the address or network the traffic will translate to/from.
      **Invert Source**                         Use this option to invert the sense of the match.
      **Source**                                Enter the internal subnet for the 1:1 mapping.
      ========================================= ====================================================================================

   .. tab:: Destination

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Invert Destination**                    Match everything except the specified destination.
      **Destination Address**                   Destination address or alias to match. The 1-1 mapping will only be used for
                                                connections to or from the specified destination. Hint: this is usually 'any'.
      ========================================= ====================================================================================

   .. tab:: Options

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Log**                                   Log packets that are handled by this rule.
      **NAT reflection**                        Choose the automatic NAT reflection mode.
      ========================================= ====================================================================================


----------------------------
Source NAT (Outbound)
----------------------------

When a client on an internal network makes an outbound request, the gateway will have to change the source IP to
the external IP of the gateway, since the outside server will not be able to send an answer back otherwise.

Source NAT (Outbound), abbreviated to SNAT, can be configured under
:menuselection:`Firewall --> NAT --> Source NAT (Outbound)`.

If you only have one external IP, the automatic mode is suitable in most cases. With multiple external addresses,
you may want to use hybrid or manual mode and add custom rules.

====================================== =====================================================================================================
 Automatic Source NAT rule generation  The default. Follows the behaviour described above, and is suitable for most scenarios.
 Manual Source NAT rule generation     No automatic rules are generated. They can be added manually.
 Hybrid Source NAT rule generation     Automatic rules are generated, and additional manual rules can be added.
 Disable Source NAT rule generation    Disables Source NAT. This is used for :doc:`transparent bridges <how-tos/transparent_bridge>`, for example.
====================================== =====================================================================================================

When adding a rule, the following fields are available:

.. tabs::

   .. tab:: Organization

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Enable**                                Enable this rule
      **Sequence**                              Rules are evaluated in sequence order.
      **Categories**                            Assign categories for rule organization.
      **No XMLRPC Sync**                        Exclude this rule from HA synchronization.
      **Description**                           Enter a description to identify this rule.
      ========================================= ====================================================================================

   .. tab:: Interface

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Interface**                             Choose the interface(s) on which the traffic originates.
      **Version**                               Select IPv4, IPv6 or both.
      **Protocol**                              Assign categories for rule organization.
      **Description**                           Select the protocol this rule should match.
      ========================================= ====================================================================================

   .. tab:: Source

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Invert Source**                         Match everything except the specified source.
      **Source Address**                        Specify the source network or alias to match.
      **Source Port**                           Source port or port range.
      ========================================= ====================================================================================

   .. tab:: Destination

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Invert Destination**                    Match everything except the specified destination.
      **Destination Address**                   Destination address or alias to match.
      **Destination Port**                      Destination port or port range.
      ========================================= ====================================================================================

   .. tab:: Translation

      .. Tip:: This translates the original source (e.g., an internal host) to a new source (e.g., the external IP address of the firewall).

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Translate Source IP**                   Packets matching this rule will be mapped to the IP address given here.
      **Translate Source Port**                 Source port number or well-known name.
      **Pool Options**                          Choose how traffic is distributed between multiple translation addresses.
      **Source Hash Key**                       Keep source-hash mappings stable across ruleset reloads.
      **Static-port**                           Prevent changes to the source port of TCP and UDP packets.
      **Endpoint Independent**                  Enable endpoint-independent mapping for UDP traffic.
      ========================================= ====================================================================================

   .. tab:: Options

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Do not NAT**                            Enabling this option will disable NAT for traffic matching this rule and stop
                                                processing Source NAT rules.
      **Log**                                   Log packets that are handled by this rule.
      **Set local tag**                         Assign a tag that other NAT or filter rules can match.
      **Match local tag**                       Used to specify that packets must already be tagged with the given tag in order
                                                to match the rule.
      ========================================= ====================================================================================


------------------------------
NPTv6
------------------------------

Network Prefix Translation, shortened to NPTv6, is used to translate IPv6 addresses. A common usage for this
is to translate global ("WAN") IPs to local ones. In this regard, it is similar to NAT, although NPTv6 can only be
used to map addresses one-to-one, unlike NAT which typically translates one external IP to several internal ones.

NPTv6 routes are listed at :menuselection:`Firewall --> NAT --> NPTv6`.

When adding a rule, the following fields are available:

.. tabs::

   .. tab:: Organization

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Enable**                                Enable this rule
      **Sequence**                              Rules are evaluated in sequence order.
      **Categories**                            Assign categories for rule organization.
      **Description**                           Enter a description to identify this rule.
      ========================================= ====================================================================================

   .. tab:: Interface

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Interface**                             Choose which interface this rule applies to.
      ========================================= ====================================================================================

   .. tab:: Mapping

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Internal IPv6 Prefix**                  Enter the internal IPv6 prefix (source) for this network prefix translation.
      **External IPv6 Prefix**                  Enter the external IPv6 prefix (target) for this network prefix translation.
                                                Leave empty to auto-detect the prefix address using the specified tracking interface
                                                instead. The prefix size specified for the internal prefix will also be applied to
                                                the external prefix.
      **Track interface**                       Use prefix defined on the selected interface instead of the interface this rule
                                                applies to when target prefix is not provided.
      ========================================= ====================================================================================

   .. tab:: Options

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================
      **Log**                                   Log packets that are handled by this rule.
      ========================================= ====================================================================================


-------
How-tos
-------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   how-tos/nat_reflection
