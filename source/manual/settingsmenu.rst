=============
Settings
=============

Besides the configuration options that every component has, OPNsense also contains a lot of general settings
that you can tweak. This page contains an overview of them.

--------------
Administration
--------------

The settings on this page concerns logging into OPNsense. The “Secure Shell” settings are described under
:doc:`Creating Users & Groups</manual/how-tos/user-local>`.


...............................
Listen interfaces
...............................

.. Warning::
    Before considering the use of manual selected interfaces, make sure to read this chapter so you are aware
    of the pitfalls upfront. Misconfigurations likely lead to a non accesible web interface and/or missing ssh access.


Both the WebUI and the Secure Shell server support the option to only listen on specific interfaces, the use of this option
however comes with clear warnings which you do need to be aware of before deciding to use this option.

By default (our recommended settings), these services listen on all addresses (interfaces).

If for whatever reason, you do need to listen only on specific interfaces, the following rules apply:

*   The interface must always be available, so do not try to bind to vpn instances of any kind (OpenVPN, Wireguard, ...)
*   The addressing must be fully static, so no IPv6 tracking configured for example

As the webgui is not able to predict with 100% certainty that these rules do apply, it is possible to select interfaces
that don't support binding for these services.

.. Note::
    When facing issues with the webgui (and/or ssh) and the above rules are not met, please do not bother to open a ticket
    as these are unsupported scenario's.


.. Tip::
    In case (**for any service**) one would like to prevent binding on all interfaces, it is possible to add a
    loopback interface (:menuselection:`Interfaces->Other Types->Loopback`), assign an ip address and bind to that.

    If traffic is being routed through the firewall, the "loopback ip" (some private addres, not in the loopback range)
    should be directly accessible from the network behind it. For example use an address like :code:`192.192.192.192/32`
    to access the web interface while your own network is using :code:`192.168.1.0/24`.

    Technologies like Network Address Translation can also be combined if the other end is not aware of the route to
    this single address.


...............................
Web GUI
...............................

============================================== ========================================================================
Protocol                                       It is strongly recommended to leave this on “HTTPS”
SSL Certificate                                By default, a self-signed certificate is used. Certificates can be
                                               added via :menuselection:`System --> Trust --> Certificates`.
SSL Ciphers                                    Can be used to limit SSL cipher selection in case the system defaults
                                               are undesired. Note that restrictive use may lead to an inaccessible
                                               web GUI.
HTTP Strict Transport Security                 Enforces loading the web GUI over HTTPS, even when the connection
                                               is hijacked (man-in-the-middle attack), and do not allow the user to
                                               trust an invalid certificate for the web GUI.
TCP port                                       Can be useful if there are other services that are reachable via port
                                               80/443 of the external IP, for example.
Disable web GUI redirect rule                  If you change the port, a redirect rule from port 80/443 will be
                                               created. Check this to disable creating this rule.
Session Timeout                                Time in minutes to expire idle management sessions.
DNS Rebind Check                               OPNsense contains protection against
                                               `DNS rebinding <https://en.wikipedia.org/wiki/DNS_rebinding>`__ by
                                               filtering out DNS replies with local IPs. Check this box to disable
                                               this protection if it interferes with web GUI access or name
                                               resolution in your environment.
Alternate Hostnames                            Alternate, valid hostnames (to avoid false positives in
                                               referrer/DNS rebinding protection).
HTTP Compression                               Reduces size of transfer, at the cost of slightly higher CPU usage.
Enable access log                              Log all access to the Web GUI (for debugging/analysis)
Listen interfaces                              Can be used to limit interfaces on which the Web GUI can be accessed.
                                               This allows freeing the interface for other services, such as HAProxy.
HTTP_REFERER enforcement check                 The origins of requests are checked in order to provide some
                                               protection against CSRF. You can turn this off of it interferes with
                                               external scripts that interact with the Web GUI.
============================================== ========================================================================

...............................
Secure Shell
...............................

User accounts can be used for logging in to the web frontend, as well as for logging in to the console (via VGA,
serial or SSH). The latter will only work if the user shell is not set to ``/sbin/nologin``.

In order to access OPNsense via SSH, SSH access will need to be configured via :menuselection:`System --> Settings --> Administration`.
Under the "Secure Shell" heading, the following options are available:

============================================== ========================================================================
Secure Shell Server                            Enable a secure shell service
Login Group                                    Select the allowed groups for remote login. The "wheel" group is
                                               always set for recovery purposes and an additional local group can be
                                               selected at will. Do not yield remote access to non-administrators
                                               as every user can access system files using SSH or SFTP.
Permit Root Login                              Root login is generally discouraged. It is advised to log in via
                                               another user and switch to root afterwards.
Permit password login                          When disabled, authorized keys need to be configured for each User
                                               that has been granted secure shell access.
SSH port	                                   Port to listen on, default is 22
Listen Interfaces                              Only accept connections from the selected interfaces.
                                               Leave empty to listen globally. Use with extreme care.
Key exchange algorithms                        The key exchange methods that are used to generate per-connection
                                               keys
Ciphers                                        The ciphers to encrypt the connection
MACs                                           The message authentication codes used to detect traffic modification
Host key algorithms                            Specifies the host key algorithms that the server offers
Public key signature algorithms                The signature algorithms that are used for public key authentication
============================================== ========================================================================



...............................
Console
...............................

In case of an emergency, it's always practical to make sure to configure a console to be able to access the firewall
when network connectivity is not possible.

.. Tip::
    After initial installation, always make sure to test if the console actually works. When concluding the console
    is not functional when you need it can be very unpractical.


============================================== ========================================================================
Use the virtual terminal driver (vt)           When unchecked, OPNsense will use the older sc driver.                |
Primary Console                                The primary console will show boot script output. All consoles display|
                                               OS boot messages, console messages, and the console menu.             |
Secondary Console                              See above.                                                            |
Serial Speed                                   Allows adjusting the baud rate. 115200 is the most common.            |
Use USB-based serial ports                     Listen on ``/dev/ttyU0``, ``/dev/ttyU1``, … instead of ``/dev/ttyu0``.|
Password protect the console menu              Can be unchecked to allow physical console access without password.   |
                                               This can avoid lock-out, but at the cost of attackers being able to   |
                                               do anything if they gain physical access to your system.              |
============================================== ========================================================================


...............................
Authentication
...............................

The authentication section of the Administrationm settings offers general security settings for users logging into the
firewall.

============================================== ========================================================================
Server                                         Select one or more authentication servers to validate user            |
                                               credentials against. Multiple servers can make sense with remote      |
                                               authentication methods to provide a fallback during connectivity      |
                                               issues. When nothing is specified the default of "Local Database"     |
                                               is used.                                                              |
Disable integrated authentication              When set, console login, SSH, and other system services can only use  |
                                               standard UNIX account authentication.                                 |
Sudo                                           Permit sudo usage for administrators with shell access.               |
User OTP seed                                  Select groups which are allowed to generate their own OTP seed on the |
                                               password page.                                                        |
============================================== ========================================================================


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

Available cron jobs are registered in the backend to prevent command injection and privilege escalation. These can be found under
`Command` and may allow an additional `Parameter`. Restart and reload actions are self-explanatory. They take no parameters and
will restart (usually slower stop and start of a process) or reload (usually a faster SIGHUP) the respective service. The availability
of restart and reload is subject to their respective services as not all software will support a reload for implementational reasons.

The most common core commands are as follows:


+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Command in GUI                              | Command in shell                       | Supported parameters    | Background information                      |
+=============================================+========================================+=========================+=============================================+
| Update and reload firewall aliases          | configctl filter refresh_aliases       | No parameters           | Updates IP aliases for DNS entries and MAC  |
|                                             |                                        |                         | addresses as well as URL tables.            |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Firmware update check                       | configctl firmware poll                | No parameters           | Refresh current update status from firmware |
|                                             |                                        |                         | mirror for e.g. remote status check via     |
|                                             |                                        |                         | API. Note this utilizes a skew interval of  |
|                                             |                                        |                         | 25 minutes.                                 |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Firmware changelog update                   | configctl firmware changelog cron      | No parameters           | Refresh current changelog status from       |
|                                             |                                        |                         | authoritative firmware location to preview  |
|                                             |                                        |                         | changelogs for new versions. Note this      |
|                                             |                                        |                         | utilizes a skew interval of 25 minutes and  |
|                                             |                                        |                         | is also performed by the firmware update    |
|                                             |                                        |                         | check.                                      |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Automatic firmware update                   | configctl firmware auto-update         | No parameters           | Perform a minor update if applicable.       |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Update and reload intrusion detection rules | configctl ids update                   | No parameters           | Fetches remote rules and reloads the IDS    |
|                                             |                                        |                         | instance to make use of newly fetched rules.|
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Periodic interface reset                    | configctl interface reconfigure        | identifier: Internal    | Cycle through an interface reset that       |
|                                             | [identifier]                           | name of the interface   | removes all connectivity and reactivates    |
|                                             |                                        | as shown in assignments | it cleanly.                                 |
|                                             |                                        | or overview page, e.g.  |                                             |
|                                             |                                        | "lan", "wan", "optX".   |                                             |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Download and reload external proxy ACLs     | configctl proxy fetchacls              | No parameters           | Fetch and activate the external ACL files   |
|                                             |                                        |                         | for configured blocklists.                  |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Remote backup                               | configctl system remote backup         | No parameters           | Trigger the remote backup at the specified  |
|                                             |                                        |                         | time as opposed to its nightly default.     |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Issue a reboot                              | configctl system reboot                | No parameters           | Perform a reboot at the specified time.     |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| HA update and reconfigure backup            | configctl system ha_reconfigure_backup | No parameters           | Synchronize the configuration to the backup |
|                                             |                                        |                         | firewall and restart its services to apply  |
|                                             |                                        |                         | the changes.                                |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| Update Unbound DNSBLs                       | configctl unbound dnsbl                | No parameters           | Update the the DNS blocklists and apply the |
|                                             |                                        |                         | changes to Unbound.                         |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| ZFS pool trim                               | configctl zfs trim [pool]              | pool: ZFS pool name to  | Initiates an immediate on-demand TRIM       |
|                                             |                                        | perform the action on   | operation for all of the free space in a    |
|                                             |                                        |                         | pool. This operation informs the underlying |
|                                             |                                        |                         | storage devices of all blocks in the pool   |
|                                             |                                        |                         | which are no longer allocated and allows    |
|                                             |                                        |                         | thinly provisioned devices to reclaim the   |
|                                             |                                        |                         | space.                                      |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+
| ZFS pool scrub                              | configctl zfs scrub [pool]             | pool: ZFS pool name to  | Begins a scrub or resumes a paused scrub.   |
|                                             |                                        | perform the action on   | The scrub examines all data in the specified|
|                                             |                                        |                         | pools to verify that it checksums correctly.|
|                                             |                                        |                         | For replicated (mirror, raidz, or draid)    |
|                                             |                                        |                         | devices, ZFS automatically repairs any      |
|                                             |                                        |                         | damage discovered during the scrub.         |
+---------------------------------------------+----------------------------------------+-------------------------+---------------------------------------------+

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

Tunables are the settings that go into the ``loader.conf`` and ``sysctl.conf`` files, which allows tweaking of low-level system
settings. They can be set by going to :menuselection:`System --> Settings --> Tunables`.

Here, the currently active settings can be viewed and new ones can be created.
A list of possible values can be obtained by issuing ``sysctl -a`` on an OPNsense shell.
Additional tunables may exist depending on boot loader capabilities and kernel module support.

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

Log settings can be found at :menuselection:`System --> Settings --> Logging`.

An overview of the local settings:

============================================ ====================================================================================================================
Setting                                      Explanation
============================================ ====================================================================================================================
Preserve logs (Days)                         Configures the number of days to keep logs.
Log Firewall Default Blocks                  Turning these off means that only hits for your custom rules will be logged.
Web Server Log                               If checked, lighttpd errors are displayed in the main system log.
Disable writing log files to the local disk  Useful to avoid wearing out flash memory (if used). Remote logging can be used to save the logs instead if desired.
Reset Logs                                   Clear all logs. Note that this will also restart the DHCP server, so make sure any DHCP settings are saved first.
============================================ ====================================================================================================================

............................
Local logs
............................

As of OPNsense 20.7 we changed our default logging method to regular files.
These files will use the following pattern on disk :code:`/var/log/<application>/<application>_[YYYYMMDD].log` (one file per day).
Our user interface provides an integrated view stitching all collected files together.


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
Certificate    Client certificate to use (when selecting a tls transport type)
Description    Set a description for you own use.
============== ================================================================================


.. Note::

    When using syslog over TLS, make sure both ends are configured properly (certificates and hostnames), certificate
    errors are quite common in these type of setups. On OPNsense the general system log usually contains more details.
    When it comes to tracking syslog-ng messages, `this <https://support.oneidentity.com/kb/263658/common-issues-of-tls-encrypted-message-transfer>`__
    is usually a good resource.

    A reconfigure doesn't always apply the new tls settings instantly, if that's not the case best stop and start
    syslog in OPNsense (using the gui).
