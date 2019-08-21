==================================
Inline Intrusion Prevention System
==================================

The inline IPS system of OPNsense is based on Suricata and utilizes Netmap to
enhance performance and minimize cpu utilization. This deep packet inspection
system is very powerful and can be used to mitigate security threats at wire speed.


---------------
General setup
---------------

The settings page contains the standard options to get your IDPS system up and running.

=====================================================================================================================

====================================  ===============================================================================
Enabled                               Enable suricata
IPS mode                              When enabled, the system can drop suspicious packets. In order for this to
                                      work, your network card needs to support netmap.
                                      The action for a rule needs to be "drop" in order to discard the packet,
                                      this can be configured per rule or ruleset (using an input filter)
Promiscuous mode                      Listen to traffic in promiscuous mode. (all packets in stead of only the
                                      ones addressed to this network interface)
Enable syslog alerts                  Send alerts to syslog, using fast log format
Enable eve syslog output              Send alerts in eve format to syslog, using log level info.
                                      This will not change the alert logging used by the product itself.
                                      Drop logs will only be send to the internal logger,
                                      due to restrictions in suricata.
Pattern matcher                       Controls the pattern matcher algorithm.
                                      Aho-Corasick is the default. On supported platforms,
                                      Hyperscan is the best option.
Interfaces                            Interfaces to protect. When in IPS mode, this need to be real interfaces
                                      supporting netmap. (when using VLAN's, enable IPS on the parent)
Rotate log                            Log rotating frequency, also used for the internal event logging
                                      (see Alert tab)
Save logs                             Number of logs to keep
====================================  ===============================================================================

.. Note::

    When using IDPS on a NAT enabled interface, you probably would need to add the WAN address to "Home network" (see advanced options).
    The advantage of enabling IDPS on a local network interface is that source and destination addresses are as originally requested.
    (Usually rules use home network to distinct traffic)


.. Tip::

    When using an external reporting tool, you can use syslog to ship your eve log easily. Just enable "Enable eve syslog output" and
    create a target in :menuselection:`System --> Settings --> Logging / Targets`. (filter application "suricata" and level "info")

----------------
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


---------------
Finger Printing
---------------
OPNsense includes a very polished solution to block protected sites based on
their SSL fingerprint, you can add rules manually in the "User defined tab".


---------------------------
Rulesets
---------------------------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   etpro_telemetry


...................................
Emerging Threats ETOpen Ruleset
...................................
The ETOpen Ruleset is an excellent anti-malware IDS/IPS ruleset that enables
users with cost constraints to significantly enhance their existing network-based
malware detection. The ETOpen Ruleset is not a full coverage ruleset, and may not
be sufficient for many regulated environments and should not be used as a
standalone ruleset.

OPNsense has integrated support for ET Open rules.
For details and Guidelines see: http://doc.emergingthreats.net/bin/view/Main/EmergingFAQ
For rules documentation: http://doc.emergingthreats.net/

...................................
Abuse.ch
...................................
Abuse.ch offer several blacklist for protecting against fraudulent networks.
OPNsense has integrated support for:

...................................
SSL Blacklist
...................................

SSL Blacklist (SSLBL) is a project maintained by abuse.ch. The goal is to provide
a list of "bad" SSL certificates identified by abuse.ch to be associated with
malware or botnet activities. SSLBL relies on SHA1 fingerprints of malicious SSL
certificates and offers various blacklists.

See for details: https://sslbl.abuse.ch/

...................................
Feodo Tracker
...................................

Feodo (also known as Cridex or Bugat) is a Trojan used to commit ebanking fraud and steal sensitive information from the victims computer, such as credit card details or credentials. At the moment, Feodo Tracker is tracking four versions of Feodo, and they are labeled by Feodo Tracker as version A, version B, version C and version D:

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

...................................
URLHaus List
...................................
With OPNsense version 18.1.7 we inroduced the URLHaus List from abuse.ch which collects
compromised sites distributing malware.

See for details: https://urlhaus.abuse.ch/

...................................
App detection rules
...................................
With OPNsense version 18.1.11 we introduced the app detection ruleset.
Since about 80 percent of traffic are web applications these rules are focused on
blocking web services and the URLs behind them.

If you want to contribute to the ruleset see: https://github.com/opnsense/rules

-------
How-tos
-------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   how-tos/ips-feodo
   how-tos/ips-sslfingerprint
