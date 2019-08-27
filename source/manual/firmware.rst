==========================
Firmware
==========================

In the firmware section you can keep your OPNsense up to date and have the ability to install additional software.


--------------------------------
Updates
--------------------------------


How to install updates and information about our versioning can be found in the Installation and setup section, which
can be found in the  :doc:`/manual/updates` document


--------------------------------
Plugins
--------------------------------

Plugins are additional software packages that are available for OPNsense, usually they come with there own
frontend components to setup the software underneath.
Here you can find community support plugins, such as  **bind**, **c-icap**, **freeradius** and others. Usually there is also
a **-devel** version available, which contains features still under development (master branch on GitHub verses release).


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
Settings
--------------------------------

The settings menu contains all available mirrors and options which you can choose for your installation.
Usually the default options are good enough here, but if you want to choose a mirror more close to home you can do so here.

OPNsense supports two flavours for its TLS crypto stack , OpenSSL and LibreSSL. Our standard is `OpenSSL <https://www.openssl.org/>`__, but some more
security minded people favor OpenBSD's `LibreSSL <https://www.libressl.org/>`__

.. Note::

    Since OpenSSL is more widely used, some software packages are not compatible with LibreSSL.


.. Tip::

    The settings menu also provides the option to test development versions, which can be practical when testing features that
    are planned for release. Just change the release type to **Development**.
