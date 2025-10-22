====================================
OpenID Connect
====================================

OpenID Connect (OIDC) is an identity layer built on top of the OAuth 2.0 protocol that allows applications to verify a user’s
identity and obtain basic profile information in a secure way.
While OAuth 2.0 is mainly used for authorization (granting access to resources),
OIDC adds authentication by introducing an ID Token, which is a digitally signed piece of information about the user.
This makes it possible for applications (called "relying parties") to confirm who the user is,
without having to manage passwords directly.
OIDC is widely used in single sign-on (SSO) scenarios, enabling users to log in with trusted identity providers
like Google, Microsoft, or enterprise systems, while keeping the process standardized and secure.


The business edition includes OpenID Connect support for some parts of the system, these will be further detailed
in this document


Basic workflow
------------------------------------------------------

In an OpenID Connect (OIDC) authentication flow, the application (client) redirects the user to an Identity Provider (IdP),
where the user logs in.
After successful authentication, the IdP sends back an authorization code (or token) to the client,
which it exchanges for an ID Token (and optionally access/refresh tokens).
The ID Token contains the user’s identity information, allowing the client to verify who the user is.

Multiple identity providers do support OIDC, the information offered for the relying party (in this case OPNsense), usually
consists of the following items:

*   Client ID (an id identifying this client)
*   Secret this client should use
*   Uri to locate the :code:`.well-known/openid-configuration` file
*   Authentication method used (for example :code:`POST`)

Usually the provider needs the return path configured as well, often these are called *"Redirect URIs"*, when our location is not in the
list, it's not allowed to return the token to the requested path.



Adding OpenID Providers
------------------------------------------------------


OpenID providers can be configured via :menuselection:`System --> Access --> OpenID Connect`, the table below describes all
available options and their purpose. The service type determines which ones are available.


.. tabs::

    .. tab:: Local settings

        Configures the service type and identification at OPNsense.


        ======================================== =====================================================================================================
        **Fieldname**                            **Purpose**
        ======================================== =====================================================================================================
        Application code                         Application code used on our end to identify this provider, this text will be used on our end as
                                                 part of the oidc endpoints. Needs to be unique in order to identify the proper IdP.
        Service                                  For which type of service may this provider be used, see services section
        Extensive log (debug)                    Log detailed audit messages
        Description                              Description of this provider
        ======================================== =====================================================================================================


    .. tab:: OpenID Connect provider

        This part of the configuration contains

        ======================================== =====================================================================================================
        **Fieldname**                            **Purpose**
        ======================================== =====================================================================================================
        Provider URL                             Location of the OpenID connect provider, e.g. https://id.provider.com,
                                                 the path ".well-known/openid-configuration" will be suffixed to find the configuration of this OP
        Client ID                                The client identifier of the RP (requesting party) at the OP (OpenID provider).
        Client Secret                            The client secret of the RP (requesting party) at the OP (OpenID provider).
        Authentication method                    Authentication method to use, eiher POST, BASIC or use what's offered by the provider.
        Additional scopes                        Select additional scopes to request, by default only oidc is requested.
        ======================================== =====================================================================================================

    .. tab:: Local database

        This section offers control on how to process authenticated users locally, independent of the type of service being used.

        ======================================== =====================================================================================================
        **Fieldname**                            **Purpose**
        ======================================== =====================================================================================================
        User identification field                Fieldname from the UserInfo response to use.
        Create user                              On successful login, create or update the user (including groups when selected)
        Group attribute                          The attribute name in UserInfo object which contains the groups this user belongs to.
        Default groups                           When created locally, always assign these groups.
        Limit groups                             When created locally, only allow these groups to be offered via the provider.
        ======================================== =====================================================================================================



Services
------------------------------------------------------

When using OIDC on OPNsense, the service decides the endpoint used on the firewall to initiate the login sequence.
As each authentication flow could use its own implementation, we need some stepping stone which guides the browser to the proper
login provider.

As these endpoints are usually also the return paths for the openid provider, we will describe the relevant paths per
service type.


WebGui / Admin
.......................................................

When the :code:`WebGui / Admin` service is selected, the OPNsense login screen will show the option below the user/password
fields.

These options do not need to be selected in the :menuselection:`System --> Settings --> Administration` page under authentication server,
as there is only one WebGui to choose from.

The following endpoints are available for this service type:

======================================== =====================================================================================================
uri                                      Purpose
======================================== =====================================================================================================
/api/oidc/rp/login/<<appcode>>           Login, locates the provider uri and initiates the flow
/api/oidc/rp/finalize/<<appcode>>        After login, the openid provider forwards to here and a session is created with the
                                         proper privileges set.
======================================== =====================================================================================================




Captive Portal
.......................................................

A captive portal provider needs to be selected in the authentication option inside the zone configuration as these can be used in different zones.

The following endpoints are available for this service type:

========================================================== =====================================================================================================
uri                                                        Purpose
========================================================== =====================================================================================================
/api/captiveportal/access_oidc/login/[<<appcode>>]         Login, when there is only one oidc provider attached to the zone, the appcode may be omitted.
                                                           In which case the controller locates the appcode and requests the proper finalize path from the OP.
/api/captiveportal/access_oidc/finalize/<<appcode>>        After login, the openid provider forwards to here and a captive portal session is
                                                           created.
/api/captiveportal/access_oidc/logout/[<<appcode>>]        End captive portal session
========================================================== =====================================================================================================

After configuring the captive portal zone to use the OIDC provider, we need to deploy a custom template as well.
The html example below explains the relevant sections to implement in order to use OIDC.

.. code-block:: html
    :linenos:
    :emphasize-lines: 5, 8, 14, 23

    ....
    <script>
        $( document ).ready(function() {
            let addr = new URL(window.location);
            /* the status parameter is used to easily determine which action is requested  */
            switch (addr.searchParams.get('status')) {
                case null:
                    /* When not set, request client status via the standard controller */
                    $.ajax({url: "/api/captiveportal/access/status/", dataType:"json"}).done(function(data) {
                        if (data['clientState'] == 'AUTHORIZED') {
                            /* already logged in */
                            $(".status-logged-in").show();
                        } else {
                            /* unhide "loader" text and redirect to trampoline */
                            $(".status-empty").show();
                            window.location = '/api/captiveportal/access_oidc/login/';
                        }
                    });
                    break;
                case 'logged-in':
                case 'logged-out':
                case 'login-failed':
                    /* show status <div/> */
                    $(".status-" + addr.searchParams.get('status')).show();
                    break;
            }
        });
    </script>
    ....
    <section class="content-row">
        <article class="wrapper">
            <div class="content status-logged-in" style="display: none;">
                <h1>Session logged in </h1><br/>
                <h1><a href="/api/captiveportal/access_oidc/logout/">Logout</a></h1>
            </div>
            <div class="content status-logged-out" style="display: none;">
                <h1>Session logged out </h1><br/>
                <h1><a href="/api/captiveportal/access_oidc/login/">Login</a></h1>
            </div>
            <div class="content status-login-failed" style="display: none;">
                <h1>Login failed </h1>
            </div>
            <div class="content status-empty" style="display: none;">
                <h1>Redirecting to login...</h1>
            </div>
        </article>
    </section>
    ....

::download:`Download full example <resources/cp_template.zip>`

The full example zip is an easy to use template package which can be uploaded via  :menuselection:`Services --> Captive Portal --> Administration`
in the templates tab.

.. Note::

    When offering a single OIDC provider for a captive portal zone, we can generalize the template as no app code needs to be offered.
    In case multiple options need to be available, a custom template need to be created offering the user a choice between options when
    no session exists yet. (e.g. :code:` window.location` can't be used to forward to the provider)

Since users need to be able to access the oidc provider (which is usally not in the same network),
the ip address (or group of addresses) should be excluded from entering the portal.
In most cases these aren't just static addresses, in which case you need to use custom firewall rules to allow traffic to the provider (such as Microsoft Entra ID).
The `captive portal documentation <../captiveportal.html#captive-portal-firewall-rules>`__  explains how to define custom rules for these case.

.. Tip::
    When your provider is hosted in a rather dynamic environment (such as Microsoft Entra ID), you probably want to put the associated
    domains in an allow list. The included Dnsmasq service can be of great help there as explained
    in the `IPset <../dnsmasq.html#firewall-alias-ipset>`__ feature documentation.


OPNWAF (Web application firewall / reverse proxy)
.......................................................

The reverse proxy defines one endpoint specifically to be used by oidc when an "OIDC Provider" is selected in the virtual server configuration:

========================================================== =====================================================================================================
uri                                                        Purpose
========================================================== =====================================================================================================
/oidc/callback                                             predefined vanity url that can not be used in the application as location.
                                                           It can be optionally changed via the ``OIDC Redirect URI`` setting in a virtual server.
========================================================== =====================================================================================================


Useful links
------------------------------------------------------

Below a collection of useful links how to setup OpenID at various providers:

*   Microsoft Entra ID (https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-openid-connect)
*   Authentic (https://docs.goauthentik.io/add-secure-apps/providers/oauth2/)
*   Jumpcloud (https://jumpcloud.com/support/sso-with-oidc)
