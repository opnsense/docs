=====================================
Configure IPv6 for generic DSL dialup
=====================================

------------
Introduction
------------

This short article shows how to setup IPv6 on a standard DSL connection and how
to handover the delegated prefix from your provider in your local LAN.

It's compatible and tested for but not limited to:

- Deutsche Telekom

-------------------------
Step 1 - General Settings
-------------------------

Go to :menuselection:`System --> Settings --> General` and check that **Prefer IPv4 over IPv6**
is not ticked. This value is default so just check if it has been touched.

Also enable **Allow DNS server list to be overridden by DHCP/PPP on WAN** at the 
bottom, so you get the correct DNS servers if you just use IPv4 ones.

-------------------
Step 2 - Allow IPv6
-------------------

Next go to :menuselection:`Firewall --> Settings --> Advanced` and verfiy that **Allow IPv6** is enabled.

--------------------------------
Step 3 - Interface Configuration
--------------------------------

In :menuselection:`Interfaces --> [WAN]` and set **IPv6 Configuration Type** to DHCPv6 and in section
**DHCPv6 client configuration** at the bottom tick:

- Request only an IPv6 prefix
- Send IPv6 prefix hint
- Use IPv4 connectivity

Set the prefix size to the one your provider delegates, mostly /56 or 64, sometimes /48.

Then change to :menuselection:`Interfaces --> [LAN]` and set **IPv6 Configuration Type** to **Track Interface**.
At the bottom in section **Track IPv6 Interface** choose **IPv6 Interface** as WAN and for
**IPv6 Prefix ID** a value of 0 is perfectly fine.

Hit Apply and disable/enable the NICs of your internal systems. Depending on the system
and vendor, also a reboot could be required.

If you experience problems with the 24h disconnect disrupting connectivity, it may help to set **Prevent Release**
in section :menuselection:`Interfaces --> Settings`.
