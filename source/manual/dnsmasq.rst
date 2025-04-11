==================
Dnsmasq DNS & DHCP
==================

.. contents:: Index


`Dnsmasq` is a lightweight and easy to configure DNS forwarder and DHCPv4/DHCPv6 server.

It is considered the replacement for `ISC-DHCP` in small and medium sized setups
and synergizes well with `Unbound DNS`, our standard enabled forward/resolver service.

Our system setup wizard configures `Unbound DNS` for DNS and `Dnsmasq` for DHCP.

---------------------------------
Considerations before deployment
---------------------------------

DNS Service
-----------------------------

`Dnsmasq` can be combined with `Unbound` to act as a "connector", in which case  DHCP leases which have their hostnames registered in `Dnsmasq` may be queried directly by `Unbound`.

Since `Dnsmasq` does not restart on configuration changes and does not need custom scripts to register DNS, it is very resilient and easy to manage.

.. Note::

    `Unbound` is a recursive resolver, `Dnsmasq` a non-resursive forwarding DNS server. This means `Dnsmasq` always
    needs a recursive DNS resolver it can forward its queries to. This can be `Unbound`, or another DNS Service on the internet.


In the configuration examples further below, we will always combine `Unbound` with `Dnsmasq`.

DHCP Service
-----------------------------

`Dnsmasq` is the perfect DHCP server for small and medium sized setups. The configuration is straight forward, and since it can register the DNS names of leases,
it can replicate the simplicity known from consumer routers.

If HA for DHCP is a requirement, split pools can be configured for two `Dnsmasq` instances. With a dhcp reply delay, the secondary instance will only answer when
the first instance is unresponsive. DHCPv6 and Router Advertisements are also an option for small HA setups that do not have fast failover requirements,
as IPv6 failover can take up to 30 seconds with available configuration options.

For larger enterprise setups, `KEA DHCP` can be a viable alternative. It supports lease synchronisation via REST API, which means both DHCP servers keep track
of all existing leases and do not need split pools. It is also far more scalable if there are thousands of leases.

The tradeoff using `KEA DHCP` is a more complicated setup, especially when custom DHCP options are needed. DNS registration is also not possible.

With this in mind, pick the right choice for your setup. When in doubt, our advise is to use `Dnsmasq` .

.. Attention::

    There is DHCPv6 and Router Advertisement support. Keep in mind that just as with DHCPv4/DHCPv6 servers, there should not be multiple Router Advertisement servers
    running on the same system. Right now, :menuselection:`Services --> Router Advertisements` is the default RA daemon. If you are unsure, do not enable them in Dnsmasq.

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
        **Add MAC**                               Add the MAC address of the requestor to DNS queries which are forwarded upstream.
                                                  The MAC address will only be added if the upstream DNS Server is in the same subnet
                                                  as the requestor. Since this is not standardized, it should be considered experiemental.
                                                  This is useful for selective DNS filtering on the upstream DNS server.
        **Add subnet**                            Add the real client IPv4 and IPv6 addresses (add-subnet=32,128) to DNS queries which are
                                                  forwarded upstream. Be careful setting this option as it can undermine privacy. This is
                                                  useful for selective DNS filtering on the upstream DNS server.
        **Strip subnet**                          Strip the subnet received by a downstream DNS server. If add_subnet is used and the
                                                  downstream DNS server already added a subnet, DNSMasq will not replace it without
                                                  setting strip_subnet.
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
        **Router Advertisements**                 Setting this will enable Router Advertisements for all configured DHCPv6 ranges with
                                                  the managed address bits set, and the use SLAAC bit reset. To change this default, select
                                                  a combination of the possible options in the individual DHCPv6 ranges.
                                                  Keep in mind that this is a global option; if there are configured DHCPv6 ranges,
                                                  RAs will be sent unconditionally and cannot be deactivated selectively.
                                                  Setting Router Advertisement modes in DHCPv6 ranges will have no effect without
                                                  this global option enabled.
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

    .. tab:: Hosts (Host Overrides)

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Host**                                  Name of the host, without the domain part. Use "*" to create a wildcard entry.
        **Domain**                                Domain of the host, e.g. example.com
        **IP addresses**                          IP addresses of the host, e.g. 192.168.100.100 or fd00:abcd::1. Can be multiple IPv4
                                                  and IPv6 addresses for dual stack configurations. Setting multiple addresses will automatically
                                                  assign the best match based on the subnet of the interface receiving the DHCP Discover.
        **Aliases**                               List of aliases (FQDN)
        **Client identifier**                     Match the identifier of the client, e.g., DUID for DHCPv6.
                                                  Setting the special character "*" will ignore the client identifier for DHCPv4 leases if a client offers both as choice.
        **Hardware addresses**                    Match the hardware address of the client. Can be multiple addresses, e.g., if the client has
                                                  multiple network cards. Though keep in mind that Dnsmasq cannot assume which address is the correct
                                                  one when multiple send DHCP Discover at the same time.
        **Lease time**                            Defines how long the addresses (leases) given out by the server are valid (in seconds)
        **Tag [set]**                             Optional tag to set for requests matching this range which can be used to selectively match DHCP options.
        **Ignore**                                Ignore any DHCP packets of this host. Useful if it should get served by a different DHCP server.
        **Description**                           You may enter a description here for your reference (not parsed).
        **Comments**                              You may enter a description here for your reference (not parsed).
        ========================================= ====================================================================================

        .. Note::

            When a domain and IP addresses are set, a host override will be created. If a client identifier or hardware addresses are set,
            an additional static DHCP reservation will be created.

    .. tab:: Domains (Domain Overrides)

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

        .. Note::

            Selecting `Query DNS servers sequentially` in :menuselection:`Services --> Dnsmasq DNS & DHCP --> General` will enforce a strict-order.
            For the processing order to work, overrides must be configured exactly the same, e.g., matching same domain and port. IP address can be different.


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
        **Start address**                         Start of the range, e.g. 192.168.1.100 for DHCPv4, 2000::1 for DHCPv6 or when a constructor
                                                  is using a suffix like ::1. To reveal IPv6 related options, enter a IPv6 address.
                                                  When using router advertisements, it is possible to use a constructor with :: as the start
                                                  address and no end address.
        **End address**                           End of the range.
        **Constructor**                           Interface to use to calculate the proper range, when selected, a range may be specified as partial (e.g. ::1, ::400).
        **Prefix length (IPv6)**                  Prefix length offered to the client. Custom values in this field will be ignored if
                                                  Router Advertisements are enabled, as SLAAC will only work with a prefix length of 64.
        **RA Mode**                               Control how IPv6 clients receive their addresses. Enabling Router Advertisements in general settings
                                                  will enable it for all configured DHCPv6 ranges with the managed address bits set, and the use SLAAC
                                                  bit reset. To change this default, select a combination of the possible options here.
                                                  "slaac", "ra-stateless" and "ra-names" can be freely combined, all other options
                                                  shall remain single selections.
        **RA Priority**                           Priority of the RA announcements.
        **RA MTU**                                Optional MTU to send to clients via Router Advertisements. If unsure leave empty.
        **RA Interval**                           Time (seconds) between Router Advertisements.
        **RA Router Lifetime**                    The lifetime of the route may be changed or set to zero, which allows a router to advertise prefixes
                                                  but not a route via itself. When using HA, setting a short timespan here is adviced for faster IPv6
                                                  failover. A good combination could be 10 seconds RA interval and 30 seconds RA router lifetime.
                                                  Going lower than that can pose issues in busy networks.
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
        **Type**                                  "Set" option to send it to a client in a DHCP offer or
                                                  "Match" option to dynamically tag clients that send it in the initial DHCP request.
        **Option**                                DHCPv4 option to offer to the client.
        **Option6**                               DHCPv6 option to offer to the client.
        **Interface**                             This adds a single interface as a tag so this DHCP option can match the interface of a DHCP range.
        **Tag**                                   If the optional tags are given, then this option is only sent when all the tags are matched.
                                                  Can be optionally combined with an interface tag.
                                                  The special address 0.0.0.0 or [::] is taken to mean "the address of the machine running dnsmasq".
                                                  When using "Match", leave empty to match on the option only.
        **Tag [set]**                             Tag to set for requests matching this range which can be used to selectively match dhcp options.
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


DHCPv4 with DNS registration
--------------------------------------------------

Dnsmasq can be used as a DNS forwarder. Though in our recommended setup, we will not use it as our default DNS server.

We will use Unbound as primary DNS server for our clients, and only forward some internal zones to Dnsmasq which manages the hostnames of
DHCP registered leases.

This requires Dnsmasq to run with a non-standard port other than 53.

- Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53053``
==================================  =======================================================================================================

- Press **Apply**

Afterwards we can configure Unbound to forward the zones to Dnsmasq.

- Go to :menuselection:`Services --> Unbound DNS --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53``
==================================  =======================================================================================================

- Press **Apply**

- Go to :menuselection:`Services --> Unbound DNS --> Query Forwarding` and create an entry for each DHCP range you plan to configure.

In our example, we use 2 DHCP ranges, so we will configure ``lan.internal`` and ``guest.internal``.

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


Now that we have the DNS infrastructure set up, we can configure the DHCP ranges and DHCP options.

- Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> General` and set:

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

    Ignore the ISC / KEA DHCP (legacy) options as our setup does not require them. We use the Dnsmasq built in DHCP/DNS register functionality
    with Unbound DNS query forwarding.

As next step we define the DHCP ranges for our interfaces.

- Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP ranges` and set:

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

- Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP options` and set:

.. tabs::

    .. tab:: LAN

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Type**                            Set
        **Option**                          router[3]
        **Interface**                       ``LAN``
        **Value**                           ``192.168.1.1`` (the interface IP address of LAN, or a virtual IP of LAN)
        ==================================  =======================================================================================================

        - Press **Save** and add next

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Type**                            Set
        **Option**                          dns-server[6]
        **Interface**                       ``LAN``
        **Value**                           ``192.168.1.1`` (Unbound listens the interface IP address of LAN, or a virtual IP of LAN)
        ==================================  =======================================================================================================

        - Press **Save** and add next

        .. Note::

            Instead of setting the interface IP address as value, the special address 0.0.0.0 can be used to implicitely set it as `the server Dnsmasq
            is running on`. Though in some scenarios that is not possible, e.g., when using a virtual IP addresses. So for consistency, this guide suggests
            setting each IP address explicitely to avoid confusion.

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Type**                            Set
        **Option**                          domain-search [119]
        **Interface**                       ``LAN``
        **Value**                           ``lan.internal``
        ==================================  =======================================================================================================

        .. Tip::

            Using a FQDN (Full Qualified Domain Name) is required for this setup to work (e.g., ``smartphone.lan.internal``)
            If you want to resolve short names inside a DHCP range (e.g., ``smartphone`` without ``.lan.internal``), add the
            ``domain-search [119]`` DHCP option to all ranges.

        - Press **Save** and add next

    .. tab:: Guest

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Type**                            Set
        **Option**                          router[3]
        **Interface**                       ``GUEST``
        **Value**                           ``192.168.10.1`` (the interface IP address of GUEST, or a virtual IP of GUEST)
        ==================================  =======================================================================================================

        - Press **Save** and add next

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Type**                            Set
        **Option**                          dns-server[6]
        **Interface**                       ``GUEST``
        **Value**                           ``192.168.10.1`` (Unbound listens the interface IP address of GUEST, or a virtual IP of GUEST)
        ==================================  =======================================================================================================

        - Press **Save** and add next

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Type**                            Set
        **Option**                          domain-search [119]
        **Interface**                       ``GUEST``
        **Value**                           ``guest.internal``
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**


.. Attention::

    If Dnsmasq does not start, check that ISC-DHCP and KEA DHCP are not active since they will block the bindable ports this DHCP server requires.
    It is also a good idea to check :menuselection:`Services --> Dnsmasq DNS & DHCP --> Log` for the error message.

Now that the setup is complete, the following will happen in regards of DHCP and DNS.

1.  A new device (e.g. a smartphone) joins the LAN network and sends a DHCP Discover broadcast.
2.  Dnsmasq receives this broadcast on port 67 and responds with a DHCP offer, containing an available IP address and DHCP options for router[3] and dns-server[6].
3.  The device sends a DHCP request to request the available IP address, and possibly send its own hostname.
4.  Dnsmasq acknowledges the request.

Our smartphone now has the following IP configuration:

- IP address: ``192.168.1.100``
- Default Gateway: ``192.168.1.1``
- DNS Server: ``192.168.1.1``

At the same time, Dnsmasq registers the DNS hostname of the smartphone (if it exists). Since we configured the FQDN option and domain in the DHCP range, the name of the
smartphone will be: ``smartphone.lan.internal``.

When a client queries `Unbound` for exactly ``smartphone.lan.internal``, the configured query forwarding sends the request to the DNS server responsible for ``lan.internal``
which is our configured `Dnsmasq` listening on ``127.0.0.1:53053``. ``Dnsmasq`` responds to this query and will resolve the current A-Record of ``smartphone.lan.internal`` to
``192.168.1.100``, sending this information to `Unbound` which in return sends the response back to the client that initially queried.

As you can see, this is a highly integrated and simple setup which leverages just the available DHCP and DNS standards with no trickery involved.


DHCPv6 and Router Advertisements
------------------------------------------------------

DHCPv6 can run at the same time as DHCPv4. Essentially, create another range for DHCPv6 for the same interface as the DHCPv6 variant.

.. Attention::

    DHCPv6 does not have a router option like DHCPv4. To push the default gateway to clients you must use Router Advertisements.
    This can be done with Dnsmasq, but also by a different service like :menuselection:`Services --> Router Advertisements`.

In this example, we add a DHCPv6 range and Router Advertisements to our LAN interface. The following configuration sets stateless
DHCPv6 and SLAAC. This means clients will use a SLAAC address but query additional DHCPv6 options, e.g. DNS Server.

- Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP ranges` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Interface**                       ``LAN``
**Start address**                   ``::``
**Constructor**                     ``LAN``
**RA Mode**                         ``ra-stateless``
==================================  =======================================================================================================

.. Attention::

    With ``ra-stateless``, clients will only generate a SLAAC address. If clients should additionally receive a DHCPv6 address, set ``slaac``
    instead.

.. Tip::

    Set ``ra-names`` in addition to ``ra-stateless`` if DNS names should be registered automatically for SLAAC addresses. Please note that this
    does not work for clients using the IPv6 privacy extensions.

.. Note::

    If do not want to use Router Advertisements, leave the RA Mode on default, and do not enable the Router Advertisement global setting. Ensure
    that the RA service you use allows for an assisted setup with SLAAC and DHCPv6.

- Press **Save** and go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP options`

We now add an additional DHCPv6 option for the DNS Server.

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Type**                            Set
**Option**                          ``None``
**Option6**                         ``dns-server [23]``
**Interface**                       ``LAN``
**Value**                           ``[::]``
==================================  =======================================================================================================

.. Note::

    When entering DHCPv6 options, enclosing them in brackets ``[]`` is mandatory. ``[::]`` is a special address and will return the GUA of
    this server Dnsmasq is running on.

Press **Save**

As final step, go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> General`

Enable the checkbox ``Router Advertisements`` if you want to use them.

Press **Apply** to activate the new configuration.


DHCP reservations
------------------------------------------

A DHCP reservation will always assign the same IPv4 and IPv6 addresses to a client.

For an IPv4 reservation, a DHCPv4 range should exist. If this DHCPv4 range should only serve reservations, set it to static.

For an IPv6 reservation, a DHCPv6 range must be configured which sets ``slaac`` as Router Advertisement option.
This sets the `A bit` so that clients can generate a SLAAC address and receive an additional DHCPv6 lease.
If a different Router Advertisement daemon is used, ensure it runs in `Assisted` mode.

.. Note::

    As all clients configure a tag with the receiving interface name automatically,
    DHCP options that are tagged with an interface will automatically match the reservations.

Here are a few examples for DHCP reservations. This assumes we already created ranges for ``LAN`` and ``GUEST`` as outlined in the previous sections.

Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> Hosts`

.. tabs::

    .. tab:: IPv4

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Host**                            ``smartphone``
        **IP addresses**                    ``192.168.1.150`` ``192.168.10.150``
        **Hardware addresses**              ``aa:bb:cc:dd:ee:ff``
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**

        .. Tip::

            Setting IP addresses for different DHCP ranges will ensure that when the client traverses between e.g., ``LAN`` and ``GUEST`` that it receives a static IP address in
            both ranges automatically.

    .. tab:: IPv6

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Host**                            ``smartphone``
        **IP addresses**                    ``::1234``
        **Client identifier**               ``00:03:00:01:aa:bb:cc:dd:ee:ff``
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**

        .. Attention::

            A Hardware address will not work for IPv6 reservations. It must be the device unique identifier (DUID). This example uses the common
            DUID-LL type.

        .. Tip::

            Setting a partial IPv6 address will ensure it uses the same constructor as the configured DHCPv6 ranges.

    .. tab:: IPv4 + IPv6 (dual stack)

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Host**                            ``smartphone``
        **IP addresses**                    ``192.168.1.150`` ``192.168.10.150`` ``::1234``
        **Client identifier**               ``00:03:00:01:aa:bb:cc:dd:ee:ff``
        **Hardware addresses**              ``aa:bb:cc:dd:ee:ff``
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**

        .. Tip::

            This combines both IPv4 and IPv6 reservations in the same configuration item.


DHCP tags
------------------------------------------

When a DHCP Discover enters a network interface, Dnsmasq will automatically set a tag with the interface name.

Additionally, tags can be set on DHCP requests by clients when they send the options they need.

There are two kinds of operations, `set` a tag and `match` a tag.

You can manually configure additional tags in :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP tags`.

- Setting these tags can be done in multiple spots, e.g., DHCP ranges, DHCP options / match, and Host Overrides.
- Matching one or multiple tags is mostly relevant in DHCP options.

As example, you could configure VoIP phones to receive a TFTP server option when they have a specific vendor id.

Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP tags`

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``voip``
==================================  =======================================================================================================

Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP options`

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Type**                            Match
**Option**                          ``vendor-class[60]``
**Tag [set]**                       ``voip``
**Value**                           The vendor ID string (e.g., ``SIPPhone``)
==================================  =======================================================================================================

Now a tag will be set if a DHCP request is sent by a VoIP phone that includes the vendor class option. If the vendor ID string matches,
Dnsmasq will look up any configuration that will match this tag. As next step we assign a TFTP server to this tag.

Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP options`

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Type**                            Set
**Option**                          ``tftp-server-address[150]``
**Tag [set]**                       ``voip``
**Value**                           IP address of your TFTP server
==================================  =======================================================================================================

This ensures that only clients identifying as VoIP phones receive the appropriate TFTP server information via option 150. You can add
additional options under the same tag if they should be offered to the VOIP phones.


DHCPv4 for small HA setups
------------------------------------------

In addition to the setup described above, Dnsmasq can be a viable option in a HA setup in small and medium sized network environments.

In contrast to KEA DHCP, it does not offer lease synchronization. Each Dnsmasq instance is a separate entity.

The main tricks to make this work are the following options:

- Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> General`:

Set this on the current master:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**DHCP reply delay**                Do not set a value here, we want the master to respond first.
**Disable HA sync**                 ``X``
==================================  =======================================================================================================

Set this on the current backup:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**DHCP reply delay**                ``10`` (10 seconds is a good starting point)
**Disable HA sync**                 ``X``
==================================  =======================================================================================================

.. Note::

    This means, each DHCP Discover will be answered by the master. If the master does not respond for 10 seconds, the backup server will respond.
    It's important to choose a high enough delay time, otherwise the behavior can be unpredictable in busy networks. The disabled HA sync ensures
    that the DHCP general settings are not synced between master and backup.

- Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP ranges`:

With LAN as example, set this on the current master:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Interface**                       ``LAN``
**Start address**                   ``192.168.1.100``
**End address**                     ``192.168.1.199``
**Disable HA sync**                 ``X``
==================================  =======================================================================================================

Set this on the current backup:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Interface**                       ``LAN``
**Start address**                   ``192.168.1.200``
**End address**                     ``192.168.1.220``
**Disable HA sync**                 ``X``
==================================  =======================================================================================================

.. Note::

    Now both master and backup have their own pool in the LAN network. The pool on master is larger, since it will respond to most DHCP discovers.
    If the master does not respond, the backup server will serve an IP address from its available pool. Since the pools do not overlap, there cannot
    be an IP address conflict between clients. The disabled HA sync ensures that these pools are not synchronized.

.. Tip::

    Reservations for single hosts created in :menuselection:`Services --> Dnsmasq DNS & DHCP --> Host Override` can still be synchronized. They count as their
    own single IP address pools outside of the defined DHCP ranges. This means both servers will serve the same IP address to a host when queried. There cannot
    be an IP address conflict in this case. Set the MAC address of the host in the Hardware address field.

With this setup, a simple and efficient HA setup with automatic DNS registration is possible. Yet for larger scalable setups with big IP address ranges in many VLANs,
KEA DHCP might be the better choice due to its robust HA synchronization options.


DHCPv6 and Router Advertisements for small HA setups
-----------------------------------------------------

Just as with DHCPv4, the same type of configuration can be done for DHCPv6 with a few minor adjustements.

Since IPv6 uses DAD (Duplicate Address Detection), you do not need to create separate pools. SLAAC and DAD will take care of avoiding duplicates.

Special care must be taken for the Router Advertisements. Since both master and backup will send them at the same time, the current default gateway
must be determined by priority and router lifetime.

- Go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> DHCP ranges`:

Set this on the current master:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Interface**                       ``LAN``
**Start address**                   ``::``
**Constructor**                     ``LAN``
**RA Mode**                         ``ra-stateless``
**RA Priority**                     ``High``
**RA Interval**                     ``10``
**RA Router Lifetime**              ``30``
**Disable HA sync**                 ``X``
==================================  =======================================================================================================

Set this on the current backup:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Interface**                       ``LAN``
**Start address**                   ``::``
**Constructor**                     ``LAN``
**RA Mode**                         ``ra-stateless``
**RA Priority**                     ``Normal``
**RA Interval**                     ``10``
**RA Router Lifetime**              ``30``
**Disable HA sync**                 ``X``
==================================  =======================================================================================================

As final step, go to :menuselection:`Services --> Dnsmasq DNS & DHCP --> General`

Enable the checkbox ``Router Advertisements`` on both master and backup and apply the configuration.

Both master and backup will now advertise their link local addresses as default gateway. As long as clients receive the RA priority ``high`` packets,
they prefer the master as the current IPv6 default gateway. When the master goes offline, the RA interval is sent every 10 seconds, yet after 30 seconds
the RA router lifetime will be reached and the master will be deprecated from the clients routing table. The backup will now be installed as new
IPv6 default route.

As soon as the master comes back online, the higher RA priority will make clients shift back eventually.

.. Note::

    This whole process is not seamless, it takes some time. At least as long as the dysfunct IPv6 route is not deprecated by the clients,
    IPv6 will still be routed to the non-existing link local address of the offline master.

.. Attention::

    Do not set the RA Interval and RA Router Lifetime too low, as clients could potentially loose their default routes in busy networks.
    The bare minimum for RA Router Lifetime should be (RA Interval*3).
