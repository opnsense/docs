=============
Settings menu
=============

Besides the configuration options that every component has, OPNsense also contains a lot of general settings
that you can tweak. This page contains an overview of them.

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
