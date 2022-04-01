==============
Unbound DNS
==============

Unbound is a validating, recursive, caching DNS resolver. It is designed to be fast and lean and incorporates modern features based on open standards.

Since OPNsense 17.7 it has been our standard DNS service, which on a new install is enabled by default.


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
DHCP Registration                     **IPv4 only** If this option is set, then machines that specify their hostname
                                      when requesting a DHCP lease will be registered in Unbound,
                                      so that their name can be resolved.

                                      The source of this data is **client-hostname** in the
                                      `dhcpd.leases <https://www.freebsd.org/cgi/man.cgi?query=dhcpd.leases>`__ file

DHCP Domain Override                  When the above registrations shouldn't use the same domain name as configured
                                      on this firewall, you can specify a different one here.
DHCP Static Mappings                  Register static dhcpd entries so clients can resolve them. Supported on IPv4 and
                                      IPv6.
IPv6 Link-local                       Register link local addresses for IPv6.
TXT Comment Support                   Register descriptions as comments for dhcp static host entries.
DNS Query Forwarding                  Forward queries to configured nameservers in
                                      :menuselection:`System --> Settings --> General : DNS Server`
Local Zone Type                       The local zone type used for the system domain.
                                      Type descriptions are available under "local-zone:" in the
                                      `unbound.conf(5) <https://nlnetlabs.nl/documentation/unbound/unbound.conf/>`__
                                      manual page. The default is 'transparent'.
====================================  ===============================================================================


.. Note::

    Be careful enabling "DNS Query Forwarding" in combination with **DNSSEC**, when the upstream server doesn't support
    DNSSEC, its answers will be considered insecure since no DNSSEC validation could be performed.

.. Note::

    In order for the client to query unbound, there need to be an ACL assigned in
    :menuselection:`Services --> Unbound DNS --> Access Lists`. The configured interfaces should gain an ACL automatically.
    If the client address is not in any of the predefined networks, please add one manually.


-------------------------
Overrides
-------------------------

Within the overrides section you can create separate host definition entries and specify if queries for a specific
domain should be forwarded to a predefined server.

**Host override settings**
=====================================================================================================================

====================================  ===============================================================================
Host                                  Name of the host, without domain part. Use "*" to create a wildcard entry.
Domain                                Domain of the host (such as example.com)
Type                                  Record type, A or AAA (IPv4 or IPv6 address), MX to define a mail exchange
IP                                    Address of the host
Description                           User readable description, only for informational purposes
Aliases                               Copies of the above data for different hosts
====================================  ===============================================================================

**Domain override settings**
=====================================================================================================================

====================================  ===============================================================================
Domain                                Domain to override
IP address                            IP address of the authoritative DNS server for this domain
Description                           User readable description, only for informational purposes
====================================  ===============================================================================


-------------------------
Advanced
-------------------------

Although the default settings should be reasonable for most setups, some need more tuning or require specific options
set.

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
                                      without waiting for the actual resolution to finish.
Message Cache Size                    Size of the message cache. The message cache stores DNS rcodes
                                      and validation statuses. The RRSet cache will automatically be
                                      set to twice this amount.
                                      The RRSet cache contains the actual RR data. The default is 4 megabytes.
Outgoing TCP Buffers                  The number of outgoing TCP buffers to allocate per thread.
                                      The default value is 10. If 0 is selected then no TCP queries,
                                      to authoritative servers, are done.
Incoming TCP Buffers                  The number of incoming TCP buffers to allocate per thread.
                                      The default value is 10. If 0 is selected then no TCP queries,
                                      from clients, are accepted.
Number of queries per thread          The number of queries that every thread will service simultaneously.
                                      If more queries arrive that need to be serviced,
                                      and no queries can be jostled, then these queries are dropped.
Jostle Timeout                        This timeout is used for when the server is very busy.
                                      This protects against denial of service by slow queries or
                                      high query rates. The default value is 200 milliseconds.
Maximum TTL for RRsets and messages   Configure a maximum Time to live for RRsets and messages in the cache.
                                      The default is 86400 seconds (1 day). When the internal TTL expires
                                      the cache item is expired. This can be configured to force the
                                      resolver to query for data more often and not trust (very large) TTL values.
Minimum TTL for RRsets and messages   Configure a minimum Time to live for RRsets and messages in the cache.
                                      The default is 0 seconds. If the minimum value kicks in,
                                      the data is cached for longer than the domain owner intended,
                                      and thus less queries are made to look up the data.
                                      The 0 value ensures the data in the cache is as the domain owner intended.
                                      High values can lead to trouble as the data in the cache might not match up
                                      with the actual data anymore.
TTL for Host cache entries            Time to live for entries in the host cache.
                                      The host cache contains roundtrip timing and
                                      EDNS support information. The default is 15 minutes.
Number of Hosts to cache              Number of hosts for which information is cached. The default is 10000.
Unwanted Reply Threshold              If enabled, a total number of unwanted replies is kept track of in every
                                      thread. When it reaches the threshold, a defensive action is taken and
                                      a warning is printed to the log file. This defensive action is to clear
                                      the RRSet and message caches, hopefully flushing away any poison.
                                      The default is disabled, but if enabled a value of 10 million is suggested.
Log level verbosity                   Select the log verbosity. Level 0 means no verbosity, only errors.
                                      Level 1 gives operational information. Level 2 gives detailed
                                      operational information. Level 3 gives query level information,
                                      output per query. Level 4 gives algorithm level information.
                                      Level 5 logs client identification for cache misses. Default is level 1.
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
Type of DNSBL                         Predefined external sources
URLs of Blacklists                    Additional http[s] location to download blacklists from, only plain text
                                      files containing a list of fqdn's (e.g. :code:`my.evil.domain.com`) are
                                      supported.
Whitelist Domains                     When a blacklist item contains a pattern defined in this list it will
                                      be ommitted from the results.  e.g. :code:`.*\.nl` would exclude all .nl domains
====================================  ===============================================================================

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
