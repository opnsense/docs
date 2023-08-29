======================================
Configure IPv6 behind an AVM Fritz!Box
======================================
**Original Author:** Thomas Klein

------------
Introduction
------------

The `AVM Fritz!Box`, or FB for short, is a popular home router for
DSL, Cable and Fiber in Germany. This guide will setup a OPNSense
behind a FB, handover delegated prefixes from the provider and
configure local interfaces on the OPNSense to cope with dynamically changing IPv6 prefixes.

This guide is based on a Vodafone Cable connection (formerly Kabel-BW) and an
`AVM Fritz!Box Cable 6591` running `Fritz!OS 7.29`.

The settings presented here should work for most other dial-up scenarios and FB models
too. The size of the delegated subnet may differ.

------------
The Scenario
------------

This guide will configure a home network behind a common dial-up type ISP connection.
The OPNsense has an interface pointing to the ISP named `WAN` and has three internal 
interfaces called `DMZ`, `LAN` and `WLAN`. Each of those internal interfaces will get a /64
subnet from the delegated IPv6 prefix. This way it is easy to control the dataflow between
all four segments on the OPNsense. 

In this example the dial-up ISP assigns a `/59` prefix to the FB, so there are enough bits left 
for subnetting in a SOHO setup. 

------------------------------
Step 1 - prepare the Fritz!Box
------------------------------

The AVM website has a knowledge base article about the basic settings required on each FB model to enable IPv6 on client devices.
https://avm.de/service/wissensdatenbank/dok/FRITZ-Box-6591-cable/1239_IPv6-Subnetz-in-FRITZ-Box-einrichten/
The crucial setting is the checkbox **allow other routers IPv6 prefixes**. Without that the delegated internal prefixes will
not be reachable from the Internet.

Also, not stated in above document, it is possible to modify the **Internet - Permit Access** settings for
the OPNsense host. Select :menuselection:`Internet --> Permit Access --> <your OPN Host> --> IPv6 Settings --> Open firewall for delegated IPv6 prefixes of this device`
in order to make your delegated internal subnets available via Internet. 

------------------------------------
Step 2 - configure the WAN interface
------------------------------------

On the OPNSense go to :menuselection:`Interfaces --> WAN` and set the configuration type for IPv6 to **DHCPv6**. On the bottom part of the dialog in
**DHCPv6 Client configuration** make sure to select 

* checkbox: **Request only an IPv6 prefix**
* checkbox: **Send IPv6 prefix hint**
* dropdown: **Prefix delegation size**. For this example setup select `60`

Note the following:

1. the requested prefix differs by one bit compared to what the ISP delegated the FB (60 vs. 59)
2. the setting **Request only an IPv6 prefix** is the important part. 
   With this setting the FB acknowledges
   the OPNsense as a router and really delegates a prefix. The OPNSense will only get a link-local `0xfe80`
   address but that is fine. If this checkbox is not selected the FB considers the OPNsense as an end-user device
   and plainly refuses to delegate a prefix to it. The OPNsense end up with an valid IPv6 address but with `/64`
   netmask so nothing to delegate into the internal network.

-----------------------------------------------------------
Step 3 - configure the internal DMZ / LAN / WLAN interfaces
-----------------------------------------------------------

Now it is time to set up the internal interfaces. The settings are more or less the same for all of them.
Instead of **DHCPv6** select **Track Interface** and on the bottom IPv6 dialog and choose the `WAN` interface for tracking.
This is also the place to divide the delegated prefix into distinct subnets. Just specify an individual **Interface prefix ID**
for each interface. In this example the FB gave us `aaaa:bbbb:cccc:9410::/60` and we choose:

=========  ===================  =======================
Interface  Interface prefix ID  result-prefix
=========  ===================  =======================
`DMZ`      `0x01`               `aaaa:bbbb:cccc:9411::`
`WLAN`     `0x02`               `aaaa:bbbb:cccc:9412::`
`LAN`      `0x03`               `aaaa:bbbb:cccc:9413::`
=========  ===================  =======================

The **Interface prefix Id** acts as the subnet extension (for lack of better wording) on top of the prefix provided by the FB.
In this example we have a /60 prefix so effectively there are 4 bits left for subnetting. As a result valid values for **Interface prefix Id** are between `0x00` and `0x0f`. 

In order to being able to setup the router advertisements in the next step make sure to select the checkbox
**Allow manual adjustment of DHCPv6 and Router Advertisements** for each of the internal interfaces.

----------------------------------------------
Step 3.1 - configure the Router Advertisements
----------------------------------------------

With the new subnets in place it is time to configure the **Router Advertisements**.
For this guide the following settings have been chosen:

===========================  ===========  ======================================================================
Setting                      Value        Comment
===========================  ===========  ======================================================================
Router Advertisements        Assisted     this enables DHCPv6 and SLAAC
Router Priority              Normal       Default is high which would work too
Source Address               Automatic    the default
Advertise Default Gateway    checked      the default
Advertise Routes             empty  
DNS options                  empty        this gives away the OPNsense as DNS server with the current dynamic IP
===========================  ===========  ======================================================================

---------------------------------------
Step 3.2 - configure the DHCPv6 service
---------------------------------------

The clients would now be able to grab an IPv6 via SLAAC, find their router and get a DNS resolver but not all clients do
know SLAAC. Also there are valid reasons to assign fixed IPv6 address via DHCP to some clients for instance to make them available
from the Internet.

In :menuselection:`Services --> DHCPv6 --> [DMZ]` (and similar for the other interfaces) the DHCPv6 settings can be configured.
Initially the dynamically acquired subnet including the interface id and the available range is shown. 

For most SOHO setups 256 clients per network zone will probably more than enough so we restrict the range for the DMZ to
`aaaa:bbbb:cccc:9411::1` --> `aaaa:bbbb:cccc:9411::ff`

But wait! The prefix is dynamic isn't it ? How to deal with that ?

Easy. Just omit the variable part and configure the DHCPv6 range to be
`::1` --> `::ff`

OPNSense will automatically prefix this pattern with the dynamically acquired prefix.

Repeat for all the other subnets. Don't forget to configure the `Domain search list` to match the SOHO internal DNS domain.

-----------------------------
Step 4 - setup Firewall rules
-----------------------------

All clients should now have a proper IPv6 address (actually more than one), know their DNS server(s) and their upstream router.
All thats left to do is adding the appropriate firewall rules. 

By default outgoing traffic should already be possible but traffic from the Internet to the internal server needs a firewall rule.
There are different philosophies on how to manage firewall rules. Just use a similar strategy as with your IPv4 setup so rule management
is consistent.

Keep in mind that the `DMZ` / `LAN` / `WLAN` prefix is dynamic. The build-in macros like `DMZ net` will work for the whole network. 
But if you need a rule for a single server your should setup an alias pointing to your (fixed) DHCP IP and use this instead.

---------------
Troubleshooting
---------------

While discovering the specifics of IPv6 behind a FB in combination with OPNsense the first point of debugging was always
connecting via SSH to OPNsense on the CLI. 

In the directory `/tmp/` you will find several IPv6 related intermediate files. The most helpful here was `/tmp/<interfacename>_prefixv6`.
In this file you will find the prefix delegated to you by your upstream router. If you are behind an FB and this file does not exist chances
are you forgot to seth the **Request only an IPv6 prefix** setting on the WAN interface.

Another helpful command is `radvdump`. This tool dumps the output of the router advertisements in a nicely formatted way.