====================
caddy: Reverse Proxy
====================

.. contents:: Index


--------
Features
--------

Reverse Proxy HTTP, HTTPS, FastCGI, WebSockets, gRPC, FastCGI (usually PHP), and more!

WWW: https://caddyserver.com/

Main features of this plugin:

* Easy to configure and reliable! Reverse Proxy any HTTP/HTTPS or WebSocket application in minutes.
* Hard to break! Extensive validations of the configuration on each save and apply.
* Automatic Let's Encrypt and ZeroSSL Certificates with HTTP-01 and TLS-ALPN-01 challenge
* DNS-01 challenge and Dynamic DNS with supported DNS Providers built right in
* Use custom certificates from OPNsense certificate store
* Wildcard Domain and Subdomain support
* Access Lists to restrict access based on static networks
* Basic Auth to restrict access by username and password
* Syslog-ng integration and HTTP Access Log
* NTLM Transport
* Header manipulation
* Simple load balancing with passive health check


--------------
How-To install
--------------

* Install "os-caddy" from the OPNsense Plugins.


---------------------------------------------
Prepare OPNsense for Caddy after installation
---------------------------------------------

.. Attention:: Caddy uses port `80` and `443`. So the OPNsense WebUI or other plugins can't bind to these ports.

Go to `System - Settings - Administration`

* Change the `TCP Port` to `8443` (example), don't forget to adjust the firewall rules to allow access to the WebUI. On `LAN` there is a hidden `anti-lockout` rule that takes care of this automatically. On other interfaces, make sure to add explicit rules.
* Enable the checkbox for `HTTP Redirect - Disable web GUI redirect rule`.

Go to `Firewall - Rules - WAN`

* Create Firewall rules that allow ``HTTP`` and ``HTTPS`` to destination ``This Firewall`` on ``WAN``

=========================== ================================
Option                      Values
=========================== ================================         
**Interface**               ``WAN``
**TCP/IP Version**          ``IPv4+IPv6``
**Protocol**                ``TCP``
**Source**                  ``Any``
**Destination**             ``This Firewall``
**Destination port range**  from: ``HTTP`` to: ``HTTP``
**Description**             ``Caddy Reverse Proxy HTTP``
=========================== ================================

=========================== ================================
Option                      Values
=========================== ================================         
**Interface**               ``WAN``
**TCP/IP Version**          ``IPv4+IPv6``
**Protocol**                ``TCP/UDP``
**Source**                  ``Any``
**Destination**             ``This Firewall``
**Destination port range**  from: ``HTTPS`` to: ``HTTPS``
**Description**             ``Caddy Reverse Proxy HTTPS``
=========================== ================================

Go to `Firewall - Rules - LAN` and create the same rules for the `LAN` interface. Now external and internal clients can connect to Caddy, and Let's Encrypt or ZeroSSL certificates will be issued automatically.


---
FAQ
---

* A DNS Provider is not required. With a static WAN IP, just skip the DNS Provider configuration and don't check the DNS-01 and Dynamic DNS checkboxes. Let's Encrypt will work with HTTP-01 (Port 80) or TLS-ALPN-01 (Port 443) challenge automatically.
* Port Forwards, NAT Reflection or Split Horizon DNS are not required. Only create Firewall rules that allow traffic to hit the ports that Caddy opens. They are TCP/UDP 80 and 443.
* Firewall rules to allow Caddy to reach upstream destinations are not required. OPNsense has a default rule that allows all traffic originating from it to be allowed.
* ACME Clients on reverse proxied upstream destinations won't be able to issue certificates. Caddy intercepts ``/.well-known/acme-challenge``. This can potentially be solved by using the `HTTP-01 challenge redirection` option in the advanced mode of domains.
* When using Caddy with IPv6, it's best to have a GUA (Global Unicast Address) on the WAN interface, since otherwise the TLS-ALPN-01 challenge might fail.
* Let's Encrypt or ZeroSSL can't be explicitely chosen. Caddy automatically issues one of these options, determined by speed and availability. These certificates can be found in ``/var/db/caddy/data/caddy/certificates``.

.. Attention:: There is no TCP/UDP stream and WAF (Web Application Firewall) support in this plugin. Caddy itself could support these features, but this plugin is focused on ease of configuration. For a business ready Reverse Proxy with WAF functionality, use OPNWAF. For TCP/UDP streaming, use either nginx or ha-proxy.

.. Tip:: As an alternative to a WAF, it's simple to integrate Caddy with CrowdSec. Check the tutorial section for guidance.


====================
caddy: Configuration
====================

.. Note:: Caddy can be found in "Services: Caddy Web Server". Some options are hidden in advanced mode.


--------------------------
General Settings - General
--------------------------

=========================== ================================
Option                      Description
=========================== ================================
**enabled**                 `enable` or `disable` Caddy. If enabled, Caddy will serve the configuration and autostart with the OPNsense.
**ACME Email**              e.g. `info@example.com`, it's mandatory for receiving automatic ZeroSSL certificates. For Let's Encrypt it is still optional, but that can change at any point in time. To have a fully supported configuration, it should be seen as mandatory to provide an Email address.
**Auto HTTPS**              `On (default)` creates automatic Let's Encrypt certificates for all domains that don't have more specific options set, like custom certificates.
**Trusted Proxies**         If Cloudflare or another CDN provider is used, create an `Access List` with the IP addresses of that CDN and add it here. Add the same Access List to the domain this CDN tries to reach.
**Abort Connections**       This option, when enabled, aborts all connections to the domain that don't match any specified handler or access list. This setting doesn't affect Let's Encrypt's ability to issue certificates, ensuring secure connections regardless of the option's status. If unchecked, the domain remains accessible even without a matching handler, allowing for connectivity and certificate checks, even in the absence of a configured upstream destination. When using Access Lists, enabling this option is recommended to reject unauthorized connections outright. Without this option, unmatched IP addresses will encounter an empty page instead of an explicit rejection, though the Access Lists continue to function and restrict access.
**Grace Period**            Defines the grace period for shutting down HTTP servers (i.e. during config changes or when Caddy is stopping) in seconds. During the grace period, no new connections are accepted, idle connections are closed, and active connections are impatiently waited upon to finish their requests. If clients do not finish their requests within the grace period, the server will be forcefully terminated to allow the reload to complete and free up resources. This can influence how long "Apply" of new configurations take, since Caddy waits for all open connections to close.
=========================== ================================


-------------------------------
General Settings - DNS Provider
-------------------------------

=========================== ================================
Option                      Description
=========================== ================================
**DNS Provider**            Select the DNS provider for the `DNS-01 Challenge` and `Dynamic DNS`. This is optional, since certificates will be requested from Let's Encrypt via HTTP-01 or TLS-ALPN-01 challenge when this option is unset. Needed for wildcard certificates, and for dynamic DNS. To use the DNS-01 challenge and dynamic DNS, enable the checkbox in a domain or subdomain. For more information: https://github.com/caddy-dns
**DNS API Fields**          These fields are for the API settings of the chosen DNS Provider. All of these fields can be left empty if they are optional with the chosen provider. The help text in the plugin will list all available providers and their expected configurations. There are additional fields if DNS providers require more fields for their configurations.
=========================== ================================


------------------------------
General Settings - Dynamic DNS
------------------------------

=========================== ================================
Option                      Description
=========================== ================================
**DynDns IP Version**       Select `IPv4+IPv6` to set IPv4 A-Records and IPv6 AAAA-Records, `Ipv4 only` for setting A-Records or `IPv6 only` for setting AAAA-Records.
**DynDns Check Interval**   Interval to poll for changes of the IP address. The default is 5 minutes. Can be a number between 1 to 1440 minutes.
**DynDns TTL**              Set the TTL (time to live) for DNS Records. The default is 1 hour. Can be a number between 1 to 24 hours.
**DynDns Check Http**       Optionally, enter an URL to test the current IP address of the firewall via HTTP procotol. Generally, this is not needed. Caddy uses default providers to test the current IP addresses. For using a custom one, enter the `https://` link to an IP address testing website.
**DynDns Check Interface**  Optionally, select an interface to extract the current IP address of the firewall. At most, one current IPv6 Global Unicast Address and one current IPv4 non-RFC1918 Address will be extracted.
=========================== ================================


-------------------------------
General Settings - Log Settings
-------------------------------

======================================= ================================
Option                                  Description
======================================= ================================
**Log Level**                           Select the minimum global Log Level. "INFO" is the default and shouldn't be changed without a reason, since that level displays the ACME Client messages for automatic certificates. This setting doesn't influence the HTTP Access logs, they're always using INFO, which is their lowest supported Log Level.
**Log Credentials**                     Log all Cookies and Authorization Headers in HTTP request logging. Use combined with HTTP Access Log in a domain. Enable this option only for troubleshooting.
**Log Access in Plain Format**          Don't send HTTP access logs to the central OPNsense logging facility but save them in plain Caddy JSON format in a subdirectory instead. Only effective for domains that have HTTP Access Log enabled. The feature is intended to have access log files processed by e.g. CrowdSec. They can be found in ``/var/log/caddy/access``.
**Keep Plain Access Logs for (days)**   How many days until the plain format log files are deleted. The default is 10 days.
======================================= ================================


-----------------------
Reverse Proxy - Domains
-----------------------

=================================== ================================
Option                              Description
=================================== ================================
**enabled**                         `enable` or `disable` this domain
**Domain**                          Can either be a domain name or an IP address. If a domain name is chosen, Caddy will automatically try to get a Let's Encrypt or ZeroSSL certificate, and the headers and real IP address will be automatically passed to the upstream destination.
**Port**                            Should be the port the OPNsense will listen on. Don't forget to create Firewall rules that allow traffic to this port on ``WAN`` and ``LAN`` to destination ``This Firewall``. Leave this empty if the default ports of Caddy (`80` and `443`) should be used with automatic redirection from HTTP to HTTPS.
**Description**                     The description is mandatory. Create descriptions for each domain. Since there could be multiples of the same domain with different ports, do it like this: ``foo.example.com`` and ``foo.example.com.8443``.
**>DNS**                            DNS options
**Dynamic DNS**                     Enable Dynamic DNS. This option needs the `General Settings - DNS Provider` configured. The DNS Records of this domain will be automatically updated with the chosen DNS Provider.
**>Trust**                          Certificate options
**DNS-01 challenge**                Enable this for using DNS-01 instead of HTTP-01 and TLS-ALPN-01 challenge. This can be set per entry, so both types of challenges can be used at the same time for different entries. This option needs the `General Settings - DNS Provider` configured.
**HTTP-01 challenge redirection**   Enter a domain name or IP address. The HTTP-01 challenge will be redirected to that destination. This enables a server behind Caddy to serve ``/.well-known/acme-challenge/``. Caddy will issue a certificate for the same domain using the TLS-ALPN-01 challenge or DNS-01 challenge instead. Please note that his is a complex scenario, Caddy can *only* continue to get automatic certificates if it can listen on Port 443 - so either specify 443 directly or leave the Port empty. Having the domain listen on any other port than 443 will mean the TLS-ALPN-01 challenge will fail too, and there won't be any automatic certificates. If the requirement is a different port than 443, the DNS-01 challenge will remain the only option. This option can also be used to redirect the HTTP-01 challenge to Caddy on a backup OPNsense firewall in a HA setup.
**Custom Certificate**              Use a certificate imported or generated in `System - Trust - Certificates`. The chain is generated automatically. Certificate + Intermediate CA + Root CA, Certificate + Root CA and self signed Certificate are all fully supported. Only SAN certificates will work.
**>Access**                         Access options
**Access List**                     Restrict the access to this domain to a list of IP addresses defined in the Access Tab. This doesn't influence Let's Encrypt certificate generation.
**Basic Auth**                      Restrict the access to this domain to one or multiple users defined in the Access Tab. This doesn't influence the Let's Encrypt certificate generation.
**HTTP Access Log**                 Enable the HTTP request logging for this domain and its subdomains. This option is mostly for troubleshooting or log analyzing tools like CrowdSec, since it will log every single request.
=================================== ================================


--------------------------
Reverse Proxy - Subdomains
--------------------------

=========================== ================================
Option                      Description
=========================== ================================
**Domain**                  Choose a wildcard domain prepared in domains, it has to be formatted like ``*.example.com``
**Subdomain**               Create a name that is seated under the wildcard domain, for example ``foo.example.com`` and ``bar.example.com``.
=========================== ================================

.. Note:: For the other options refer to `Reverse Proxy - Domains`. It's best to leave `Access Lists` and `Basic Auth` unconfigured in wildcard domains, and set these per subdomain.


-----------------------
Reverse Proxy - Handler
-----------------------

.. Attention:: Leaving `Handle Path` empty creates a catch-all handler that proxies all traffic while retaining the original path. This is strongly **recommended**.

=================================== ================================
Option                              Description
=================================== ================================
**enabled**                         `enable` or `disable` this handler
**Domain**                          Select a domain.
**Subdomain**                       Select a subdomain. This will put the handler on the subdomain instead of the domain. Use only with wildcard domains and subdomains.
**Handle Type**                     `handle` or `handle path` can be chosen. If in doubt, always use `handle`, the most common option. `handle path` is used to strip the path from the URI.
**Handle Path**                     Leave this empty to create a catch all location or enter a location like  `/foo/*` or `/foo/bar*`.
**>Header**                         Header options
**Header Manipulation**             Select one or multiple header manipulations. These will be set to this handler.
**>Upstream**                       Upstream options
**Upstream Domain**                 Should be an internal domain name or an IP Address of the upstream destination that should receive the reverse proxied traffic. If multiple upstream destinations are chosen, they will be load balanced with the default random policy. If unhealthy upstreams should be removed, set the Upstream Fail Duration for a passive health check.
**Upstream Port**                   Should be the port the upstream destination listens on. This can be left empty to use Caddy default port 80.
**Upstream Path**                   When using "reverse_proxy" (default), in case the backend application resides in a sub-path of the web root and its path shouldn't be visible in the frontend URL, this setting can be used to prepend an initial path starting with '/' to every backend request. Java applications running in a servlet container like Tomcat are known to behave this way, so set it to e.g. '/guacamole' to access Apache Guacamole at the frontend root URL without needing a redirect.
**Upstream Fail Duration**          Enables a passive health check when multiple upstream destinations have been defined for load balancing. `fail_duration` is a duration value that defines how long to remember a failed request. A duration of 1 or more seconds enables passive health checking; the default is empty (off). A reasonable starting point might be 30s to balance error rates with responsiveness when bringing an unhealthy upstream back online.
**>Trust**                          Certificate options
**TLS**                             If the upstream destination only accepts HTTPS, enable this option. If the upstream destination has a globally trusted certificate, this TLS option is the only needed one.
**NTLM**                            If the upstream destination needs NTLM authentication, enable this option together with TLS. For example: Exchange Server.
**TLS Insecure Skip Verify**        Turns off TLS handshake verification, making the connection insecure and vulnerable to man-in-the-middle attacks. Do not use in production.
**TLS Trusted CA Certificates**     Choose a CA certificate to trust for the upstream destination connection. Import a self-signed certificate or a CA certificate into the OPNsense `System - Trust - Authorities` store, and select it here.
**TLS Server Name**                 If the SAN (Subject Alternative Name) of the offered trusted CA certificate or self-signed certificate doesn't match with the IP address or hostname of the `Upstream Domain`, enter it here. This will change the SNI (Server Name Identification) of Caddy to the `TLS Server Name`. IP address e.g. ``192.168.1.1`` or hostname e.g. ``localhost`` or ``opnsense.local`` are all valid choices. Only if the SAN and SNI match, the TLS connection will work, otherwise an error is logged that can be used to troubleshoot.
=================================== ================================

.. Attention:: Only use `TLS Insecure Skip Verify` if absolutely necessary. Using it makes the connection to the upstream destination insecure. It might look like an easy way out for all kinds of certiciate issues, but in the end it is always a bad choice and proper certificate handling is strongly preferred. Please use the `TLS`, `TLS Trusted CA Certificates` and `TLS Server Name` options instead to get a **secure TLS connection** to the upstream destination. Another option is to use plain HTTP, since it doesn't imply that the connection is secure and encrypted.


----------------------------
Reverse Proxy - Access Lists
----------------------------

=========================== ================================
Option                      Description
=========================== ================================
**Access List name**        Choose a name for the Access List, for example ``private_ips``.
**Client IP Addresses**     Enter any number of IPv4 and IPv6 addresses or networks that this access list should contain. For matching only internal networks, add ``192.168.0.0/16`` ``172.16.0.0/12`` ``10.0.0.0/8`` ``127.0.0.1/8`` ``fd00::/8`` ``::1``.
**HTTP Response Code**      Set a custom HTTP response code that should be returned to the requesting client when the access list doesn't match. Setting this will replace "Abort Connections", all clients will stay connected but will receive the response code. Generally, using "Abort Connections" is recommended, because it will actively disconnect clients without serving anything.
**HTTP Response Message**   Set a custom HTTP response message in addition to the HTTP response code. 
**Invert List**             Invert the logic of the access list. If unchecked, the Client IP Addresses will be allowed. If checked, the Client IP Addresses will be blocked.
=========================== ================================

.. Note:: Go back to domains or subdomains and add the access list to them. All handlers created under these domains will get an additional matcher. That means, the requests still reach Caddy, but if the IP Addresses don't match with the access list, the request will be dropped before being reverse proxied.


--------------------------
Reverse Proxy - Basic Auth
--------------------------

=========================== ================================
Option                      Description
=========================== ================================
**User**                    Enter a username. Afterwards, select it in domains or subdomains to restrict access with basic auth. Usernames are only allowed to have alphanumeric characters.
**Password**                Enter a password. Write it down. It will be hashed with bcrypt. It can only be set and changed but won't be visible anymore. The hash can't be turned back into the original password.
=========================== ================================

.. Note:: Basic auth matches after access lists, so set both to first restrict access by IP address, and then additionally by username and password. Don't set basic auth on top of a wildcard domain directly, always set it on the subdomains instead.


-----------------------
Reverse Proxy - Headers
-----------------------

=========================== ================================
Option                      Description
=========================== ================================
**Header**                  ``header_up`` sets, adds (with the + prefix), deletes (with the - prefix), or performs a replacement (by using two arguments, a search and replacement) in a request header going upstream to the backend. ``header_down`` sets, adds (with the + prefix), deletes (with the - prefix), or performs a replacement (by using two arguments, a search and replacement) in a response header coming downstream from the backend. For more information: https://caddyserver.com/docs/caddyfile/directives/reverse_proxy#headers.
**Header Type**             Enter a header, for example ``Host``. Use the ``+`` or ``-`` prefix to add or remove this header, for example ``-Host`` or ``+Host``. A suffix match like ``-Host-*`` is also supported. To replace a header, use ``Some-Header`` without ``+`` or ``-``.
**Header Value**            Enter a value for the above header. One of the most common options is ``{upstream_hostport}``. It's also possible to use a regular expression to search for a specific value in a header. For example: ``^prefix-([A-Za-z0-9]*)$`` which uses the regular expression language RE2 included in Go.
**Header Replace**          If a regular expression is used to search for a `Header Value`, here the replacement string can be set. For example: ``replaced-$1-suffix`` which expands the replacement string, allowing the use of captured values, ``$1`` being the first capture group.
=========================== ================================

.. Attention:: Setting headers to handlers should be considered an advanced option for experts. Please don't set them without any reason. Caddy uses safe defaults. https://caddyserver.com/docs/caddyfile/directives/reverse_proxy#defaults


================
caddy: Tutorials
================

.. Attention:: The tutorial section implies that `Prepare OPNsense for Caddy after installation` has been followed.
.. Note:: Filling out `Description` fields is mandatory because they are used to display and reference items in forms and error messages.


-------------------------------
Creating a simple reverse proxy
-------------------------------

.. Note:: Make sure the chosen domain is externally resolvable. Create an A-Record with an external DNS Provider that points to the external IP Address of the OPNsense.

Go to `Services - Caddy Web Server - General Settings`

* Check **enabled**
* Input a valid Email address into the `Acme Email` field. This should be seen as mandatory to receive automatic Let's Encrypt and ZeroSSL certificates.
* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy - Domains`

* Press **+** to create a new domain

============================== ====================
Options                        Values
============================== ====================
**Domain:**                    ``foo.example.com``
============================== ====================

* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy - Handler`

* Press **+** to create a new Handler

============================== ====================
Options                        Values
============================== ====================
**Domain:**                    ``foo.example.com``
**Upstream Domain:**           ``192.168.10.1``
============================== ====================

* Press **Save** and **Apply**

.. Note:: After just a few seconds the Let's Encrypt certificate will be installed and the reverse proxy works. Check the Logfile for that. Now the TLS Termination reverse proxy is configured.
.. Note:: **Result:** HTTPS foo.example.com:80/443 --> OPNsense (Caddy) --> HTTP 192.168.10.1:80


-------------------------------
Restrict Access to internal IPs
-------------------------------

.. Tip:: The reverse proxy will accept all connections. Restricting access with a firewall rule, would impact all domains. That's where `Access Lists` come in handy. They can be used to restrict access per domain. In this example, they are used to restrict access to only internal IPv4 networks, refusing connections from the internet.

Go to `Services - Caddy Web Server - Reverse Proxy - Access - Access Lists`

* Press **+** to create a new `Access List`

============================== ============================================================
Options                        Values
============================== ============================================================
**Access List Name:**          ``private_ipv4``
**Client IP Addresses:**       ``192.168.0.0/16`` ``172.16.0.0/12`` ``10.0.0.0/8``
**Description:**               ``Allow access from private IPv4 ranges``
============================== ============================================================

* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy - Domains`

* Edit an existing `Domain` or `Subdomain` and expand the `Access` Tab.

============================== ====================
Options                        Values
============================== ====================
**Access List:**               ``private_ipv4``
============================== ====================

* Press **Save** and **Apply**

Now, all connections not having a private IPv4 address will be served an empty page for the chosen domain. To outright refuse the connection, the option ``Abort Connections`` in `Services: Caddy Web Server: General Settings` should be additionally enabled.

.. Note:: Some applications might demand a HTTP Error code instead of having their connection refused, an example could be monitoring systems. For these, in `advanced mode` of `Access Lists`, a custom ``HTTP Response Code`` can be enabled.


-----------------
Using dynamic DNS
-----------------

Go to `Services - Caddy Web Server - General Settings - DNS Provider`

* Select one of the supported DNS Providers from the list
* Input the `DNS API Key`, and any number of the additional required fields in `Additional Fields`. Read the full help for details.

Go to `Services - Caddy Web Server - General Settings - Dynamic DNS`

* Choose if `DynDns IP Version` should include IPv4 and/or IPv6.
* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy – Domains`

* Press **+** to create a new Domain. ``mydomain.duckdns.org`` is an example if `duckdns` is used as DNS Provider.

============================== ========================
Options                        Values
============================== ========================
**Domain:**                    ``mydomain.duckdns.org``
**Dynamic DNS:**               ``X``
============================== ========================

Go to `Services - Caddy Web Server - Reverse Proxy – Handlers`

* Press **+** to create a new handler

============================== ========================
Options                        Values
============================== ========================
**Domain:**                    ``mydomain.duckdns.org``
**Upstream Domain:**           ``192.168.1.1``
============================== ========================

* Press **Save** and **Apply**

.. Note:: Now Caddy listens on Port 80 and 443, and reverse proxies everything from mydomain.duckdns.org to 192.168.1.1:80. All headers and the real IP are automatically passed to the upstream destination. Let's Encrypt Certificate and Dynamic DNS Updates are all handled automatically.


---------------------------------
Creating a wildcard reverse proxy
---------------------------------

.. Attention:: The certificate of a wildcard domain will only contain ``*.example.com``, not a SAN for ``example.com``. Create an additional domain for ``example.com`` and create a handler for the upstream destination.

Go to `Services - Caddy Web Server - General Settings - DNS Provider`

* Select one of the supported DNS Providers from the list
* Input the `DNS API Key`, and any number of the additional required fields in `Additional Fields`. Read the full help for details.

Go to `Services - Caddy Web Server - Reverse Proxy – Domains`

* Create ``*.example.com`` as domain and activate the `DNS-01` checkbox. Alternatively, use a certificate imported or generated in `System - Trust - Certificates`. It has to be a wildcard certificate.
* Create all subdomains in relation to the ``*.example.com`` domain. So for example ``foo.example.com`` and ``bar.example.com``.

Go to `Services - Caddy Web Server - Reverse Proxy – Handlers`

* Create a Handler with ``*.example.com`` as domain and ``foo.example.com`` as subdomain. Mostly the same configuration as with normal domains is possible. There are some features that are only possible with normal domains.

.. Tip:: If in doubt, don't use subdomains. If there should be ``foo.example.com``, ``bar.example.com`` and ``example.com``, just create them as three normal domains. This way, there is the most flexibility, and the most features are supported.


--------------------------------
Reverse proxy the OPNsense WebUI
--------------------------------

* Open the OPNsense WebUI in a Browser (e.g. Chrome or Firefox). Inspect the certificate. Copy the SAN for later use, for example ``OPNsense.localdomain``.
* Save the certificate as .pem file. Open it up with a text editor, and copy the contents into a new entry in `System - Trust - Authorities`. Name the certificate ``opnsense-selfsigned``.
* Add a new Domain in Caddy, for example ``opn.example.com``. Make sure the name is externally resolvable to the WAN IP of the OPNsense.
* Add a new Handler with the following options:

=================================== ============================
Options                             Values
=================================== ============================
**Domain:**                         ``opn.example.com``
**Upstream Domain:**                ``127.0.0.1``
**Upstream Port:**                  ``8443 (Webui Port)``
**TLS:**                            ``X``
**TLS Trusted CA Certificates:**    ``opnsense-selfsigned``
**TLS Server Name:**                ``OPNsense.localdomain``
=================================== ============================

* Press **Save** and **Apply**

Go to `System - Settings - Administration`

* Input ``opn.example.com`` in `Alternate Hostnames` to prevent the error `The HTTP_REFERER "https://opn.example.com/" does not match the predefined settings` after logging in.
* Press **Save**

.. Note:: Open ``https://opn.example.com`` and it should serve the reverse proxied OPNsense WebUI. Check the log file for errors if it doesn't work, most of the time the TLS Server Name doesn't match the SAN of the `TLS Trusted CA Certificate`. Caddy doesn't support CN (Common Name) in certificate since it's been deprecated since many years. Only SAN certificates work.
.. Attention:: Create an access list to restrict access to the WebUI. Add that access list to this domain.


-------------------------------
Redirect ACME HTTP-01 challenge
-------------------------------

Sometimes an application behind Caddy uses its own ACME Client to get certificates, most likely with the HTTP-01 challenge. This plugin has a built in mechanism to redirect this challenge type easily to a destination behind it.

.. Note:: Make sure the chosen domain is externally resolvable. Create an A-Record with an external DNS Provider that points to the external IP Address of the OPNsense. In case of IPv6 availability, it is mandatory to create an AAAA-Record too, otherwise the TLS-ALPN-01 challenge might fail.

.. Attention:: It is mandatory that the domain in Caddy uses an empty port or 443 in the GUI, otherwise it can't use the TLS-ALPN-01 challenge for itself. The upstream destination has to listen on Port 80 and serve ``/.well-known/acme-challenge/``, for the same domain that is configured in Caddy.

Go to `Services - Caddy Web Server - Reverse Proxy - Domains`

* Press **+** to create a new domain
* enable `advanced mode`

=================================== ====================
Options                             Values
=================================== ====================
**Domain:**                         ``foo.example.com``
**Description:**                    ``foo.example.com``
**HTTP-01 challenge redirection:**  ``192.168.10.1``
=================================== ====================

* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy - Handler`

* Press **+** to create a new Handler

=================================== ============================
Options                             Values
=================================== ============================
**Domain:**                         ``foo.example.com``
**Upstream Domain:**                ``192.168.10.1``
**Upstream Port:**                  ``443``
**TLS:**                            ``X``
**TLS Server Name**:                ``foo.example.com``
=================================== ============================

* Press **Save** and **Apply**

.. Note:: With this configuration, Caddy will eventually choose the TLS-ALPN-01 challenge for its own ``foo.example.com`` domain, and reverse proxy the HTTP-01 challenge to ``192.168.10.1``, where the upstream destination can listen on port 80 for ``foo.example.com`` and solve its own challenge for a certificate. With TLS enabled in the Handler, an encrypted connection is automatically possible. The automatic HTTP to HTTPS redirection is also taken care of.


-----------------------------------------------------
Reverse Proxy to an upstream webserver serving vhosts
-----------------------------------------------------

Sometimes it is necessary to alter the host header in order to reverse proxy to another webserver with vhosts. Since Caddy passes the original host header by default (e.g. ``app.external.example.com``), if the upstream destination listens on a different hostname (e.g. ``app.internal.example.com``), it wouldn't be able to serve this request.

Go to `Services - Caddy Web Server - Reverse Proxy - Domains`

* Press **+** to create a new domain

=================================== ============================
Options                             Values
=================================== ============================
**Domain:**                         ``app.external.example.com``
=================================== ============================

* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy - Headers`

* Press **+** to create a new header

=================================== ============================
Options                             Values
=================================== ============================
**Header:**                         ``header_up``
**Header Type:**                    ``Host``
**Header Value:**                   ``{upstream_hostport}``
=================================== ============================

* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy - Handler`

* Press **+** to create a new Handler

=================================== ========================================
Options                             Values
=================================== ========================================
**Domain:**                         ``app.external.example.com``
**Upstream Domain:**                ``app.internal.example.com``
**Header Manipulation:**            ``header_up Host {upstream_hostport}``
=================================== ========================================

* Press **Save** and **Apply**

.. Tip:: Since (most) headers retain their original value when being proxied, it is often necessary to override the Host header with the configured upstream address when proxying to HTTPS, such that the Host header matches the TLS ServerName value. https://caddyserver.com/docs/caddyfile/directives/reverse_proxy#https


-------------------------------
Integrating Caddy with CrowdSec
-------------------------------

.. Tip:: CrowdSec is a powerful alternative to a WAF. It uses logs to dynamically ban IP addresses of known bad actors. The Caddy plugin is prepared to emit the json logs for this integration.

Go to `Services - Caddy Web Server - General Settings - Log Settings`

* Enable `Log HTTP Access in JSON Format`
* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy – Domains`

* Open each domain that should be monitored by CrowdSec
* Open `Access`
* Enable `HTTP Access Log`

.. Note:: Now the HTTP access logs will appear in ``/var/log/caddy/access`` in json format, one file for each domain.

Next, connect to the OPNsense via SSH or console, go into the shell with Option 8.

.. Attention:: This step requires the ``os-crowdsec`` plugin.

* Once in the shell, install the caddy collection from CrowdSec Hub. ``cscli collections install crowdsecurity/caddy``
* Create the configuration file as ``/usr/local/etc/crowdsec/acquis.d/caddy.yaml`` with the following content:

.. code-block::

    filenames:
      - /var/log/caddy/access/*.log

    force_inotify: true
    poll_without_inotify: true

    labels:
      type: caddy

* Go into the OPNsense WebUI and restart CrowdSec.


----------------------------------
Caddy and High Availability Setups
----------------------------------

There are a few possible configurations to run Caddy successfully in a High Availability Setup with two OPNsense firewalls.

.. Tip:: The main issue to think about is the certificate handling. If a CARP VIP is used on the WAN interface, and the A and AAAA Records of all domains point to this CARP VIP, the backup Caddy won't be able to issue ACME certificates without some additional configuration.

There are three methods that support XMLRPC sync:

.. Note:: These methods can be mixed, just make sure to use a coherent configuration. It's best to decide for one method.

* Using custom certificates from the OPNsense Trust store for all domains.
* Using the `DNS-01 challenge` in the settings of domains.
* Using the `HTTP-01 challenge redirection` option in the advanced settings of domains.

Since the HTTP-01 challenge redirection needs some additional steps to work, it should be set up as followed:

* Configure Caddy on the master OPNsense firewall until the whole initial configuration is completed.
* On the master OPNsense, select each domain, and set the IP Address in `HTTP-01 challenge redirection` to the same value as in `Synchronize Config to IP` found in `System - High Availability - Settings`.
* Create a new Firewall rule on the master OPNsense that allows Port ``80`` and ``443`` to ``This Firewall`` on the interface that has the prior selected IP Address (most likely LAN or a VLAN interface).
* Sync this configuration with XMLRPC sync. Restart Caddy on both Firewalls.

.. Note:: Now both Caddy instances will be able to issue ACME certificates at the same time. Caddy on the master OPNsense uses the TLS-ALPN-01 challenge for itself and reverse proxies the HTTP-01 challenge to the Caddy of the backup OPNsense. Please make sure, that the master and backup OPNsense are listening on their WAN and LAN (or VLAN) interfaces on port ``80`` and ``443``, since both ports are required for these challenges to work.

.. Tip:: Check the Logfile on both Caddy instances for successful challenges. Look for ``certificate obtained successfully`` Informational messages.


-------------------------------------
Keeping track of large configurations
-------------------------------------

Having a large configuration can become a bit cumbersome to navigate. To help, a new filter functionality has been added to the top right corner of the `Domains` and `Handlers` tab, called `Filter by Domain`.

.. Tip:: In `Filter by Domain`, one or multiple `Domains` can be selected, and as filter result, only their corresponding configuration will be displayed in `Domains`, `Subdomains` and `Handlers`. This makes keeping track of large configurations a breeze.


------------------------
Advanced Troubleshooting
------------------------

Sometimes, things don't work as expected. Caddy provides a few powerful debugging tools to see what's going on.

.. Note:: As first troubleshooting step, change the global Log Level to `DEBUG`. This will log `everything` the reverse_proxy directive handles.

Go to `Services - Caddy Web Server - General Settings - Log Settings`

* Set the `Log Level` to `DEBUG`
* Press **Apply**

Go to `Services - Caddy Web Server - Log File`

* Change the dropdown from `INFORMATIONAL` to `DEBUG`

Now the ``reverse_proxy`` debug logs will be visible.

.. Note:: As troubleshooting for developers and experts, a special admin endpoint can be activated.

.. Attention:: This admin endpoint is deactivated by default. To enable it and access it on the OPNsense, follow these additional steps. Don't forget to deactivate it again. Anybody with network access to the admin endpoint can use REST API to change the running configuration of Caddy, without authentication.

* SSH into the OPNsense shell
* Stop Caddy with ``configctl caddy stop``
* Go to ``/usr/local/etc/caddy/caddy.d/``
* Create a new file called ``admin.global`` and put the following content into it: ``admin :2019``
* After saving the file, go to ``/usr/local/etc/caddy`` and run ``caddy validate`` to ensure the configuration is valid.
* Start Caddy with ``configctl caddy start``
* Use sockstat to see if the admin endpoint has been created. ``sockstat -l | grep -i caddy`` - it should show the endpoint ``*:2019``.
* Create a firewall rule on ``LAN`` that allows ``TCP`` to destination ``This Firewall`` and destination port ``2019``.
* Open the admin endpoint: ``http://YOUR_LAN_IP:2019/debug/pprof/``

.. Note:: Follow the instructions on https://caddyserver.com/docs/profiling how to debug and profile Caddy.


--------------------------------
Using custom configuration files
--------------------------------

* The Caddyfile has an additional import from the path ``/usr/local/etc/caddy/caddy.d/``. Place custom configuration files inside that adhere to the Caddyfile syntax.
* ``*.global`` files will be imported into the global block of the Caddyfile.
* ``*.conf`` files will be imported at the end of the Caddyfile. Don't forget to test the custom configuration with ``caddy validate --config /usr/local/etc/caddy/Caddyfile``.

.. Note:: With these imports, the full potential of Caddy can be unlocked. The GUI options will remain focused on the reverse proxy. There is no community support for configurations that have not been created with the offered GUI.
