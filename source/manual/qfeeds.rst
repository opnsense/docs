=================================================================
Q-Feeds connector
=================================================================

.. contents:: Index

--------------------------------------
Introduction
--------------------------------------

In today's world, keeping your network secure is super important. Next Generation Firewalls (NGFWs) are essential
tools for protecting your network. They can filter DNS and web traffic using external dynamic lists of threat
indicators, known as Indicators of Compromise (IoCs).

Q-Feeds provides dynamic, up-to-date lists of these IoCs, designed specifically for use with security controls like
NGFWs. By integrating Q-Feeds into your OPNsense firewall, you can improve your network's protection against
new and emerging threats. This means your firewall can automatically block harmful traffic and stay updated with
the latest threat information.

Two types of lists are supported by this plugin, IPs using firewall aliases and domains using an integration with
Unbound blocklists or DNSCrypt-Proxy.

This document explains how to install and use Q-Feeds on your OPNsense firewall.

--------------------------------------
External resources
--------------------------------------

In order to use Q-Feeds, a (free or paid) subscription is required. Please visit `https://qfeeds.com/opnsense/ <https://qfeeds.com/opnsense/>`__
for more information and to sign up for access.
The differences between available service offerings and extensive documentation is available there as well.

--------------------------------------
Installation
--------------------------------------

Installation of this plugin is rather easy, go to :menuselection:`System --> Firmware --> Plugins` and search for **os-q-feeds-connector**,
use the [+] button to install it.

Next go to :menuselection:`Security --> Q-Feeds Connect` to configure the service.



--------------------------------------
Activate the plugin
--------------------------------------

To activate the plugin please go to :menuselection:`Security --> Q-Feeds Connect`.
The settings page of the Q-Feeds plugin will now open and it asks for an API token.

You can obtain this token by register an account on our Threat Intelligence Portal (`https://tip.qfeeds.com <https://tip.qfeeds.com>`__).


After you've registered an account and logged in, on the dashboard you will find the **Manage API Keys** page. On
this page click **Create Free API Key**.

Copy the API token into the settings page of the plugin on your OPNsense appliance.
Click Apply and the plugin will start fetching the Threat Intelligence and create firewall aliases.


--------------------------------------
Menu options
--------------------------------------

The (configuration) options available via the plugin can be accessed via a set of tabs in :menuselection:`Security --> Q-Feeds Connect`.
Below you will find their purpose.

.. tabs::

    .. tab:: Setting

        Subscription configuration

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **//General Settings**
        **API key**                               The API key needed to access Q-Feeds.
        **Register domain feeds**                 Use domain feeds in Unbound DNS and DNScrypt-proxy blocklists,
                                                  requires blocklists to be enabled in order to have effect
        **//Unbound blocklist settings**
        **Allowlist Domains**                     Domains to allow (regex supported), only applies to blocklist matches
        **Source Net(s)**                         Source networks to apply policy on, leave empty for all
        **Destination Address**                   IP for blocklist entries (default 0.0.0.0)
        **Return NXDOMAIN**                       Use NXDOMAIN response instead of destination address
        ========================================= ====================================================================================

    .. tab:: Feeds

        Shows subscription status.

        ========================================= ====================================================================================
        **Field**                                 **Description**
        ========================================= ====================================================================================
        Description                               Name of the list
        Type                                      IP (firewall rules), domain (DNS, Unbound or DNSCrypt-Proxy)
        Updated at                                Last updated at (iso date)
        Next update                               Scheduled to be updated again at (iso date)
        Licensed                                  Valid license on this list installed
        ========================================= ====================================================================================

    .. tab:: Events

        When firewall rules are being send to the log, you can gather a list of events that took place for items in the firewall table.

        ========================================= ====================================================================================
        **Field**                                 **Description**
        ========================================= ====================================================================================
        Timestamp                                 Time the event occurred
        Interface                                 Which interface it was logged on
        Direction                                 Did this concern in(bound) or out(bound) traffic
        Source                                    Source IP address
        Destination                               Destination IP address
        ========================================= ====================================================================================



--------------------------------------
Firewall setup
--------------------------------------

In order to block traffic originating or going to addresses on the list, you will need firewall rules.
The most simple scenario would drop traffic coming from :code:`lan` going to items in our list or entering via :code:`wan`
originating from entries in the list.

From LAN:

==================================== ============================================== ===================================================
Parameter                            Value                                          Short description
==================================== ============================================== ===================================================
Action                               :code:`Block`                                  Drop packets silently
Interface                            :code:`LAN`                                    Traffic on the LAN interface
TCP/IP Version                       :code:`IPV4/IPV6`                              Both protocols are supported
Direction                            :code:`in`                                     By default we filter on inbound traffic
Destination                          :code:`__qfeeds_malware_ip`                    The QFeeds offered malware locations
Logging                              :code:`checked`                                With logging enabled, you can track offenders
==================================== ============================================== ===================================================

From WAN:

==================================== ============================================== ===================================================
Parameter                            Value                                          Short description
==================================== ============================================== ===================================================
Action                               :code:`Block`                                  Drop packets silently
Interface                            :code:`WAN`                                    Traffic on the LAN interface
TCP/IP Version                       :code:`IPV4/IPV6`                              Both protocols are supported
Direction                            :code:`in`                                     By default we filter on inbound traffic
Source                               :code:`__qfeeds_malware_ip`                    The QFeeds offered malware locations
Logging                              :code:`checked`                                With logging enabled, you can track offenders
==================================== ============================================== ===================================================


.. Note::

    Only non default rule settings which are offered in the tables above. More information about using firewall rules and aliases
    can be found in the :doc:`Firewall </firewall>` section.

--------------------------------------
DNS/Domain blocking using Unbound
--------------------------------------

.. Note::

    In order to make us of DNS based logging you need to configure Unbound as your primary DNS server. More
    information on how to configure this can be found  :doc:`here </manual/unbound>`


In :menuselection:`Security --> Q-Feeds Connect` make sure to enable **"Register domain feeds"** and hit Apply.
For older versions (<25.7.9) also make sure Unbound Blocklists are enabled in :menuselection:`Services --> Unbound DNS --> Blocklist`.

Additional Unbound blocklist options: **Allowlist Domains** lets you whitelist domains that would otherwise be blocked
(regex supported). **Source Net(s)** restricts the policy to specific client networks, e.g. 192.168.1.0/24; leave empty
for all clients. **Destination Address** sets the IP returned for blocked domains (default 0.0.0.0). **Return NXDOMAIN**
returns a non-existent domain response instead of redirecting, which hides blocklist behavior from clients.

You can use :menuselection:`Reporting --> Unbound DNS` to gain insights into the requested domains.

--------------------------------------
DNS/Domain blocking using DNSCrypt-Proxy
--------------------------------------

When the DNSCrypt-Proxy plugin is installed, domain feeds can be used for DNS blocking. Enable **"Register domain feeds"**
in :menuselection:`Security --> Q-Feeds Connect`, then select the Q-Feeds blocklist within the DNSCrypt-Proxy plugin
settings to activate it.


