====================================
BIOS updates
====================================

This page is dedicated to up-to-date BIOS update downloads as well as a generic instruction on
how to install them.

=====================================================================================================================

.. contents:: Table of Contents
    :local:


**Product families**
=====================================================================================================================

--------------------------------------
DEC800, DEC3800 & DEC4000 series
--------------------------------------

+---------------+------------------------------------------------------------------------------------------------------------------------------------------+
|**12-2022**: Version 10a (latest)                                                                                                                         |
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
|      OS       | Download                                                                |SHA256 Checksum                                                 |
+===============+=========================================================================+================================================================+
| Windows       |:download:`Windows installer <files/NetBoard_A20_010a_USB_installer.zip>`|7911491dd1980affc189c290a4590c72105445aab3c74163b649daba1b9fd271|
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
| Linux         |:download:`Image <files/A20_010a_BIOS_USB_IMG.img.bz2>`                  |19d2d011b2d63eff3d6e422b475a1bde2dd76c752d1abcb224c2c4310f273a44|
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
| CVE update.                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

+---------------+------------------------------------------------------------------------------------------------------------------------------------------+
|**03-2022**: Version 9                                                                                                                                    |
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
|      OS       | Download                                                                |SHA256 Checksum                                                 |
+===============+=========================================================================+================================================================+
| Windows       |:download:`Windows installer <files/NetBoard_A20_0009_USB_installer.zip>`|e92dc8e3822ae295e218a3e67fe86743ccb0220fcbd98e22dbfa5fd9e3b7d9f7|
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
| Linux         |:download:`Image <files/A20_0009_BIOS_USB_IMAGE.img.bz2>`                |d217149a90f5ed2b3fe6a317b5317c94d4f4988a9065249ce6addf790e42b609|
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
|   Addresses a series of                                                                                                                                  |
|   `vulnerabilities <https://www.bleepingcomputer.com/news/security/uefi-firmware-vulnerabilities-affect-at-least-25-computer-vendors/>`_                 |
|   found in the InsydeH2O UEFI firmware, which affects the NetBoard `A20 <https://www.deciso.com/netboard-a20/>`_ security appliances from Deciso.        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+


-------------------------
DEC700 and DEC2700 series
-------------------------

+---------------+------------------------------------------------------------------------------------------------------------------------------------------+
|**03-2023**: Version 24 (latest)                                                                                                                          |
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
|      OS       | Download                                                                |SHA256 Checksum                                                 |
+===============+=========================================================================+================================================================+
| Windows       |:download:`Windows installer <files/NetBoard_A10_0024_USB_installer.zip>`|a4f63ac91a20a74ef32a74e18f791186fba1b281734024fe52f317a59ddc3eb3|
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
| Linux         |:download:`Image <files/A10_0024_BIOS_USB_IMAGE.img.bz2>`                |6831eb1945ea71b27c9fe420a842b2a8a6966c53c1935232d57cef35e1598e25|
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
|   CVE Update and improved fan control.                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

+---------------+------------------------------------------------------------------------------------------------------------------------------------------+
|**03-2022**: Version 22                                                                                                                                   |
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
|      OS       | Download                                                                |SHA256 Checksum                                                 |
+===============+=========================================================================+================================================================+
| Windows       |:download:`Windows installer <files/NetBoard_A10_0022_USB_installer.zip>`|5fc6fcc98d17d207b29e4e8f9ac5a0765a2f69b2ff058f958e7727519d0b676f|
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
| Linux         |:download:`Image <files/A10_0022_BIOS_USB_IMAGE.img.bz2>`                |a4c107d7fa1240fbb1e2fd5368c30d5ff7e66897424cf34942dd260b11eca9b8|
+---------------+-------------------------------------------------------------------------+----------------------------------------------------------------+
|   Addresses a series of                                                                                                                                  |
|   `vulnerabilities <https://www.bleepingcomputer.com/news/security/uefi-firmware-vulnerabilities-affect-at-least-25-computer-vendors/>`_                 |
|   found in the InsydeH2O UEFI firmware, which affects the NetBoard `A10 <https://www.deciso.com/netboard-a10/>`_ security appliances from Deciso.        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

|

**Installation instructions**
=====================================================================================================================

Updating the UEFI firmware requires writing a bootable image to a USB drive on a separate machine.
Make sure you have an empty or unused USB drive before starting this procedure.

.. warning::

    All data on the USB drive will be overwritten. Make sure you have no important data on there.
    As a general warning, following this procedure is on your own risk.


**Step 1**

Download the right file depending on your platform from the section above. For Windows,
an installer is provided. For Linux, an image is provided.

**Step 2**


Optionally verify the SHA256 checksum.

**Step 3**

Insert the USB drive. For Windows, unzip and start the installer executable and follow the instructions.
When prompted for a drive select the USB drive.


For Linux, decompress the image and write the image to the USB drive::

    cd /<directory where image is located>
    bzip2 -d <image name>.bz2
    sudo dd if=./<image name>.img of=/dev/<drivename> bs=1024k

Where *image name* refers to the downloaded image, and *drivename* refers to the USB drive.

.. note::

    When selecting a drive on Linux, make sure you select the *entire* drive, not a single partition
    (e.g. */dev/sdb*, not */dev/sdb1*)


**Step 4**

If all went well and no errors occurred, safely remove the USB drive from the computer and plug it into
the appliance.

**Step 5**

Connect to the appliance using a :ref:`serial` connection. Open a terminal to the relevant COM port.

**Step 6**

Boot the appliance and enter the BIOS by pressing Escape. The current BIOS version (suffix) should show up.
Make note of it so you can compare it to the new version to verify everything went well.

**Step 7**

Go to Setup Utility --> AMD CBS --> FCH Common Options --> UART Configuration Options --> UART 0 Legacy Options.
Make sure this setting is set to **Disabled**. This is explained in :ref:`legacy_uart`.

.. note::

    Should your serial terminal highlight a BIOS option selection in such a way that it is unreadable, for
    the A20 appliance it's the very first option in the UART Configuration Options menu screen.

**Step 8**

Select **Boot manager** and boot the USB drive. The UEFI shell will take over and execute the necessary BIOS update.
If the update is complete, the machine will power off. **Do NOT do anything until the machine has shutdown.**

.. note::

    Should the USB drive not show up, something went wrong during writing. The newly created FAT32 partition
    should be the very first block on the drive. Inspect the drive on a different machine to check the layout.

**Step 9**

Reboot the machine and check the new BIOS version in either the boot log or the BIOS itself.
