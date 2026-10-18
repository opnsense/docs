==============================
IPv6 for generic DSL dialup
==============================

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

Next go to :menuselection:`Interfaces --> Settings` and verify that **Turn off IPv6** is disabled.

--------------------------------
Step 3 - Interface Configuration
--------------------------------

Go to :menuselection:`Interfaces --> Assignments`, edit WAN, set **IPv6 Configuration Type** to DHCPv6 and select:

- Request prefix only
- Send prefix hint

Set the prefix size to the one your provider delegates, mostly /56 or 64, sometimes /48.

Then edit LAN on the Assignments page and set **IPv6 Configuration Type** to **Track Interface (legacy)**.
Choose WAN as the **Parent interface**; ``0x0`` is a valid **Assign prefix ID**.

Hit Apply and disable/enable the NICs of your internal systems. Depending on the system
and vendor, also a reboot could be required.

If you experience problems with the 24h disconnect disrupting connectivity, it may help to set **Prevent Release**
in section :menuselection:`Interfaces --> Settings`.
