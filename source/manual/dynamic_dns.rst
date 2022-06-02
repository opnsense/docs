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
======================= =======================================================================================================================================================================


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
Username                Login or user name to use, could be empty for token based authentication
Password                Password or security token to use
Hostname                Enter the fully qualified domain names to update via the selected service. For example: *myhost.dyndns.org*
Check ip method         Service to query the current IP address
Interface to monitor    Interface to collect an address from when choosing "Interface" as check ip method, or source interface used to connect to the check ip service
Description             A description to easily identify this rule in the overview.
======================= =======================================================================================================================================================================
