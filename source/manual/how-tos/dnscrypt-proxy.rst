==============
DNSCrypt-Proxy
==============

------------
Installation
------------

First of all, you have to install the dnscrypt-proxy plugin (os-dnscrypt-proxy) from the plugins view
reachable via **System->Firmware->Plugins**.

After a page reload you will get a new menu entry under **Services** for DNSCrypt-Proxy. 

When you start the daemon, it looks for a list of public DNS server from here:
https://dnscrypt.info/public-servers

Depending on all settings below the list will shortened to your choice, like only IPv4, or logging disabled.
The fastest two servers will be used for DNS queries. If you use Unbound as your main resolver and want to
send your queries to Unbound first and forward to DNSCrypt-Proxy, just set this in your Unbound Advanced
settings:

.. code-block:: sh

    do-not-query-localhost: no
    forward-zone:
    name: "."
    forward-addr: 127.0.0.1@5353

----------------
General Settings
----------------

:Enable DNSCrypt-Proxy:
    Enable and start DNSCrypt-Proxy.
:Listen Address:
    Here you set the addresses and ports to listen on. Default is localhost and port 5353.
    If you want it to listen to port 53 you should enable **Allow Privileged Ports**, especially
    when the system itself should treat it as a resolver. 
:Allow Privileged Ports:
    This allows the service to listen on ports below 1024, like 53.
:Max Client Connections:
    How many clients are allowed to contact the daemon.
:Use IPv4 Servers:
    Use IPv4 enabled servers.
:Use IPv6 Servers:
    Only use IPv6 enabled servers.
:Use DNSCrypt Servers:
    Include resolvers supporting DNSCrypt protocol in the decision process.
:Use DNS-over-HTTPS Servers:
    Include resolvers supporting DNS-over-HTTPS in the decision process.
:Require DNSSEC:
    Only use resolvers supporting DNSSEC protocol.
:Require NoLog:
    Only use resolvers with disabled loggong.
:Require NoFilter:
    Only use resolvers without filtering. Otherwise requests would also filtered for adult content or ad's.
:Force TCP:
    Always use TCP to connect to upstream servers. This can be can be useful if you need to route everything
    through Tor, otherwise keep it disabled.
:Proxy:
    Use this to route all TCP connections to a local Tor node, format has to be like 127.0.0.1:9050
:Timeout:
    How long a DNS query will wait for a response in milliseconds.
:Keepalive:
    Keepalive for HTTP (HTTPS, HTTP/2) queries in seconds.
:Cert Refresh Delay:
    Delay in minutes after which certificates are reloaded.
:Ephemeral Keys:
    Create a new, unique key for every single DNS query. This may improve privacy but can also have a
    significant impact on CPU usage.
:TLS Disable Session Tickets:
    Disable TLS session tickets - increases privacy but also latency.
:Fallback Resolver:
    This is a normal, non-encrypted DNS resolver, that will be only used for one-shot queries when
    retrieving the initial resolvers list, and only if the system DNS configuration does not work.
:Block IPv6:
    Immediately respond to IPv6-related queries with an empty response. 
    This makes things faster when there is no IPv6 WAN connectivity.
:Cache:
    Enable a DNS cache to reduce latency and outgoing traffic.
:Cache Size:
    Set the cache size.
:Cache Min TTL:
    Minimum TTL for cached entries.
:Cache Max TTL:
    Maximum TTL for cached entries.
:Cache Negative Min TTL:
    Minimum TTL for negatively cached entries.
:Cache Negative Max TTL:
    Maximum TTL for negatively cached entries.
