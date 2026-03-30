====================================
Support
====================================

Firewalls can be complex devices, in which case it helps to have some pointers when running into
issues. When official hardware is used, a free year of OPNsense Business Edition is offered with the product.

In case a problem emerges, we need to establish if this is related to either hardware or software. Over the years
we have seen quite some different challenges people run into, which we would like to highlight in this chapter, including
feedback our engineers need to assess if an issue is hardware related. To assist with installation and/or configuration
challenges, we can always offer support when subscribed to our business support service.


.. Tip::

    Always make sure to backup your configuration before doing any debugging.

.. Note::

    To start an RMA procedure, always contact our sales team (sales at opnsense dot com) first, make sure to let us know which device serial number it relates to.

.. Note::

    When redacting output for security reasons, always make sure networks are replaced with similar numbers (specifically using the same subnets),
    for example when using :code:`192.168.1.1/24` on the firewall and not wanting to share that information, just replace it with
    something like :code:`x1.x1.x1.1/24` so we know there is a :code:`/24` network for which we use the `.1` address.


When sharing information with our team, you often need to collect some data from the machine, you can either arrange that via
`serial connectivity <serial_connectivity.html>`__ or a `secure shell <../manual/settingsmenu.html#secure-shell>`__.


Network connectivity issues
------------------------------------------

When there's no or limited network connectivity, we need to establish if there is a physical connectivity issue first.
Always make sure to use well shielded network cables and check connectivity on the same switch port using a laptop or other
device to rule out issues with the other end of the connection.

Knowing both cable and switch (or modem) connectivity is fine, we can start investigating if the issue is caused by a specific
port or if its a more generic issue. We can use :menuselection:`Interfaces --> Assignments` to switch ports around, so for example if :code:`igc0`
is having issues, try to move the function to another port and see if the issue persists after a clean reboot.

If the issue seems to be isolated to a single (specific) port, when contacting our office, please share the status of the lights
for both working and non working ports and via a console collect the output of the following commands after a clean reboot:

.. code-block:: sh

    dmesg
    ifconfig -m -v
    ifinfo

In cases where the issue seems to persist when chosing another port, the easiest option to rule out hardware issues is to
reinstall the device and retest with our default settings.


Boot issues / drive issues
------------------------------------------

In order to debug, we need to establish console connectivity first using the (serial) console port.
When powering up the machine, after a while, there's usually some output from the bios of the machine.

You can use the :code:`<ESC>` key to select a boot device, with this you can boot from a usb stick to reinstall if
you're not able to boot into OPNsense at all.

In some cases, even with a zfs filesystem, it happens that the filesystem gets corrupted, if that's the case, it's usually best
to reinstall the device (see reinstalling).

Most of our devices use NVME storage, if your device contains one and you wish to reinstall as clean as possible (which is advisable in some situations),
boot into the installer, login using :code:`opnsense` with the password :code:`root` next choose 8 for console and execute the following command:

.. code-block:: sh

    nvmecontrol format nvme0

Then exit to login prompt (type exit and select 0) And try re-installing (using :code:`installer` with password :code:`opnsense`).


Random crashes or reboots
------------------------------------------

When the machine crashes with a "kernel" crash, there's often a crash report in :menuselection:`System --> Firmware --> Reporter`, you can upload that
via the reporter to us adding your email address (to help us find it) or you can copy any relevant information that is reported there and
send it to our team.

In most cases, to exclude hardware issues, it's best to reinstall the machine and test it without any additional plugins installed.
If the machine remains unstable in that case, please share the crash reporter output and the output of the following commands so we can assess next steps on our end:

.. code-block:: sh

    dmesg
    cat /var/log/system/latest.log



Reinstalling the Business Edition
------------------------------------------

Using your license number, you can always download the latest software installers from our servers, these are located at
`https://opnsense-update.deciso.com/[license_number]/Installers <https://opnsense-update.deciso.com/>`__.

The filenames are similar to the ones used for the community edition, these are explained `here <../manual/install.html#image-filename-composition>`__,
just continue reading in that section of the manual to learn how to verify the files, create a bootable usb stick and run the installer.
Both versions are similar when it comes to installation.

.. Note::

    For installs on our hardware, you will need the :code:`serial` type.


