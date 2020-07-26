==================
Tayga NAT64 how-to
==================

------------
Introduction
------------
IPv6-only networks are less complex to plan, configure, maintain and troubleshoot than dual-stack networks. But many services on the Internet
are still IPv4-only. NAT64 preserves access to these services by performing IPv6-to-IPv4 translation. The NAT64 implementation currently
available for OPNsense is the Tayga plugin.

.. Note::
   This how-to focuses on providing IPv6-only LANs with access to IPv4-only services. However, this is not the only use case for NAT64.

-------------
Prerequisites
-------------
OPNsense should be configured with working dual-stack Internet access and at least one IPv6-only LAN.

--------------------------------
Installing and configuring Tayga
--------------------------------
Go to :menuselection:`System --> Firmware --> Plugins` and install the `os-tayga` plugin. Then go to :menuselection:`Services --> Tayga`.

Tick `Enable` and configure all prefixes and addresses:

:IPv6 Prefix:
   The IPv6 prefix which Tayga uses to translate IPv4 addresses. You can use the default well-known prefix 64:ff9b::/96 or an unused /96 from
   your site's GUA prefix.

   .. Warning::
      When using the well-known prefix 64:ff9b::/96, Tayga will prohibit IPv6 hosts from contacting IPv4 hosts that have private (RFC1918)
      addresses. This is not relevant when using NAT64 for accessing IPv4 services on the Internet. However, if access to local services with
      private IPv4 addresses is required, a GUA /96 prefix must be used.

   .. Note::
      While technically possible, using a ULA prefix for NAT64 is not recommended. This can cause issues with certain hosts, especially those
      which support 464XLAT.

:IPv4 Pool:
   The virtual IPv4 addresses which Tayga maps to LAN IPv6 addresses. Can be left to its default value unless this overlaps with existing
   subnets in your network. Must be sufficiently large to fit all devices in your IPv6-only LAN(s).

Tayga is a hop in the path, so it needs its own IP addresses for ICMP:

:IPv4 Address:
   Will show up in traceroutes from the IPv4 side to the IPv6 side. Can be left to its default value unless you changed the `IPv4 Pool`.
   Should be located in the `IPv4 Pool` subnet.

:IPv6 Address:
   Will show up in traceroutes from the IPv6 side to the IPv4 side. Should be left empty in most cases. It will then get automatically
   created by Tayga.

   .. Note::
      Unless manually configured, Tayga generates its `IPv6 Address` by mapping its `IPv4 Address` into its `IPv6 Prefix`. For example, if
      the default `IPv6 Prefix` 64:ff9b::/96 and `IPv4 Address` 192.168.255.1 are being used, Tayga's `IPv6 Address` will be
      64:ff9b::192.168.255.1 (64:ff9b::c0a8:ff01).

Tayga behaves like an external device connected to OPNsense via a point-to-point interface. This interface requires IP addresses for ICMP:

:IPv4 NAT64 Interface Address:
   Can be left to its default value unless this conflicts with your network. Must not be located in the `IPv4 Pool` subnet. For simplicity,
   you may reuse an address of another OPNsense interface.

:IPv6 NAT64 Interface Address:
   Must not be located in the `IPv6 Prefix` subnet. For simplicity, you may reuse an address of another OPNsense interface.

   .. Warning::
      The default value must not be used since 2001:db8::/32 is a documentation-only prefix.

Save. Tayga should now be running.

---------------------
Adding firewall rules
---------------------
Tayga uses a tunnel interface for packet exchange with the system. Rules are required to prevent the firewall from blocking these packets.
Additionally, an outbound NAT rule is required for IPv4 Internet access.

Go to :menuselection:`Firewall --> Rules --> Tayga`, add a new rule, set the `TCP/IP Version` to `IPv4+IPv6`, leave all other settings to
their default values and save.

.. Note::
   If you just enabled Tayga and can't find :menuselection:`Firewall --> Rules --> Tayga`, go to :menuselection:`Interfaces --> Assignments`,
   click `Save` and reload the page.

Go to :menuselection:`Firewall --> Settings --> Normalization`, add a new rule, set the `Interface` to `Tayga`, leave all other settings to
their default values and save.

.. Note::
   This rule is required for proper handling of fragmented packets.

Go to :menuselection:`Firewall --> NAT --> Outbound`, add a new rule, set `Source address` to `Single host or network`, enter your Tayga
`IPv4 Pool`, leave all other settings to their default values and save.

Apply the firewall changes. NAT64 should now be fully operational.

-----------------
Configuring DNS64
-----------------
In most scenarios, NAT64 also requires DNS64. If you use OPNsense's :doc:`/manual/unbound` DNS resolver, DNS64 can be enabled by going to
:menuselection:`Services --> Unbound DNS --> General` and ticking `Enable DNS64 Support`. If you don't use the default 64:ff9b::/96 prefix,
you also have to enter your /96 prefix there.

.. Note::
   You may also use any other DNS64 capable DNS server. If you use the default 64:ff9b::/96 prefix, using a service like `Google's Public
   DNS64 <https://developers.google.com/speed/public-dns/docs/dns64>` is possible, too.

-------
Testing
-------
You can use a service like https://internet.nl/connection/ to verify that devices in your IPv6-only LAN have IPv6 and IP4 Internet access.
