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
**Interface**               WAN
**TCP/IP Version**          IPv4+IPv6
**Protocol**                TCP/UDP
**Source**                  Any
**Destination**             This Firewall
**Destination port range**  from: HTTP to: HTTP
**Description**             Caddy Reverse Proxy HTTP
=========================== ================================

=========================== ================================
Option                      Values
=========================== ================================         
**Interface**               WAN
**TCP/IP Version**          IPv4+IPv6
**Protocol**                TCP/UDP
**Source**                  Any
**Destination**             This Firewall
**Destination port range**  from: HTTPS to: HTTPS
**Description**             Caddy Reverse Proxy HTTPS
=========================== ================================

Go to `Firewall - Rules - LAN` and create the same rules for the `LAN` interface. Now external and internal clients can connect to Caddy, and Let's Encrypt or ZeroSSL certificates will be issued automatically.


---
FAQ
---

* A DNS Provider is not required. With a static WAN IP, just skip the DNS Provider configuration and don't check the DNS-01 and Dynamic DNS checkboxes. Let's Encrypt will work with HTTP-01 (Port 80) or TLS-ALPN-01 (Port 443) challenge automatically.
* Port Forwards, NAT Reflection or Split Horizon DNS are not required. Only create Firewall rules that allow traffic to hit the ports that Caddy opens. That is 80 (optionally) and 443 (required). If only Port 443 is opened, and IPv6 is available, make sure the Firewall rule allows IPv6 traffic to reach Caddy on WAN.
* Firewall rules to allow Caddy to reach Backend Servers are not required. OPNsense has a default rule that allows all traffic originating from it to be allowed.
* ACME Clients on reverse proxied Backend Servers won't be able to issue certificates. Caddy intercepts ``/.well-known/acme-challenge``. Either configure the DNS-01 challenge on these servers, use a self-signed certificate, or turn off TLS. In trusted networks, TLS is usually not needed. Caddy is primarily a `TLS Termination Proxy`.
* When using Caddy with IPv6, it's best to have a GUA (Global Unicast Address) on the WAN interface.
* Let's Encrypt or ZeroSSL can't be explicitely chosen. Caddy automatically issues one of these options, determined by speed and availability.

.. Attention:: There is no TCP/UDP stream, load balancing and WAF (Web Application Firewall) support in this plugin. Caddy itself could support these features, but this plugin is focused on ease of configuration. For a business ready Reverse Proxy with WAF functionality, use OPNWAF. For TCP/UDP streaming, use either nginx or ha-proxy.

.. Tip:: As an alternative to a WAF, it's simple to integrate Caddy with CrowdSec. Check the tutorial section for guidance.


====================
caddy: Configuration
====================

.. Note:: Caddy resides in "Services: Caddy Web Server". Some options are hidden in advanced mode.


--------------------------
General Settings - General
--------------------------

=========================== ================================
Option                      Description
=========================== ================================
**enabled**                 `enable` or `disable` Caddy. If enabled, Caddy will serve the configuration and autostart with the OPNsense.
**ACME Email**              e.g. `info@example.com`, it's optional for receiving Email updates on Let's Encrypt certificates.
**Auto HTTPS**              `On (default)` creates automatic Let's Encrypt certificates for all domains that don't have more specific options set, like custom certificates.
**Trusted Proxies**         If Cloudflare or another CDN provider is used, create an `Access List` with the IP addresses of that CDN and add it here. Add the same Access List to the domain this CDN tries to reach.
**Abort Connections**       This option, when enabled, aborts all connections to the domain that don't match any specified handler or access list. This setting doesn't affect Let's Encrypt's ability to issue certificates, ensuring secure connections regardless of the option's status. If unchecked, the domain remains accessible even without a matching handler, allowing for connectivity and certificate checks, even in the absence of a configured Backend Server. When using Access Lists, enabling this option is recommended to reject unauthorized connections outright. Without this option, unmatched IP addresses will encounter an empty page instead of an explicit rejection, though the Access Lists continue to function and restrict access.
=========================== ================================


-------------------------------
General Settings - DNS Provider
-------------------------------

=========================== ================================
Option                      Description
=========================== ================================
**DNS Provider**            Select the DNS provider for the `DNS-01 Challenge` and `Dynamic DNS`. This is optional, since certificates will be requested from Let's Encrypt via HTTP-01 or TLS-ALPN-01 challenge when this option is unset. Needed for wildcard certificates, and for dynamic DNS. To use the DNS-01 challenge and dynamic DNS, enable the checkbox in a domain or subdomain. For more information: https://github.com/caddy-dns
**DNS API Fields**          These fields are for the API settings of the chosen DNS Provider. All of these fields can be left empty if they are optional with the chosen provider. The help text in the plugin will list all available providers and their expected configurations. There are additional fields in the advanced mode if DNS providers require more fields for their configurations.
=========================== ================================


------------------------------
General Settings - Dynamic DNS
------------------------------

=========================== ================================
Option                      Description
=========================== ================================
**DynDns Check Http**       Optionally, enter an URL to test the current IP address of the firewall via HTTP procotol. Generally, this is not needed. Caddy uses default providers to test the current IP addresses. For using a custom one, enter the `https://` link to an IP address testing website.
**DynDns Check Interface**  Optionally, select an interface to extract the current IP address of the firewall. At most, one current IPv6 Global Unicast Address and one current IPv4 non-RFC1918 Address will be extracted.
**DynDns Check Interval**   Interval to poll for changes of the IP address. The default is 5 minutes. Can be a number between 1 to 1440 minutes.
**DynDns IP Version**       Leave on `None` to set IPv4 A-Records and IPv6 AAAA-Records. Select `Ipv4 only` for setting A-Records. Select `IPv6 only` for setting AAAA-Records.
**DynDns TTL**              Set the TTL (time to live) for DNS Records. The default is 1 hour. Can be a number between 1 to 24 hours.
=========================== ================================


-------------------------------
General Settings - Log Settings
-------------------------------

======================================= ================================
Option                                  Description
======================================= ================================
**Log Credentials**                     Log all Cookies and Authorization Headers in HTTP request logging. Use combined with HTTP Access Log in a domain. Enable this option only for troubleshooting.
**Log Access in Plain Format**          Don't send HTTP access logs to the central OPNsense logging facility but save them in plain Caddy JSON format in a subdirectory instead. Only effective for domains that have HTTP Access Log enabled. The feature is intended to have access log files processed by e.g. CrowdSec. They can be found in ``/var/log/caddy/access``.
**Keep Plain Access Logs for (days)**   How many days until the plain format log files are deleted. The default is 10 days.
======================================= ================================


-----------------------
Reverse Proxy - Domains
-----------------------

=========================== ================================
Option                      Description
=========================== ================================
**enabled**                 `enable` or `disable` this domain
**Reverse Proxy Domain**    Can either be a domain name or an IP address. If a domain name is chosen, Caddy will automatically try to get a Let's Encrypt or ZeroSSL certificate, and the headers and real IP address will be automatically passed to the Backend Server.
**Reverse Proxy Port**      Should be the port the OPNsense will listen on. Don't forget to create Firewall rules that allow traffic to this port on ``WAN`` and ``LAN`` to destination ``This Firewall``. Leave this empty if the default ports of Caddy (`80` and `443`) should be used with automatic redirection from HTTP to HTTPS.
**Access List**             Restrict the access to this domain to a list of IP addresses defined in the Access Tab. This doesn't influence Let's Encrypt certificate generation.
**Basic Auth**              Restrict the access to this domain to one or multiple users defined in the Access Tab. This doesn't influence the Let's Encrypt certificate generation.
**DNS-01 challenge**        Enable this for using DNS-01 instead of HTTP-01 and TLS-ALPN-01 challenge. This can be set per entry, so both types of challenges can be used at the same time for different entries. This option needs the `General Settings - DNS Provider` configured.
**Dynamic DNS**             Enable Dynamic DNS. As the option above, the DNS Provider is a requirement. The DNS Records of this domain will be automatically updated with the chosen DNS Provider.
**Custom Certificate**      Use a certificate imported or generated in `System - Trust - Certificates`. The chain is generated automatically. Certificate + Intermediate CA + Root CA, Certificate + Root CA and self signed Certificate are all fully supported. Only SAN certificates will work.
**HTTP Access Log**         Enable the HTTP request logging for this domain and its subdomains. This option is mostly for troubleshooting or log analyzing tools like CrowdSec, since it will log every single request.
**Description**             The description is mandatory. Create descriptions for each domain. Since there could be multiples of the same domain with different ports, do it like this: ``foo.example.com`` and ``foo.example.com.8443``.
=========================== ================================


--------------------------
Reverse Proxy - Subdomains
--------------------------

=========================== ================================
Option                      Description
=========================== ================================
**Reverse Proxy Domain**    Choose a wildcard domain prepared in domains, it has to be formatted like ``*.example.com``
**Reverse Proxy Subdomain** Create a name that is seated under the wildcard domain, for example ``foo.example.com`` and ``bar.example.com``.
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
**Reverse Proxy Domain**            Select a domain.
**Reverse Proxy Subdomain**         Select a subdomain. This will put the handler on the subdomain instead of the domain. Use only with wildcard domains and subdomains.
**Handle Type**                     `handle` or `handle path` can be chosen. If in doubt, always use `handle`, the most common option. `handle path` is used to strip the path from the URI.
**Handle Path**                     Leave this empty to create a catch all location or enter a location like  `/foo/*` or `/foo/bar*`.
**Backend Server Domain**           Should be an internal domain name or an IP Address of the Backend Server that should receive the reverse proxied traffic.
**Backend Server Port**             Should be the port the Backend Server listens on. This can be left empty to use Caddy default port 80.
**Backend Server Path**             In case the backend application resides in a sub-path of the web root and its path shouldn't be visible in the frontend URL, this setting can be used to prepend an initial path starting with '/' to every backend request. Java applications running in a servlet container like Tomcat are known to behave this way, so set it to e.g. '/guacamole' to access Apache Guacamole at the frontend root URL without needing a redirect.
**TLS**                             If the Backend Server only accepts HTTPS, enable this option. If the Backend Server has a globally trusted certificate, this TLS option is the only needed one.
**TLS Trusted CA Certificates**     Choose a CA certificate to trust for the Backend Server connection. Import a self-signed certificate or a CA certificate into the OPNsense `System - Trust - Authorities` store, and select it here.
**TLS Server Name**                 If the SAN (Subject Alternative Name) of the offered trusted CA certificate or self-signed certificate doesn't match with the IP address or hostname of the `Backend Server Domain`, enter it here. This will change the SNI (Server Name Identification) of Caddy to the `TLS Server Name`. IP address e.g. ``192.168.1.1`` or hostname e.g. ``localhost`` or ``opnsense.local`` are all valid choices. Only if the SAN and SNI match, the TLS connection will work, otherwise an error is logged that can be used to troubleshoot.
**NTLM**                            If the Backend Server needs NTLM authentication, enable this option together with TLS. For example, Exchange Server.
**TLS Insecure Skip Verify**        Turns off TLS handshake verification, making the connection insecure and vulnerable to man-in-the-middle attacks. Do not use in production.
=================================== ================================

.. Attention:: Only use `TLS Insecure Skip Verify` if absolutely necessary. Using it makes the connection to the Backend Server insecure. It might look like an easy way out for all kinds of certiciate issues, but in the end it is always a bad choice and proper certificate handling is strongly preferred. Please use the `TLS`, `TLS Trusted CA Certificates` and `TLS Server Name` options instead to get a **secure TLS connection** to the Backend Server. Another option is to use plain HTTP, since it doesn't imply that the connection is secure and encrypted.


-------------------------------------
Reverse Proxy - Access - Access Lists
-------------------------------------

=========================== ================================
Option                      Description
=========================== ================================
**Access List name**        Choose a name for the Access List, for example ``private_ips``.
**Client IP Addresses**     Enter any number of IPv4 and IPv6 addresses or networks that this access list should contain. For matching only internal networks, add `192.168.0.0/16` `172.16.0.0/12` `10.0.0.0/8` `127.0.0.1/8` `fd00::/8` `::1`.
**Invert List**             Invert the logic of the access list. If unchecked, the Client IP Addresses will be allowed. If checked, the Client IP Addresses will be blocked.
=========================== ================================

.. Note:: Go back to domains or subdomains and add the access list to them (advanced mode). All handlers created under these domains will get an additional matcher. That means, the requests still reach Caddy, but if the IP Addresses don't match with the access list, the request will be dropped before being reverse proxied.


-----------------------------------
Reverse Proxy - Access - Basic Auth
-----------------------------------

=========================== ================================
Option                      Description
=========================== ================================
**User**                    Enter a username. Afterwards, select it in domains or subdomains to restrict access with basic auth. Usernames are only allowed to have alphanumeric characters.
**Password**                Enter a password. Write it down. It will be hashed with bcrypt. It can only be set and changed but won't be visible anymore. The hash can't be turned back into the original password.
=========================== ================================

.. Note:: Basic auth matches after access lists, so set both to first restrict access by IP address, and then additionally by username and password. Don't set basic auth on top of a wildcard domain directly, always set it on the subdomains instead.

================
caddy: Tutorials
================

.. Attention:: The tutorial section implies that `Prepare OPNsense for Caddy after installation` has been followed.


-------------------------------
Creating a simple reverse proxy
-------------------------------

.. Note:: Make sure the chosen domain is externally resolvable. Create an A-Record with an external DNS Provider that points to the external IP Address of the OPNsense.

Go to `Services - Caddy Web Server - General Settings`

* Check **enabled** and press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy - Domains`

* Press **+** to create a new domain
* **Reverse Proxy Domain:** `foo.example.com`
* **Description:** `foo.example.com`
* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy - Handler`

* Press **+** to create a new Handler
* **Reverse Proxy Domain:** `foo.example.com`
* **Backend Server Domain:** `192.168.10.1`
* Press **Save** and **Apply**

.. Note:: Leave all other fields to default or empty. After just a few seconds the Let's Encrypt certificate will be installed and the reverse proxy works. Check the Logfile for that. Now the TLS Termination reverse proxy is configured.
.. Note:: **Result:** HTTPS foo.example.com:80/443 --> OPNsense (Caddy) --> HTTP 192.168.10.1:80


-----------------
Using dynamic DNS
-----------------

Go to `Services - Caddy Web Server - General Settings - DNS Provider`

* Select one of the supported DNS Providers from the list
* Input the `DNS API Key`, and any number of the additional required fields in advanced mode. Read the full help for details.

Go to `Services - Caddy Web Server - General Settings - Dynamic DNS`

* Choose if `DynDns IP Version` should include IPv4 and/or IPv6. None option means both protocols.
* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy – Domains`

* Press **+** to create a new Reverse Proxy Domain. `mydomain.duckdns.org` is an example if `duckdns` is used as DNS Provider.

============================== ====================
Options                        Values
============================== ====================
Reverse Proxy Domain           mydomain.duckdns.org
DNS-01                         enabled
Dynamic DNS                    enabled
Description                    mydomain.duckdns.org
============================== ====================

Go to `Services - Caddy Web Server - Reverse Proxy – Handlers`

* Press **+** to create a new handler

============================== ====================
Options                        Values
============================== ====================
Reverse Proxy Domain           mydomain.duckdns.org
Backend Server                 192.168.1.1
============================== ====================

* Press **Save** and **Apply**

.. Note:: Now Caddy listens on Port 80 and 443, and reverse proxies everything from mydomain.duckdns.org to 192.168.1.1:80. All headers and the real IP are automatically passed to the Backend Server. For different ports, check the advanced settings. Let's Encrypt Certificate and Dynamic DNS Updates are all handled automatically.


---------------------------------
Creating a wildcard reverse proxy
---------------------------------

Go to `Services - Caddy Web Server - General Settings - DNS Provider`

* Select one of the supported DNS Providers from the list
* Input the `DNS API Key`, and any number of the additional required fields in advanced mode. Read the full help for details.

Go to `Services - Caddy Web Server - Reverse Proxy – Domains`

* Create ``*.example.com`` as domain and activate the `DNS-01` checkbox. A DNS Provider has to be configured. Alternatively, use a certificate imported or generated in `System - Trust - Certificates`. It has to be a wildcard certificate.
* Create all subdomains in relation to the ``*.example.com`` domain. So for example ``foo.example.com`` and ``bar.example.com``.

Go to `Services - Caddy Web Server - Reverse Proxy – Handlers`

* Create a Handler with ``*.example.com`` as domain and ``foo.example.com`` as subdomain. All the same configuration as with normal domains is possible.


--------------------------------
Reverse proxy the OPNsense WebUI
--------------------------------

* Open the OPNsense WebUI in a Browser (e.g. Chrome or Firefox). Inspect the certificate. Copy the SAN for later use, for example ``OPNsense.localdomain``.
* Save the certificate as .pem file. Open it up with a text editor, and copy the contents into a new entry in `System - Trust - Authorities`. Name the certificate ``opnsense-selfsigned``.
* Add a new Domain in Caddy, for example ``opn.example.com``. Make sure the name is externally resolvable to the WAN IP of the OPNsense.
* Add a new Handler with the following options (enable advanced mode):

=================================== ====================
Options                             Values
=================================== ====================
**Reverse Proxy Domain**            opn.example.com
**Backend Server Domain**           127.0.0.1
**Backend Server Port**             8443 (Webui Port)
**TLS**                             enabled
**TLS Trusted CA Certificates**     opnsense-selfsigned
**TLS Server Name**                 OPNsense.localdomain
=================================== ====================

* Press **Save** and **Apply**

.. Note:: Open ``https://opn.example.com`` and it should serve the reverse proxied OPNsense WebUI. Check the log file for errors if it doesn't work, most of the time the TLS Server Name doesn't match the SAN of the `TLS Trusted CA Certificate`. Caddy doesn't support CN (Common Name) in certificate since it's been deprecated since many years. Only SAN certificates work.
.. Attention:: Create an access list to restrict access to the WebUI. Add that access list to the domain in advanced mode.


-------------------------------
Integrating Caddy with CrowdSec
-------------------------------

.. Tip:: CrowdSec is a powerful alternative to a WAF. It uses logs to dynamically ban IP addresses of known bad actors. The Caddy plugin is prepared to emit the json logs for this integration.

Go to `Services - Caddy Web Server - General Settings - Log Settings`

* Enable `advanced mode`
* Enable `Log HTTP Access in JSON Format`
* Press **Save**

Go to `Services - Caddy Web Server - Reverse Proxy – Domains`

* Open each domain that should be monitored by CrowdSec
* Enable `advanced mode`
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


--------------------------------
Using custom configuration files
--------------------------------

* The Caddyfile has an additional import from the path ``/usr/local/etc/caddy/caddy.d/``. Place custom configuration files inside that adhere to the Caddyfile syntax.
* ``*.global`` files will be imported into the global block of the Caddyfile.
* ``*.conf`` files will be imported at the end of the Caddyfile. Don't forget to test the custom configuration with `caddy run --config /usr/local/etc/caddy/Caddyfile`.
* With these imports, the full potential of Caddy can be unlocked. The GUI options will remain focused on the reverse proxy.
