======================================
Configure IPv6 behind an AVM Fritz!Box
======================================
**Original Author:** Thomas Klein

------------
Introduction
------------

The `AVM Fritz!Box`, or FB for short, is a popular home router for
DSL, Cable and Fiber in Germany. This guide will setup an OPNSense
behind an FB, handover delegated prefixes from the provider and
configure local interfaces on the OPNSense to cope with dynamically changing IPv6 prefixes.

This guide is based on a Vodafone Cable connection (formerly Kabel-BW) and an
`AVM Fritz!Box Cable 6591` running `Fritz!OS 7.29`.

The settings presented here should work for most other dial-up scenarios and FB models
too. Just the size of the delegated subnet might differ.

------------
The Scenario
------------

We will configure a home network behind a common dial-up type ISP connection.
Our OPNsense has one interface pointing to the ISP, we call it `WAN`, and has three internal 
interfaces called `DMZ`, `LAN` and `WLAN`. Each of those internal interfaces should get it's own 
subnet aka IPv6 präfix. This way we can easily control the dataflow on our OPNsense between
all four segments. 

Our dial-up ISP presents us a `/59` präfix, so we have enough bits left for easy subnetting.

------------------------------
Step 1 - prepare the Fritz!Box
------------------------------

The AVM website has a knowledge base article about the basic settings required on each FB model to enable IPv6 on client devices.
https://avm.de/service/wissensdatenbank/dok/FRITZ-Box-6591-cable/1239_IPv6-Subnetz-in-FRITZ-Box-einrichten/
The crucial setting is the checkbox **allow other routers IPv6 präfixes**. Without that your delegated internal prefixes will
not be reachable from the Internet.

Also, not stated in above document, I found it necessary to modify the **Internet - Permit Access** settings for
the OPNsense host. Make sure to select :menuselection:`Internet --> Permit Access -> <your OPN Host> --> IPv6 Settings --> Open firewall for delegated IPv6 prefixes of this device` in order to make your delegated
internal subnets available via Internet. 

------------------------------------
Step 2 - configure the WAN interface
------------------------------------

On OPNSense go to :menuselection:`Interfaces --> WAN` and set the configuration type for IPv6 to **DHCPv6**. On the bottom part of the dialog in
**DHCPv6 Client configuration** make sure to select 

* checkbox: **Request only an IPv6 prefix**
* checkbox: **Send IPv6 prefix hint**
* dropdown: **Prefix delegation size** in our example select `60`

Two things to notice here:

1. the prefix you are requesting has one bit more compared to what your ISP assigned the FB (60 vs. 59)
2. the setting **Request only an IPv6 prefix** is the important part. With this setting the FB aknowledges
   your OPNsense as a router and really delegates a prefix. Your OPNSense will only get a link-local `0xfe80`
   address but that is fine. If you do not use this checkbox the FB considers your OPNsense as an end-user device
   and plainly refuses to delegate a prefix to your OPNsense. You end up with an valid IPv6 address but with `/64`
   netmask so nothing to delegate in your home net.


-------------------------------------------------
Step 3 - configure the DMZ / LAN / WLAN interface
-------------------------------------------------

Now it's time to setup your internal interfaces. The settings are more or less the same for all of them.
Instead of 'DHCPv6' you select 'Track Interface' and on the bottom IPv6 dialog choose the WAN interface to track.
This is also the place to divide your delegated prefix into distinct sub-nets. Just specify an idividual 'Interface prefix ID'
for each interface. In our example our FB gave us `aaaa:bbbb:cccc:9410::/60` and we choose:

=========  ============  =======================
Interface  Interface ID  result-prefix
=========  ============  =======================
DMZ        `0x01`        `aaaa:bbbb:cccc:9411::`
WLAN       `0x02`        `aaaa:bbbb:cccc:9412::`
LAN        `0x03`        `aaaa:bbbb:cccc:9413::`
=========  ============  =======================

---------------------------------------------
Step 3.1 - configure the Router Advertisments
---------------------------------------------

With the new subnets in place it's time to configure the `Router Advertisments`. Not too much to configure here
as the defaults are already pretty good. 
For this guide i did choose the following settings:

===========================  ===========  =========================================================================
Setting                      Value        Comment
===========================  ===========  =========================================================================
Router Advertisements        Assissted    this gives us DHCPv6 and SLAAC
Router Priority              Normal       Default is high which would work too
Source Address               Automatic    the default
Advertise Default Gateway    checked      the default
Advertise Routes             empty  
DNS options                  empty        this gives away our OPNsense as DNS server with it's current dynamic IP's
===========================  ===========  =========================================================================


---------------------------------------
Step 3.2 - configure the DHCPv6 service
---------------------------------------

Our clients would now be able to grab an IPv6 via SLAAC, find their router and even get a DNS resolver but not all clients do
know SLAAC or we might like to give out a 'fixed' IPv6 address via DHCP for reasons.

In :menuselection:`Services --> DHCPv6 --> [DMZ]` (and similar for the others) we configure the DHCPv6 settings to our needs.
You will regognize that the Subnet is already shown to the dynamically aquired subnet including the interface id and the 
available range lists all possible combinations we can add to the DHCPv6 Server.

As these are quite a few and we'd like to keep our clients together we will restrict that range a bit. For most
SOHO setups 256 clients per network zone will probably more than enough so we restrict the range for the DMZ to
`aaaa:bbbb:cccc:9411::1` --> `aaaa:bbbb:cccc:9411::ff`

But wait! The prefix is dynamic isn't it ? How can we deal with that ?

Easy. Just omit the variable part and configure the DHCPv6 range to be
`::1` --> `::ff`

OPNSense will automagically add the assigned dynamic prefix to that in front.

Repeat for all the other subnets. Don't forget to configure the `Domain search list` to point to your home network.

-----------------------------
Step 4 - setup Firewall rules
-----------------------------

We are getting close. All our clients should now have a proper IPv6 address (actually more than one), know their DNS server(s) and their upstream router.
All thats left to do is adding the appropriate firewall rules. 

By default outgoing traffic should already be possible but traffic from the Internet to your internal webserver needs a firewall rule.
There are different philosophies on how to manage firewall rules so I spare me the details here.

Just keep in mind that your DMZ/LAN/WLAN prefix is dynamic. The build-in macros `DMZ net` will work for the whole network. 
But if youlike a rule for a single server your should setup an alias pointing to your (fixed) DHCP IP and use this instead.

---------------
Troubleshooting
---------------

While discovering the specifics of IPv6 behind a FB in combination with OPNsense the first point of debugging was always
going via SSH to OPNsense on the CLI. 

In the directory `/tmp/` you will find several IPv6 related intermediate files. The most helpful here was `/tmp/<interfacename>_prefixv6`.
In this file you will find the prefix delegated to you by your upstream router. If you are behind an FB and this file does not exist chances
are you forgot to seth the 'Request only an IPv6 prefix' setting on the WAN interface.

Another helpful command was 'radvdump'. This tool dumps the output of the router advertisments in a nicly formatted way.