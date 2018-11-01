===========================
Reverse Proxy and Webserver
===========================

.. Note::
    All reverse proxies are plugins and need to be installed first.

Why should a reverse proxy be used?
===================================

The packet filter itself cannot decide what should be done in application protocols.
For such an inspection you can use deep packet inspection or a reverse proxy.

In addition, a reverse proxy can implement protocol specific access control lists
as well as other checks to protect the application behind. Such checks are malware,
spam, web attack detection and so on.

.. Warning::
    This tools support you to prevent some bad things from happening but will never
    provide a 100% success rate. Do not use them as a replacement / excuse for (not)
    fixing the upstream.

Supported Reverse Proxies in OPNsense
=====================================

========= ==========================
ftp-proxy Makes FTP working
nginx     HTTP, TCP- and UDP streams
HAProxy   HTTP and TCP streams
postfix   SMTP (e-mail)
relayd    TCP and UDP Streams
========= ==========================

Terms
=====

**Forward Proxy**

A Proxy which is used by a client to connect to the internet. It is usually
used in companies to scan traffic for malware. See the more specific pages
(:doc:`proxy`) for more background information.

**Reverse Proxy**

A software which takes a request or a connection from a client and sends is to an upstream server.
It may change some data if needed (for exmaple inject HTTP header).

**Webserver**

A webserver in contrast to a reverse proxy sends an answer to the reverse
proxy sends out the answer to the request which may be modified or cached
by a reverse or forward proxy.

**Upstream, Backend**

A single or multiple servers which can be used for load balancing the client
request to. All servers used in an upstream must act equally (same protocol
etc.) but do not need to run on the same port.

**Upstream Server, Backend Server**

This is your listening application like nginx on port 80 for HTTP or your
LDAP server on TCP/389.

**Frontends (HAProxy) and HTTP(S)/Stream Servers (nginx)**

These are the the configurations for the ports used for incoming connections.
For example, if you bind a port to TCP/80 (standard port of HTTP), you can
decide, what is going to be done with this request. The same is true for
connections.

**TLS and SSL**

TLS replaced SSL and it is used to protect the application protocol against a broad
range of attacks like snooping, data manipulation (for example ad injection,
redirects, manipulation of downloaded files like executables).

Modern clients and servers should support TLS 1.2 and TLS 1.3. All others should
be disabled.

TLS - Diffenent ways to use it
==============================

1) Breaking up the connection on the firewall (down- and upstream are using TLS)
--------------------------------------------------------------------------------

In this setup we do have two TLS protected connections. One from the client to
the firewall, and one from the firewall to the backend.

.. image::  images/sample_network_tls_broken_up.png

The advantage of this setup is that you can use it to route based on paths or
other properties and you can present another certificate to the client.
For example, you can use an internal certificate on the server and the reverse
proxy will present a probably trusted certificate like one of Let's Encrypt to
the client. This simplifies certificate handling because the upstream client
may be invalid (for example outdated). Please note that it is not recommended
to disable certificate checks in the upstream but it may be required in some
setups.

2) Decrypt an encrypted upstream (downstream plain, upstream TLS protected)
---------------------------------------------------------------------------

.. image::  images/sample_network_tls_decrypt.png

This setup may not make much sense in most cases. It may have the advantage
if you have trouble with some software which does not allow a not encrypted
port but a special internal client does not support it. For example a machine
needs to talk to a server but cannot use TLS because the hardware does not
support it. If you need that, do not make it available via the internet
because there is probably a reason that the upstream server is TLS only.


3) TLS Offloading (downstream is TLS protected, upstream is plain)
------------------------------------------------------------------

.. image::  images/sample_network_tls_offload.png

This setup should be preferred when it is supported. It has the advantage
that it fully supports TLS for the client while it does not need a lot of
power to do a TLS handshake inside your own computer centre.

.. Warning::
    You should not use this for upstream servers reachable via untrusted newtworks.
    Use (1) or (4) in such cases.

(4) TLS Passthough
------------------

.. image::  images/sample_network_tls_pass_trough.png

In this mode, the proxy will just pass though the connection and has no access
to the encrypted payload. You cannot match on anything of the protocol itself.
You may use some extension headers like SNI to decide, which upstream is used.
This setup is recommended if you only want some improved routing decisions
better than plain NAT.


Tutorials
=========

Basic Reverse Proxy Setup
-------------------------
* :doc:`how-tos/nginx`
* :doc:`how-tos/nginx_streams`
* :doc:`how-tos/haproxy`
* :doc:`how-tos/mailgateway`


Setup Authentication
--------------------
* :doc:`how-tos/nginx_basic_auth`
* :doc:`how-tos/nginx_tls_auth`

Firewalling
-----------
* :doc:`how-tos/nginx_waf`

Misc
----
* :doc:`how-tos/nginx_hosting`
* :doc:`how-tos/haproxy_howtos`
