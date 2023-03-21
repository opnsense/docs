===========================
Intrusion Prevention System
===========================

The Intrusion Prevention System (IPS) system of OPNsense is based on Suricata_
and utilizes Netmap_ to enhance performance and minimize CPU utilization. This
deep packet inspection system is very powerful and can be used to detect and
mitigate security threats at wire speed.

.. _Netmap: https://www.freebsd.org/cgi/man.cgi?query=netmap&sektion=4&manpath=FreeBSD+12.2-RELEASE+and+Ports
.. _Suricata: https://suricata.io/

IDS and IPS
-----------

It is important to define the terms used in this document. An *Intrustion
Detection System* (IDS) watches network traffic for suspicious patterns and
can alert operators when a pattern matches a database of known behaviors. An
*Intrusion Prevention System* (IPS) goes a step further by inspecting each packet
as it traverses a network interface to determine if the packet is suspicious in
some way. If it matches a known pattern the system can drop the packet in
an attempt to mitigate a threat.

The Suricata_ software can operate as both an IDS and IPS system.

Choosing an interface
---------------------

You can configure the system on different interfaces. One of the most commonly
asked questions is which interface to choose. Considering the continued use
IPv4, usually combined with :doc:`/manual/nat`, it is quite important to use
the correct interface. If you are capturing traffic on a WAN interface you will
see only traffic after address translation. This means all the traffic is
originating from your firewall and not from the actual machine behind it that
is likely triggering the alert.

Rules for an IDS/IPS system usually need to have a clear understanding about
the internal network; this information is lost when capturing packets behind
NAT.

Without trying to explain all the details of an IDS rule (the people at
Suricata are way better in doing `that
<https://suricata.readthedocs.io/en/suricata-5.0.5/rules/index.html>`__), a
small example of one of the ET-Open rules usually helps understanding the
importance of your home network.

.. code-block:: sh

    alert tls $HOME_NET any -> $EXTERNAL_NET any (msg:"ET TROJAN Observed Glupteba CnC Domain in TLS SNI"; flow:established,to_server; tls_sni; content:"myinfoart.xyz"; depth:13; isdataat:!1,relative; metadata: former_category MALWARE; reference:md5,4cc43c345aa4d6e8fd2d0b6747c3d996; classtype:trojan-activity; sid:2029751; rev:2; metadata:affected_product Windows_XP_Vista_7_8_10_Server_32_64_Bit, attack_target Client_Endpoint, deployment Perimeter, signature_severity Major, created_at 2020_03_30, updated_at 2020_03_30;)


The :code:`$HOME_NET` can be configured, but usually it is a static net defined
in `RFC 1918`_. Using advanced mode you can choose an external address, but
bear in mind you will not know which machine was really involved in the attack
and it should really be a static address or network.

:code:`$EXTERNAL_NET` is defined as being not the home net, which explains why
you should not select all traffic as home since likely none of the rules will
match.

Since the firewall is dropping inbound packets by default it usually does not
improve security to use the WAN interface when in IPS mode because it would
drop the packet that would have also been dropped by the firewall.


.. Note::

    IDS mode is available on almost all (virtual) network types. IPS mode is
    *only* available with `supported physical adapters`_.

.. _RFC 1918: https://tools.ietf.org/html/rfc1918
.. _supported physical adapters: https://www.freebsd.org/cgi/man.cgi?query=netmap&sektion=4&manpath=FreeBSD+12.1-RELEASE+and+Ports#SUPPORTED_DEVICES

General setup
-------------

The settings page contains the standard options to get your IDS/IPS system up
and running.

=====================================================================================================================

====================================  ===============================================================================
Enabled                               Enable Suricata
IPS mode                              When enabled, the system can drop suspicious packets. In order for this to
                                      work, your network card needs to support netmap.
                                      The action for a rule needs to be "drop" in order to discard the packet,
                                      this can be configured per rule or ruleset (using an input filter)
Promiscuous mode                      Listen to traffic in promiscuous mode. (all packets in stead of only the
                                      ones addressed to this network interface)
Enable syslog alerts                  Send alerts to syslog, using fast log format
Enable eve syslog output              Send alerts in EVE_ format to syslog, using log level info.
                                      This will not change the alert logging used by the product itself.
                                      Drop logs will only be send to the internal logger,
                                      due to restrictions in suricata.
Pattern matcher                       Controls the pattern matcher algorithm.
                                      Aho–Corasick is the default. On supported platforms, Hyperscan is the best option.
                                      On commodity hardware if Hyperscan is not available the suggested setting is "Aho–Corasick Ken                                           Steele variant" as it performs better than "Aho–Corasick".
Interfaces                            Interfaces to protect. When in IPS mode, this need to be real interfaces
                                      supporting netmap. (when using VLAN's, enable IPS on the parent)
Rotate log                            Log rotating frequency, also used for the internal event logging
                                      (see Alert tab)
Save logs                             Number of logs to keep
====================================  ===============================================================================


.. Tip::

    When using an external reporting tool, you can use syslog to ship your EVE_
    log easily. Just enable "Enable EVE syslog output" and create a target in
    :menuselection:`System --> Settings --> Logging / Targets`. (filter
    application "suricata" and level "info")


.. Note::

    When using IPS mode make sure all hardware offloading features are disabled
    in the interface settings (:menuselection:`Interfaces --> Settings`). Prior
    to version 20.7, "VLAN Hardware Filtering" was not disabled which may cause
    issues for some network cards.

.. _EVE: https://suricata.readthedocs.io/en/suricata-5.0.5/output/eve/eve-json-output.html

Advanced options
----------------

Some less frequently used options are hidden under the "advanced" toggle.

=====================================================================================================================

====================================  ===============================================================================
Home networks                         Define custom home networks, when different than an RFC1918 network.
                                      In some cases, people tend to enable IDPS on a wan interface behind NAT
                                      (Network Address Translation), in which case Suricata would only see
                                      translated addresses in stead of internal ones. Using this option, you can
                                      define which addresses Suricata should consider local.
default packet size                   With this option, you can set the size of the packets on your network.
                                      It is possible that bigger packets have to be processed sometimes.
                                      The engine can still process these bigger packets,
                                      but processing it will lower the performance.
====================================  ===============================================================================

Download rulesets
-----------------

When enabling IDS/IPS for the first time the system is active without any rules
to detect or block malicious traffic. The download tab contains all rulesets
available on the system (which can be expanded using plugins).

In this section you will find a list of rulesets provided by different parties
and when (if installed) they where last downloaded on the system. In previous
versions (prior to 21.1) you could select a "filter" here to alter the default
behavior of installed rules from alert to block. As of 21.1 this functionality
will be covered by **Policies**, a separate function within the IDS/IPS module,
which offers more fine grained control over the rulesets.


.. Note::

    When migrating from a version before 21.1 the filters from the download
    rulesets page will automatically be migrated to policies.


Policies
--------

The **policy** menu item contains a grid where you can define policies to apply
to installed rules. Here you can add, update or remove policies as well as
disabling them. Policies help control which rules you want to use in which
manner and are the prefered method to change behaviour. Although you can still
update separate rules in the rules tab, adding a lot of custom overwrites there
is more sensitive to change and has the risk of slowing down the
user-interface.

A policy entry contains 3 different sections. First some general information,
such as the description and if the rule is enabled as well as a priority.
Overlapping policies are taken care of in sequence, the first match with the
lowest priority number is the one to use.

Secondly there are the matching criterias, these contain the **rulesets** a
policy applies on as well as the action configured on a rule (disabled by
default, alert or drop), finally there is the **rules** section containing the
metadata collected from the installed rules, these contain options as affected
product (Android, Adobe flash, ...) and deployment (datacenter, perimeter).

The last option to select is the new action to use, either disable selected
rules, only alert on them or drop traffic when matched.

.. Note::

    The options in the **rules** section depend on the vendor, when no metadata
    is provided in the source rule, none can be used at our end.


Installed rules
---------------

The rules tab offers an easy to use grid to find the installed rules and their
purpose, using the selector on top one can filter rules using the same metadata
properties available in the policies view.

.. Tip::

    After applying rule changes, the rule action and status (enabled/disabled)
    are set, to easily find the policy which was used on the rule, check the
    matched_policy option in the filter. Manual (single rule) changes are being
    marked as policy **"__manual__"**



Fingerprinting
--------------

OPNsense includes a very polished solution to block protected sites based on
their SSL fingerprint. You can manually add rules in the "User defined" tab.


Alerts
------

In the "Alerts" tab you can view the alerts triggered by the IDS/IPS system.
Use the info button here to collect details about the detected event or threat.

Advanced configuration
------------------------

OPNsense supports custom Suricata configurations in `suricata.yaml <https://suricata.readthedocs.io/en/suricata-6.0.0/configuration/suricata-yaml.html>`__
format. In order to add custom options, create a template file named :code:`custom.yaml` in the :code:`/usr/local/opnsense/service/templates/OPNsense/IDS/` directory.

Since this file is parsed by our template system, you are able to use template tags using the :doc:`Jinja2 </development/backend/templates/>` language.

Available rulesets
------------------

Emerging Threats
................

Emerging Threats (ET) has a variety of IDS/IPS rulesets. There is a free,
BSD-licensed version and a paid version available.

.. Tip::

    Proofpoint offers a community portal which provides access to documentation and updates about rules,
    you can visit it at https://community.emergingthreats.net/ . The `Frequently asked questions <https://community.emergingthreats.net/t/frequently-asked-questions/56>`__
    might be a good place to start reading.


ET Open
+++++++

The ETOpen Ruleset is *not* a full coverage ruleset and may not be sufficient
for many regulated environments and thus should not be used as a standalone
ruleset.

OPNsense has integrated support for ETOpen rules.


ETPro Telemetry
+++++++++++++++

Proofpoint offers a free alternative for the well known
:doc:`etpro_telemetry` ruleset.

Abuse.ch
........

`Abuse.ch <https://abuse.ch>`_ offers several blacklists for protecting against
fraudulent networks.


SSL Blacklist
+++++++++++++

*SSL Blacklist* (SSLBL) is a project maintained by abuse.ch. The goal is to provide
a list of "bad" SSL certificates identified by abuse.ch to be associated with
malware or botnet activities. SSLBL relies on SHA1 fingerprints of malicious SSL
certificates and offers various blacklists.

See for details: https://sslbl.abuse.ch/

Feodo Tracker
+++++++++++++

Feodo (also known as Cridex or Bugat) is a Trojan used to commit ebanking fraud
and steal sensitive information from the victim's computer, such as credit card
details or credentials. At the moment, Feodo Tracker is tracking four versions
of Feodo, and they are labeled by Feodo Tracker as version A, version B,
version C and version D:

*   **Version A**
    *Hosted on compromised webservers running an nginx proxy on port 8080 TCP
    forwarding all botnet traffic to a tier 2 proxy node. Botnet traffic usually
    directly hits these hosts on port 8080 TCP without using a domain name.*

*   **Version B**
    *Hosted on servers rented and operated by cybercriminals for the exclusive
    purpose of hosting a Feodo botnet controller. Usually taking advantage of a
    domain name within ccTLD .ru. Botnet traffic usually hits these domain names
    using port 80 TCP.*

*   **Version C**
    *Successor of Feodo, completely different code. Hosted on the same botnet
    infrastructure as Version A (compromised webservers, nginx on port 8080 TCP
    or port 7779 TCP, no domain names) but using a different URL structure.
    This Version is also known as Geodo and Emotet.*

*   **Version D**
    *Successor of Cridex. This version is also known as Dridex*

See for details: https://feodotracker.abuse.ch/

URLHaus List
++++++++++++

OPNsense version 18.1.7 introduced the URLHaus List from abuse.ch which collects
compromised sites distributing malware.

See for details: https://urlhaus.abuse.ch/

App detection rules
+++++++++++++++++++

OPNsense 18.1.11 introduced the app detection ruleset. Since about 80
percent of traffic are web applications these rules are focused on blocking web
services and the URLs behind them.

If you want to contribute to the ruleset see: https://github.com/opnsense/rules

How-tos
-------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   how-tos/ips-feodo
   how-tos/ips-sslfingerprint
