====================================================
Dynamic DNS
====================================================

In order to update DNS records when the firewall's IP address changes, use a dynamic DNS service provider.

Our `os-ddclient` plugin offers support for various dynamic DNS services using either the `ddclient <https://ddclient.net/>`_ software or our native backend.

Prerequisites
---------------------------

Before installing and using this plugin, make sure to register an account with one of the supported DNS providers.

Installation
---------------------------

Installation of this plugin is rather easy, go to :menuselection:`System --> Firmware --> Plugins` and search for **os-ddclient**,
use the [+] button to install it.

Next go to :menuselection:`Services --> Dynamic DNS --> Settings` to configure one or more Dynamic DNS services.

General settings
---------------------------
The general settings tab allows you to customize the services settings which will affect all dynamic DNS accounts.

======================= =======================================================================================================================================================================
Option                  Description
======================= =======================================================================================================================================================================
Enable                  Enable or disable the service
Verbose                 Enable or disable detailed log messages for the service
Allow IPv6              Enable or disable retrieving and updating IPv6 addresses
Interval                How often (in seconds) the service checks if the appliance's IP addresses have changed
Backend                 The system the Select the backend to use, either "ddclient" or "native" (see below)
======================= =======================================================================================================================================================================

.. Note::

      With :code:`ddclient` developments sunsetting [`* <https://github.com/ddclient/ddclient/issues/528>`__] we decided to offer an alternative written in
      Python. Selecting the native backend replaces the employed implementation. If your service is supported, we do advise to try out the new native backend
      which also offers support for custom HTTP requests.

Accounts
---------------------------

The accounts tab allows you to configure one or more dynamic DNS providers which the service will update using an API call over HTTP(S).

======================= =======================================================================================================================================================================
Option                  Description
======================= =======================================================================================================================================================================
Enabled                 Enable or disable the account (allows turning entries off without removing them)
Description             A descriptive name for the account
Service                 The provider of your Dynamic DNS Service
resourceId              A pointer to the service to be updated, currently only relevant for Azure
Username                Login or user name to authenticate with, left empty when using token-based authentication
Password                Password, API key or security token to authenticate with
Zone                    Typically the second-level domain name to update. for example: *example.com*
Hostname(s)             A list of fully-qualified domain names to update via the selected service, separated by commas. For example: *subdomain.example.com*
Check ip method         The IP checking service to get the appliance's current IP address from
Interface to monitor    The interface to connect to the IP checking service from, or if the "Check ip method" is set to "Interface" the interface to collect an address from
Check ip timeout        How long to wait in seconds for the IP checking service to respond with an IP address
Force SSL               Enable connecting to IP checking and updating services over HTTPS, though majority only support HTTPS anyway
======================= =======================================================================================================================================================================

.. Note::

      To update a fully-qualified domain name's :code:`A` (IPv4) record and :code:`AAAA` (IPv6) record, you must:
      * Add one account for IPv4 with the "Check ip method" set to an IPv4 service
      * Add one account for IPv6 with the "Check ip method" set to an IPv6 service
      * On the *General Settings* tab, enable "Allow IPv6"

Provider-specific configuration
-------------------------------------

Cloudflare
```````````````````````````
For accounts with Cloudflare as provider, there is an additional option **Zone**, which should be set as the name of the zone containing the host to be updated, not its zone ID.

Cloudflare accepts authorization with the global token with the options

======================= =======================================================================================================================================================================
Option                  Value
======================= =======================================================================================================================================================================
Username                The email of the Cloudflare account.
Password                Global API Key.
======================= =======================================================================================================================================================================

Using an API token is recommended for security reasons, with ``Permissions`` :menuselection:`Zone --> DNS --> Edit` and ``Zone Resources`` :menuselection:`Include --> Specific zone --> zone with the host`, and the account options

======================= =======================================================================================================================================================================
Option                  Value
======================= =======================================================================================================================================================================
Username                token
Password                API token.
======================= =======================================================================================================================================================================

Netcup DNS
```````````````````````````

Netcup is a German hosting provider who offers an API for DNS manipulation:

*     Wiki: https://www.netcup-wiki.de/wiki/DNS_API
*     Technical documentation: https://ccp.netcup.net/run/webservice/servers/endpoint.php


======================= =======================================================================================================================================================================
Option                  Value
======================= =======================================================================================================================================================================
Username                customer number
Password                APIPassword|APIKey, both fields need to be concatenated using a pipe (:code:`|`) symbol as separator.
======================= =======================================================================================================================================================================

Mythic Beasts
```````````````````````````

Mythic Beasts is a UK based hosting provider who offers an API for DNS manipulation:

*     Wiki: https://www.mythic-beasts.com/support/API/DNSv2/dynamic-DNS
*     Technical documentation: https://www.mythic-beasts.com/support/API/DNSv2


======================= =======================================================================================================================================================================
Option                  Value
======================= =======================================================================================================================================================================
Username                Key ID
Password                Secret
======================= =======================================================================================================================================================================

