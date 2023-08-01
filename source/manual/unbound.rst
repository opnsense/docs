==============
Unbound DNS
==============

Unbound is a validating, recursive, caching DNS resolver. It is designed to be fast and lean and incorporates modern features based on open standards.

Since OPNsense 17.7 it has been our standard DNS service, which on a new install is enabled by default.

.. _general:

-------------------------
General settings
-------------------------

Below you will find the most relevant settings from the **General** menu section.

=====================================================================================================================

====================================  ===============================================================================
Enable                                Enable our DNS resolver
Listen Port                           Port to listen on, when blank, the default (53) is used.
Network Interfaces                    Interface IP addresses used for responding to queries from clients.
                                      If an interface has both IPv4 and IPv6 IPs, both are used.
                                      Queries to other interface IPs not selected are discarded.
                                      The default behavior is to respond to queries on every
                                      available IPv4 and IPv6 address.
DNSSEC                                Enable `DNSSEC <https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions>`__
                                      to use digital signatures to validate results from upstream servers and mitigate
                                      against `cache poisoning <https://en.wikipedia.org/wiki/DNS_spoofing>`__.
DNS64                                 Enable `DNS64 <https://en.wikipedia.org/wiki/IPv6_transition_mechanism#DNS64>`__
                                      so IPv6-only clients can reach IPv4-only servers. If enabled, Unbound synthesizes
                                      AAAA records for domains which only have A records. DNS64 requires NAT64 to be
                                      useful, e. g. the Tayga plugin or a third-party NAT64 service. The DNS64 prefix
                                      must match the IPv6 prefix used be the NAT64.
AAAA-only mode                        If this option is set, Unbound will remove all A records from the answer section
                                      of all responses.
DHCP Registration                     **IPv4 only** If this option is set, then machines that specify their hostname
                                      when requesting a DHCP lease will be registered in Unbound,
                                      so that their names can be resolved.

                                      The source of this data is **client-hostname** in the
                                      `dhcpd.leases <https://www.freebsd.org/cgi/man.cgi?query=dhcpd.leases>`__ file.
                                      This can also be inspected using the `Leases <dhcp.html#diagnostics>`__ page.
DHCP Domain Override                  When the above registrations shouldn't use the same domain name as configured
                                      on this firewall, you can specify a different one here.
DHCP Static Mappings                  Register static dhcpd entries so clients can resolve them. Supported on IPv4 and
                                      IPv6.
No IPv6 Link-local aaddresses         Do not register link local addresses for IPv6. This will prevent the return of
                                      unreachable addresses when more than one listen interface is configured.
System A/AAAA records                 If this option is set, then no A/AAAA records for the configured listen interfaces
                                      will be generated. This also means that no PTR records will be created. If desired,
                                      you can manually add A/AAAA records in :ref:`overrides`. Use this to control which
                                      interface IP addresses are mapped to the system host/domain name as well as to
                                      restrict the amount of information exposed in replies to queries for the
                                      system host/domain name.
TXT Comment Support                   Register descriptions as comments for dhcp static host entries.
Local Zone Type                       The local zone type used for the system domain.
                                      Type descriptions are available under "local-zone:" in the
                                      `unbound.conf(5) <https://nlnetlabs.nl/documentation/unbound/unbound.conf/>`__
                                      manual page. The default is 'transparent'.
====================================  ===============================================================================

.. Note::

    In order for the client to query unbound, there need to be an ACL assigned in
    :menuselection:`Services --> Unbound DNS --> Access Lists`. The configured interfaces should gain an ACL automatically.
    If the client address is not in any of the predefined networks, please add one manually.

.. _overrides:

-------------------------
Overrides
-------------------------

Within the overrides section you can create separate host definition entries and specify if queries for a specific
domain should be forwarded to a predefined server.

**Host override settings**
=====================================================================================================================

Host overrides can be used to change DNS results from client queries or to add custom DNS records. PTR records
are also generated under the hood to support reverse DNS lookups. These are generated in the following way:

* If **System A/AAAA records** in :ref:`general` is unchecked, a PTR record is created for the primary interface.
* Each host override entry **that does not include a wildcard for a host**, is assigned a PTR record.
* If a host override entry **includes a wildcard for a host**, the first defined alias is assigned a PTR record.
* Every other alias does not get a PTR record.

====================================  ===============================================================================
Host                                  Name of the host, without domain part. Use "*" to create a wildcard entry.
Domain                                Domain of the host (such as example.com)
Type                                  Record type, A or AAA (IPv4 or IPv6 address), MX to define a mail exchange
IP                                    Address of the host
Description                           User readable description, only for informational purposes
Aliases                               Copies of the above data for different hosts
====================================  ===============================================================================

**Aliases**

You may create alternative names for a Host. E.g. when having a webserver with several virtual hosts
you create a Host override entry with the IP and name for the webserver and an alias name for every virtual host on this webserver.

You have to select the host in the top list and it will the show you the assigned aliases in the bottom list.

**Domain override settings**
=====================================================================================================================

Domain overrides can be used to forward queries for specific domains (and subsequent subdomains) to local or remote DNS servers.

.. Important::

    Domain overrides has been superseded by :ref:`forwarding`. Query forwarding also allows you to forward every single
    request.

====================================  ===============================================================================
Domain                                Domain to override
IP address                            IP address of the authoritative DNS server for this domain
Description                           User readable description, only for informational purposes
====================================  ===============================================================================


-------------------------
Advanced
-------------------------

Although the default settings should be reasonable for most setups, some need more tuning or require specific options
set. Some of these settings are enabled and given a default value by Unbound,
refer to `unbound.conf(5) <https://nlnetlabs.nl/documentation/unbound/unbound.conf/>`__ for the defaults.

=====================================================================================================================

====================================  ===============================================================================
Hide Identity                         If enabled, id.server and hostname.bind queries are refused.
Hide Version                          If enabled version.server and version.bind queries are refused.
Prefetch Support                      Message cache elements are prefetched before they expire to help keep the
                                      cache up to date. When enabled, this option can cause an increase of
                                      around 10% more DNS traffic and load on the server,
                                      but frequently requested items will not expire from the cache.
Prefetch DNS Key Support              DNSKEY's are fetched earlier in the validation process when a
                                      Delegation signer is encountered.
                                      This helps lower the latency of requests but does utilize a little more CPU.
Harden DNSSEC data                    DNSSEC data is required for trust-anchored zones.
                                      If such data is absent, the zone becomes bogus.
                                      If this is disabled and no DNSSEC data is received,
                                      then the zone is made insecure.
Serve expired responses               Serve expired responses from the cache with a TTL of 0
                                      without waiting for the actual resolution to finish. When checked,
                                      multiple options to customize the behaviour regarding expired responses
                                      will appear.
Expired Record Reply TTL Value        TTL value to use when replying with expired data.
                                      If "Client Expired Response Timeout" is also used then it is recommended
                                      to use 30 as the default value as per RFC 8767.
                                      Only applicable when "Serve expired responses" is checked.
TTL for Expired Responses             Limits the serving of expired responses to the configured amount of seconds
                                      after expiration. A value of 0 disables the limit. A suggested value
                                      as per RFC 8767 is between 86400 (1 day) and 259200 (3 days).
                                      Only applicable when "Serve expired responses" is checked.
Reset Expired Record TTL              Set the TTL of expired records to the "TTL for Expired Responses" value
                                      after a failed attempt to retrieve the record from an upstream server.
                                      This makes sure that the expired records will be served as long as
                                      there are queries for it.
                                      Only applicable when "Serve expired responses" is checked.
Client Expired Response Timeout       Time in milliseconds before replying to the client with expired data.
                                      This essentially enables the serve- stable behavior as specified in RFC 8767
                                      that first tries to resolve before immediately responding with expired data.
                                      A recommended value per RF 8767 is 1800. Setting this to 0 will disable this behavior.
                                      Only applicable when "Serve expired responses" is checked.
Strict QNAME Minimisation             Send minimum amount of information to upstream servers to enhance privacy.
                                      Do not fall-back to sending full QNAME to potentially broken nameservers.
                                      A lot of domains will not be resolvable when this option in enabled.
                                      Only use if you know what you are doing.
Extended Statistics                   If enabled, extended statistics are printed to syslog.
Log Queries                           If enabled, prints one line per query to the log, with the log timestamp
                                      and IP address, name, type and class. Note that it takes time to print these lines,
                                      which makes the server (significantly) slower. Odd (non-printable) characters
                                      in names are printed as '?'.
Log Replies                           If enabled, prints one line per reply to the log, with the log timestamp
                                      and IP address, name, type, class, return code, time to resolve,
                                      whether the reply is from the cache and the response size.
                                      Note that it takes time to print these lines, which makes the server (significantly) slower.
                                      Odd (non-printable) characters in names are printed as '?'.
Tag Queries and Replies               If enabled, prints the word 'query: ' and 'reply: ' with logged queries and replies.
                                      This makes filtering logs easier.
Log level verbosity                   Select the log verbosity. Level 0 means no verbosity, only errors.
                                      Level 1 gives operational information. Level 2 gives detailed
                                      operational information. Level 3 gives query level information,
                                      output per query. Level 4 gives algorithm level information.
                                      Level 5 logs client identification for cache misses. Default is level 1.
Private Domains                       List of domains to mark as private. These domains and all its subdomains
                                      are allowed to contain private addresses.
Rebind Protection networks            These are addresses on your private network, and are not allowed to
                                      be returned for public internet names. Any occurrence of such addresses
                                      are removed from DNS answers. Additionally, the DNSSEC validator may mark the answers bogus.
                                      This protects against so-called DNS Rebinding.
                                      (Only applicable when DNS rebind check is enabled in
                                      `Administration <settingsmenu.html#administration>`__)
Insecure Domains                      List of domains to mark as insecure. DNSSEC chain of trust is ignored towards the domain name.
Message Cache Size                    Size of the message cache. The message cache stores DNS rcodes and validation statuses.
                                      The RRSet cache (which contains the actual RR data) will automatically be set to twice this amount.
                                      Valid input is plain bytes, optionally appended with 'k', 'm', or 'g' for kilobytes,
                                      megabytes or gigabytes respectively.
RRset Cache Size                      Size of the RRset cache. Contains the actual RR data. Valid input is plain bytes,
                                      optionally appended with 'k', 'm', or 'g' for kilobytes, megabytes or gigabytes respectively.
                                      Automatically set to twice the amount of the Message Cache Size when empty, but can be manually
                                      modified.
Outgoing TCP Buffers                  The number of outgoing TCP buffers to allocate per thread.
                                      If 0 is selected then no TCP queries to authoritative servers are done.
Incoming TCP Buffers                  The number of incoming TCP buffers to allocate per thread.
                                      If 0 is selected then no TCP queries from clients are accepted.
Number of queries per thread          The number of queries that every thread will service simultaneously.
                                      If more queries arrive that need to be serviced, and no queries can be jostled out (see "Jostle Timeout"),
                                      then these queries are dropped. This forces the client to resend after a timeout,
                                      allowing the server time to work on the existing queries.
Outgoing Range                        The number of ports to open. This number of file descriptors can be opened per thread.
                                      Larger numbers need extra resources from the operating system.
                                      For performance a very large value is best. For reference,
                                      usually double the amount of queries per thread is used.
Jostle Timeout                        This timeout is used for when the server is very busy.
                                      Set to a value that usually results in one round-trip to the authority servers.
                                      If too many queries arrive, then 50% of the queries are allowed to run to completion,
                                      and the other 50% are replaced with the new incoming query if they have already spent
                                      more than their allowed time. This protects against denial of service by
                                      slow queries or high query rates.
Maximum TTL for RRsets and messages   Configure a maximum Time to live in seconds for RRsets and messages in the cache.
                                      When the internal TTL expires the cache item is expired.
                                      This can be configured to force the resolver to query for
                                      data more often and not trust (very large) TTL values.
Minimum TTL for RRsets and messages   Configure a minimum Time to live in seconds for RRsets and messages in the cache.
                                      If the minimum value kicks in, the data is cached for longer than the domain owner intended,
                                      and thus fewer queries are made to look up the data. The 0 value ensures
                                      the data in the cache is as the domain owner intended. High values can lead to
                                      trouble as the data in the cache might not match up with the actual data anymore.
TTL for Host cache entries            Time to live in seconds for entries in the host cache.
                                      The host cache contains round-trip timing, lameness and EDNS support information.
Keep probing down hosts               Keep probing hosts that are down in the infrastructure host cache. Hosts that are down
                                      are probed about every 120 seconds with an exponential backoff. If hosts do not respond
                                      within this time period, they are marked as down for the duration of the host cache TTL.
                                      This setting can be used in conjunction with "TTL for Host cache entries" to increase
                                      responsiveness if internet connectivity bounces happen frequently.
Number of Hosts to cache              Number of hosts for which information is cached.
Unwanted Reply Threshold              If enabled, a total number of unwanted replies is kept track of in every
                                      thread. When it reaches the threshold, a defensive action is taken and
                                      a warning is printed to the log file. This defensive action is to clear
                                      the RRSet and message caches, hopefully flushing away any poison.
====================================  ===============================================================================


-------------------------
Access Lists
-------------------------

Access lists define which clients may query our dns resolver.
Records for the assigned interfaces will be automatically created and are shown in the overview.
You can also define custom policies, which apply an action to predefined networks.

.. Note::
    The action can be as defined in the list below.  The most specific netblock match is used,  if
    none match deny is used.  The order of the access-control statements therefore does not matter.


**Actions**
=====================================================================================================================

====================================  ===============================================================================
Deny                                  This action stops queries from hosts within the defined networks.
Refuse                                This action also stops queries from hosts within the defined networks,
                                      but sends a DNS rcode REFUSED error message back to the client.
Allow                                 This action allows queries from hosts within the defined networks.
Allow Snoop                           This action allows recursive and nonrecursive access from hosts within
                                      the defined networks. Used for cache snooping and ideally
                                      should only be configured for your administrative host.
Deny Non-local                        Allow only authoritative local-data queries from hosts within the
                                      defined networks. Messages that are disallowed are dropped.
Refuse Non-local                      Allow only authoritative local-data queries from hosts within the
                                      defined networks. Sends a DNS rcode REFUSED error message back to the
                                      client for messages that are disallowed.
====================================  ===============================================================================

-------------------------
Blocklists
-------------------------

Enable integrated dns blacklisting using one of the predefined sources or custom locations.

=====================================================================================================================

====================================  ===============================================================================
Enable                                Enable blacklists
Enable SafeSearch                     Force the usage of SafeSearch on Google, DuckDuckGo, Bing, Qwant, PixaBay and YouTube.
Type of DNSBL                         Predefined external sources
URLs of Blacklists                    Additional http[s] location to download blacklists from, only plain text
                                      files containing a list of fqdn's (e.g. :code:`my.evil.domain.com`) are
                                      supported.
Whitelist Domains                     When a blacklist item contains a pattern defined in this list it will
                                      be ommitted from the results.  e.g. :code:`.*\.nl` would exclude all .nl domains.
                                      Blocked domains explicitly whitelisted using the :doc:`/manual/reporting_unbound_dns`
                                      page will show up in this list.
Blocklist Domains                     List of domains to explicitly block. Regular expressions are not supported.
                                      Passed domains explicitly blocked using the :doc:`/manual/reporting_unbound_dns`
                                      page will show up in this list.
Wildcard Domains                      List of wildcard domains to blocklist. All subdomains of the given domain will
                                      be blocked. Blocking first-level domains (e.g. 'com') is not supported.
Destination Address                   Specify an IP address to return when DNS records are blocked. Can be used to
                                      redirect such domains to a separate webserver informing the user that the
                                      content has been blocked. The default is 0.0.0.0. Any value in this field
                                      is skipped if "Return NXDOMAIN" is checked.
Return NXDOMAIN                       Instead of returning the "Destination Address", return the DNS return code
                                      "NXDOMAIN". This is useful in cases where devices cannot cope
                                      with the 0.0.0.0 destination address, such as certain Apple devices.
====================================  ===============================================================================

.. Note::

    Applying the blocklist settings will not restart Unbound, rather it will signal to Unbound to dynamically
    process the blocklists as soon as they're downloaded. There may be up to a minute of delay before Unbound
    has loaded everything. During this time Unbound will still be just as responsive.

When any of the DNSBL types are used, the content will be fetched directly from its original source, to
get a better understanding of the source of the lists we compiled the list below containing references to
the list maintainers.

*Predefined sources*
=====================================================================================================================

====================================  ===============================================================================
Abuse.ch - ThreatFox IOC database     https://threatfox.abuse.ch/
AdAway                                https://adaway.org
AdGuard List                          https://justdomains.github.io/blocklists/#the-lists
Blocklist.site                        https://github.com/blocklistproject/Lists
EasyList                              https://justdomains.github.io/blocklists/#the-lists
Easyprivacy                           https://justdomains.github.io/blocklists/#the-lists
NoCoin List                           https://justdomains.github.io/blocklists/#the-lists
PornTop1M List                        https://github.com/chadmayfield/my-pihole-blocklists
Simple Ad List                        https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt
Simple Tracker List                   https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt
StevenBlack/hosts                     https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
WindowsSpyBlocker                     https://github.com/crazy-max/WindowsSpyBlocker
YoYo List                             https://pgl.yoyo.org/adservers/
====================================  ===============================================================================

.. Note::

    In order to automatically update the lists on timed intervals you need to add a cron task, just go to
    :menuselection:`System -> Settings ->Cron` and a new task for a command called "Update Unbound DNSBLs".

    Usually once a day is a good enough interval for these type of tasks.


.. _forwarding:

-------------------------
Query Forwarding
------------------------- 

The Query Forwarding section allows for entering arbitrary nameservers to forward queries to. It is assumed 
that the nameservers entered here are capable of handling further recursion for any query. In this section 
you are able to specify nameservers to forward to for specific domains queried by clients, catch all domains 
and specify nondefault ports.

=====================================================================================================================

====================================  ===============================================================================
Use System Nameservers                The configured system nameservers will be used to forward queries to. 
                                      This will override any entry made in the custom forwarding grid, except for 
                                      entries targeting a specific domain. If there are no system nameservers, you
                                      will be prompted to add one in `General <settingsmenu.html#general>`__. 
                                      If you expected a DNS server from your WAN and it's not listed, make sure you 
                                      set "Allow DNS server list to be overridden by DHCP/PPP on WAN" there as well.
====================================  ===============================================================================

.. note::

    Keep in mind that if the "Use System Nameservers" checkbox is checked, the system nameservers will be preferred
    over any **catch-all entry** in **both** Query Forwarding and DNS-over-TLS, this means that entries with a specific domain
    will still be forwarded to the specified nameserver.

====================================  ===============================================================================
Enabled                               Enable query forwarding for this domain.
Domain                                Domain of the host. All queries for this domain will be forwarded to the 
                                      nameserver specified in "Server IP". Leave empty to catch all queries and
                                      forward them to the nameserver.
Server IP                             Address of the DNS server to be used for recursive resolution.
Port                                  Specify the port used by the DNS server. Default is port 53. Useful when
                                      configuring e.g. :doc:`/manual/how-tos/dnscrypt-proxy`
====================================  ===============================================================================

.. warning::

    Be careful enabling "DNS Query Forwarding" in combination with **DNSSEC**, no DNSSEC validation will be performed
    for forwards with a specific domain, as the upstream server might be a local controller. If forwarding
    everything and the upstream server doesn't support DNSSEC, its answers will not reach the client as no DNSSEC
    validation could be performed.

-------------------------
DNS over TLS
-------------------------

DNS over TLS uses the same logic as Query Forwarding, except it uses TLS for transport. 

=====================================================================================================================

.. note:: 

    Please be aware of interactions between Query Forwarding and DNS over TLS. Since the same principle as Query 
    Forwarding applies, a **catch-all entry** specified in both sections will be considered a duplicate zone. 
    In our case DNS over TLS will be preferred.


====================================  ===============================================================================
Enabled                               Enable DNS over TLS for this domain.
Domain                                Domain of the host. All queries for this domain will be forwarded to the 
                                      nameserver specified in "Server IP". Leave empty to catch all queries and
                                      forward them to the nameserver.
Server IP                             Address of the DNS server to be used for recursive resolution.
Port                                  Specify the port used by the DNS server. Always enter port 853 here unless 
                                      there is a good reason not to, such as when using an SSH tunnel.
Verify CN                             The name to use for certificate verification, e.g. "445b9e.dns.nextdns.io".
                                      Used by Unbound to check the TLS authentication certificates.
                                      It is strongly discouraged to omit this field since man-in-the-middle attacks
                                      will still be possible.
====================================  ===============================================================================

.. tip:: 

    To ensure a validated environment, it is a good idea to block all outbound DNS traffic on port 53 using a 
    firewall rule when using DNS over TLS. Should clients query other nameservers directly themselves, a NAT 
    redirect rule to 127.0.0.1:53 (the local Unbound service) can be used to force these requests over TLS.
    

**Public Resolvers**

+-------------------+-----------------------------------------+-------------+------------------------------+
| Hosted by         | Server IP                               | Server Port | Verify CN                    |
+===================+=========================================+=============+==============================+
| `Cloudflare`_     | 1.1.1.1                                 | 853         | cloudflare-dns.com           |
|                   +-----------------------------------------+             |                              |
|                   | 1.0.0.1                                 |             |                              |
|                   +-----------------------------------------+             |                              |
|                   | 2606:4700:4700::1111                    |             |                              |
|                   +-----------------------------------------+             |                              |
|                   | 2606:4700:4700::1001                    |             |                              |
+-------------------+-----------------------------------------+-------------+------------------------------+
| `Google`_         | 8.8.8.8                                 | 853         | dns.google                   |
|                   +-----------------------------------------+             |                              |
|                   | 8.8.4.4                                 |             |                              |
|                   +-----------------------------------------+             |                              |
|                   | 2001:4860:4860::8888                    |             |                              |
|                   +-----------------------------------------+             |                              |
|                   | 2001:4860:4860::8844                    |             |                              |
+-------------------+-----------------------------------------+-------------+------------------------------+
| `Quad9`_          | 9.9.9.9                                 | 853         | dns.quad9.net                |
|                   +-----------------------------------------+             |                              |
|                   | 149.112.112.112                         |             |                              |
|                   +-----------------------------------------+             |                              |
|                   | 2620:fe::fe                             |             |                              |
|                   +-----------------------------------------+             |                              |
|                   | 2620:fe::9                              |             |                              |
+-------------------+-----------------------------------------+-------------+------------------------------+

.. _Cloudflare: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-tls/
.. _Google: https://developers.google.com/speed/public-dns
.. _Quad9: https://www.quad9.net/service/service-addresses-and-features/

-------------------------
Statistics
-------------------------

The statistics page provides some insights into the running server, such as the number of queries executed,
cache usage and uptime.

-------------------------
Advanced Configurations
-------------------------

Some installations require configuration settings that are not accessible in the UI.
To support these, individual configuration files with a ``.conf`` extension can be put into the
``/usr/local/etc/unbound.opnsense.d`` directory. These files will be automatically included by
the UI generated configuration. Multiple configuration files can be placed there. But note that

* As it cannot be predicted in which clause the configuration currently takes place, you must prefix the configuration with the required clause.
  For the concept of "clause" see the ``unbound.conf(5)`` documentation.
* The wildcard include processing in Unbound is based on ``glob(7)``. So the order in which the files are included is in ascending ASCII order.
* Name collisions with plugin code, which use this extension point e. g. ``dnsbl.conf``, may occur. So be sure to use a unique filename.
* It is a good idea to check the complete configuration via::

   # check if the resulting configuration is valid
   configctl unbound check

  This will report errors that prevent Unbound from starting and also list warnings that may give hints as to why a particular configuration
  is not working or how it could be improved.

This is a sample configuration file to add an option in the server clause:

::

    server:
      private-domain: xip.io


.. Note::
  As a more permanent solution the template system (":doc:`/development/backend/templates`") can be used to automatically generate these files.

  To get the same effect as placing the file in the sample above directly in ``/usr/local/etc/unbound.opnsense.d`` follow these steps:

  #. Create a ``+TARGETS`` file in ``/usr/local/opnsense/service/templates/sampleuser/Unbound``::

      sampleuser_additional_options.conf:/usr/local/etc/unbound.opnsense.d/sampleuser_additional_options.conf

  #. Place the template file as ``sampleuser_additional_options.conf`` in the same directory::

      server:
        private-domain: xip.io

  #. Test the template generation by issuing the following command::

      # generate template
      configctl template reload sampleuser/Unbound


  #. Check the output in the target directory::

      # show generated file
      cat /usr/local/etc/unbound.opnsense.d/sampleuser_additional_options.conf
      # check if configuration is valid
      configctl unbound check


.. Warning::
    It is the sole responsibility of the administrator which places a file in the extension directory to ensure that the configuration is
    valid.

.. Note::
    This method replaces the ``Custom options`` settings in the General page of the Unbound configuration,
    which was removed in version 21.7.
