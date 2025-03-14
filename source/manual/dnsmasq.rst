==================
Dnsmasq DNS & DHCP
==================

`DNSmasq` is a lightweight and easy to configure DNS forwarder and DHCP server.

It is considered the replacement for `ISC-DHCP` in small and medium sized setups,
and synergizes well with `Unbound DNS`, our standard enabled forward/resolver service.

---------------------------------
Considerations before deployment
---------------------------------

DNS Service
-----------------------------

Combining `DNSmasq` with `Unbound` can enable synergies, such as DHCP leases that have their hostnames registered in `DNSmasq` to be queried by `Unbound`.

Since `DNSmasq` does not restart on configuration changes and does not need custom scripts to register DNS, it is very resilient and easy to manage.

.. Note::

    `Unbound` is a recursive resolver, `DNSmasq` a non-resursive forwarding DNS server. This means `DNSmasq` always
    needs a recursive DNS resolver it can forward its queries to. This can be `Unbound`, or another DNS Service on the internet.


In the configuration examples further below, we will always combine `Unbound` with `DNSmasq`.

DHCP Service
-----------------------------

`DNSmasq` is the perfect DHCP server for small and medium sized setups. The configuration is straight forward, and since it can register the DNS names of leases,
it can replicate the simplicity known from consumer routers.

If HA for DHCP is a requirement, split pools can be configured for two `DNSmasq` instances. With a dhcp reply delay, the secondary instance will only answer when
the first instance is unresponsive.

For larger enterprise setups, `KEA DHCP` can be a viable alternative. It supports lease synchronisation via REST API, which means both DHCP servers keep track
of all existing leases and do not need split pools. It is also far more scalable if there are thousands of leases.

The tradeoff using `KEA DHCP` is a more complicated setup, especially when custom DHCP options are needed. DNS registration is also not possible.

With this in mind, pick the right choice for your setup. When in doubt, using `DNSmasq` can be the best choice.

-------------------------
General Settings
-------------------------

Most settings are pretty straightforward here when the service is enabled, it should just start forwarding dns requests
when received from the network. DHCP requires at least one dhcp-range and matching dhcp-options.

.. tabs::

    .. tab:: General

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Enable**                                Enable Dnsmasq.
        **Interface**                             Interface IPs used to responding to queries from clients. If an interface has both IPv4
                                                  and IPv6 IPs, both are used. Queries to other interface IPs not selected below are
                                                  discarded. The default behavior is to respond to queries on every available IPv4 and
                                                  IPv6 address.
        **Strict Interface Binding**              By default we bind the wildcard address, even when listening on some interfaces.
                                                  Requests that shouldn't be handled are discarded, this has the advantage of working
                                                  even when interfaces come and go and change address. This option forces binding to
                                                  only the interfaces we are listening on, which is less stable in non-static environments.
        ========================================= ====================================================================================

        .. Attention::

            When DHCP is used, select the interfaces that serve DHCP ranges to register automatic firewall rules for them.

    .. tab:: DNS

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Listen Port**                           The port used for responding to DNS queries. It should normally be left blank unless
                                                  another service needs to bind to TCP/UDP port 53. Setting this to zero (0) completely
                                                  disables DNS function.
        **DNSSEC**
        **No Hosts Lookup**                       Do not read hostnames in /etc/hosts.
        **Log the results of DNS queries**
        **Maximum concurrent queries**            Set the maximum number of concurrent DNS queries. On configurations with tight
                                                  resources, this value may need to be reduced.
        **Cache size**                            Set the size of the cache. Setting the cache size to zero disables caching. Please
                                                  note that huge cache size impacts performance.
        **Local DNS entry TTL**                   This option allows a time-to-live (in seconds) to be given for local DNS entries,
                                                  i.e. /etc/hosts or DHCP leases. This will reduce the load on the server at the
                                                  expense of clients using stale data under some circumstances. A value of zero will
                                                  disable client-side caching.
        **No ident**                              Do not respond to class CHAOS and type TXT in domain bind queries. Without this option
                                                  being set, the cache statistics are also available in the DNS as answers to queries of
                                                  class CHAOS and type TXT in domain bind.
        ========================================= ====================================================================================

    .. tab:: DNS Query Forwarding

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Query DNS servers sequentially**        If this option is set, we will query the DNS servers sequentially in the order specified
                                                  (System: General Setup: DNS Servers), rather than all at once in parallel.
        **Require domain**                        If this option is set, we will not forward A or AAAA queries for plain names, without
                                                  dots or domain parts, to upstream name servers. If the name is not known from /etc/hosts
                                                  or DHCP then a "not found" answer is returned.
        **Do not forward private reverse**        If this option is set, we will not forward reverse DNS lookups (PTR) for private
        **lookups**
                                                  addresses (RFC 1918) to upstream name servers. Any entries in the Domain Overrides
                                                  section forwarding private "n.n.n.in-addr.arpa" names to a specific server are still
                                                  forwarded. If the IP to name is not known from /etc/hosts, DHCP or a specific domain
                                                  override then a "not found" answer is immediately returned.
        ========================================= ====================================================================================

    .. tab:: DHCP

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Interface [no dhcp]**                   Do not provide DHCP, TFTP or router advertisement on the specified interfaces, but do
                                                  provide DNS service.
        **DHCP fqdn**                             In the default mode, we insert the unqualified names of DHCP clients into the DNS, in
                                                  which case they have to be unique. Using this option the unqualified name is no longer
                                                  put in the DNS, only the qualified name.
        **DHCP default domain**                   To ensure that all names have a domain part, there must be a default domain specified
                                                  when dhcp-fqdn is set. Leave empty to use the system domain.
        **DHCP max leases**                       Limits dnsmasq to the specified maximum number of DHCP leases. This limit is to prevent
                                                  DoS attacks from hosts which create thousands of leases and use lots of memory in the
                                                  dnsmasq process.
        **DHCP authoritative**                    Should be set when dnsmasq is definitely the only DHCP server on a network. For DHCPv4,
                                                  it changes the behaviour from strict RFC compliance so that DHCP requests on unknown
                                                  leases from unknown hosts are not ignored.
        **DHCP Reply delay**                      Delays sending DHCPOFFER and PROXYDHCP replies for at least the specified number of
                                                  seconds. This can be practical for split DHCP solutions, to make sure the secondary
                                                  server answers slower than the primary.
        **DHCP register firewall rules**          Automatically register firewall rules to allow DHCP traffic for all explicitly selected
                                                  interfaces, can be disabled for more fine-grained control if needed. Changes are only
                                                  effective after a firewall service restart (see system diagnostics).
        **Disable HA sync**                       Ignore the DHCP general settings from being updated using HA sync.
        ========================================= ====================================================================================

    .. tab:: ISC / KEA DHCP (legacy)

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Register ISC DHCP4 Leases**             If this option is set, then machines that specify their hostname when requesting a
                                                  DHCP lease will be registered, so that their name can be resolved.
        **DHCP Domain Override**                  The domain name to use for DHCP hostname registration. If empty, the default system
                                                  domain is used. Note that all DHCP leases will be assigned to the same domain. If this
                                                  is undesired, static DHCP lease registration is able to provide coherent mappings.
        **Register DHCP Static Mappings**         If this option is set, then DHCP static mappings will be registered, so that their name
                                                  can be resolved.
        **Prefer DHCP**                           If this option is set, then DHCP mappings will be resolved before the manual list of
                                                  names below. This only affects the name given for a reverse lookup (PTR).
        ========================================= ====================================================================================


-------------------------
DNS Settings
-------------------------

.. tabs::

    .. tab:: Hosts

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Host**                                  Name of the host, without the domain part. Use "*" to create a wildcard entry.
        **Domain**                                Domain of the host, e.g. example.com
        **IP address**                            IP address of the host, e.g. 192.168.100.100 or fd00:abcd::1
        **Aliases**                               List of aliases (FQDN)
        **Hardware address**                      When offered and the client requests an address via DHCP, assign the address provided here.
        **Tag [set]**                             Optional tag to set for requests matching this range which can be used to selectively match DHCP options.
        **Description**                           You may enter a description here for your reference (not parsed).
        **Comments**                              You may enter a description here for your reference (not parsed).
        ========================================= ====================================================================================

    .. tab:: Domains

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Sequence**                              Sort with a sequence number, e.g., for strict processing order when using the "strict-order" option.
        **Domain**                                Domain to override (NOTE: this does not have to be a valid TLD!).
        **IP address**                            IP address of the authoritative DNS server for this domain, leave empty to prevent lookups for this domain.
        **Port**                                  Specify a non-standard port number here, leave blank for default.
        **Source IP**                             Source IP address for queries to the DNS server for the override domain. Best to leave empty.
        **Description**                           You may enter a description here for your reference (not parsed).
        ========================================= ====================================================================================


-------------------------
DHCP Settings
-------------------------

.. tabs::

    .. tab:: DHCP ranges

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Interface**                             Interface to serve this range.
        **Tag [set]**                             Optional tag to set for requests matching this range which can be used to selectively match DHCP options.
        **Start address**                         Start of the range, e.g. 192.168.1.100, 2000::1 or when constructor is used a partial like ::1.
        **End address**                           End of the range.
        **Constructor**                           Interface to use to calculate the proper range, when selected, a range may be specified as partial (e.g. ::1, ::400).
        **Prefix length (IPv6)**                  Prefix length offered to the client.
        **Mode**                                  Mode flags to set for this range, 'static' means no addresses will be automatically assigned.
        **Lease time**                            Defines how long the addresses (leases) given out by the server are valid (in seconds).
        **Domain**                                Offer the specified domain to machines in this range.
        **Disable HA sync**                       Ignore this range from being transferred or updated by HA sync.
        **Description**                           You may enter a description here for your reference (not parsed).
        ========================================= ====================================================================================

    .. tab:: DHCP options

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Option**                                Option to offer to the client.
        **Interface**                             This adds a single interface as a tag so this DHCP option can match the interface of a DHCP range.
        **Tag**                                   If the optional tags are given, then this option is only sent when all the tags are matched.
                                                  Can be optionally combined with an interface tag.
        **Value**                                 Value (or values) to send to the client.
                                                  The special address 0.0.0.0 is taken to mean "the address of the machine running dnsmasq".
        **Force**                                 Always send the option, even when the client does not ask for it in the parameter request list.
        **Description**                           You may enter a description here for your reference (not parsed).
        ========================================= ====================================================================================


    .. tab:: DHCP tags

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Tag**                                   An alphanumeric label which marks a network so that DHCP options may be specified on a per-network basis.
        ========================================= ====================================================================================

        .. Note::

            Interfaces set tags automatically, you do not need to set tags for them. Just select the interface in a DHCP range or DHCP option
            for the match to happen.


    .. tab:: DHCP options / match

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Option**                                 Option to offer to the client.
        **Tag [set]**                              Tag to set for requests matching this range which can be used to selectively match DHCP options.
        **Value**                                  Value to match, leave empty to match on the option only.
        **Description**                            You may enter a description here for your reference (not parsed).
        ========================================= ====================================================================================


-------------------------
Advanced settings
-------------------------

To configure options that are not available in the gui one can add custom configuration files on the firewall itself.
Files can be added in :code:`/usr/local/etc/dnsmasq.conf.d/`, these should use as extension .conf (e.g. custom-options.conf).
When more files are placed inside the directory, all will be included in alphabetical order.

.. Warning::
    It is the sole responsibility of the administrator which places a file in the extension directory to ensure that the configuration is
    valid.

.. Note::
    This method replaces the ``Custom options`` settings in the Dnsmasq configuration, which was removed in version 21.1.


The DHCP service in `Unbound` uses tags to determine which DHCP ranges and DHCP options to send.

Each interface sets a tag automatically when a DHCP broadcast is received. Choosing an interface in a DHCP range and DHCP option matches this tag.


---------------------------------
Configuration examples
---------------------------------


Combining `DNSmasq DNS` and `Unbound DNS``
------------------------------------------



Register hostnames of DHCP leases
------------------------------------------



Understanding DHCP tags
------------------------------------------



DHCP for simple networks
------------------------------------------



DHCP for small and medium sized HA setups
------------------------------------------
