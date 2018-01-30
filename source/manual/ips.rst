==================================
Inline Intrusion Prevention System
==================================

The inline IPS system of OPNsense is based on Suricata and utilizes Netmap to
enhance performance and minimize cpu utilization. This deep packet inspection
system is very powerful and can be used to mitigate security threats at wire speed.

-------------------------------
Emerging Threats ETOpen Ruleset
-------------------------------
The ETOpen Ruleset is an excellent anti-malware IDS/IPS ruleset that enables
users with cost constraints to significantly enhance their existing network-based
malware detection. The ETOpen Ruleset is not a full coverage ruleset, and may not
be sufficient for many regulated environments and should not be used as a
standalone ruleset.

OPNsense has integrated support for ET Open rules.
For details and Guidelines see: http://doc.emergingthreats.net/bin/view/Main/EmergingFAQ
For rules documentation: http://doc.emergingthreats.net/

--------
Abuse.ch
--------
Abuse.ch offer several blacklist for protecting against fraudulent networks.
OPNsense has integrated support for:

SSL Blacklist
-------------
SSL Blacklist (SSLBL) is a project maintained by abuse.ch. The goal is to provide
a list of "bad" SSL certificates identified by abuse.ch to be associated with
malware or botnet activities. SSLBL relies on SHA1 fingerprints of malicious SSL
certificates and offers various blacklists.

See fore details: https://sslbl.abuse.ch/

Feodo Tracker
-------------
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

------------------------
Maxmind GeoLite2 Country
------------------------
GeoLite2 databases are free IP geolocation databases comparable to, but less
accurate than, MaxMind’s GeoIP2 databases. GeoLite2 databases are updated on the
first Tuesday of each month.

For more details see: http://dev.maxmind.com/geoip/geoip2/geolite2/

OPNsense has integrated GeoLite2 Country database support.

---------------
Finger Printing
---------------
OPNsense includes a very polished solution to block protected sites based on
their SSL fingerprint.

--------
How-to's
--------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   how-tos/ips-feodo
   how-tos/ips-geoip
   how-tos/ips-sslfingerprint
