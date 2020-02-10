=============
Settings
=============

Besides the configuration options that every component has, OPNsense also contains a lot of general settings
that you can tweak. This page contains an overview of them.

--------------
Administration
--------------

The settings on this page concerns logging into OPNsense. The “Secure Shell” settings are described under
:ref:`Creating Users & Groups<SSH and console login>`.

+----------------------------------------------+-----------------------------------------------------------------------+
| Setting                                      | Explanation                                                           |
+==============================================+=======================================================================+
| **Web GUI**                                                                                                          |
+----------------------------------------------+-----------------------------------------------------------------------+
| Protocol                                     | It is strongly recommended to leave this on “HTTPS”                   |
+----------------------------------------------+-----------------------------------------------------------------------+
| SSL Certificate                              | By default, a self-signed certificate is used. Certificates can be    |
|                                              | added via :menuselection:`System --> Trust --> Certificates`.         |
+----------------------------------------------+-----------------------------------------------------------------------+
| SSL Ciphers                                  | Can be used to limit SSL cipher selection in case the system defaults |
|                                              | are undesired. Note that restrictive use may lead to an inaccessible  |
|                                              | web GUI.                                                              |
+----------------------------------------------+-----------------------------------------------------------------------+
| Enable HTTP Strict Transport Security        | Enforces loading the web GUI over HTTPS, even when the connection     |
|                                              | is hijacked (man-in-the-middle attack), and do not allow the user to  |
|                                              | trust an invalid certificate for the web GUI.                         |
+----------------------------------------------+-----------------------------------------------------------------------+
| TCP port                                     | Can be useful if there are other services that are reachable via port |
|                                              | 80/443 of the external IP, for example.                               |
+----------------------------------------------+-----------------------------------------------------------------------+
| Disable web GUI redirect rule                | If you change the port, a redirect rule from port 80/443 will be      |
|                                              | created. Check this to disable creating this rule.                    |
+----------------------------------------------+-----------------------------------------------------------------------+
| Disable logging of web GUI successful logins |                                                                       |
+----------------------------------------------+-----------------------------------------------------------------------+
| Session Timeout                              | Time in minutes to expire idle management sessions.                   |
+----------------------------------------------+-----------------------------------------------------------------------+
| Disable DNS Rebinding Checks                 | OPNsense contains protection against                                  |
|                                              | `DNS rebinding <https://en.wikipedia.org/wiki/DNS_rebinding>`__ by    |
|                                              | filtering out DNS replies with local IPs. Check this box to disable   |
|                                              | this protection if it interferes with web GUI access or name          |
|                                              | resolution in your environment.                                       |
+----------------------------------------------+-----------------------------------------------------------------------+
| Alternate Hostnames                          | Alternate, valid hostnames (to avoid false positives in               |
|                                              | referrer/DNS rebinding protection).                                   |
+----------------------------------------------+-----------------------------------------------------------------------+
| HTTP Compression                             | Reduces size of transfer, at the cost of slightly higher CPU usage.   |
+----------------------------------------------+-----------------------------------------------------------------------+
| Enable access log                            | Log all access to the Web GUI (for debugging/analysis)                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| Listen interfaces                            | Can be used to limit interfaces on which the Web GUI can be accessed. |
|                                              | This allows freeing the interface for other services, such as HAProxy.|
+----------------------------------------------+-----------------------------------------------------------------------+
| Disable HTTP_REFERER enforcement check       | The origins of requests are checked in order to provide some          |
|                                              | protection against CSRF. You can turn this off of it interferes with  |
|                                              | external scripts that interact with the Web GUI.                      |
+----------------------------------------------+-----------------------------------------------------------------------+
| **Console**                                                                                                          |
+----------------------------------------------+-----------------------------------------------------------------------+
| Use the virtual terminal driver (vt)         | When unchecked, OPNsense will use the older sc driver.                |
+----------------------------------------------+-----------------------------------------------------------------------+
| Primary Console                              | The primary console will show boot script output. All consoles display|
|                                              | OS boot messages, console messages, and the console menu.             |
+----------------------------------------------+-----------------------------------------------------------------------+
| Secondary Console                            | See above.                                                            |
+----------------------------------------------+-----------------------------------------------------------------------+
| Serial Speed                                 | Allows adjusting the baud rate. 115200 is the most common.            |
+----------------------------------------------+-----------------------------------------------------------------------+
| Use USB-based serial ports                   | Listen on ``/dev/ttyU0``, ``/dev/ttyU1``, … instead of ``/dev/ttyu0``.|
+----------------------------------------------+-----------------------------------------------------------------------+
| Password protect the console menu            | Can be unchecked to allow physical console access without password.   |
|                                              | This can avoid lock-out, but at the cost of attackers being able to   |
|                                              | do anything if they gain physical access to your system.              |
+----------------------------------------------+-----------------------------------------------------------------------+
| **Authentication**                                                                                                   |
+----------------------------------------------+-----------------------------------------------------------------------+
| Server                                       | Select one or more authentication servers to validate user            |
|                                              | credentials against. Multiple servers can make sense with remote      |
|                                              | authentication methods to provide a fallback during connectivity      |
|                                              | issues. When nothing is specified the default of "Local Database"     |
|                                              | is used.                                                              |
+----------------------------------------------+-----------------------------------------------------------------------+
| Sudo                                         | Permit sudo usage for administrators with shell access.               |
+----------------------------------------------+-----------------------------------------------------------------------+
| Disable integrated authentication            | When set, console login, SSH, and other system services can only use  |
|                                              | standard UNIX account authentication.                                 |
+----------------------------------------------+-----------------------------------------------------------------------+

----
Cron
----

`Cron <https://en.wikipedia.org/wiki/Cron>`__ is a service that is used to execute jobs periodically. Cron jobs can be viewed by navigating to
:menuselection:`System --> Settings --> Cron`. New jobs can be added by click the ``+`` button in the lower right
corner.

When adding a new job or modifying an existing one, you will be presented with fields that directly reflect the
cron file syntax and that mostly speak for themselves. A job needs a name, a command, command parameters (if
applicable), a description (optional, but recommend) and most importantly, a schedule. All time-related fields
share the same syntax:

- An asterisk (\*) can be used to mean “any”
- Specifying multiple values is possible using the comma: ``1,4,9``
- Ranges can be specified using a dash: ``4-9``

-------
General
-------

The general settings mainly concern network-related settings like the hostname. The general setting can be set by
going to :menuselection:`System --> Settings --> General`. The following settings are available:

+---------------------------------+------------------------------------------------------------------------------------+
| Setting                         | Explanation                                                                        |
+=================================+====================================================================================+
| **System**                                                                                                           |
+---------------------------------+------------------------------------------------------------------------------------+
| Hostname                        | Hostname without domain, e.g.: ``firewall``                                        |
+---------------------------------+------------------------------------------------------------------------------------+
| Domain                          | The domain, e.g. ``mycorp.com``, ``home``, ``office``, ``private``, etc. Do not    |
|                                 | use 'local' as a domain name. It will cause local hosts running mDNS (avahi,       |
|                                 | bonjour, etc.) to be unable to resolve local hosts not running mDNS.               |
+---------------------------------+------------------------------------------------------------------------------------+
| Time zone                       |                                                                                    |
+---------------------------------+------------------------------------------------------------------------------------+
| Language                        | Default language. Can be overridden by users.                                      |
+---------------------------------+------------------------------------------------------------------------------------+
| Theme                           | More themes can be installed via plug-ins.                                         |
+---------------------------------+------------------------------------------------------------------------------------+
| **Networking**                                                                                                       |
+---------------------------------+------------------------------------------------------------------------------------+
| Prefer to use IPv4 even         |                                                                                    |
| if IPv6 is available            |                                                                                    |
+---------------------------------+------------------------------------------------------------------------------------+
| DNS servers                     | A list of DNS servers, optionally with a gateway. These DNS servers are also used  |
|                                 | for the DHCP service, DNS services and for PPTP VPN clients. When using multiple   |
|                                 | WAN connections there should be at least one unique DNS server per gateway.        |
+---------------------------------+------------------------------------------------------------------------------------+
| Allow DNS server list to be     | If this option is set, DNS servers assigned by a DHCP/PPP server on the WAN will   |
| overridden by DHCP/PPP on WAN   | be used for their own purposes (including the DNS services). However, they will    |
|                                 | not be assigned to DHCP and PPTP VPN clients.                                      |
+---------------------------------+------------------------------------------------------------------------------------+
| Do not use the local DNS        | When enabling local DNS services such as Dnsmasq and Unbound, OPNsense will use    |
| service as a nameserver for     | these as a nameserver. Check this option to prevent this.                          |
| this system                     |                                                                                    |
+---------------------------------+------------------------------------------------------------------------------------+
| Allow default gateway switching | If the link where the default gateway resides fails switch the default gateway to  |
|                                 | another available one.                                                             |
+---------------------------------+------------------------------------------------------------------------------------+


--------
Tunables
--------

Tunables are the settings that go into the ``sysctl.conf`` file, which allows tweaking of low-level system
settings. They can be set by going to :menuselection:`System --> Settings --> Tunables`.

Here, the currently active settings can be viewed and new ones can be created. All valid ``sysctl.conf``
settings can be added this way if desired. A list of possible values can be obtained by issuing
``sysctl -a`` on an OPNsense shell.

-------------
Miscellaneous
-------------

As the name implies, this section contains the settings that do not fit anywhere else.

================================= ======================================================================================================================================================================================================
Setting                           Explanation
================================= ======================================================================================================================================================================================================
**Cryptography settings**
Diffie-Hellman parameters         The server and client needs to use the same parameters in order to set up a connection. How parameters are updated can be tweaked. Please leave on default unless you know why to change it.
Hardware acceleration             Select your method of hardware acceleration, if present. Check the full help for hardware-specific advice.
Use /dev/crypto                   Old hardware crypto drivers expose the /dev/crypto interface. This is not used by newer hardware or software any more.
**Thermal Sensors**
Hardware                          Select between No/ACPI thermal sensor driver and processor-specific drivers.
**Periodic Backups**
Periodic RRD Backup               Periodically backup Round Robin Database.
Periodic DHCP Leases Backup       Periodically backup DHCP leases.
Periodic NetFlow Backup           Periodically backup Netflow state.
Periodic Captive Portal Backup    Periodically backup Captive Portal state.
**Power Savings**
Use PowerD                        PowerD allows tweaking power conservation features. The modes are maximum (high performance), minimum (maximum power saving), adaptive (balanced), hiadaptive (balanced, but with higher performance).
On AC Power Mode
On Battery Power Mode
On Normal Power Mode
**Disk / Memory Settings**
Swap file                         Create a 2 GB swap file. This can increase performance, at the cost of increased wear on storage, especially flash.
/var RAM disk                     This can be useful to avoid wearing out flash storage. **Everything in /var, including logs will be lost upon reboot.**
/tmp RAM disk                     See above.
**System Sounds**
Disable the startup/shutdown beep Disable beeps via the built-in speaker (“PC Speaker”)
================================= ======================================================================================================================================================================================================


------------
Logging
------------

Log settings can be found at :menuselection:`System --> Settings --> Logging`. The settings are in two groups,
one for local logging and one for remote logging.

An overview of the local settings:

============================================ ====================================================================================================================
Setting                                      Explanation
============================================ ====================================================================================================================
Reverse Display                              When enabled, the most recent log entry will be displayed on top.
GUI Log Entries to Display                   Number of log entries displayed in the GUI.
Log File Size (Bytes)                        Maximum size of circular logs (which most OPNsense log files are)
Log Firewall Default Blocks                  Turning these off means that only hits for your custom rules will be logged.
Web Server Log                               If checked, lighttpd errors are displayed in the main system log.
Disable writing log files to the local disk  Useful to avoid wearing out flash memory (if used). Remote logging can be used to save the logs instead if desired.
Reset Logs                                   Clear all logs. Note that this will also restart the DHCP server, so make sure any DHCP settings are saved first.
============================================ ====================================================================================================================

An overview of the remote settings (superseded by new Logging/target syslog-ng menu):

======================= ===============================================================================================
Setting                 Explanation
======================= ===============================================================================================
Enable Remote Logging   Master on/off switch
Source Address          Which interface to bind to. Select “any” if you want to use a mix of IPv4 and IPv6 servers.
IP Protocol             Preferred IP version (it will this first). Will only be used if “Source Address” is not an IP.
Remote Syslog Servers   IP addresses of remote syslog servers, or IP:port combinations.
Remote Syslog Contents  Can be used to selectively log event categories
======================= ===============================================================================================

.. Note::

    The remote logging feature will likely be removed in OPNsense 20.1, since the new **Logging / targets**
    offers more flexibility and has overlapping functionality. We advise to switch as soon as possible.



.....................
Circular Logs
.....................

Most of the core features log to circular log files so they will not grow bigger
than a predefined size. You can tune this value via :menuselection:`System --> Settings --> Logging`.
There, you can also disable the writing of logs to disk or reset them all.

You can view the contents via CLI with:

.. code-block:: sh

    clog /path/to/log

or follow the contents via:

.. code-block:: sh

    clog -f /path/to/log

.....................
Plugin Logs
.....................

Many plugins have their own logs. In the UI, they are grouped with the settings of that plugin.
They mostly log to /var/log/ in text format, so you can view or follow them with *tail*.


----------------------
Logging / targets
----------------------

With OPNsense version 19.7, syslog-ng for remote logging was introduced.
If you want to benefit from all new features and already have the legacy system available,
please remove all remote logging from **System->Settings->Logging** and go to
**System->Settings->Logging / targets** and *Add* a new *Destination*.

============== ================================================================================
Setting                 Explanation
============== ================================================================================
Enabled        Master on/off switch.
Transport      Protocol to use for syslog.
Applications   Select a list of applications to send to remote syslog. Leave empty for *all*.
Levels         Choose which levels to include, omit to select all.
Facilities     Choose which facilities to include, omit to select all.
Hostname       Hostname or IP address where to send logs to.
Port           Port to use, usually 514.
Description    Set a description for you own use.
============== ================================================================================
