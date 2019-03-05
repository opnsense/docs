=============
Settings menu
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
| Enable HTTP Strict Transport Security        | Avoids ever loading the web interface over HTTPS, even when the       |
|                                              | connection is hijacked (man-in-the-middle attack).                    |
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
| Enable access log                            | Log all access to the Web GUI (for debuggin/analysis)                 |
+----------------------------------------------+-----------------------------------------------------------------------+
| Listen interfaces                            | Can be used to limit interfaces on which the Web GUI can be accessed. |
|                                              | Doing so can increase security but also the risk of lock-out.         |
+----------------------------------------------+-----------------------------------------------------------------------+
| Disable HTTP_REFERER enforcement check       | The origins of requests are checked in order to provide some          |
|                                              | protection against CSRF. You can turn this off of it interferes with  |
|                                              | external scripts that interact with the Web GUI.                      |
+----------------------------------------------+-----------------------------------------------------------------------+
| **Console**                                                                                                          |
+----------------------------------------------+-----------------------------------------------------------------------+
| Use the virtual terminal driver (vt)         | When unchecked, OPNsense will use the older sc    driver.             |
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
|                                              | This can avoid lock-out, but at the cost of an attacker being able to |
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
