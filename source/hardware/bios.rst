====================================
BIOS updates
====================================

This page is dedicated to up-to-date BIOS update downloads as well as a generic instruction on
how to install them. 

=====================================================================================================================

-------------------
BIOS version 0009
-------------------

To address a series of 
`vulnerabilities <https://www.bleepingcomputer.com/news/security/uefi-firmware-vulnerabilities-affect-at-least-25-computer-vendors/>`_ 
found in the InsydeH2O UEFI firmware, which affects security appliances from Deciso, the necessary
downloads as well as the instructions to update the UEFI firmware are included here.

**Affected appliances**
=====================================================================================================================

The following appliances using the Netboard `A20 <https://www.deciso.com/netboard-a20/>`_ 
are affected:

- `DEC800 series <https://shop.opnsense.com/dec800-series-opnsense-desktop-security-appliance/>`_
- `DEC3800 series <https://shop.opnsense.com/dec3800-series-opnsense-rack-security-appliance/>`_

=====================================================================================================================

--------------------------
Installation instructions
--------------------------

Updating the UEFI firmware requires writing a bootable image to a USB drive on a separate machine. 
Make sure you have an empty or unused USB drive before starting this procedure.

.. warning:: 
    
    All data on the USB drive will be overwritten. Make sure you have no important data on there.
    As a general warning, following this procedure is on your own risk.


**Step 1**
=====================================================================================================================

Download the right file depending on your platform from the :ref:`downloads <downloads>` section below. For Windows,
an installer is provided. For Linux, an image is provided.

**Step 2** 
=====================================================================================================================


Optionally verify the SHA256 checksum.

**Step 3**
=====================================================================================================================

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
=====================================================================================================================

If all went well and no errors occurred, safely remove the USB drive from the computer and plug it into
the appliance.

**Step 5**
=====================================================================================================================

Boot the appliance and enter the BIOS by pressing Escape. The current BIOS version (suffix) should show up.
Make note of it so you can compare it to the new version to verify everything went well.

**Step 6**
=====================================================================================================================

Select **Boot manager** and boot the USB drive. The UEFI shell will take over and execute the necessary BIOS update.
If the update is complete, the machine will power off. **Do NOT do anything until the machine has shutdown.**

.. note:: 

    Should the USB drive not show up, something went wrong during writing. The newly created FAT32 partition
    should be the very first block on the drive. Inspect the drive on a different machine to check the layout.

**Step 7**
=====================================================================================================================

Reboot the machine and check the new BIOS version in either the boot log or the BIOS itself. 

.. _downloads:

--------------------
Downloads
--------------------

**BIOS version 0009**
=====================================================================================================================

=====================================================================================================================

**Windows**

*Netboard A20*: :download:`Windows installer <files/NetBoard-A20-0009-USB-installer.zip>`

NetBoard-A20-USB-installer.zip (SHA256):13be16e3d7b081e7293a51d811610b87b265ee306396ff18a90450758c9c652d

**Linux**

*Netboard A20*: :download:`Image <files/A20_0009_BIOS_USB_IMAGE.img.bz2>`

A20_009_BIOS_USB_IMAGE.img.bz2 (SHA256):da38482d3f9bcbea8aa6fe34c68b64ffb6f896ac9daa3011efb70b420e31ca01
