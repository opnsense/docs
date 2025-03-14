==================
Dnsmasq DNS & DHCP
==================

`DNSmasq` is a lightweight and easy to configure DNS forwarder and DHCP server.

It is considered the replacement for `ISC-DHCP` in small and medium sized setups,
and synergizes well with `Unbound DNS`, our standard enabled forward/resolver service.

Our system setup wizard configures `Unbound DNS` for DNS and `DNSmasq` for DHCP.

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


---------------------------------
Configuration examples
---------------------------------

.. Tip::

    Using DNSmasq for DHCP and DNS for internal device hostnames
    is the recommended default configuration for most setups.

DNS and DHCP for simple networks
------------------------------------------

DNSmasq can be used as a DNS forwarder. Though in our recommended setup, we will not use it as our default DNS server.

We will use Unbound as primary DNS server for our clients, and only forward some internal zones to DNSmasq which manages the hostnames of
DHCP registered leases.

This requires DNSmasq to run with a non-standard port other than 53.

- Go to :menuselection:`Services --> DNSmasq DNS & DHCP --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53053``
==================================  =======================================================================================================

- Press **Apply**

Afterwards we can configure Unbound to forward the zones to DNSmasq.

- Go to :menuselection:`Services --> Unbound DNS --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53``
==================================  =======================================================================================================

- Press **Apply**

- Go to :menuselection:`Services --> Unbound DNS --> Query Forwarding` and create an entry for each DHCP range you plan to configure.

In our example, we use 3 DHCP ranges, so we will configure ``lan.internal`` and ``guest.internal``.

.. tabs::

    .. tab:: lan.internal

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Domain**                          ``lan.internal``
        **Server IP**                       ``127.0.0.1``
        **Server Port**                     ``53053``
        ==================================  =======================================================================================================

        - Press **Save** and add next

    .. tab:: guest.internal

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Domain**                          ``guest.internal``
        **Server IP**                       ``127.0.0.1``
        **Server Port**                     ``53053``
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**

.. Note::

    ``.internal`` is the IANA and ICANN approved TLD (Top Level Domain) for internal use. If you instead own a TLD, e.g., ``example.com``, you could create a zone
    thats not used on the internet, e.g., ``lan.internal.example.com``.

.. Attention::

    Using a FQDN (Full Qualified Domain Name) is required for this setup to work. You cannot use short names since they cannot be matched by query forwarding.
    If you instead want to resolve short names directly, using DNSmasq as primary DNS server for clients is the only choice.
    Though this comes with more restrictions, since the same short name cannot exist in two DHCP ranges at the same time.
    Using FQDNs is superior and prevents these issues.


Now that we have the DNS infrastructure set up, we can configure the DHCP ranges and DHCP options.

- Go to :menuselection:`Services --> DNSmasq DNS & DHCP --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Interface**                       ``LAN, GUEST`` (The network interfaces which will serve DHCP, this registers firewall rules)
**DHCP fqdn**                       ``X``
**DHCP default domain**             ``internal`` (or leave empty to use this system's domain)
**DHCP register firewall rules**    ``X``
==================================  =======================================================================================================

- Press **Apply**

.. Note::

    Ignore the ISC / KEA DHCP (legacy) options as our setup does not require them. We use the DNSmasq built in DHCP/DNS register functionality
    with Unbound DNS query forwarding.

As next step we define the DHCP ranges for our interfaces.

- Go to :menuselection:`Services --> DNSmasq DNS & DHCP --> DHCP ranges` and set:

.. tabs::

    .. tab:: LAN

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Interface**                       ``LAN``
        **Start address**                   ``192.168.1.100``
        **End address**                     ``192.168.1.199``
        **Domain**                          ``lan.internal``
        ==================================  =======================================================================================================

        - Press **Save** and add next

        .. Note::

            If a host receives a DHCP lease from this range, and it advertises a hostname, it will be registered under the chosen domain name.
            E.g., a host named ``nas01`` will become ``nas01.lan.internal``. This is the FQDN a client can query to receive the current
            IP address.

    .. tab:: GUEST

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Interface**                       ``GUEST``
        **Start address**                   ``192.168.10.100``
        **End address**                     ``192.168.10.199``
        **Domain**                          ``guest.internal``
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**

The final step is to set DHCP options for the ranges, at least router[3] and dns-server[6] should be announced.

- Go to :menuselection:`Services --> DNSmasq DNS & DHCP --> DHCP options` and set:

.. tabs::

    .. tab:: LAN

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Option**                          router[3]
        **Interface**                       ``LAN``
        **Value**                           ``192.168.1.1`` (the interface IP address of LAN, or a virtual IP of LAN)
        ==================================  =======================================================================================================

        - Press **Save** and add next

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Option**                          dns-server[6]
        **Interface**                       ``LAN``
        **Value**                           ``192.168.1.1`` (Unbound listens the interface IP address of LAN, or a virtual IP of LAN)
        ==================================  =======================================================================================================

        - Press **Save** and add next

        .. Note::

            Instead of setting the interface IP address as value, the special address 0.0.0.0 can be used to implicitely set it as `the server DNSmasq
            is running on`. Though in some scenarios that is not possible, e.g., when using a virtual IP addresses. So for consistency, this guide suggests
            setting each IP address explicitely to avoid confusion.

    .. tab:: Guest

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Option**                          router[3]
        **Interface**                       ``GUEST``
        **Value**                           ``192.168.10.1`` (the interface IP address of GUEST, or a virtual IP of GUEST)
        ==================================  =======================================================================================================

        - Press **Save** and add next

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Option**                          dns-server[6]
        **Interface**                       ``GUEST``
        **Value**                           ``192.168.10.1`` (Unbound listens the interface IP address of GUEST, or a virtual IP of GUEST)
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**


.. Attention::

    If DNSmasq does not start, check that ISC-DHCP and KEA DHCP are not active since they will block the bindable ports this DHCP server requires.


Verifying the setup
------------------------------------------

Now that the setup is complete, the following will happen in regards of DHCP and DNS.

1.  A new device (e.g. a smartphone) joins the LAN network and sends a DHCP Discover broadcast.
2.  DNSmasq receives this broadcast on port 67 and responds with a DHCP offer, containing an available IP address and DHCP options for router[3] and dns-server[6].
3.  The device sends a DHCP request to request the available IP address, and possibly send its own hostname.
4.  DNSmasq acknowledges the request.

Our smartphone now has the following IP configuration:

- IP address: ``192.168.1.100``
- Default Gateway: ``192.168.1.1``
- DNS Server: ``192.168.1.1``

At the same time, DNSmasq registers the DNS hostname of the smartphone (if it exists). Since we configured the FQDN option and domain in the DHCP range, the name of the
smartphone will be: ``smartphone.lan.internal``.

When a client queries `Unbound` for exactly ``smartphone.lan.internal``, the configured query forwarding sends the request to the DNS server responsible for ``lan.internal``
which is our configured `DNSmasq` listening on ``127.0.0.1:53053``. ``DNSmasq`` responds to this query and will resolve the current A-Record of ``smartphone.lan.internal`` to
``192.168.1.100``, sending this information to `Unbound` which in return sends the response back to the client that initially queried.

As you can see, this is a highly integrated and simple setup which leverages just the available DHCP and DNS standards with no trickery involved.


DHCP for small and medium sized HA setups
------------------------------------------
