====================================
Password reset
====================================

Sometimes people lose their passwords, in which case it can be practical to reset the root password
without performing a reinstall.

This guide describes step by step how to reset the root password.

.. Note::

    You can also use the installer to reset the password,
    use the :code:`Password Reset - Recover Installation` option in the installer after the keymap selection.


-----------------------------
Step 1 : power
-----------------------------

Since you need to influence the boot process to reset the password, you should start with powering off the (virtual) device.

-----------------------------
Step 2 : console
-----------------------------

Make sure you are able to access the (virtual) console, in case it's a physical machine you might want to connect a
monitor and keyboard, when it's an appliance with serial access, make sure to connect to the serial/usb port using an application
like putty.

.. Tip::

    When using devices from the OPNsense shop (https://shop.opnsense.com), usually there's a mini-usb to serial cable included
    in the box, the :doc:`Serial Console connectivity </hardware/serial_connectivity>` guide will help you with the setup.

-----------------------------
Step 3 : boot single
-----------------------------

Switch the power and wait for the OPNsense splash screen to appear, the choose "Boot [S]single User" which should be option 2 in the list.
(press 2)

-----------------------------
Step 4: password reset
-----------------------------

This stage depends on the type of installation, the root filesystem could either be UFS or ZFS, both requiring different commands to
enable modifications in single user mode.


For UFS file systems, execute the following command in the shell to enable disk modifications:

.. code-block:: sh

    /sbin/mount -o rw /


When using ZFS, the following commands are required

.. code-block:: sh

    /sbin/mount -u /
    /sbin/zfs mount -a

Now the disk can be written to, use the following commands to reset the password and reboot the machine:

.. code-block:: sh

    opnsense-shell password
    reboot

The `opnsense-shell` will ask for a confirmation, respond with `Y`
