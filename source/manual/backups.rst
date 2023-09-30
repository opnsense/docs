==========================
Configuration
==========================

The configuration section contains some tools to keep track of your setup.

--------------------------------
Backup
--------------------------------

You can backup and restore your machines configuration using the :menuselection:`System --> Configuration --> Backups` section.
When performing a local backup, you can choose to protect it with a password and decide whether or not you
would like to store rrd statistics as well (in which case they will be stored in the same export xml file).

.. Warning::

    The configured console settings of a machine may not be applicable to the situation of other (virtual) hardware platforms.
    To avoid losing console access to the firewall in these cases, the configuration restore will not apply the backups'
    console settings by default. To disable this behaviour, uncheck **Exclude console settings from import**.

.. Note::

    Due to the sensitive nature of your configuration data, its advisable to protect backups with a strong password when
    storing them or distributing them to others.

.. Note::

    RRD statistics are used in System Health


Restoring backups can either be performed partially or for the complete configuration. Since configurations usually
have various components that depend on each other, it's most safe to restore a complete configuration.

.. Warning::

    Partial restores can lead to unexpected behavior, use with care. Future versions might not support this feature due
    to consistency reasons. (not all components can be partially exported)

.. Note::

    If restoring a backup on a different (virtual) machine and the hardware interface names do not match, a reboot will
    not automatically take place, instead you will be prompted to fix the interface assignments.


.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/cloud_backup
   git-backup


--------------------------------
Defaults
--------------------------------

With the defaults tool you can reset your firewall back to firmware defaults and shutdown when done.


--------------------------------
History
--------------------------------

The history menu helps you track changes between modifications and offer the opportunity to download older
versions of your settings.

.. Tip::

    You can specify the number of backups to keep in the backups menu, which can be quite practical when a higher level of
    auditability is required.
