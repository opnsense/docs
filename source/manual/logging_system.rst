==============
Log Files
==============

When troubleshooting problems with your firewall, it is very likely you have to check
the logs available on your system. In the UI of OPNsense, the log files are generally grouped
with the settings of the component they belong to. The log files can be found here:

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
