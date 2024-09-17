======================================
Web Application Firewall
======================================

.. contents:: Index


As part of the OPNsense Business Edition, Deciso offers a plugin to easily protect webservices against all sort
of injection attacks and provides encryption for traffic to and from the outside world.

Our Web Application Firewall plugin offers some functionality which can also be found in community plugins available,
but in a more user friendly manner. It combines the features most commonly used in `reverse proxies <https://en.wikipedia.org/wiki/Reverse_proxy>`__,
such as TLS offloading and load balancing.

To ease maintenance the :code:`OPNWAF` plugin offers usage of both internal certificates or newly generated
using the ACME protocol via `Let's Encrypt <https://letsencrypt.org/>`__ with a single click.


Prerequisites
---------------------------

Before using this plugin in combination with Let's Encrypt, make sure port 443 isn't being used for the
web gui of this firewall (:menuselection:`System->Settings->Administration`).

.. Note::

    When using Let's Encrypt, The Web Application Firewall uses the `tls-alpn-01` challenge type for easy domain verification, this requires the
    virtual server to listen on port 443. Make sure the firewall allows incoming HTTPS connections on port 443. If the client connects
    via a custom port, you can forward these requests to port 443, and configure the virtual server to forward these requests to the
    correct internal port.


Installation
---------------------------

To install this plugin, go to :menuselection:`System --> Firmware --> Plugins` and search for **os-OPNWAF**,
the [+] button downloads and installs the software.

Next go to :menuselection:`Firewall --> Web Application --> Settings` to enable it.


General
---------------------------

Before deep diving into the settings pages, we will explain the most important terminology used in this module.


Virtual servers
~~~~~~~~~~~~~~~~

A virtual server (also known as a virtual host) is a a concept which allows the use of multiple domains on a single webserver using
the same port.
In our case it offers the possibility to host various webservers inside your network and forward traffic to them in a secure fashion.


Locations
~~~~~~~~~~~~~~~~

Locations reside in virtual servers and describe on a path level how requests are being handled, if for example one would
like to forward only a subdirectory (like :code:`/api`) to a server in the network, the location is where to configure this.


Web protection
~~~~~~~~~~~~~~~~

The web protection options offer easy access to the `OWASP ModSecurity ruleset <https://owasp.org/www-project-modsecurity-core-rule-set/>`__
, which offers a set of generic attack detection rules against a wide range attacks including the `OWASP Top Ten <https://owasp.org/www-project-top-ten/>`__.


Setup
---------------------------

Before configuring virtual servers, let's take a look at the general settings pages (:menuselection:`Firewall --> Web Application --> Settings`).
After installation, the module itself should be enabled by default.

In order to use the integrated ACME client (for Let's Encrypt), the ACME enable checkbox needs to be set, the certificate agreement needs to be accepted
(next checkbox) and contact email needs to be specified.

Optionally a permanent redirect from HTTP to HTTPS can be enabled for all virtual servers (available as of 24.4.3).
The HTTP port can be customized if necessary by enabling the advanced mode.
Do not forget to create an additional firewall rule to allow access to the HTTP Port. When it is non standard, a port forward is necessary
(e.g., listen on 8080, forward 80 to 8080).

.. image:: images/OPNWAF_settings.png
    :width: 100%


Web protection is not enabled by default, but you can enable it in the `Web protection` tab. This is also the place
to configure the module and settings which apply for all virtual hosts.


Configure virtual servers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the general settings in place, we can start adding virtual servers to offload traffic to machines in our network.
First go to :menuselection:`Firewall --> Web Application --> Gateways` and click on the [+] in the top section of the screen,
which defines the virtual servers.


================================ ========================================================================================
Option                           Description
================================ ========================================================================================
Enabled                          Enable this virtual server.
LogLevel                         (advanced mode) Log verbosity level (available as of 24.4.2)
ServerName                       Fully qualified hostname for this server.
Port                             Port number this vhost will listen on, can easily be combined with firewall nat rules
                                 to map traffic to non standard ports when origination from remote destinations.
                                 (e.g., listen on 8443, forward 443 to 8443).
Description                      User friendly description for this vhost (optional).
**Trust**
Enable ACME                      Enable the ACME protocol to automatically provision certificates using Let's Encrypt,
                                 when set will ignore the selected certificate (and enable SSL on this virtual server).
Certificate                      When using a certificate available in the system trust store, select it here.
**Access**
CA for client auth               Require a client certificate signed by the provided authority before allowing
                                 a connection.
CRL for client auth              Attach the (first) found certificate revocation list for the selected CA to
                                 this virtual host. Please note when no CRL is offered all clients are rejected.
Verify depth for client auth     The depth actually is the maximum number of intermediate certificate
                                 issuers, i.e. the number of CA certificates which are max allowed to be followed while
                                 verifying the client certificate.
SSL Proxy check peer             This directive configures host name checking for server certificates when mod_ssl is
                                 acting as an SSL client. The check will succeed if the host name from the request URI
                                 matches one of the CN attribute(s) of the certificate's subject, or matches the
                                 subjectAltName extension. If the check fails, the SSL request is aborted and a 502
                                 status code (Bad Gateway) is returned.
**Security**
Header Security                  Header security, by default several privacy and security related headers are set,
                                 in some cases (old applications for example) you might want to disable
                                 sending default headers to clients. HSTS can be disabled here if necessary.
TLS Security profile             TLS security profile as documented by
                                 `Mozilla <https://wiki.mozilla.org/Security/Server_Side_TLS>`__
Disable Security Rules by ID     Select one or multiple Web Protection rules to disable via their IDs. This can help to
                                 selectively disable rules that cause false positives, without disabling the
                                 Web Protection completely. (available as of 24.4.3)
Web Protection                   When Web Protection is enabled for the host you may disable it for specific
                                 destinations here, or set it to detection only for logging purposes.
================================ ========================================================================================


The section above defines the port the virtual server will listen on. Remember, in order to use ACME (Let's encrypt) this should either
be 443 or the traffic should be forwarded from port 443 to the port defined here.

.. Note::

    Port numbers don't have to be unique when more virtual servers are defined as the hostname correctly identifies the
    location. Yet, there can't be duplicate hostnames, these have to be unique.


.. Warning::

    The `ALPN` protocol (the challenge type used by Let's Encrypt) will resolve the FQDNs specified in the virtual host
    entry to the IP address of the firewall. If your DNS records point to both IPv4 and IPv6 addresses, IPv6 will
    be preferred by the challenge, so make sure your firewall is reachable via IPv6 as well if this is the case.

When supplying a certificate manually via the system trust store you can assign it in this dialog as well.


Configure locations
~~~~~~~~~~~~~~~~~~~~~~~~

The virtual server itself doesn't provide much content to the user other than offering a page telling access is prohibited,
so the next step is to map directories to external locations. These can be defined in the "Locations" Grid underneath
the Virtual servers.

There are two different modes for locations:

#. | ProxyPass, which Reverse Proxies the HTTP traffic
#. | Redirect, which creates a HTTP redirect (available as of 24.10)


ProxyPass
^^^^^^^^^^^^^^^^^^^^^^^^

================================ ========================================================================================
Option                           Description
================================ ========================================================================================
Enabled                          Enable this location
VirtualServer                    The server this location belongs to
Path                             Path of the HTTP request to match (e.g. :code:`/` for all paths). You can also create
                                 multiple location entries, each with their own specific path (e.g. :code:`/docs`).
                                 They will be processed in the order of their creation.
Type                             Controls if its a ProxyPass or Redirect (available as of 24.10)
Remote destinations              Locations to forward requests to, when more than one is provided, requests will be
                                 loadbalanced in a round robin fashion. Supports :code:`http`, :code:`https`, :code:`ws`
                                 and :code:`wss` destinations.
                                 When your webapp uses websockets and https requests, use :code:`wss://`
                                 (available as of 22.10.1)
Access control                   List of networks allowed to access this path (empty means any)
Description                      User friendly description for this location
**Proxy Options**
TLS header passthrough           Select which headers to passthrough to the client, all headers will be prefixed with
                                 X- to distinct them more easily from the applications perspective. The original headers
                                 use underscores (_) these will be replaced for minus (-) signs to prevent applications
                                 dropping them. (available as of 24.4.2)
Preserve Host                    When enabled, this option will pass the Host: line from the incoming request to the
                                 proxied host, instead of the hostname specified in the location. This option should
                                 normally be turned Off. It is mostly useful in special configurations like proxied mass
                                 name-based virtual hosting, where the original Host header needs to be evaluated by the
                                 backend server. (available as of 24.4.2)
Connection timeout               Connect timeout in seconds. The number of seconds the server waits for the creation
                                 of a connection to the backend to complete. (available as of 24.4.2)
================================ ========================================================================================


The options here are quite simple, first you define a path on your end (:code:`/` in our example), next you define one or more
destinations this path should map to (for example you could point to a public server here, like https://opnsense.org).


.. Note::

    When more than one destination is provided, the load will be balanced automatically.

.. Tip::

    Constraining access to allow only specific networks or hosts can be arranged using the :code:`Access control` input.


Redirect
^^^^^^^^^^^

================================ ========================================================================================
Option                           Description
================================ ========================================================================================
Enabled                          Enable this location
VirtualServer                    The server this location belongs to
Path                             Path of the HTTP request to match (e.g. :code:`/` for all paths). You can also create
                                 multiple location entries, each with their own specific path (e.g. :code:`/docs`).
                                 They will be processed in the order of their creation.
Type                             Controls if its a ProxyPass or Redirect (available as of 24.10)
HTTP redirection message         Choose the HTTP redirection message. The default is 307, but others like 301 and 308 are
                                 also available.
Remote destinations              Locations to redirect requests to, only one is allowed per location per redirect
Access control                   List of networks allowed to access this path (empty means any)
Description                      User friendly description for this location
================================ ========================================================================================


When setting up a redirect, it will also match HTTPS if `Redirect HTTP to HTTPS` in General Settings has been enabled. If not,
only HTTPS is matched.

.. Note::

    When a :code:`/` location with a `Redirect` has been created, there can't be any additional `ProxyPass` locations that match
    the same :code:`/` location, nor a more specific :code:`/docs` location. The redirect will match first, since it will catch and
    redirect all traffic of the virtual server location. What is possible though, is that there is a :code:`/docs` location that
    redirects, and an additional :code:`/html` location that proxies traffic, in the scope of the same virtual server.


Test web protection
~~~~~~~~~~~~~~~~~~~~~~~~

When web protection was enabled, we always advise to test if it's actually functional. Luckily this is quite easy to test
using a webbrowser. For this example we will try to inject some sql code in the url, which should be blocked when properly configured:


:code:`https://your.example.domain/?id=100 or 'x'='y'`

This should show a page similar to the one below:

.. image:: images/OPNWAF_forbidden.png
    :width: 50%


When deploying web protection for virtual servers, it is a good idea to start with the `Detection Only` setting that can be set per virtual server.
This way, you can evaluate the `Web Security` log file, and look for rules that match.

This will reveal if the web application might be outdated and needs patching, because several web protection rules match
and would block connections.

If they are false positives, the rule IDs can be set as excemptions with the option `Disable Security Rules by ID`. Search the rules
in the dropdown, and select multiple ones you want to exclude.

After this configuration, set the Web Protection to `On (default)` to enable it. The web application should now be configured for production.
If there are still errors, repeat the above steps.

.. Attention::
    Do not exclude too many rules. These matches could be a potential misconfiguration of the web application behind the WAF. Only exclude rules
    that totally break the functionality of the web application.


Secure WebDav and HTTP File Servers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These servers have specific requirements to work through a WAF. They need an extended set of HTTP Verbs, and higher thresholds for the Request and Response Body.

A popular example for a WebDAV Server is Nextcloud or Owncloud.

Go to the `Web Protection` Settings, and set the `Allowed HTTP Verbs` (available as of 24.4.3) to:

`COPY, DELETE, GET, HEAD, LOCK, MKCOL, MOVE, OPTIONS, POST, PROPFIND, PROPPATCH, PUT, TRACE, UNLOCK`.

To allow large file uploads, set `Request Body Limit Action` (available as of 24.10) to `Process Partial`.
If you want to process as much content of the file as possible, enable the
`advanced mode` and set custom values for the `Request Body` and `Response Body` limits.

If the file is larger than the configured limits, it will only be processed partially.
This means, the whole file will be uploaded, but only a portion of the file is analyzed by the web application parser.
Rejecting can improve security, yet will make large files fail completely if they exceed the configured hard limits.

.. Note::

    Increasing the `Body` limits will increase the log file sizes, and will eventually use the disk of the OPNsense to write files upon inspection.
    For this, the `Request Body in Memory Limit` can be increased to 1GB to focus on RAM usage. If you want to use the least ressources, logging and disk I/O,
    leave all settings on default, and set `Request Body Limit Action` to `Process Partial`.


.. Tip::

    If many different file extensions are hosted on the WebDAV server, some of these will be blocked by default rules. In that case,
    disable the rule: :code:`920440 (URL file extension is restricted by policy)`


Protect a local server with certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the above virtual host configuration there are a couple of parameters related to client authentication. The
advantage of using these is that you can prevent unauthorized access to services using certificates signed by a (local)
certificate authority.

To use this functionality, first make sure you have a certificate authority defined in :menuselection:`System --> Trust --> Authorities`
which you are going to use to create certificates for your clients.

Next step is to add a VirtualServer which contains at least the following information:

================================ ========================================================================================
Option                           Description
================================ ========================================================================================
ServerName                       The fully qualified domain name this host listens to
Port                             Port number to bind to, you can use :doc:`Port forwarding </manual/nat>`
                                 to redirect traffic from standard ports to non standard ones when needed
Certificate / Enable ACME        Either use an ACME certificate or define one yourself,
                                 this one should be trusted by the browser connecting to this host
CA for client auth               select the Authority created earlier
================================ ========================================================================================


Followed by a location, which maybe as simple as binding path :code:`/` to a local machine without certificate at :code:`http://10.0.0.1`.

.. Tip::

    You can use revocation lists to pull back access rights for selected clients, just make sure to restart the service in
    order to make the changes effective.


After this step, clients should not be able to access the virtual host, next you can create a certificate for the client and import
it in the trust store. Usually browsers automatically pick these up when allowed by the client.
