====================
Caddy: Reverse Proxy
====================

.. contents:: Index


--------
Features
--------

Caddy - The Ultimate Server - makes your sites more secure, more reliable, and more scalable than any other solution.
By default, Caddy automatically obtains and renews TLS certificates (Let's Encrypt and ZeroSSL) for all your sites.
It's the most advanced HTTPS server in the world.

* Reverse Proxy HTTP, HTTPS and WebSockets
* Route UDP/TCP traffic with the included Layer4 module: https://github.com/mholt/caddy-l4
* Dynamic DNS module included: https://github.com/mholt/caddy-dynamicdns
* Large selection of DNS Providers available: https://github.com/caddy-dns

WWW: https://caddyserver.com/

All available options and help-texts can be found on `Github <https://github.com/opnsense/plugins/tree/master/www/caddy/src/opnsense/mvc/app/controllers/OPNsense/Caddy/forms>`_


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

Go to :menuselection:`Firewall --> Rules --> LAN` and create the same rules for the `LAN` interface. Now external and internal clients can connect to Caddy, and `Let's Encrypt` or `ZeroSSL` certificates will be issued automatically. If using a VPN to connect remote clients to the OPNsense, additional firewall rules could be needed.

.. Note:: If you disable ``QUIC`` by removing ``HTTP/3`` in :menuselection:`Services --> Caddy Web Server --> General Settings --> Advanced Settings`, the ``Caddy Reverse Proxy HTTPS`` rule only needs ``TCP`` as protocol.


---
FAQ
---

* | A `DNS Provider` is not required to get automatic certificates.
* | `Port Forwards`, `NAT Reflection`, `Split Horizon DNS` or `DNS Overrides in Unbound` are not required. Only create Firewall rules that allow traffic to the default ports of Caddy.
* | Even though internal clients will use the external IP address to access the reverse proxied services, the traffic will not pass over the internet. It will stay inside the OPNsense. Only in rare cases where there is multi WAN, the traffic can be routed from one WAN interface to the other over the internet, due to `reply-to` settings.
* | Firewall rules to allow Caddy to reach internal services are not required. OPNsense has a default rule that allows all traffic originating from itself to be allowed.
* | ACME clients on reverse proxied upstream destinations will not be able to issue certificates. Caddy intercepts ``/.well-known/acme-challenge``. This can be solved by using the `HTTP-01 Challenge Redirection` option in the advanced mode of domains. Please check the tutorial section for an example.
* | When using Caddy with IPv6, the best choice is to have a GUA (Global Unicast Address) on the WAN interface, since otherwise the TLS-ALPN-01 challenge might fail.
* | `Let's Encrypt` or `ZeroSSL` can not be explicitely chosen. Caddy automatically issues one of these options, determined by speed and availability. These certificates can be found in ``/var/db/caddy/data/caddy/certificates``.
* | When an `Upstream Destination` only supports TLS connections, yet does not offer a valid certificate, enable ``TLS Insecure Skip Verify`` in a `Handler` to mitigate connection problems.
* | Caddy upgrades all connections automatically from HTTP to HTTPS. When cookies do not have have the ``secure`` flag set by the application serving them, they can still be transmitted unencrypted before the connection is upgraded. If these cookies contain very sensitive information, it might be a good choice to close port 80.
* | There is optional Layer4 TCP/UDP routing support. In the scope of this plugin, only traffic that looks like TLS and has SNI can be routed. The `HTTP App` and `Layer4 App` can work together at the same time.
* | There is no WAF (Web Application Firewall) support in this plugin. For a business grade Reverse Proxy with WAF functionality, use ``os-OPNWAF``. As an alternative to a WAF, it is simple to integrate Caddy with CrowdSec. Check the tutorial section for guidance.


====================
Caddy: HTTP Handlers
====================


----------------------
Standard Configuration
----------------------

.. Note:: The tutorial section implies that :ref:`Prepare OPNsense for Caddy after installation <prepare-opnsense-caddy>` has been followed.


Creating a Simple Reverse Proxy
-------------------------------

.. Attention:: The domain has to be externally resolvable. Create an A-Record with an external DNS Provider that points your domain to the external IP address of your OPNsense.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings`

* | Check **Enabled** to enable Caddy
* | Input a valid email address into the `Acme Email` field. This is mandatory to receive automatic `Let's Encrypt` and `ZeroSSL` certificates
* | `Auto HTTPS` should be set to ``On (default)``
* | Press **Apply**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* | Press **Step 1: Add Domain**. This will be the frontend that receives the traffic for the chosen domain name.

============================== =====================================================================
Options                        Values
============================== =====================================================================
*Frontend*
**Protocol:**                  ``https://``
**Domain:**                    ``foo.example.com``
**Port:**                      `Leave empty`
**Certificate:**               ``ACME (HTTP-01, TLS-ALPN-01)``
============================== =====================================================================

* | Press **Save**
* | Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> HTTP Handlers`
* | Press **Step 2: Add HTTP Handler**. This will create a `HTTP Handler` that routes the traffic from the frontend domain to the an internal service.

============================== ======================================================================
Options                        Values
============================== ======================================================================
*Frontend*
**Domain:**                    ``https://foo.example.com``
*Upstream*
**Protocol:**                  ``http://`` or ``https://`` - depending on your upstream webserver
**Upstream Domain:**           ``192.168.10.1``
**Upstream Port:**             ``80`` - `or set the port required by your upstream webserver`
**TLS Insecure Skip Verify**   ``X`` - `if https:// was chosen`
============================== ======================================================================

* | Press **Save** and **Apply**

The automatic certificate will be installed, check the Logfile if there are errors. Now the frontend domain ``foo.example.com:80/443`` receives all requests, and reverse proxies them to the upstream destination ``192.168.10.1:80`` (or custom port).

And that's it, a working reliable reverse proxy in less than a minute. There are a lot of additional options, but this is essentially all that is needed for simple setups.

.. Tip:: There is a `Caddy Certificate` Dashboard widget that shows all issued automatic certificates.
.. Note:: `TLS Insecure Skip Verify` can be used in private networks. If the upstream destination is in an insecure network, like the internet or a dmz, consider using proper :ref:`certificate handling <webgui-opnsense-caddy>`.

.. _accesslist-opnsense-caddy:


Restrict Access to Internal IPs
-------------------------------

Since the reverse proxy will accept all connections, restricting access with a firewall rule would impact all domains. `Access Lists` can restrict access per domain. In this example, they are used to restrict access to only internal IPv4 networks, refusing connections from the internet.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> HTTP Access --> Access Lists`

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

Now, all connections without a private IPv4 address will be blocked. Some applications might demand a HTTP Error code instead of having their connection blocked, an example are monitoring systems. For these a custom ``HTTP Response Code`` can be set in the advanced mode.

.. Note:: Access Lists can be set on `Domains`, `Subdomains` and `HTTP Handlers`.


Restrict Access with Basic Auth
-------------------------------

Since the reverse proxy will accept all connections, restricting access with a firewall rule would impact all domains. `Basic Auth` will restrict access to one or multiple users.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> HTTP Access --> Basic Auth`

* Press **+** to create a new `User`

============================== ============================================================
Options                        Values
============================== ============================================================
**User:**                      ``John``
**Password:**                  ``RandomPassword``
============================== ============================================================

* Press **Save** and create additional `Users` if needed, e.g. ``Sarah``.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Edit an existing `Domain` or `Subdomain` and expand the `Access` Tab.

============================== ====================
Options                        Values
============================== ====================
**Basic Auth:**                ``John``, ``Sarah``
============================== ====================

* Press **Save** and **Apply**

Now, all anonymous connections have to authenticate with Basic Auth before accessing the reverse proxied service.

.. Note:: Using Crowdsec is recommended. It will log authentication errors, and will ban these IP addresses. This prevents password bruteforcing.

.. _dynamicdns-opnsense-caddy:


Dynamic DNS
-----------

Supported Dynamic DNS Providers and requests for additions can be found `here <https://github.com/opnsense/plugins/issues/3872>`_.

.. Tip:: Read the full help text for guidance. It could also be necessary to check the selected provider module at `Caddy DNS <https://github.com/caddy-dns>`_ for further instructions. These modules are community maintained. When a module introduces issues that are not fixed it will be removed from this plugin.

.. Note::

    Enabling the `Dynamic DNS` checkboxes can have different results based on domain type. Enable it only where you need it, and test how your provider requires it for your hosted DNS zone:

    - Base Domain: ``example.com @``
    - Wildcard Domain: ``example.com *``
    - Subdomain: ``example.com opn``

    Use subdomains if you see errors in the log like:

    `failed setting DNS record(s) with new IP address(es)","zone":"opn.example.com","error":"expected 1 zone, got 0`

    This means the zone ``opn.example.com @`` does not exist, and the provider expects ``example.com opn`` for the update. You can see the current configuration in :menuselection:`Services --> Caddy Web Server --> Diagnostics --> Caddyfile`.


Dynamic DNS with Reverse Proxy
++++++++++++++++++++++++++++++

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

Go to :menuselection:`Services - Caddy Web Server - Reverse Proxy – HTTP Handlers`

* Press **+** to create a new `HTTP Handler`

============================== ========================
Options                        Values
============================== ========================
**Domain:**                    ``mydomain.duckdns.org``
**Upstream Domain:**           ``192.168.1.1``
============================== ========================

* Press **Save** and **Apply**

Check the Logfile for the DynDNS updates. Set it to `Informational` and search for the chosen domain.


Dynamic DNS in Client Mode
++++++++++++++++++++++++++

Sometimes, only the Dynamic DNS functionality is needed. There can be cases where a DNS Provider is fully supported in `os-caddy`, yet not in other DynDNS plugins of the OPNsense. With the right configuration, this plugin can be used as DynDNS Client without using port 80 and 443, which stay free to use for other services.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings`

* | Check **enabled** to enable Caddy
* Set `AutoHTTPS` to `off` - This will ensure port ``80`` will not be used by Caddy.
* Enable the `advanced options` and set the `HTTPS Port` to a random upper TCP port, e.g. ``20000``.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> DNS Provider`

* Select one of the supported `DNS Providers` from the list.
* Input the `DNS API Key`, and any number of the additional required fields in `Additional Fields`.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> Dynamic DNS`

* Choose if `DynDns IP Version` should include IPv4 and/or IPv6.
* Extend `Additional Checks` and for `DynDns Check Interface` select the ``WAN`` interface.
* | Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Press **+** to create a new `Domain`. ``mydomain.duckdns.org`` is an example if `duckdns` is used as DNS Provider.

============================== ====================================================================
Options                        Values
============================== ====================================================================
**Domain:**                    ``mydomain.duckdns.org``
**Dynamic DNS:**               ``X``
============================== ====================================================================

* | Create any additional domains for DynDNS updates just like that.
* | Press **Save** and **Apply**


Wildcard Domain with Subdomains
-------------------------------

.. Note:: If you use :ref:`Dynamic DNS <dynamicdns-opnsense-caddy>`, subdomains are needed due to the way the API updates the DNS Records in hosted zones. For `DNS Providers` like `Cloudflare`, this is the recommended setup.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> DNS Provider`

* Select one of the supported `DNS Providers` from the list
* Input the `DNS API Key`, and any number of the additional required fields in `Additional Fields`. Read the full help for details.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* | Create ``*.example.com`` as domain and activate the `DNS-01 Challenge` checkbox. Alternatively, use a certificate imported or generated in :menuselection:`System --> Trust --> Certificates`. It has to be a wildcard certificate.
* | Press **Apply** to enable :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Subdomains`. This tab only shows when a wildcard domain has been configured.
* | Create all subdomains in relation to the ``*.example.com`` domain, for example ``foo.example.com`` and ``bar.example.com``.
* | Check `Dynamic DNS` for the new subdomains, if needed.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> HTTP Handlers`

* Create a `HTTP Handler` with ``*.example.com`` as domain and ``foo.example.com`` as subdomain. Most of the same configuration as with base domains are possible. The subdomain dropdown only shows when a wildcard domain has been configured.

.. Note:: The certificate of a wildcard domain will only contain ``*.example.com``, not a SAN for ``example.com``. If there is a service that should match ``example.com`` exactly, create an additional domain for ``example.com`` with an additional `HTTP Handler` for its upstream destination. Subdomains do not support setting ports, they will always track the ports of their assigned parent wildcard domain.

.. Tip::

    If a domain should listen on more than one port, add it multiple times. The domains will automatically share the same wildcard certificate.

    - `*.example.com:443`
    - `*.example.com:8443`

    Afterwards inherit the port from the domain by choosing it in the `Subdomains` tab. The same subdomain can be created multiple times under different wildcard domains if it should be available on multiple ports. To tell multiple same subdomains apart, give them a description with their port. Each of these subdomains need their own `HTTP Handlers`.


.. _webgui-opnsense-caddy:


Reverse Proxy the OPNsense WebGUI
---------------------------------

.. Tip:: The same approach can be used for any upstream destination using TLS and a self-signed certificate.
.. Attention::
    | The OPNsense WebGUI is only bound to 127.0.0.1 when no specific interface is selected: :menuselection:`System --> Settings --> Administration` - `Listen Interfaces - All (recommended)`. Otherwise, use the IP address of the specific interface as "Upstream Domain".
    | When setting `Enable syncookies` to `always` in :menuselection:`Firewall --> Settings --> Advanced`, reverse proxying the WebGUI is currently not possible. Set it to an `adaptive` setting, or `never (default)`.

* | Open the OPNsense WebGUI in a browser (e.g. Chrome or Firefox). Inspect the certificate by clicking on the 🔒 in the address bar. Copy the SAN for later use. It can be a hostname, for example ``OPNsense.localdomain``
* | Save the certificate as ``.pem`` file. Open it up with a text editor, and copy the contents into a new entry in :menuselection:`System --> Trust --> Authorities`. Name the certificate ``opnsense-selfsigned``
* | Add a new `Domain`, for example ``opn.example.com``
* | Add a new `HTTP Handler` with the following options:

=================================== ============================
Options                             Values
=================================== ============================
*Frontend*
**Domain:**                         ``opn.example.com``
*Upstream*
**Protocol**                        ``https://``
**Upstream Domain:**                ``127.0.0.1``
**Upstream Port:**                  ``8443`` - `WebGUI Port`
**TLS Trust Pool:**                 ``opnsense-selfsigned``
**TLS Server Name:**                ``OPNsense.localdomain``
=================================== ============================

* Press **Save** and **Apply**

Go to :menuselection:`System --> Settings --> Administration`

* Input ``opn.example.com`` in `Alternate Hostnames` to prevent the error: `The HTTP_REFERER "https://opn.example.com/" does not match the predefined settings`
* Press **Save**

Open ``https://opn.example.com`` and it should serve the reverse proxied OPNsense WebGUI. Check the log file for errors if it does not work, most of the time the `TLS Server Name` doesn't match the SAN of the `TLS Trust Pool`. Caddy does not support certificates with only a CN `Common Name`.

.. Attention:: Create an :ref:`Access List <accesslist-opnsense-caddy>` to restrict access to the WebGUI.


Redirect ACME HTTP-01 Challenge
-------------------------------

Sometimes an application behind Caddy uses its own ACME Client to get certificates, most likely with the HTTP-01 challenge. This plugin has a built in mechanism to redirect this challenge type easily to a destination behind it.

Make sure the chosen domain is externally resolvable. Create an A-Record with an external DNS Provider that points to the external IP Address of the OPNsense. In case of IPv6 availability, it is mandatory to create an AAAA-Record too, otherwise the TLS-ALPN-01 challenge might fail.

The configured `Domain` must use an ``empty port`` or ``443`` in the GUI, otherwise it can not use the TLS-ALPN-01 challenge for itself. The upstream destination must listen on Port ``80`` and serve ``/.well-known/acme-challenge/``, for the same `Domain` that is configured in Caddy.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Press **✎** and open an existing `Domain` or `Subdomain` and enable `advanced mode`

=================================== ====================
Options                             Values
=================================== ====================
**Domain:**                         ``foo.example.com``
**HTTP-01 Challenge Redirection:**  ``192.168.10.1``
=================================== ====================

* Press **Save** and **Apply**

The `HTTP-01 Challenge Redirection` is active and the upstream destination located at ``192.168.10.1`` will be able to issue the certificate for the domain ``foo.example.com``.

With this configuration, Caddy will choose the TLS-ALPN-01 challenge to get its own certificate for ``foo.example.com``, and reverse proxy the HTTP-01 challenge to ``192.168.10.1``, where the upstream destination can listen on port 80 for ``foo.example.com``. With TLS enabled in the `Handler`, an encrypted connection is automatically possible. The automatic HTTP to HTTPS redirection is also taken care of.


Filter by Domain
----------------

A large configuration can be challenging to navigate. To help, a filter functionality has been added to the top right corner of the `Domains`, `Subdomains` and `HTTP Handlers` tab, called `Filter by Domain`.

In `Filter by Domain`, one or multiple `Domains` can be selected, and as filter result, only their corresponding configuration will be displayed in `Domains`, `Subdomains` and `HTTP Handlers`.


----------------------
Advanced Configuration
----------------------


Multiple HTTP Handlers for the same Domain
------------------------------------------

`HTTP Handlers` are not limited to one per domain or subdomain. If there are multiple different paths to handle (e.g. ``/foo/*`` and ``/bar/*``), create a `HTTP Handler` for each of them.

When creating a `HTTP Handler` with an empty path, the templating logic will automatically place it last in the Caddyfile site block. This means, specific paths will always match before an empty path, regardless of their position in the configuration. This could be used to block specific paths with an `Access List`, route some paths to different upstreams, and then set an empty handle for all unmatched paths.

Different handling logics can be selected. E.g., `handle_path` to strip the path from all requests, or `handle` to preserve the path from all requests.

When using a mix of wildcard domains and subdomains, a `HTTP Handler` set exclusively on the wildcard domain will match after all subdomains. That way, all unmatched subdomains can be sent to a custom upstream.

Multiple domains with the same hostname and different ports can be created at the same time. E.g., ``opn.example.com:443`` and ``opn.example.com:8443``. Now the frontend can listen on multiple ports for the same domain. These domains will share the same certificate automatically if ACME manages them. Each of these sockets need their own `HTTP Handler` to proxy traffic.

An example Caddyfile could look like this:

.. code-block::

    # Reverse Proxy Domain: "531e7877-0b58-4f93-a9f0-54beee58bdea"
    opn.example.com:443 {
            handle /private/* {
                    @d72c1182-6f05-4c25-8d9f-6a226a9039ea {
                            not client_ip 192.168.0.0/16 172.16.0.0/12 10.0.0.0/8
                    }
                    handle @d72c1182-6f05-4c25-8d9f-6a226a9039ea {
                            abort
                    }

                    reverse_proxy 172.16.99.10:8443 {
                    }
            }

            handle /different_upstream/* {
                    reverse_proxy 192.168.1.33 {
                    }
            }

            handle {
                    reverse_proxy 172.16.99.10:8443 {
                    }
            }
    }
    # Reverse Proxy Domain: "58760ae1-2409-4a6b-a6c4-d58b15706b55"
    opn.example.com:8443 {
            handle_path /strip_this {
                    reverse_proxy 10.10.10.10:8443 {
                    }
            }
    }

.. Tip:: `Access Lists` can match directly on `HTTP Handlers` for more complex access control scenarios.


Reverse Proxy a Webserver with Vhosts
-------------------------------------

Sometimes it is necessary to alter the host header in order to reverse proxy to another webserver with vhosts.

Since Caddy passes the original host header by default (e.g. ``app.external.example.com``), if the upstream destination listens on a different hostname (e.g. ``app.internal.example.com``), it would not be able to serve this request.

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Domains`

* Press **+** to create a new `Domain`

=================================== ============================
Options                             Values
=================================== ============================
**Domain:**                         ``app.external.example.com``
=================================== ============================

* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> HTTP Headers`

* Press **+** to create a new `HTTP Header`

=================================== ============================
Options                             Values
=================================== ============================
**Header:**                         ``header_up``
**Header Type:**                    ``Host``
**Header Value:**                   ``{upstream_hostport}``
=================================== ============================

* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> HTTP Handler`

* Press **+** to create a new `HTTP Handler` and enable `advanced mode`

=================================== ========================================
Options                             Values
=================================== ========================================
**Domain:**                         ``app.external.example.com``
**Upstream Domain:**                ``app.internal.example.com``
**HTTP Headers:**                   ``header_up Host {upstream_hostport}``
=================================== ========================================

* Press **Save** and **Apply**


CrowdSec Integration
--------------------

CrowdSec is a powerful alternative to a WAF. It uses logs to dynamically ban IP addresses of known bad actors. The Caddy plugin is prepared to emit the json logs for this integration.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> Log Settings`

* Enable `Log HTTP Access in JSON Format`
* Press **Save**

Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy –-> Domains`

* Open each `Domain` that should be monitored by CrowdSec and open `Access`
* Enable `HTTP Access Log`

Now the HTTP access logs will appear in ``/var/log/caddy/access`` in json format, one file for each domain.

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


High Availability Setups
------------------------

There are a few possible configurations to run Caddy successfully in a High Availability Setup with two OPNsense firewalls.

The main issue is the certificate handling. If a CARP VIP is used on the WAN interface, and the A and AAAA Records of all domains point to this CARP VIP, the backup Caddy will not be able to issue ACME certificates without some additional configuration.

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

Now both Caddy instances will be able to issue ACME certificates at the same time. Caddy on the master OPNsense uses the TLS-ALPN-01 challenge for itself and reverse proxies the HTTP-01 challenge to the Caddy of the backup OPNsense. Please make sure, that the master and backup OPNsense are both listening on their WAN and LAN (or VLAN) interfaces on port ``80`` and ``443``, since both ports are required for these challenges to work.

.. Tip:: Check the Logfile on both Caddy instances for successful challenges. Look for ``certificate obtained successfully`` informational messages.


Forward Auth
------------

Delegating authentication to Authelia, before serving an app via reverse proxy, is a very advanced usecase. `The Forward Auth Documentation <https://caddyserver.com/docs/caddyfile/directives/forward_auth#authelia>`_ should be used for inspiration.

To attach the Forward Auth directive to a handler, the Auth Provider has to be filled out in the General Settings. Afterwards, the Forward Auth checkbox in a Handler can be selected in `advanced mode`. This will prepend the `forward_auth` directive in front of the `reverse_proxy` directive in the scope of that Handler. Headers are set automatically.

Using Access Lists and Basic Auth in the Domain this Handler matches on is not recommended.

An example Caddyfile could look like this:

.. code::

    app1.example.com {
        handle {
            forward_auth authelia:9091 {
                uri /api/verify?rd=https://auth.example.com
                copy_headers Remote-User Remote-Groups Remote-Name Remote-Email
            }
            reverse_proxy 192.168.10.1:8080 {
            }
        }
    }

Requests from clients to `app1.example.com` will be sent to Authelia via the `forward_auth` directive. Then, after the authentication has been completed, the `reverse_proxy` directive sends the traffic to the Upstream.


Run Caddy Process Unprivileged
------------------------------

In this plugin, Caddy runs as root. This is required when well-known ports are used. Since the default ports are 80 and 443, Caddy will be started as superuser.

For higher security demands, there is the option to run Caddy as `www` user and group. This comes with the restriction of only being able to use upper ports (≥ 1024).

Make sure all of the domains have empty ports, or ports above the well-known port range before continuing. There is a validation that will prevent configuring well-known ports when the `www user` is active.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> Advanced Settings`

* | Add custom upper `HTTP Port`, e.g. ``8080``
* | Add custom upper `HTTPS Port`, e.g. ``8443``
* | Select ``www`` as `System User`
* | Restart Caddy completely. Disable it and press Apply, then enable it and press Apply.

From now on, Caddy will run as `www` user and group. This can be verified by checking the user of the Caddy process.

.. Note:: With this configuration, `Port Forward` should be used to forward port 80 and 443 to the new alternative HTTP and HTTPS Ports. For IPv6 additional steps could be required.


Bind Caddy to Interfaces
------------------------

.. Warning:: Binding a service to a specific interface via IP address can cause lots of issues. If the IP address is dynamic, the service can crash or refuse to start. During boot, the service can refuse to start if the interface IP addresses are assigned too late. Configuration changes on the interfaces can cause the service to crash. **Only use this with static IP addresses! There is no OPNsense community support for this configuration.**

This configuration is only useful if there are two or more WAN interfaces, and Caddy should only respond on one of them. It can also solve port conflicts, for example if one interface should DNAT or host a different service with the default webserver ports.

* Create the following files with the following content in the OPNsense filesystem:

1. ``/usr/local/etc/caddy/caddy.d/defaultbind.global``

.. code::

    default_bind 203.0.113.1 192.168.1.1


2. ``/usr/local/etc/caddy/caddy.d/defaultbind.conf``


.. code::

    http:// {
    bind 203.0.113.1 192.168.1.1
    }

Now Caddy will only bind to ``203.0.113.1`` and ``192.168.1.1``. It can still be configured in the GUI without restrictions.

Read more about the ``default_bind`` directive: `Default Bind <https://caddyserver.com/docs/caddyfile/options#default-bind>`_


Custom Configuration Files
--------------------------

* | The Caddyfile has an additional import from the path ``/usr/local/etc/caddy/caddy.d/``. Place custom configuration files inside that adhere to the Caddyfile syntax.
* | ``*.global`` files will be imported into the ``global block``.
* | ``*.conf`` files will be imported into the ``site block``.
* | ``*.layer4`` files will be imported into the ``layer4 directive``.
* | Don't forget to test the custom configuration with ``caddy validate --config /usr/local/etc/caddy/Caddyfile``.

With these imports, the full potential of Caddy can be unlocked. The GUI options will remain focused on the reverse proxy. **There is no OPNsense community support for configurations that have not been created with the offered GUI**. For customized configurations, the Caddy community is the right place to ask.


====================
Caddy: Layer4 Routes
====================


-------------
Enable Layer4
-------------

* | Go to :menuselection:`Services --> Caddy Web Server --> General Settings` and enable the `advanced mode`
* | Enable the checkbox `Enable Layer4`
* | Press **Apply**, then go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Layer4 Routes`

.. Tip::
    **Layer4 Routing Precedence**

    - automatic, order of listed items in the WebGUI does not influence this

    #. `SSH (and other protocols that can only match all traffic)`
    #. `HTTP (Host Header)`
    #. `TLS (SNI)`
    #. `TLS (inverted SNI)`
    #. `HTTP Handlers` (hidden default route)


--------
Matchers
--------

A matcher checks the first bytes of a TCP/UDP paket and decides which protocol it could be. Right now, SNI and Host matchers are supported. They either check the contents of the `Client Hello` at the start of a TLS handshake, or the `Host Header` in case of HTTP traffic. Since most traffic is TLS and HTTP, there is a lot of flexibility without making configuration too complicated. There are also protocol matchers like `SSH` that can match and route raw traffic without making decisions based on SNI or Host, since the SSH protocol does not send that information.

`Layer4 Routes` match before domains in the `Domains Tab`. That is why already existing domains can not be selected in a matcher. They have to be manually filled in. Multiple domains and even wildcards can be matched in the same `Layer4 Route`.


SSH, RDP, and other protocols
-----------------------------

This is a raw protocol matcher. It will match **all** traffic that looks like the chosen protocol on the default ports of Caddy, and proxy it to the selected upstream. **Only one of these routes per protocol will match. Host Headers or SNI can not be evaluated.**

* Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Layer4 Routes`
* Press **+** to create a new `Layer4 Route`

=================================== ============================
Options                             Values
=================================== ============================
**Domain:**                         ``*``
**Matcher:**                        ``SSH``
**Upstream Domain:**                ``192.168.1.1``
**Upstream Port:**                  ``22``
=================================== ============================

* Press **Save** and **Apply**

Now an SSH client can open up a proxied connection like ``ssh app1.example.com -p 443`` and the SSH traffic will go over the same port as other HTTP/HTTPS traffic. Caddy becomes a protocol multiplexer.

.. Tip:: If another route is added, e.g. with the RDP matcher, then SSH and RDP will be on the same port but will be proxied to different upstreams.


HTTP (Host Header)
------------------

Same logic as the `SNI` matcher, but can be used to route `HTTP` traffic, since the `Host Header` is evaluated.

.. Note:: `Host` and `SNI` matchers can be used at the same time for the same domains, to route HTTP and TLS traffic to different sockets.
.. Attention:: When Browsers find an available HTTPS socket for the same domain name, they might force a redirect to the secure channel. Verify with curl that the HTTP route indeed works as intended.


TLS (SNI)
---------

As example, there is an application with the hostname `app1.example.com` which should **not** be handled by the default `HTTP Handlers`. The TLS `TCP/UDP` traffic of this application should be routed directly to the upstream destination without TLS termination. At the same time, all other traffic should be routed to the default `HTTP Handlers`.

* Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Layer4 Routes`
* Press **+** to create a new `Layer4 Route`

=================================== ============================
Options                             Values
=================================== ============================
**Domain:**                         ``app1.example.com``
**Matcher:**                        ``SNI``
**Upstream Domain:**                ``192.168.1.1``
**Upstream Port:**                  ``8443``
=================================== ============================

* Press **Save** and **Apply**

Caddy listens on the default HTTP and HTTPS ports. All traffic it receives on these or any other listening ports, gets passed to the `listener_wrapper`. Inside this wrapper, the traffic can be inspected on Layer4, and routing decisions can be made.

With the matcher `TLS (SNI)`, the `Client Hello` of the TLS traffic is analyzed. When the `Client Hello` includes `app1.example.com`, the traffic will be matched by the new `Layer4 Route`. The raw `TCP/UDP` traffic will be streamed to the chosen socket - which consists of `Upstream Domain` and `Upstream Port`.

Any other traffic that is not matched by any `Layer4 Route` will be routed to the `HTTP Handlers`, where the configured `Domains` and `Subdomains` can receive and reverse proxy it.

.. Note:: When `Auto HTTPS` is enabled, all clients will be permanently redirected to HTTPS automatically. If that should not happen, set it to `Disable Redirects`.


TLS (inverted SNI)
------------------

This matcher is very powerful. It can route all unmatched domains, for example to a hosting panel where the domains are not under administrative control and can change at any time. Any matched domains will be routed to the `HTTP Handlers`.

* Go to :menuselection:`Services --> Caddy Web Server --> Reverse Proxy --> Layer4 Routes`
* Press **+** to create a new `Layer4 Route`

=================================== ====================================
Options                             Values
=================================== ====================================
**Domain:**                         ``*.example.com`` ``*.opnsense.com``
**Matcher:**                        ``not SNI``
**Upstream Domain:**                ``192.168.1.1`` ``192.168.1.2``
**Upstream Port:**                  ``443``
**Fail Duration:**                  ``10``
=================================== ====================================

* Press **Save** and **Apply**

With the Matcher `TLS (inverted SNI)`, the `Client Hello` of the TLS traffic is analyzed. When the `Client Hello` includes either of `*.example.com` or `*.opnsense.com`, the traffic will be sent to the default `HTTP Handlers`, where the configured `Domains` and `Subdomains` can receive and reverse proxy it.

All other `TCP/UDP` traffic will be streamed to the chosen socket of `Upstream Domain` and `Upstream Port`. Since we chose multiple upstreams and a health check, two servers can load balance all requests. The load balancing is just an example, and not necessary for this matcher to work.

.. Tip:: If there are domains inside `*.example.com` that should be routed to a different upstream, just create an additional `TLS (SNI)` matcher for them. It will automatically match before the `TLS (inverted SNI)` - compare to the `Layer4 Routing Precedence`.
.. Tip:: Caddy supports the HA Proxy Protocol. If the Protocol Header should be added to the upstream, set the `Proxy Protocol` version to ``v1`` or ``v2``.


======================
Caddy: Troubleshooting
======================


--------------------
Help, Nothing Works!
--------------------

.. Note:: Even though Caddy itself is quite easy to configure in the plugin, setting the infrastructure up correctly poses the real challenge. If you feel stumped, the best approach is knowledge about what `should` happen. This section tries to explain that and gives examples how to resolve issues.
.. Tip:: Most errors happen because the infrastructure is not set up correctly, or wrong options for the `HTTP Handler` have been set.
.. Attention:: Do not use the Layer4 module without knowing the implications of it. It is for very advanced usecases. Better deactivate it if things do not work as expected.

**This is what should happen if Caddy works correctly:**

#. | A `Web Browser` is opened and an `URL` is put into the address bar: `https://example.com`
#. | The underlying `Operating System` of the `Web Browser` sends a request to its default `DNS Server`, and asks where to find `example.com`. The `DNS Server` will try to find the requested `A- and/or AAAA-Record` for that domain, and will answer with e.g. `203.0.113.1`.
#. | The `Web Browser` now sends a `HTTPS request` to `203.0.113.1`. This request contains a `Client Hello` in the TLS handshake, that contains `example.com`.
#. | This `HTTPS request` hits port `443` of the OPNsense's `WAN`, `LAN` (or `VPN`) interface, determined by the network location of the `Web Browser`.
#. | There is a Firewall rule that allows destination port `443` to access `This Firewall`. The request will then be received by Caddy, because it listens on `This Firewall` on port `443`.
#. | In Caddy, there is a domain for `example.com` set up. It has a valid Let's Encrypt or ZeroSSL certificate. Since the `Client Hello` contains `example.com`, Caddy will match it with the domain, and the `Web Browser` shows a certificate next to `https://example.com` in the address bar.
#. | Caddy takes the `HTTPS` request and terminates the `TLS` connection. That means, it will convert the `HTTPS` into `HTTP`, so it can be processed by the `HTTP Handler`.
#. | Caddy checks if there is a matching `HTTP Handler` set up. It will be used to `reverse proxy` the `HTTP request` to an internal service.
#. | Inside the `HTTP Handler`, the domain `example.com` and an `Upstream Domain` e.g. `192.168.10.1` and `Upstream Port` e.g. `8080` point the request to the internal service. Caddy then sends the `HTTP request` directly to the internal service.
#. | The `HTTP response` from the internal service is received by Caddy, wrapped back into `TLS`, and sent back to the `Web Browser` as `HTTPS response`.
#. | The website of the internal service shows up in the `Web Browser`, secured by `HTTPS`.

.. Attention:: If that does not work, it means that one or multiple steps in that chain of events fail. Please check the following steps for initial troubleshooting.

**1. Check the Infrastructure:**

* Do `A- and/or AAAA-Record` for all `Domains` and `Subdomains` exist?
* In case of activated :ref:`Dynamic DNS <dynamicdns-opnsense-caddy>`, check that the correct `A- and/or AAAA-Records` have been set automatically with the DNS Provider.
* Do they point to one of the external IPv4 or IPv6 addresses of the OPNsense Firewall? Check that with commands like ``nslookup example.com``
* Do the OPNsense `Firewall Rules` allow connections from `any` source to destination ports `80` and `443` to the destination `This Firewall`?
* Is the Caddy service running?

**2. Check if the Domain is set up correctly:**

* Open the `Domain` in a `Web Browser`. Inspect the certificate by clicking on the 🔒 in the address bar. It should be a `Let's Encrypt`, `ZeroSSL` or `custom certificate` (if chosen).
* Activate the `HTTP Access Log` in a `Domain`, and check the `Log File`. Are there any log entries that show connections?
* If nothing shows up, go back to Step 1 and check the infrastructure.

**3. Check the functionality of the internal webserver:**

* Does the service accept `HTTP` or `HTTPS` connections? It is recommended to connect via `HTTP`, since it removes complexity.
* Open the internal service via IP address and port in a `Web Browser`, e.g. ``http://192.168.10.1:8080``. Validate that it shows the website on either `HTTP` or `HTTPS` ports.
* Does the internal service actually use the `HTTP` or `HTTPS` protocol? Other protocols will not work, e.g. `SSH`.
* If the `Web Browser` can not connect, it is a good idea to troubleshoot the internal webserver before continuing.

**4. Check the setup of the HTTP Handler:**

* Is the correct `Domain` chosen?
* Are `Upstream Domain` and `Upstream Port` correct? Do they point to the internal service, e.g ``192.168.10.1:8080``?
* If the internal service only accepts HTTPS connections, is `https://` chosen and `TLS insecure skip verify` checked?

.. Attention:: If the configuration is still not working, it is time to continue with logs and Caddyfile syntax checks.


---------------------------------
Get Help from the Caddy Community
---------------------------------

Sometimes, things do not work as expected. Caddy provides a few powerful debugging tools to analyze issues.

This section explains how to obtain the required files to get help from the `Caddy Community <https://caddy.community>`_.

1. Change the global Log Level to `DEBUG`. This will log `everything` the ``reverse_proxy`` directive handles.

Go to :menuselection:`Services --> Caddy Web Server --> General Settings --> Log Settings`

* Set the `Log Level` to `DEBUG`
* Press **Apply**

Go to :menuselection:`Services --> Caddy Web Server --> Log File`

* Change the dropdown from `INFORMATIONAL` to `DEBUG`

Now the ``reverse_proxy`` debug logs will be visible and can be downloaded.

2. Validate and download the Caddyfile.

Go to :menuselection:`Services --> Caddy Web Server --> Diagnostics --> Caddyfile`

* | Press the `Validate Caddyfile` button to make sure the current Caddyfile is valid. Refresh the page afterwards to ensure the Caddyfile is correctly formatted.
* | Press the `Download` button to get this current Caddyfile.
* | If there are custom imports in ``/usr/local/etc/caddy/caddy.d/``, download the JSON configuration.

.. Attention:: Rarely, a performance profile might be requested. For this, a special admin endpoint can be activated. This admin endpoint is deactivated by default. To enable it and access it on the OPNsense, follow these additional steps. Do not forget to deactivate it after use. Anybody with network access to the admin endpoint can use REST API to change the running configuration of Caddy, without authentication.

* | SSH into the OPNsense shell
* | Stop Caddy with ``configctl caddy stop``
* | Go to ``/usr/local/etc/caddy/caddy.d/``
* | Create a new file called ``admin.global`` and put the following content into it: ``admin :2019``
* | After saving the file, go to ``/usr/local/etc/caddy`` and run ``caddy validate`` to ensure the configuration is valid.
* | Start Caddy with ``configctl caddy start``
* | Use sockstat to see if the admin endpoint has been created. ``sockstat -l | grep -i caddy`` - it should show the endpoint ``*:2019``.
* | Create a firewall rule on ``LAN`` that allows ``TCP`` to destination ``This Firewall`` and destination port ``2019``.
* | Open the admin endpoint: ``http://YOUR_LAN_IP:2019/debug/pprof/``
* | Follow the instructions on `Profiling Caddy <https://caddyserver.com/docs/profiling>`_.
