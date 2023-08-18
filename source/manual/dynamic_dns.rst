====================================================
Dynamic DNS
====================================================

In order to update dns registations when the local IP address changes, a Dynamic DNS service provider can be used.
Our `os-ddclient` plugin offers support for various services using the `ddclient <https://ddclient.net/>`__
software.

Prerequisites
---------------------------

Before installing and using this plugin, make sure to register an account with one of the supported services.


Installation
---------------------------

Installation of this plugin is rather easy, go to :menuselection:`System --> Firmware --> Plugins` and search for **os-ddclient**,
use the [+] button to install it.

Next go to :menuselection:`Services --> Dynamic DNS --> Settings` to configure one or more Dynamic DNS services.


General settings
---------------------------
The general settings tab offers access to general options used by all configured dynamic dns services on this firewall.
By default the service is enabled after installation,

======================= =======================================================================================================================================================================
Option                  Description
======================= =======================================================================================================================================================================
Enable                  Enable the client
Interval                The number of seconds address changes will be queried
Backend                 Select the backend to use, either "ddclient" or "native"
======================= =======================================================================================================================================================================

.. Note::

      With :code:`ddlient` developments sunsetting [`* <https://github.com/ddclient/ddclient/issues/528>`__] we decided to offer an alternative written in
      Python. Selecting the native backend replaces the employed implementation. If your service is supported, we do advice to try out the new native backend
      which also offers support for custom HTTP requests.

Accounts
---------------------------

In the primary tab you can register one or more dynamic dns providers which will be used to update dns registrations
using an api call over http(s) to the selected service.

.. Note::

      The local IP address used for this firewall will be obtained by querying one of the selected providers. Since ddclient
      currently doesn't support dual stack (IPv4+IPv6) opertion, make sure to either select an IPv4 or IPV6 address
      provider in the settings tab.

======================= =======================================================================================================================================================================
Option                  Description
======================= =======================================================================================================================================================================
Enable                  Enable this rule (allows turning entries off without removing them).
Service                 The provider of your Dynamic DNS Service.
resourceId              A pointer to the service to be updated, currently only relevant for Azure
Username                Login or user name to use, could be empty for token based authentication
Password                Password or security token to use
Hostname                Enter the fully qualified domain names to update via the selected service. For example: *myhost.dyndns.org*
Check ip method         Service to query the current IP address
Check ip timeout        How long to wait before the checkip process times out
Force SSL               Choose to use HTTP or HTTPS, but only for selected services. Most services only support HTTPS nowadays.
Interface to monitor    Interface to collect an address from when choosing "Interface" as check ip method, or source interface used to connect to the check ip service
Description             A description to easily identify this rule in the overview.
======================= =======================================================================================================================================================================

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
