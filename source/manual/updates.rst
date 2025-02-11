=======
Updates
=======

The OPNsense update schedule consists of two major releases each year, which receive minor updates about every two weeks.
The major release version number consists of the year and months of release (e.g. 25.1 for the January 2025 release),
with the fortnightly minor updates adding a third number (e.g. 25.1.3 for the third update to 25.1).

---------------
Update settings
---------------

By navigating to :menuselection:`System --> Firmware --> Settings`, you can influence the firmware update settings:

* **Fimware Mirror:** this influences where OPNsense tries to get its updates from. If you have troubles updating or searching for updates, or if your current mirror is running slowly, you can change it here.
* **Release Type:** With this setting, you can switch between the regular fortnightly schedule of tested releases (Production) or the newest, not fully tested code (Development). **Please leave this setting on "Production", unless you fully understand the implications of switching.**

.. Tip::
    The settings page is also the place where you can run audits which help debugging common connectivitty issues,
    just press the "Run an audit" and choose "Connectivity" from the list.

-------------
Minor updates
-------------

Updates can be installed from the web interface, by going to :menuselection:`System --> Firmware --> Status`.
On this page, you can click **Check for updates** to search for updates.
If they are available, a button will appear to install them.

--------------
Major Upgrades
--------------

Major upgrades are recommended to do via VGA display or serial console because you can see what is going on.

.. Note::
    You can find some documentation about serial access under :doc:`how-tos/serial_access`

.. Warning::
    Major updates are installed offline. So no web interface or SSH is running to monitor the upgrade.
    If something fails, you need a second connection or direct access to revert the VM or repair the installation.

If you choose option 12 on the console menu on latest release, you are asked if you want to upgrade to the newest
version or to the next major release. Type in the major release number (for example "19.1") and press enter.
OPNsense will download all release files for an offline upgrade (kernel, packages etc.) and will reboot afterwards.

After a reboot, it will install all updates and when it is done, it will reboot again, then you should be on the
desired release.

-----------------------
Troubleshooting updates
-----------------------

The connectivity audit offers a direction where to look for issues during updates and the following causes are
in our experience most common:

* Misconfigured DNS settings, check :menuselection:`System --> Settings --> General` for configured servers the firewall is allowed to use
* Misconfigured IPv6, in which case "Prefer IPv4 over IPv6" in :menuselection:`System --> Settings --> General` might help to prevent the system from using IPv6 in these cases
* In HA (carp) setups, using the wrong extrenal IPaddress, usually caused by a misconfigued outbound nat rule, easy to check by disabling manual outbound nat rules in :menuselection:`Firewall --> NAT --> Outbound`.

The heath audit can also help with uncovering installation and disk / file system issues.
Additionally, major ugpgrades may not pass certain sanity checks that need to be corrected first which may include the command line:

* "Could not determine core package name." can indicate that the local package manager databse was lost. See `opnsense-bootstrap` command to fix.
* "No package manager is installed to perform upgrades." can indicate a broken installation. Try to reinstall the "pkg" package via `System --> Firmware --> Packages`.
* "The Package manager is incompatible and needs a reinstall." can indicate misuse of the FreeBSD repository. Try to reinstall the "pkg" package via `System --> Firmware --> Packages`.
* "Core package not known to package database." can mean that the mirror settings are wrong, the main mirror no longer holds any packages or that the mirror is unreachable for other reasons.

The forum is a good place to post your update and upgrade issues if you get stuck despite the best effort.
