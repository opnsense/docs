==========================
Firmware
==========================

In the firmware section you can keep your OPNsense up to date and have the ability to install additional software.


--------------------------------
Updates
--------------------------------


How to install updates and information about our versioning can be found in the Installation and setup section, which
can be found in the  :doc:`/manual/updates` document.


--------------------------------
Plugins
--------------------------------

Plugins are additional software packages that are available for OPNsense, usually they come with their own
frontend components to setup the software underneath.  Shown by default are support tier 1 and 2 plugins.

Here you can also find community plugins from lower tiers, such as  **bind**, **c-icap**, **freeradius** and others.
These are not listed by default.  To view them use the **Show community plugins** checkbox.

When on the development version, a **-devel** version is also available available, which may contain features still under development
or ready for wider testing before their eventual release (master branch on GitHub versus release).

Our plugin support tiers are explained in detail in the :doc:`/support` document.

.. Note::

    .. raw:: html

          You can use the <i class="fa fa-plus fa-fw"></i> symbol to install the package.


.. Tip::

  .. raw:: html

        Use the info <i class="fa fa-info-circle fa-fw"></i> button to display information about the package and to find the active maintainer of this piece of software.


--------------------------------
Packages
--------------------------------

The packages tab contains the installed ports packages, here you can check licenses, force reinstalls or lock
versions.

--------------------------------
Changelog
--------------------------------

If you would like to read about the changes in (past) releases, you can do so in the **Changelog** tab.

--------------------------------
Status (firmware audits)
--------------------------------

Audits provided are troubleshooting tools for a variety of purposes explained below.
The forum is a good place to post your update and upgrade issues if you get stuck despite the best effort.

The cleanup audit triggers an immediate removal of all tempporary update files. Sometimes these files are not
cleaned up correctly and can cause issues with the next round of package updates.

The connectivity audit offers a direction where to look for issues during updates and the following causes are
in our experience most common:

* Misconfigured DNS settings, check :menuselection:`System --> Settings --> General` for configured servers the firewall is allowed to use
* Misconfigured IPv6, in which case "Prefer IPv4 over IPv6" in :menuselection:`System --> Settings --> General` might help to prevent the system from using IPv6 in these cases
* In HA (carp) setups, using the wrong extrenal IPaddress, usually caused by a misconfigued outbound nat rule, easy to check by disabling manual outbound nat rules in :menuselection:`Firewall --> NAT --> Outbound`.

The heath audit can also help with uncovering installation and disk / file system issues.
Additionally, major ugpgrades may not pass certain sanity checks that need to be corrected first which may include the command line:

* "Could not determine core package name." can indicate that the local package manager database was lost. See `opnsense-bootstrap` command to fix.
* "No package manager is installed to perform upgrades." can indicate a broken installation. Try to reinstall the "pkg" package via `System --> Firmware --> Packages`.
* "The Package manager is incompatible and needs a reinstall." can indicate misuse of the FreeBSD repository. Try to reinstall the "pkg" package via `System --> Firmware --> Packages`.
* "Core package not known to package database." can mean that the mirror settings are wrong, the main mirror no longer holds any packages or that the mirror is unreachable for other reasons.

The security audit checks each installed package's version against a database of known vulnerabilities. Vulnerabilities
are reported for triage and inspection, not for reporting them to OPNsense. The appearance of vulnerabilities in an install
indicate that the next update will likely address them.

After having performed a major upgrade, the upgrade audit shows the package upgrade log for further inspection.
This can be helpful to identify package conflicts that led to partial or full upgrade failures.

--------------------------------
Settings
--------------------------------

The settings menu contains all available mirrors and options which you can choose for your installation.
Usually the default options are good enough here, but if you want to choose a mirror more close to home you can do so here.


.. Tip::

    The settings menu also provides the option to test development versions, which can be practical when testing features that
    are planned for release. Just change the release type to **Development**.


.. Note::

    Although OPNsense does not support the configuration of a proxy server, for services like the firmware updater it is possible
    to add these settings manually in our :code:`configd` service.
    For more information we refer to :doc:`the envronment section in our development docs </development/backend/configd>`.


Apply the Business Edition
...........................................

When you have purchased a license for the Business Edition or received it pre-installed on an appliance, you will
have to enable the license first.

In order to do so, please choose the following settings:

============== ==================================================================================
Mirror:        Deciso (HTTPS,NL,Commercial)
Flavour:       OpenSSL
Type:          Business
Subscription:  XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX (the activation key for the product)
============== ==================================================================================


.. image:: ../hardware/images/quickstart_be.png
    :width: 500px


After save, go back to the status tab and click **Check for updates**


.. Note::

    Upgrading to OPNsense BE is only possible when the installed community version number is lower than the
    last available business edition. E.g. you can upgrade **22.7.x** to **22.10.x**, but you can not upgrade
    **23.1** to **22.10**. You can always re-install using the installer found on the `business mirror <https://opnsense-update.deciso.com/>`__

