==============
System Logging
==============

When troubleshooting problems with your firewall, it is very likely you have to check
the logs available on your system. In the UI of OPNsense, the log files are generally grouped
with the settings of the component they belong to. The log files can be found here:

------
System
------

============================= =================================================== =============================================================
 **System Log**                :menuselection:`System --> Log Files --> General`   *Most of all system related events go here*
 **Backend / config daemon**   :menuselection:`System --> Log Files --> Backend`   *Here you can find logs for config generation of API usage*
 **Web GUI**                   :menuselection:`System --> Log Files --> Web GUI`   *Lighttpd, the webserver of OPNsense itself, logs here*
 **Firmware**                  :menuselection:`System --> Firmware --> Log File`   *Updates from the packaging system go here*
 **Gateways**                  :menuselection:`System --> Gateways --> Log File`   *Lists Dpinger gateway tracking related log messages*
 **Routing**                   :menuselection:`System --> Routes --> Log File`     *Routing changes or interface events*
============================= =================================================== =============================================================

.. Note::
   Log files on file system:
   /var/log/system.log (clog)
   /var/log/configd.log (clog)
   /var/log/lighttpd.log (clog)
   /var/log/pkg.log (clog)
   /var/log/gateways.log (clog) Note: By default gateway monitoring is disabled, so the log will be empty.
   /var/log/routing.log (clog)

----------
Interfaces
----------

==================== ============================================================== ===================================================================
 **Wireless**         :menuselection:`Interfaces --> Wireless --> Log File`         *When using wireless features of OPNsense you find the logs here*
 **Point-to-Point**   :menuselection:`Interfaces --> Point-to-Point --> Log File`   *PPP dialup logs like PPPoE are found here*
==================== ============================================================== ===================================================================

.. Note::
   Log files on file system:
   /var/log/wireless.log (clog)
   /var/log/ppps.log (clog)

--------
Firewall
--------

================ ======================================================== =============================================================================
 **Live View**    :menuselection:`Firewall --> Log Files --> Live View`    *View firewall logs in realtime, smart filtering can be applied*
 **Plain View**   :menuselection:`Firewall --> Log Files --> Plain View`   *Just the plain contents how **pf** logs into **filter.log** *
================ ======================================================== =============================================================================

.. Note::
   Log files on file system:
   /var/log/filter.log (clog)

Live View
---------

Live view updates itself in realtime if a rule is matched that has logging enabled or one of the global logging options is enabled under:
:menuselection:`System --> Settings --> Logging`

For better troubleshooting you can provide a filter string. This filter may include regular expressions.
Lets assume one logging entry as one single string without special separators.

So for just displaying packets that match DNS replies from wan to your lan clients in segment 192.168.1.0/24, you have to use:

.. code-block:: sh

    WAN.*:53.*192.168.1

or to be even more correct

.. code-block:: sh

    WAN.*:53.*192\.168\.1\.

==========  ====================== ===================== ======================  ========================
 **WAN**     **.***                 **:53**               **.***                  **192\.168\.1\.**
 Interface   1 or more characters   first match of port   1 or more characters    destination ip address
==========  ====================== ===================== ======================  ========================

---
VPN
---

================= =============================================== =====================================
 **IPsec Log**     :menuselection:`VPN --> IPsec --> Log File`     *Everything around IPsec goes here*
 **OpenVPN Log**   :menuselection:`VPN --> OpenVPN --> Log File`   *OpenVPN logs everything here*
================= =============================================== =====================================

.. Note::
   Log files on file system:
   /var/log/ipsec.log (clog)
   /var/log/openvpn.log (clog)

--------
Services
--------

========================= ================================================================ =============================================
 **Captive Portal**        :menuselection:`Services --> Captive Portal --> Log File`        *Events from Captive Portal go here*
 **DHCPv4**                :menuselection:`Services --> DHCPv4 --> Log File`                *DHCP events get logged here*
 **Dnsmasq DNS**           :menuselection:`Services --> Dnsmasq DNS --> Log File`           *The DNSmasq Forwarder logs*
 **HAProxy**               :menuselection:`Services --> HAProxy --> Log File`               *The logs of the Reverse Proxy*
 **Intrusion Detection**   :menuselection:`Services --> Intrusion Detection --> Log File`   *Suricata Logs are here*
 **Network Time**          :menuselection:`Services --> Network Time --> Log File`          *NTP daemon logs*
 **Unbound DNS**           :menuselection:`Services --> Unbound DNS --> Log File`           *Unbound resolver logs can be found here*
 **Web Proxy**             :menuselection:`Services --> Web Proxy --> Log File`             *Squid access.log, store.log and cache.log*
========================= ================================================================ =============================================

.. Note::
   Log files on file system:
   /var/log/portalauth.log (clog)
   /var/log/dhcpd.log (clog)
   /var/log/dnsmasq.log (clog)
   /var/log/haproxy.log (clog)
   /var/log/ntpd.log (clog)
   /var/log/suricata.log (clog)
   /var/log/resolver.log (clog)
   /var/log/squid/access.log (text)
   /var/log/squid/cache.log (text)
   /var/log/squid/store.log (text)

-------------
Circular Logs
-------------

Most of the core features log to circular log files so they will not grow bigger
than a predefined size. You can tune this value via :menuselection:`System --> Settings --> Logging`.
There, you can also disable the writing of logs to disk or reset them all.

You can view the contents via CLI with:

.. code-block:: sh

    clog /path/to/log

or follow the contents via:

.. code-block:: sh

    clog -f /path/to/log

-----------
Plugin Logs
-----------

Many plugins have their own logs. In the UI, they are grouped with the settings of that plugin.
They mostly log to /var/log/ in text format, so you can view or follow them with *tail*.
