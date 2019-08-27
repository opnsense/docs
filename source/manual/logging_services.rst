==============
Log Files
==============

When troubleshooting problems with your firewall, it is very likely you have to check
the logs available on your system. In the UI of OPNsense, the log files are generally grouped
with the settings of the component they belong to. The log files can be found here:

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
