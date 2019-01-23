=======
Updates
=======

OPNsense's update schedule consists of two major releases each year, which are updated about every two weeks. The major
releases' version number consists of the year and months of release (e.g. 19.1 for the January 2019 release), with
the fortnightly updates adding a third number (e.g. 19.1.3 for the third update to 19.1).

------------------
Installing updates
------------------

Updates can be installed from the web interface, by going to **System->Firmware->Updates**. On this page, you can click
**Check for updates** to search for updates. If they are available, a button will appear to install them.

---------------
Update settings
---------------

By navigating to **System->Firmware->Settings**, you can influence the firmware update settings:

* **Fimware Mirror:** this influences where OPNsense tries to get its updates from. If you have troubles updating or searching for updates, or if your current mirror is running slowly, you can change it here.
* **Firmware Flavour:** OPNsense is available in different flavours. Currently, these flavours influence which cryptographic library to use: OpenSSL (the default) or its drop-in replacement LibreSSL.
* **Release Type:** With this setting, you can switch between the regular fortnightly schedule of tested releases (Production) or the newest, not fully tested code (Development). **Please leave this setting on "Production", unless you fully understand the implications of switching.**

