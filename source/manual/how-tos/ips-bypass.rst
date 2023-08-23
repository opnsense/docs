==========================
IPS - Bypass local traffic from inspection
==========================

This tutorial explains how to bypass traffic between local attached networks. Following this tutorial will result in traffic only being inspected between external (WAN) networks and internal (LAN) networks.

* **Benefit**: There will be faster routing performance between local networks when Intrusion Detection is enabled in IPS mode.
* **Potential Risk: Internal traffic WON'T be inspected anymore, so use this with care!**

-------------
Prerequisites
-------------

* Some features described on this page were added in the latest version. Always keep your system up to date.
* Intrusion Detection should be **Enabled** and **IPS mode** selected. 
* There should only be **internal networks** selected in **Interfaces** (LAN, OPT1 etc..), not the WAN interfaces.

To start go to :menuselection:`Services --> Intrusion Detection --> Administration`.

------------
User defined
------------

Select the tab **User defined**.

-----------------
Create new Rules
-----------------

Select **+** to add a new rule.

* Input the **Source IP** as IP with CIDR-Suffix or Prefix, e.g. ``10.0.0.0/8`` or ``2003:a:a:a::/56``
* Input the **Destination IP** as IP with CIDR-Suffix or Prefix, e.g. ``10.0.0.0/8`` or ``2003:a:a:a::/56``
* Select the **Action** as *Pass*
* Enable the **Bypass** checkbox
* Set the **Description** as "Bypass net 10.0.0.0 to 10.0.0.0"

Select **+** to create additional new rules

* Repeat the above steps to create rules between each of the RFC1918 Private IPv4 subnets. (``192.168.0.0/16``, ``172.16.0.0/12``, ``10.0.0.0/8``). This will result in 9 rules.
* If you use IPv6, create additional rules between your IPv6 Prefixes. You can find them in :menuselection:`Interfaces --> Overview` at IPv6 prefix of the selected WAN interface. (e.g ``2003:a:a:a::/56``)

The finished IPv4 ruleset should include the following rules:

* ``Bypass net 10.0.0.0 to 10.0.0.0``
* ``Bypass net 10.0.0.0 to 172.16.0.0``
* ``Bypass net 10.0.0.0 to 192.168.0.0``
* ``Bypass net 172.16.0.0 to 10.0.0.0``
* ``Bypass net 172.16.0.0 to 172.16.0.0``
* ``Bypass net 172.16.0.0 to 192.168.0.0``
* ``Bypass net 192.168.0.0 to 10.0.0.0``
* ``Bypass net 192.168.0.0 to 172.16.0.0``
* ``Bypass net 192.168.0.0 to 192.168.0.0``

-------------------
Apply configuration
-------------------

First apply the configuration by pressing the **Apply** button at the bottom of
the form.
