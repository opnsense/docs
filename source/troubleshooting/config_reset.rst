====================================
Restore Configuration via Console
====================================

Sometimes you may accidentally introduce a breaking change that interrupts network access, prevents user login or makes SSH and WebGUI inaccessible.
Rolling back without a reinstall is possible if there is serial and console access.

For serial access to the console, reference this guide: :doc:`Serial Console connectivity </hardware/serial_connectivity>`

Console access is also possible directly when running a virtual machine or hardware with VGA capabilities.

This guide describes step by step how to restore a previous configuration via console.

.. Attention::

    This requires automatic backups being retained. If you changed `Backup Count` settings in :menuselection:`System --> Configuration --> Backups`,
    the history can be too short to restore a working configuration from the local backup cache. 
    Mounting a USB flash drive with a previous configuration might be necessary.

.. Tip::

    Using :doc:`Snapshots </manual/snapshots>` with a ZFS filesystem can make rollbacks simpler.


-----------------------------
1. Power off the device
-----------------------------

Since you need to influence the boot process to reset the configuration, you should start with powering off the (virtual) device.

.. Attention::

    If you run a HA setup, ensure any cron jobs that synchronize the configuration are turned off. Otherwise they can overwrite the
    configuration that you restored.

-----------------------------
2. Access console
-----------------------------

Make sure you are able to access the (virtual) console, in case it is a physical machine you might want to connect a
monitor and keyboard, when it is an appliance with serial access, make sure to connect to the serial/usb port using an application
like putty.

.. Tip::

    When using devices from the OPNsense shop (https://shop.opnsense.com), usually there's a mini-usb to serial cable included
    in the box, the :doc:`Serial Console connectivity </hardware/serial_connectivity>` guide will help you with the setup.

-----------------------------
3. Power on and boot
-----------------------------

Switch the power and wait for the OPNsense splash screen to appear. Do not interact with the splash screen, wait for the actual boot to start.

When the text scrolls fast, hold the **CTRL** button and press **C** rapidly to break out of the boot process into a shell. This does not need any
authentication.

-----------------------------
4. Replace configuration
-----------------------------

Now that you are in the shell, you can do changes to the filesystem. In our example, we will restore a previous config.xml version.

First we will evaluate which config.xml version should be restored:

.. code-block:: sh

    cd /conf/backup
    ls -la

Check out the timestamps of the backup configurations, copy the filename of one that was before you made the breaking change.
We will backup our current config.xml and then overwrite it with a previous version.

.. Attention::
    
    The below example must be adjusted to represent your config.xml timestamp.

.. code-block:: sh

    cp /conf/config.xml /conf/config.xml.backup
    cp /conf/backup/config-YOURTIMESTAMP.xml /conf/config.xml

Reboot and the replaced configuration will be loaded.

.. code-block:: sh

    reboot

After the reboot, confirm that you can log in and that the breaking change has been rolled back. If not, repeat the above steps and go back 
further with the backup configuration timestamp.

If this cannot fix it, :doc:`reinstall your appliance </manual/install>` with the latest available image and restore a
known-good configuration you have kept safe.
