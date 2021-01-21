==============
Dnsmasq DNS
==============

Dnsmasq is a lightweight, easy to configure, DNS forwarder, which can be used to answer to dns queries
from your network.

Similar functionality is also provided by "Unbound DNS", our standard enabled forward/resolver service.

In some cases people prefer to use dnsmasq or combine it with our default enabled resolver (Unbound).

.. Note::

    Since OPNsense 17.7 Unbound has been our standard DNS service, the main reason for Dnsmasq being shipped
    in our product is for compatibility. Although there are some use-cases that require Dnsmasq specifically,
    most users better opt for Unbound.


-------------------------
General settings
-------------------------

Most settings are pretty straightforward here when the service is enabled, it should just start forwarding dns requests
when received from the network.

===========================================================================================================================

========================================  =================================================================================
Enable                                    Enable our DNS Forwarder
Listen Port                               The port used for responding to DNS queries, when empty the standard (53) will
                                          be used.
Network Interfaces                        The interfaces to listen on, when using dynamic interfaces it's not recommended
                                          to bind to addresses from these interfaces. [All] is the standard, in which
                                          case you can limit access using the firewall.
Bind Mode / strict binding                When network interfaces are provided, only bind to the interfaces containing
                                          the IP addresses selected above, rather than binding to all interfaces and
                                          discarding queries to other addresses.
                                          This option does not work with IPv6. If set, Dnsmasq will not
                                          bind to IPv6 addresses.
DNSSEC                                    Validate DNS replies and cache DNSSEC data.
DHCP Registration                         Register dhcp leases in Dnsmasq, so that their hostnames can be resolved.
                                          (IPv4 only)
DHCP Domain Override                      When set use the domain name specified here instead of the system domain
                                          for registering addresses.
Static DHCP                               Register static dhcp addresses as well.
Query DNS servers sequentially            If this option is set, Dnsmasq will query the DNS servers sequentially in the
                                          order specified (System: General Setup: DNS Servers),
                                          rather than all at once in parallel.
Require domain                            If this option is set, Dnsmasq will not forward A or AAAA queries for
                                          plain names, without dots or domain parts, to upstream name servers.
                                          If the name is not known from /etc/hosts or DHCP then a "not found" answer
                                          is returned.
Do not forward private reverse lookups    If this option is set, Dnsmasq will not forward reverse DNS lookups (PTR)
                                          for private addresses (RFC 1918) to upstream name servers.
                                          Any entries in the Domain Overrides section forwarding
                                          private "n.n.n.in-addr.arpa" names to a specific server are still forwarded.
                                          If the IP to name is not known from /etc/hosts, DHCP or a specific
                                          domain override then a "not found" answer is immediately returned.
Log Queries                               Send the results of dns queries to the log.
========================================  =================================================================================




-------------------------
Host overrides
-------------------------

Here you define static hostnames, which allow you to reply a specific address when being asked, per entry the following options
are available.

============================================================================================================================

========================================  ==================================================================================
Host                                      The hostname to register
Domain                                    The domain name to use
IP address                                IP address of the host, can be an IPv4 (A record) or an IPv6 address (AAAA record)
Description                               Descriptive text for this host
Aliases                                   Register alternative host + domain names for the same IP address
========================================  ==================================================================================


-------------------------
Domain Overrides
-------------------------

If a specific domain should be answered by a different DNS server, you can configure it here.

============================================================================================================================

========================================  ==================================================================================
Domain                                    The domain name to use
IP address                                IP address of the authoritative DNS server for this domain
Port                                      Port number of the target dns server, leave blank for default (53)
Source IP                                 Source IP address for queries to the DNS server for the override domain.
                                          Leave blank unless your DNS server is accessed through a VPN tunnel.
Description                               Descriptive text for this entry
========================================  ==================================================================================


-------------------------
Advanced settings
-------------------------

To configure options that are not available in the gui one can add custom configuration files on the firewall itself.
Files can be added in :code:`/usr/local/etc/dnsmasq.conf.d/`, these should use as extension .conf (e.g. custom-options.conf).
When more files are placed inside the directory, all will be included in alphabetical order.
