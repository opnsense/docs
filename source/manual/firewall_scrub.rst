===========================
Normalization
===========================

Traffic normalization adjusts selected packet properties before the final pass or block decision.
Global defaults are available under :menuselection:`Firewall --> Settings --> Filter`, while custom
normalization is configured as part of :menuselection:`Firewall --> Rules [new]`.

Global settings
---------------

==========================  =============================================================================================
**Option**                  **Description**
==========================  =============================================================================================
**Enable scrub**            Enable default packet scrubbing and generated interface MSS rules.
**IP Do-Not-Fragment**      Clear the DF bit when fragmented IPv4 packets are reassembled.
**IP Random ID**            Randomize the identification field of IPv4 packets using a generated match rule.
==========================  =============================================================================================

Filling in **MSS** on an interface under :menuselection:`Interfaces --> Assignments` generates IPv4 and IPv6
normalization match rules for that interface. Disabling scrub also disables these generated rules.

Rule normalization
------------------

Select the **Match** action to apply normalization without deciding whether traffic is passed or blocked. A **Pass**
rule can apply the same options while also allowing traffic. Match rules follow the normal firewall rule ordering;
they are usually not quick so evaluation can continue after their options have been applied.

The normalization fields are available in the advanced section of the rule dialog.

==========================  =============================================================================================
**Option**                  **Description**
==========================  =============================================================================================
**Clear DF bit**            Clear the don't-fragment bit on matching IPv4 packets.
**Random ID**               Replace the IPv4 identification field with random values.
**Maximum MSS**             Reduce the maximum segment size on matching TCP SYN packets.
**Minimum TTL**             Enforce a minimum TTL on matching IP packets.
**Set TOS / DSCP**          Set the TOS or DSCP value on matching packets.
==========================  =============================================================================================
