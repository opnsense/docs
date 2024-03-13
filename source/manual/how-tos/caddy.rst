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

.. Attention:: If you use Caddy in HA (High Availability), only use your own custom certificates from the OPNsense Trust store. Caddy needs a shared storage with atomic writes for the ACME challenges to work without interruption in clusters. This is out of scope in this plugin. You can potentially ignore this if you only serve a few sites, and use ACME in HA. There will be a small downtime where Caddy will collect new certificates for each site on the Backup Firewall during a failover. 

--------------
How to install
--------------

* Install "os-caddy" from the OPNsense Plugins.

---------------------------------------------
Prepare OPNsense for Caddy after installation 
---------------------------------------------

* Make sure that port ``80`` and ``443`` aren't occupied. You have to change the default listen port of the OPNsense WebUI to ``8443`` (for example). Go to ``System: Settings: Administration`` to change the ``TCP Port``. Then also enable ``HTTP Redirect - Disable web GUI redirect rule``.
* If you have other reverse proxy or webserver plugins installed, make sure they don't use the same ports as Caddy
* Create Firewall rules that allow ``HTTP`` and ``HTTPS`` to destination ``This Firewall`` on ``WAN`` and ``LAN``. On ``WAN``, external clients will connect to your Domains via FQDN, and Let's Encrypt will connect to your Firewall to issue certificates. On ``LAN`` your internal clients will access the Domains via FQDN.

---
FAQ
---

* A DNS Provider is not required. With a static WAN IP, just skip the DNS Provider configuration and don't check the DNS-01 and Dynamic DNS checkboxes. Let's Encrypt will work with HTTP-01 (Port 80) or TLS-ALPN-01 (Port 443) challenge automatically.
* Opening Port 80 is not required. Caddy will also issue certificates on Port 443 with the TLS-ALPN-01 challenge. https://letsencrypt.org/docs/challenge-types/#tls-alpn-01
* Port Forwards, NAT Reflection or Split Horizon DNS are not required. Only create Firewall rules that allows traffic to hit the ports that Caddy opens. That is 80 (optionally) and 443 (required).
* Firewall rules to allow Caddy to reach Backend Servers are not required. OPNsense has a default rule that allows all traffic originating from it to be allowed.

====================
caddy: Configuration
====================

.. Note:: You can find Caddy in "Services: Caddy Web Server". Some options are hidden in advanced mode.

--------------------------
General Settings - General
--------------------------

* ``enable`` or ``disable`` Caddy. If enabled, Caddy will serve your configuration and autostart with the OPNsense.
* ``ACME Email``: e.g. ``info@example.com``, it's optional for receiving Email updates on Let's Encrypt certificates.
* ``Auto HTTPS``: ``On (default)`` creates automatic Let's Encrypt certificates for all domains that don't have more specific options set, like custom certificates.
* ``Trusted Proxies``: Leave empty if you don't use a CDN in front of your OPNsense. If you use Cloudflare or another CDN provider, create an Access List with the IP addresses of that CDN and add it here. Add the same Access List to the domain this CDN tries to reach.
* ``Abort Connections``: This option, when enabled, aborts all connections to the domain that don't match any specified handler or access list. This setting doesn't affect Let's Encrypt's ability to issue certificates, ensuring secure connections regardless of the option's status. If unchecked, the domain remains accessible even without a matching handler, allowing for connectivity and certificate checks, even in the absence of a configured Backend Server. When using Access Lists, enabling this option is recommended to reject unauthorized connections outright. Without this option, unmatched IP addresses will encounter an empty page instead of an explicit rejection, though the Access Lists continue to function and restrict access.

-------------------------------
General Settings - DNS Provider
-------------------------------

* ``DNS Provider``: Select the DNS provider for the DNS-01 Challenge and Dynamic DNS. This is optional, since certificates will be requested from Let's Encrypt via HTTP-01 or TLS-ALPN-01 challenge when this option is unset. You mostly need this for wildcard certificates, and for dynamic DNS. To use the DNS-01 challenge and dynamic DNS, enable the checkbox in a domain or subdomain. For more information: https://github.com/caddy-dns
* ``DNS API Fields``: These fields are for the API settings of the chosen DNS Provider. All of these fields can be left empty if they are optional with the chosen provider. The help text in the plugin will list all available providers and their expected configurations. There are additional fields in the advanced mode if DNS providers require more fields for their configurations.

------------------------------
General Settings - Dynamic DNS
------------------------------

* ``DynDns Check Http``: Optionally, enter an URL to test the current IP address of the firewall via HTTP procotol. Generally, this is not needed. Caddy uses default providers to test the current IP addresses. If you rather use your own, enter the ``https://`` link to an IP address testing website.
* ``DynDns Check Interface``: Optionally, select an interface to extract the current IP address of the firewall. At most, one current IPv6 Global Unicast Address and one current IPv4 non-RFC1918 Address will be extracted. 
* ``DynDns Check Interval``: Interval to poll for changes of the IP address. The default is 5 minutes. Can be a number between 1 to 1440 minutes.
* ``DynDns IP Version``: Leave on ``None`` to set IPv4 A-Records and IPv6 AAAA-Records. Select ``Ipv4 only`` for setting A-Records. Select ``IPv6 only`` for setting AAAA-Records.
* ``DynDns TTL``: Set the TTL (time to live) for DNS Records. The default is 1 hour. Can be a number between 1 to 24 hours.

-------------------------------
General Settings - Log Settings
-------------------------------

* ``Log Credentials``: Log all Cookies and Authorization Headers in HTTP request logging. Use combined with HTTP Access Log in a domain. Enable this option only for troubleshooting.
* ``Log Access in Plain Format``: Don't send HTTP access logs to the central OPNsense logging facility but save them in plain Caddy JSON format in a subdirectory instead. Only effective for domains that have HTTP Access Log enabled. The feature is intended to have access log files processed by e.g. CrowdSec. They can be found in `/var/log/caddy/access`.
* ``Keep Plain Access Logs for (days)``: How many days until the plain format log files are deleted. The default is 10 days.

-----------------------
Reverse Proxy - Domains
-----------------------

* Press ``+`` to create a new domain
* ``enable`` or ``disable`` this domain 
* ``Reverse Proxy Domain``: Can either be a domain name or an IP address. If a domain name is chosen, Caddy will automatically try to get a Let's Encrypt or ZeroSSL certificate, and the headers and real IP address will be automatically passed to the Backend Server.
* ``Reverse Proxy Port``: Should be the port the OPNsense will listen on. Don't forget to create Firewall rules that allow traffic to this port on ``WAN`` and ``LAN`` to destination ``This Firewall``. You can leave this empty if you want to use the default ports of Caddy (`80` and `443`) with automatic redirection from HTTP to HTTPS.
* ``Access List``: Restrict the access to this domain to a list of IP addresses you define in the Access Tab. This doesn't influence Let's Encrypt certificate generation, so you can be as restrictive as you want here.
* ``Basic Auth``: Restrict the access to this domain to one or multiple users you define in the Access Tab. This doesn't influence the Let's Encrypt certificate generation, so you can be as restrictive as you want here.
* ``DNS-01 challenge``: Enable this if you want to use the DNS-01 challenge instead of HTTP-01 and TLS-ALPN-01 challenge. This can be set per entry, so you can have both types of challenges at the same time for different entries. This option needs the ``General Settings - DNS Provider`` configured.
* ``Dynamic DNS``: Enable Dynamic DNS. As the option above, the DNS Provider is a requirement. The DNS Records of this domain will be automatically updated with your DNS Provider.
* ``Custom Certificate``: Use a certificate you imported or generated in ``System - Trust - Certificates``. The chain is generated automatically. Certificate + Intermediate CA + Root CA, Certificate + Root CA and self signed Certificate are all fully supported. Only SAN certificates will work. 
* ``HTTP Access Log``: Enable the HTTP request logging for this domain and its subdomains. This option is mostly for troubleshooting or log analyzing tools like Crowdsec, since it will log every single request.
* ``Description``: The description is mandatory. Create descriptions for each domain. Since there could be multiples of the same domain with different ports, do it like this: ``foo.example.com`` and ``foo.example.com.8443``.

--------------------------
Reverse Proxy - Subdomains
--------------------------

* Press ``+`` to create a new subdomain
* ``Reverse Proxy Domain`` - Choose a wildcard domain you prepared in domains, it has to be formatted like ``*.example.com``
* ``Reverse Proxy Subdomain`` - Create a name that is seated under the Wildcard domain, for example ``foo.example.com`` and ``bar.example.com``. But **not** ``foo.bar.example.com`` if your domain is ``*.example.com``. This would be an invalid choice.
* For the other options refer to ``Reverse Proxy - Domains``. It's best to leave Access Lists and Basic Auth unconfigured in your wildcard domain, and set these per subdomain. Otherwise you can create an invalid configuration, which the inbuild validation will warn about on apply. 

-----------------------
Reverse Proxy - Handler
-----------------------

.. Note:: The order that handlers are saved in the scope of each domain or domain/subdomain can influence functionality; The first matching handler wins. So if you put /ui* in front of a more specific handler like /ui/opnsense, the /ui* will match first and /ui/opnsense won't ever match (in the scope of their domain). Right now there isn't an easy way to move the position of handlers in the grid, so you have to clone them if you want to change their order, and delete the old entries afterwards. Most of the time, creating just one empty catch-all handler is the best choice. The template logic makes sure that catch-all handlers are always placed last, after all other handlers.

* Press ``+`` to create a new ``Handler``. A handler is like a location in nginx.
* ``enable`` or ``disable`` this new entry.
* ``Reverse Proxy Domain``: Select the domain you have created.
* ``Reverse Proxy Subdomain``: Select the subdomain you have created. This will put the handler on the subdomain instead of the domain. Use only with wildcard domains and subdomains. 
* ``Handle Type``: ``handle`` or ``handle path` can be chosen. If in doubt, always use `handle`, the most common option. `handle path` is used to strip the path from the URI. For example if you have example.com/opnsense internally, but want to call it with just example.com externally.
* ``Handle Path``: Leave this empty if you want to create a catch all location or enter a location like  `/foo/*` or `/foo/bar*`. 
* ``Backend Server Domain``: Should be an internal domain name or an IP Address of the Backend Server that should receive the reverse proxied traffic. 
* ``Backend Server Port``: Should be the port the Backend Server listens on. This can be left empty to use Caddy default ports 80 and 443.
* ``Backend Server Path``: In case the backend application resides in a sub-path of the web root and you don't want this path visible in the frontend URL you can use this setting to prepend an initial path starting with '/' to every backend request. Java applications running in a servlet container like Tomcat are known to behave this way, so you can set it to e.g. '/guacamole' to access Apache Guacamole at the frontend root URL without needing a redirect.
* ``TLS``: If your Backend Server only accepts HTTPS, enable this option. If the Backend Server has a globally trusted certificate, this is all you need.
* ``TLS Trusted CA Certificates``: Choose a CA certificate to trust for the Backend Server connection. Import your self-signed certificate or your CA certificate into the OPNsense "System - Trust - Authorities" store, and select it here.
* ``TLS Server Name``: If the SAN (Subject Alternative Names) of the offered trusted CA certificate or self-signed certificate doesn't match with the IP address or hostname of the `Backend Server Domain`, you can enter it here. This will change the SNI (Server Name Identification) of Caddy to the `TLS Server Name`. IP address e.g. `192.168.1.1` or hostname e.g. `localhost` or `opnsense.local` are all valid choices. Only if the SAN and SNI match, the TLS connection will work, otherwise an error is logged that can be used to troubleshoot.
* ``NTLM``: If your Backend Server needs NTLM authentication, enable this option together with TLS. For example, Exchange Server.

.. Attention:: The GUI doesn't allow "tls_insecure_skip_verify" due to safety reasons, as the Caddy documentation states not to use it. Use the `TLS Trusted CA Certificates` and `TLS Server Name` options instead to get a **secure TLS connection** to your Backend Server. Otherwise, use HTTP. If you really need to use "tls_insecure_skip_verify" and know the implications, use the import statements of custom configuration files.

-------------------------------------
Reverse Proxy - Access - Access Lists
-------------------------------------

* Press ``+`` to create a new Access List
* ``Access List name``: Choose a name for the Access List, for example ``private_ips``.
* ``Client IP Addresses``: Enter any number of IPv4 and IPv6 addresses or networks that this access list should contain. For matching only internal networks, add `192.168.0.0/16` `172.16.0.0/12` `10.0.0.0/8` `127.0.0.1/8` `fd00::/8` `::1`.
* ``Invert List``: Invert the logic of the access list. If unchecked, the Client IP Addresses will be ALLOWED, all other IP addresses will be blocked. If checked, the Client IP Addresses will be BLOCKED, all other IP addresses will be allowed.

.. Note:: Go back to domains or subdomains and add the access list to them (advanced mode). All handlers created under these domains will get an additional matcher. That means, the requests still reach Caddy, but if the IP Addresses don't match with the access list, the request will be dropped before being reverse proxied.

-----------------------------------
Reverse Proxy - Access - Basic Auth
-----------------------------------

* Press ``+`` to create a new User for Basic Auth
* ``User``: Enter a username. Afterwards, you can select it in domains or subdomains to restrict access with basic auth. Usernames are only allowed to have alphanumeric characters.
* ``Password``: Enter a password. Write it down. It will be hashed with bcrypt. It can only be set and changed but won't be visible anymore. The hash can't be turned back into the original password.

.. Note:: Basic auth matches after access lists, so you can set both to first restrict access by IP address, and then additionally by username and password. Don't set basic auth on top of a wildcard domain directly, always set it on the subdomains instead.

================
caddy: Tutorials  
================

.. Attention:: The tutorial section implies that "Prepare OPNsense for Caddy after installation" has been read.

------------------------------------
HOW TO: Create an easy reverse proxy
------------------------------------

.. Note:: Make sure your domain is externally resolvable. Create an A-Record with your DNS Provider that points to the external IP Address of your OPNsense. 

Go to Services - Caddy Web Server - General Settings

* ``enable`` Caddy and press ``Save``

Go to Services - Caddy Web Server - Reverse Proxy - Domains

* Press ``+`` to create a new domain
* ``Reverse Proxy Domain`` - ``foo.example.com``
* ``Description`` - ``foo.example.com``
* ``Save``

Go to Services - Caddy Web Server - Reverse Proxy - Handler

* Press ``+`` to create a new Handler
* ``Reverse Proxy Domain`` - ``foo.example.com``
* ``Backend Server Domain`` - ``192.168.10.1``
* ``Save`` and ``Apply``

.. Note:: Leave all other fields to default or empty. You don't need the advanced mode options. After just a few seconds the Let's Encrypt certificate will be installed and the reverse proxy works. Check the Logfile for that. Now you have a TLS Termination reverse proxy.
.. Note:: Internet HTTPS (80/443) --> OPNsense (Caddy) --> HTTP (80) Backend Server

----------------------------------------
HOW TO: Dynamic DNS and DNS-01 Challenge 
----------------------------------------

Choose a supported DNS Provider
-------------------------------

* Go to ``Services: Caddy Web Server: General Settings``
* Click on the Tab ``DNS Provider``
* Select one of the supported DNS Providers from the Dropdown List
* Input the ``DNS API Key``, and any number of the additional required fields in advanced mode. Read the full help for details.
* Choose if DynDns IP Version in the ``Dynamic DNS`` Tab should only include the IPv4, IPv6, or both IP addresses of your Firewall. None option means both protocols.
* ``Save``

Create a Domain
---------------

* Go to „Services: Caddy Web Server: Reverse Proxy“ – Domains Tab
* Press „+“ to create a new Reverse Proxy Domain

============================== ====================
Options                        Data
============================== ====================
Reverse Proxy Domain           mydomain.duckdns.org
DNS-O1                         enabled
Dynamic DNS                    enabled
Description                    mydomain.duckdns.org
============================== ====================

Create a Handler
----------------

* Go to ``Services: Caddy Web Server: Reverse Proxy – Handlers`` 
* Press ``+`` to create a new handler
* Choose the domain ``mydomain.duckdns.org`` from the dropdown list.
* Input the IP address of your Backend Server Domain: ``192.168.1.1``
* Press ``Save`` and ``Apply``

.. Note:: Now Caddy listens on Port 80 and 443, and Reverse Proxies everything going to mydomain.duckdns.org to 192.168.1.1:80. All headers and the real IP are automatically passed to your backend server. For different ports, check the advanced settings.
.. Note:: Let's Encrypt Certificate and Dynamic DNS Updates are all handled automatically, it’s like magic.

---------------------------------------
HOW TO: Create a wildcard reverse proxy
---------------------------------------

* Create ``*.example.com`` as domain and activate the DNS-01 challenge checkbox. A DNS Provider has to be configured. Alternatively, use a certificate imported or generated in `System - Trust - Certificates`. It has to be a wildcard certificate.
* Go to ``subdomain`` and create all subdomains that you need in relation to the ``*.example.com`` domain. So for example ``foo.example.com`` and ``bar.example.com``.
* Create descriptions for each subdomain.
* Create a Handler with ``*.example.com`` as domain and ``foo.example.com`` as subdomain. All the same configuration as with normal domains is possible.

----------------------------------------
HOW TO: Reverse Proxy the OPNsense WebUI 
----------------------------------------

* Open the OPNsense GUI in a Browser (e.g. Chrome or Firefox). Inspect the certificate. Copy the SAN for later use, for example ``OPNsense.localdomain``.
* Save the certificate as .pem file. Open it up with a text editor, and copy the contents into a new entry in ``System - Trust - Authorities``. Name the certificate ``opnsense-selfsigned``.
* Add a new domain in Caddy, for example ``opn.example.com``. Make sure the name is externally resolvable to the IP of your OPNsense Firewall.
* Add a new handler with the following options (enable advanced mode):

============================== ====================
Options                        Data
============================== ====================
Reverse Proxy Domain           opn.example.com
Backend Server Domain          127.0.0.1
Backend Server Port            8443 (Webui Port)
TLS                            enabled
TLS Trusted CA Certificates    opnsense-selfsigned
TLS Server Name                OPNsense.localdomain
============================== ==================== 

* ``Save`` and ``Apply``

.. Note:: Open ``https://opn.example.com`` and it should serve the reverse proxied OPNsense WebUI. Check the log file for errors if it doesn't work, most of the time the TLS Server Name doesn't match the SAN of the TLS Trusted CA Certificate. Please note that Caddy doesn't support CN (Common Name) in certificate since it's been deprecated since many years. Only SAN Certificates work.
.. Attention:: Create an access list to restrict access to the WebUI. Add that access list to the domain in advanced mode. 

----------------------------------
HOW TO: Custom configuration files
----------------------------------

* The Caddyfile has an additional import from the path ``/usr/local/etc/caddy/caddy.d/``. Place custom configuration files inside that adhere to the Caddyfile syntax.
* ``*.global`` files will be imported into the global block of the Caddyfile.
* ``*.conf`` files will be imported at the end of the Caddyfile. Don't forget to test your custom configuration with `caddy run --config /usr/local/etc/caddy/Caddyfile`.
* With these imports, you can unlock the full potential of Caddy to serve anything. The GUI options will remain focused on the reverse proxy.
