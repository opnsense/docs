====================
Caddy: Reverse Proxy
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
* Automatic Let's Encrypt and ZeroSSL certificates with HTTP-01 and TLS-ALPN-01 challenge
* DNS-01 challenge and Dynamic DNS with supported DNS Providers built right in
* Use custom certificates from OPNsense certificate store
* Wildcard Domain and Subdomain support
* Access Lists to restrict access based on static networks
* Basic Auth to restrict access by username and password
* Syslog-ng integration and HTTP Access Log
* NTLM Transport
* Header manipulation
* Simple load balancing with passive health check


------------
Installation
------------

* Install "os-caddy" from the OPNsense Plugins.

.. _prepare-opnsense-caddy:


---------------------------------------------
Prepare OPNsense for Caddy After Installation
---------------------------------------------

.. Attention:: Caddy uses port `80` and `443`. So the OPNsense WebGUI or other plugins can't bind to these ports.

Go to :menuselection:`System --> Settings --> Administration`

* Change the `TCP Port` to `8443` (example), do not forget to adjust the firewall rules to allow access to the WebGUI. On `LAN` there is a hidden `anti-lockout` rule that takes care of this automatically. On other interfaces, make sure to add explicit rules.
* Enable the checkbox for `HTTP Redirect - Disable web GUI redirect rule`.

Go to :menuselection:`Firewall --> Rules --> WAN`

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

Go to :menuselection:`Firewall --> Rules --> LAN` and create the same rules for the `LAN` interface. Now external and internal clients can connect to Caddy, and `Let's Encrypt` or `ZeroSSL` certificates will be issued automatically.

.. Note:: Caddy upgrades all connections automatically from HTTP to HTTPS. When cookies do not have have the ``secure`` flag set by the application serving them, they can still be transmitted unencrypted before the connection is upgraded. If these cookies contain very sensitive information, it might be a good choice to close port 80.


---
FAQ
---

* | A `DNS Provider` is not required. With a static WAN IP, just skip the `DNS Provider` configuration and do not check the `DNS-01 challenge` and `Dynamic DNS` checkboxes. `Let's Encrypt` or `ZeroSSL` will work with `HTTP-01` (Port 80) or `TLS-ALPN-01` (Port 443) challenge automatically.
* | `Port Forwards`, `NAT Reflection`, `Split Horizon DNS` or `DNS Overrides` in Unbound are not required. Only create Firewall rules that allow traffic to the default ports of Caddy.
* | Firewall rules to allow Caddy to reach upstream destinations are not required. OPNsense has a default rule that allows all traffic originating from it to be allowed.
* | ACME Clients on reverse proxied upstream destinations will not be able to issue certificates. Caddy intercepts ``/.well-known/acme-challenge``. This can be solved by using the `HTTP-01 Challenge Redirection` option in the advanced mode of domains. Please check the tutorial section for an example.
* | When using Caddy with IPv6, the best choice is to have a GUA (Global Unicast Address) on the WAN interface, since otherwise the TLS-ALPN-01 challenge might fail.
* | `Let's Encrypt` or `ZeroSSL` can not be explicitely chosen. Caddy automatically issues one of these options, determined by speed and availability. These certificates can be found in ``/var/db/caddy/data/caddy/certificates``.
* | When an `Upstream Destination` only supports TLS connections, yet does not offer a valid certificate, enable ``TLS Insecure Skip Verify`` in a `Handler` to mitigate connection problems.

.. Attention:: There is no TCP/UDP stream and WAF (Web Application Firewall) support in this plugin. For a business grade Reverse Proxy with WAF functionality, use ``os-OPNWAF``. For TCP/UDP streaming, use either ``os-nginx`` or ``os-haproxy``.

.. Tip:: As an alternative to a WAF, it is simple to integrate Caddy with CrowdSec. Check the tutorial section for guidance.


================
Caddy: Tutorials
================

.. Attention:: The tutorial section implies that :ref:`Prepare OPNsense for Caddy after installation <prepare-opnsense-caddy>` has been followed.
.. Note:: Filling out `Description` fields is mandatory because they are used to display and reference items in forms and error messages.
.. Tip:: Handlers are not limited to one per domain/subdomain. If there are multiple different URIs to handle (e.g. ``/foo/*`` and ``/bar/*``), create a handler for each of them. Just make sure each of these URIs are on the same level, creating ``/foo/*`` and ``/foo/bar/*`` will make ``/foo/*`` match everything. Additionally, when creating an empty handler for a domain/subdomain, the templating logic will always automatically place it last in the Caddyfile site block. This means, specific URIs will always match before an empty URI. Though, using just one handler with an empty URI is recommended for most usecases, since it catches all traffic directed at a domain/subdomain.


-------------------------------
Creating a Simple Reverse Proxy
-------------------------------

.. Note:: Make sure the chosen domain is externally resolvable. Create an A-Record with an external DNS Provider that points to the external IP Address of the OPNsense. The reverse proxy will do an automatic redirection from HTTP to HTTPS with this setup.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings`

* Check **enabled** to enable Caddy
* Input a valid email address into the `Acme Email` field. This is mandatory to receive automatic `Let's Encrypt` and `ZeroSSL` certificates.
* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Press **+** to create a new `Domain`, this will be the frontend that receives the traffic for the chosen domain name. The OPNsense listens for this domain on all interfaces.

============================== =====================================================================
Options                        Values
============================== =====================================================================
**Domain:**                    ``foo.example.com``
**Port:**                      `Leave empty to use port 443 with automatic redirection from port 80`
**Description:**               ``foo.example.com - frontend``
============================== =====================================================================

* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Handler`

* Press **+** to create a new `Handler`, this will route the traffic from the frontend domain to the upstream destination. The upstream is an internal service that should receive the reverse proxied traffic from the OPNsense.

============================== ======================================================================
Options                        Values
============================== ======================================================================
**Domain:**                    ``foo.example.com``
**Description:**               ``foo.example.com - upstream``
**Upstream Domain:**           ``192.168.10.1``
**Upstream Port:**             `Leave empty to use port 80, or input a custom port like e.g., 8080`
**TLS Insecure Skip Verify**   `Enable this, if the upstream destination requires HTTPS connection`
============================== ======================================================================

* Press **Save** and **Apply**

.. Note:: After just a few seconds the automatic certificate will be installed, check the Logfile. Now the frontend domain ``foo.example.com`` receives all requests on Port 80 and 443, and reverse proxies these requests to the upstream destination ``192.168.10.1:80``

.. Tip:: `TLS Insecure Skip Verify` can be used in private networks. If the upstream destination is in an insecure network, like the internet or a dmz, consider using proper :ref:`certificate handling <webgui-opnsense-caddy>`.

.. _accesslist-opnsense-caddy:


-------------------------------
Restrict Access to Internal IPs
-------------------------------

.. Tip:: The reverse proxy will accept all connections. Restricting access with a firewall rule, would impact all domains. That is where `Access Lists` come in handy. They can be used to restrict access per domain. In this example, they are used to restrict access to only internal IPv4 networks, refusing connections from the internet.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Access --> Access Lists`

* Press **+** to create a new `Access List`

============================== ============================================================
Options                        Values
============================== ============================================================
**Access List Name:**          ``private_ipv4``
**Client IP Addresses:**       ``192.168.0.0/16`` ``172.16.0.0/12`` ``10.0.0.0/8``
**Description:**               ``Allow access from private IPv4 ranges``
============================== ============================================================

* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Edit an existing `Domain` or `Subdomain` and expand the `Access` Tab.

============================== ====================
Options                        Values
============================== ====================
**Access List:**               ``private_ipv4``
============================== ====================

* Press **Save** and **Apply**

Now, all connections not having a private IPv4 address will be served an empty page for the chosen domain. To outright refuse the connection, the option ``Abort Connections`` in :menuselection:`Services --> Caddy Web Server --> General Settings` should be additionally enabled.

.. Note:: Some applications might demand a HTTP Error code instead of having their connection aborted, an example could be monitoring systems. For these a custom ``HTTP Response Code`` can be enabled.


-----------
Dynamic DNS
-----------

.. Note:: All currently supported Dynamic DNS Providers and requests for additions can be found at https://github.com/opnsense/plugins/issues/3872

.. Attention:: Read the full help text for guidance. It could also be necessary to check the selected provider module at https://github.com/caddy-dns for further instructions. These modules are community maintained. When a module introduces issues that are not fixed it will be removed from this plugin.


Use Dynamic DNS with Reverse Proxy
----------------------------------

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> DNS Provider`

* Select one of the supported `DNS Providers` from the list
* Input the `DNS API Key`, and any number of the additional required fields in `Additional Fields`.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> Dynamic DNS`

* Choose if `DynDns IP Version` should include IPv4 and/or IPv6.
* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Press **+** to create a new `Domain`. ``mydomain.duckdns.org`` is an example if `duckdns` is used as DNS Provider.

============================== ========================
Options                        Values
============================== ========================
**Domain:**                    ``mydomain.duckdns.org``
**Dynamic DNS:**               ``X``
============================== ========================

Go to `Services - Caddy Web Server - Reverse Proxy – Handlers`

* Press **+** to create a new `Handler`

============================== ========================
Options                        Values
============================== ========================
**Domain:**                    ``mydomain.duckdns.org``
**Upstream Domain:**           ``192.168.1.1``
============================== ========================

* Press **Save** and **Apply**

.. Tip:: Check the Logfile for the dynamic dns updates. Set it to `Informational` and `Search` for the chosen domain.
.. Tip:: In addition to `Dynamic DNS`, the `DNS-01 Challenge` can also be selected.


Use Dynamic DNS in Client Mode only
-----------------------------------

.. Tip:: Sometimes, only the Dynamic DNS functionality is needed. There can be cases where a DNS Provider is fully supported in `os-caddy`, yet not in other Dynamic DNS plugins of the OPNsense. With the right configuration, `os-caddy` can be used as Dynamic DNS Client without using port 80 and 443, which stay free to use for other services.

.. Attention:: Using this setup doesn't require any Firewall rules, the OPNsense WebGUI can stay on `TCP port` 443, and `HTTP Redirect - Disable web GUI redirect rule` for port 80 can stay unchecked.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings`

* Check **enabled** to enable Caddy
* Set `AutoHTTPS` to `off` - This will ensure port ``80`` will not be used by Caddy.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> DNS Provider`

* Select one of the supported `DNS Providers` from the list
* Input the `DNS API Key`, and any number of the additional required fields in `Additional Fields`.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> Dynamic DNS`

* Choose if `DynDns IP Version` should include IPv4 and/or IPv6.
* Extend `Additional Checks` and for `DynDns Check Interface` select the ``WAN`` interface.
* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Press **+** to create a new `Domain`. ``mydomain.duckdns.org`` is an example if `duckdns` is used as DNS Provider.

============================== ====================================================================
Options                        Values
============================== ====================================================================
**Domain:**                    ``mydomain.duckdns.org``
**Port:**                      ``20000`` - `A random upper TCP port so Caddy does not bind to 443.`
**Description:**               ``mydomain.duckdns.org - DynDNS only``
**Dynamic DNS:**               ``X``
============================== ====================================================================

* | Create any additional domains for DynDNS updates just like that.
* | Press **Save** and **Apply**

.. Tip:: Check the Logfile for the dynamic dns updates. Set it to `Informational` and `Search` for the chosen domain.


-----------------------------------------------------
Create a Wildcard Reverse Proxy with DNS-01 Challenge
-----------------------------------------------------

.. Attention:: The certificate of a wildcard domain will only contain ``*.example.com``, not a SAN for ``example.com``. Create an additional domain for ``example.com`` with an additional handler for its upstream destination.

.. Note:: Subdomains do not support setting ports, they will always track the ports of their assigned parent wildcard domain.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> DNS Provider`

* Select one of the supported `DNS Providers` from the list
* Input the `DNS API Key`, and any number of the additional required fields in `Additional Fields`. Read the full help for details.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Create ``*.example.com`` as domain and activate the `DNS-01 challenge` checkbox. Alternatively, use a certificate imported or generated in :menuselection:`System --> Trust --> Certificates`. It has to be a wildcard certificate.
* Create all subdomains in relation to the ``*.example.com`` domain, for example ``foo.example.com`` and ``bar.example.com``.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Handlers`

* Create a `Handler` with ``*.example.com`` as domain and ``foo.example.com`` as subdomain. Most of the same configuration as with base domains are possible.

.. Tip:: If in doubt, do not use subdomains. If there should be ``foo.example.com``, ``bar.example.com`` and ``example.com``, just create them as three base domains. This way, there is the most flexibility, and the most features are supported.

.. _webgui-opnsense-caddy:


---------------------------------
Reverse Proxy the OPNsense WebGUI
---------------------------------

.. Tip:: The same approach can be used for any upstream destination using TLS and a self-signed certificate.
.. Attention:: The OPNsense WebGUI is only bound to 127.0.0.1 when no specific interface is selected: :menuselection:`System --> Settings --> Administration` - `Listen Interfaces - All (recommended)`. Otherwise, use the IP address of the specific interface as "Upstream Domain".
.. Attention:: When setting `Enable syncookies` to `always` in :menuselection:`Firewall --> Settings --> Advanced`, reverse proxying the WebGUI is currently not possible. Set it to an `adaptive` setting, or `never (default)`.

* | Open the OPNsense WebGUI in a browser (e.g. Chrome or Firefox). Inspect the certificate by clicking on the 🔒 in the address bar. Copy the SAN for later use. It can be a hostname, for example ``OPNsense.localdomain``.
* | Save the certificate as ``.pem`` file. Open it up with a text editor, and copy the contents into a new entry in :menuselection:`System --> Trust --> Authorities`. Name the certificate ``opnsense-selfsigned``.
* | Add a new `Domain` in Caddy, for example ``opn.example.com``.
* | Add a new `Handler` with the following options:

=================================== ============================
Options                             Values
=================================== ============================
**Domain:**                         ``opn.example.com``
**Upstream Domain:**                ``127.0.0.1``
**Upstream Port:**                  ``8443 (WebGUI Port)``
**TLS:**                            ``X``
**TLS Trusted CA Certificates:**    ``opnsense-selfsigned``
**TLS Server Name:**                ``OPNsense.localdomain``
=================================== ============================

* Press **Save** and **Apply**

Go to :menuselection:`System --> Settings --> Administration`

* Input ``opn.example.com`` in `Alternate Hostnames` to prevent the error ``The HTTP_REFERER "https://opn.example.com/" does not match the predefined settings``
* Press **Save**

.. Note:: Open ``https://opn.example.com`` and it should serve the reverse proxied OPNsense WebGUI. Check the log file for errors if it does not work, most of the time the `TLS Server Name` doesn't match the SAN of the `TLS Trusted CA Certificate`. Caddy does not support certificates with only a CN `Common Name`.
.. Attention:: Create an :ref:`Access List <accesslist-opnsense-caddy>` to restrict access to the WebGUI.


-------------------------------
Redirect ACME HTTP-01 Challenge
-------------------------------

Sometimes an application behind Caddy uses its own ACME Client to get certificates, most likely with the HTTP-01 challenge. This plugin has a built in mechanism to redirect this challenge type easily to a destination behind it.

.. Note:: Make sure the chosen domain is externally resolvable. Create an A-Record with an external DNS Provider that points to the external IP Address of the OPNsense. In case of IPv6 availability, it is mandatory to create an AAAA-Record too, otherwise the TLS-ALPN-01 challenge might fail.

.. Attention:: It is mandatory that the domain in Caddy uses an ``empty port`` or ``443`` in the GUI, otherwise it can not use the TLS-ALPN-01 challenge for itself. The upstream destination has to listen on Port ``80`` and serve ``/.well-known/acme-challenge/``, for the same domain that is configured in Caddy.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Press **+** to create a new `Domain`

=================================== ====================
Options                             Values
=================================== ====================
**Domain:**                         ``foo.example.com``
**HTTP-01 Challenge Redirection:**  ``192.168.10.1``
=================================== ====================

* Press **Save** and **Apply**

.. Note:: The `HTTP-01 Challenge Redirection` already works now and the internal resource located at ``192.168.10.1`` will be able to issue the certificate for the domain name ``foo.example.com``. If the internal ressource should also be reverse proxied, add a handler to the domain.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Handler`

* Press **+** to create a new `Handler`

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

.. Note:: With this configuration, Caddy will eventually choose the TLS-ALPN-01 challenge for its own ``foo.example.com`` domain, and reverse proxy the HTTP-01 challenge to ``192.168.10.1``, where the upstream destination can listen on port 80 for ``foo.example.com`` and solve its own challenge for a certificate. With TLS enabled in the `Handler`, an encrypted connection is automatically possible. The automatic HTTP to HTTPS redirection is also taken care of.


----------------------------------------
Reverse Proxy to a Webserver with Vhosts
----------------------------------------

Sometimes it is necessary to alter the host header in order to reverse proxy to another webserver with vhosts. Since Caddy passes the original host header by default (e.g. ``app.external.example.com``), if the upstream destination listens on a different hostname (e.g. ``app.internal.example.com``), it would not be able to serve this request.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Press **+** to create a new `Domain`

=================================== ============================
Options                             Values
=================================== ============================
**Domain:**                         ``app.external.example.com``
=================================== ============================

* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Headers`

* Press **+** to create a new `Header`

=================================== ============================
Options                             Values
=================================== ============================
**Header:**                         ``header_up``
**Header Type:**                    ``Host``
**Header Value:**                   ``{upstream_hostport}``
=================================== ============================

* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Handler`

* Press **+** to create a new `Handler`

=================================== ========================================
Options                             Values
=================================== ========================================
**Domain:**                         ``app.external.example.com``
**Upstream Domain:**                ``app.internal.example.com``
**Header Manipulation:**            ``header_up Host {upstream_hostport}``
=================================== ========================================

* Press **Save** and **Apply**

.. Note:: Since (most) headers retain their original value when being proxied, it is often necessary to override the Host header with the configured upstream address when proxying to HTTPS, such that the Host header matches the TLS Server Name value. https://caddyserver.com/docs/caddyfile/directives/reverse_proxy#https


-------------------------------
Integrating Caddy with CrowdSec
-------------------------------

.. Tip:: CrowdSec is a powerful alternative to a WAF. It uses logs to dynamically ban IP addresses of known bad actors. The Caddy plugin is prepared to emit the json logs for this integration.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> Log Settings`

* Enable `Log HTTP Access in JSON Format`
* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy –-> Domains`

* Open each `Domain` that should be monitored by CrowdSec
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

* Go into the OPNsense WebGUI and restart CrowdSec.


----------------------------------
Caddy and High Availability Setups
----------------------------------

There are a few possible configurations to run Caddy successfully in a High Availability Setup with two OPNsense firewalls.

.. Tip:: The main issue to think about is the certificate handling. If a CARP VIP is used on the WAN interface, and the A and AAAA Records of all domains point to this CARP VIP, the backup Caddy will not be able to issue ACME certificates without some additional configuration.

There are three methods that support XMLRPC sync:

.. Note:: These methods can be mixed, just make sure to use a coherent configuration. It is best to decide for one method. Only `Domains` need configuration, `Subdomains` do not need any configuration for HA.

#. Using custom certificates from the OPNsense Trust store for all `Domains`.
#. Using the `DNS-01 Challenge` in the settings of `Domains`.
#. Using the `HTTP-01 Challenge Redirection` option in the advanced settings of `Domains`.

Since the `HTTP-01 Challenge Redirection` needs some additional steps to work, it should be set up as followed:

* | Configure Caddy on the master OPNsense until the whole initial configuration is completed.
* | On the master OPNsense, select each `Domain`, and set the IP Address in `HTTP-01 Challenge Redirection` to the same value as in `Synchronize Config to IP` found in :menuselection:`System --> High Availability --> Settings`.
* | Create a new Firewall rule on the master OPNsense that allows Port ``80`` and ``443`` to ``This Firewall`` on the interface that has the prior selected IP Address (most likely a LAN or VLAN interface).
* | Sync this configuration with XMLRPC sync.

.. Note:: Now both Caddy instances will be able to issue ACME certificates at the same time. Caddy on the master OPNsense uses the TLS-ALPN-01 challenge for itself and reverse proxies the HTTP-01 challenge to the Caddy of the backup OPNsense. Please make sure, that the master and backup OPNsense are both listening on their WAN and LAN (or VLAN) interfaces on port ``80`` and ``443``, since both ports are required for these challenges to work.

.. Tip:: Check the Logfile on both Caddy instances for successful challenges. Look for ``certificate obtained successfully`` Informational messages.


-------------------------------------
Keeping Track of Large Configurations
-------------------------------------

Having a large configuration can become a bit cumbersome to navigate. To help, a new filter functionality has been added to the top right corner of the `Domains` and `Handlers` tab, called `Filter by Domain`.

.. Tip:: In `Filter by Domain`, one or multiple `Domains` can be selected, and as filter result, only their corresponding configuration will be displayed in `Domains`, `Subdomains` and `Handlers`. This makes keeping track of large configurations a breeze.


------------------------------------------
Advanced: Bind Caddy to specific Interface
------------------------------------------

.. Warning:: Binding a service to a specific interface via IP address can cause lots of issues. If the IP address is dynamic, the service can crash or refuse to start. During boot, the service can refuse to start if the interface IP addresses are assigned too late. Configuration changes on the interfaces can cause the service to crash. **Only use this with static IP addresses! There is no OPNsense community support for this configuration.**

.. Note:: This configuration is only useful if there are two or more WAN interfaces, and Caddy should only respond on one of them. It can also solve port conflicts, for example if one interface should DNAT or host a different service with the default webserver ports. **In all other cases, it is always better not to do this.**

* Create the following files with the following content in the OPNsense filesystem:

1. ``/usr/local/etc/caddy/caddy.d/defaultbind.global``

.. code::

    default_bind 192.168.1.1


2. ``/usr/local/etc/caddy/caddy.d/defaultbind.conf``


.. code::

    http:// {
    bind 192.168.1.1
    }

* Now Caddy will only bind to ``192.168.1.1`` and it can still be configured in the GUI without restrictions.

.. Tip:: Read more about the ``default_bind`` directive: https://caddyserver.com/docs/caddyfile/options#default-bind


-------------------------
Advanced: Troubleshooting
-------------------------

Sometimes, things do not work as expected. Caddy provides a few powerful debugging tools to analyze issues.

.. Tip:: This section explains how to obtain the required files to get help from https://caddy.community.

.. Note:: First, change the global Log Level to `DEBUG`. This will log `everything` the ``reverse_proxy`` directive handles. 

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> Log Settings`

* Set the `Log Level` to `DEBUG`
* Press **Apply**

Go to :menuselection:`Services --> Caddy Web Server --> Log File`

* Change the dropdown from `INFORMATIONAL` to `DEBUG`

Now the ``reverse_proxy`` debug logs will be visible and can be downloaded.

.. Note:: Second, validate and download the Caddyfile.

Go to :menuselection:`Services --> Caddy Web Server --> Diagnostics --> Caddyfile`

* | Press the `Validate Caddyfile` button to make sure the current Caddyfile is valid.
* | Press the `Download` button to get this current Caddyfile.
* | If there are custom imports in ``/usr/local/etc/caddy/caddy.d/``, download the JSON configuration.

.. Note:: Rarely, a performance profile might be requested. For this, a special admin endpoint can be activated.

.. Attention:: This admin endpoint is deactivated by default. To enable it and access it on the OPNsense, follow these additional steps. Do not forget to deactivate it after use. Anybody with network access to the admin endpoint can use REST API to change the running configuration of Caddy, without authentication.

* | SSH into the OPNsense shell
* | Stop Caddy with ``configctl caddy stop``
* | Go to ``/usr/local/etc/caddy/caddy.d/``
* | Create a new file called ``admin.global`` and put the following content into it: ``admin :2019``
* | After saving the file, go to ``/usr/local/etc/caddy`` and run ``caddy validate`` to ensure the configuration is valid.
* | Start Caddy with ``configctl caddy start``
* | Use sockstat to see if the admin endpoint has been created. ``sockstat -l | grep -i caddy`` - it should show the endpoint ``*:2019``.
* | Create a firewall rule on ``LAN`` that allows ``TCP`` to destination ``This Firewall`` and destination port ``2019``.
* | Open the admin endpoint: ``http://YOUR_LAN_IP:2019/debug/pprof/``

.. Note:: Follow the instructions on https://caddyserver.com/docs/profiling how to debug and profile Caddy.


--------------------------------
Using Custom Configuration Files
--------------------------------

* | The Caddyfile has an additional import from the path ``/usr/local/etc/caddy/caddy.d/``. Place custom configuration files inside that adhere to the Caddyfile syntax.
* | ``*.global`` files will be imported into the global block of the Caddyfile.
* | ``*.conf`` files will be imported at the end of the Caddyfile. Don't forget to test the custom configuration with ``caddy validate --config /usr/local/etc/caddy/Caddyfile``.

.. Note:: With these imports, the full potential of Caddy can be unlocked. The GUI options will remain focused on the reverse proxy. There is no OPNsense community support for configurations that have not been created with the offered GUI. For customized configurations, the Caddy community is the right place to ask.
