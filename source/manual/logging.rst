==============
System Logging
==============

When troubleshooting problems with your Firewall you are heavily constrained to 
the logs available on your system. Via the UI you can find them distributed within 
the depending Menues which are:

------
System 
------

============================= ================================ =============================================================
 **System Log**                **System->Log Files->General**   *Most of all system related events go here*
 **Backend / config daemon**   **System->Log Files->Backend**   *Here you can find logs for config generation of API usage*
 **Web GUI**                   **System->Log Files->Web GUI**   *Lighttpd, the webserver of OPNsense itslef logs here*
 **Firmware**                  **System->Firmware->Log File**   *Updates from the packaging system go here*
 **Gateways**                  **System->Gateways->Log File**   *All about gateway tracking*
 **Routing**                   **System->Routes->Log File**     *Routing changes or interface events*
============================= ================================ ============================================================= 

Log files on file system:
/var/log/system.log (clog)
/var/log/configd.log (clog)
/var/log/lighttpd.log (clog)
/var/log/pkg.log (clog)
/var/log/gateways.log (clog)
/var/log/routing.log (clog)

----------
Interfaces 
----------

==================== ========================================== ===================================================================
 **Wireless**         **Interfaces->Wireless->Log File**         *When using wireless features of OPNsense you find the logs here*
 **Point-to-Point**   **Interfaces->Point-to-Point->Log File**   *PPP dialup logs like PPPoE get's here*
==================== ========================================== ===================================================================

Log files on file system:
/var/log/wireless.log (clog)
/var/log/ppps.log (clog)

--------
Firewall 
--------

================ ===================================== =============================================================================
 **Live View**    **Firewall->Log Files->Live View**    *Dynamically updateing windows of logs services search filter and coloring*
 **Plain View**   **Firewall->Log Files->Plain View**   *Just the plain contents how **pf** logs into **filter.log** *
================ ===================================== =============================================================================

Log files on file system:
/var/log/filter.log (clog)

---
VPN
---

================= ============================ =====================================
 **IPsec Log**     **VPN->IPsec->Log File**     *Everything around IPsec goes here*
 **OpenVPN Log**   **VPN->OpenVPN->Log File**   *OpenVPN logs everything here*
================= ============================ =====================================

Log files on file system:
/var/log/ipsec.log (clog)
/var/log/openvpn.log (clog)

--------
Services
--------

========================= ============================================= ======================================================
 **Captive Portal**        **Services->Captive Portal->Log File**        *Events from Captive Portal goes here*
 **DHCPv4**                **Services->DHCPv4->Log File**                *DHCP events get logged here*
 **Dnsmasq DNS**           **Services->Dnsmasq DNS->Log File**           *The DNSmasq Forwarder logs*
 **HAProxy**               **Services->HAProxy->Log File**               *The logs of the Reverse Proxy*
 **Intrusion Detection**   **Services->Intrusion Detection->Log File**   *Suricata Logs are here*
 **Network Time**          **Services->Network Time->Log File**          *NTP daemon logs*
 **Unbound DNS**           **Services->Unbound DNS->Log File**           *Unbound resolver logs can be found here*
 **Web Proxy**             **Services->Web Proxy->Log File**             *Squid logs can be found here, three tabs available*
========================= ============================================= ======================================================

Log files on file system:
/var/log/portalauth.log (clog)
/var/log/dhcpd.log (clog)
/var/log/dnsmasq.log (clog)
/var/log/haproxy.log (clog)
/var/log/ntpd.log (clog)
/var/log/suricata.log (text)
/var/log/suricata.syskig.log (clog)
/var/log/resolver.log (clog)
/var/log/squid.syslog.log (clog)
/var/log/squid/access.log (text)
/var/log/squid/cache.log (text)
/var/log/squid/store.log (text)

------------
Circular Log
------------

Most of the core features log to circular log files so they will not grow bigger
then a predefined size. You can tune this value via **System->Settings->Logging**.
There you can also disable the writing of logs to disk or reset them all.

------
Syslog
------

In **System->Settings->Logging** you can also set a remote log server where to send
your log files. Choose a **Source Address** if needed and set a **Remote Syslog Server**.
Via **Remote Syslog Contents** you can choose which kinds of logs to send.

-----------
Plugin Logs
-----------

Many plugins have their own logs, via GUI you can find them it their own menu.
They mostly log to /var/log/ in text format, so you can view or follow them with *tail*.
