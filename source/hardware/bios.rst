====================================
BIOS updates / settings
====================================

This page is dedicated to the latest BIOS update downloads for Deciso appliances as well as a generic instruction on
how to install them.

=====================================================================================================================

.. contents:: Table of Contents
    :local:


**Product families**
=====================================================================================================================

--------------------------------------
DEC4200 series
--------------------------------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
|**04-2025** Version 26                                                                                                                                   |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Download                                                                |SHA256 Checksum                                                                |
+=========================================================================+===============================================================================+
|:download:`Archive <files/A30_v26_bios.tar.gz>`                          |b6833fc82902b67b1d5636f3df940f8a4d45cc157609c37d79139c3bc83325b3               |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CVE updates and performance bugfix causing slow traffic throughput.                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+


--------------------------------------
DEC800, DEC3800 & DEC4000 series
--------------------------------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
|**04-2025** Version 17                                                                                                                                   |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Download                                                                |SHA256 Checksum                                                                |
+=========================================================================+===============================================================================+
|:download:`Archive <files/A20_v17_bios.tar.gz>`                          |1f178be8d57f152601c7d76ae01dab573d104843c7c3bf5e830e9cfeee16a2ce               |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CVE Update.                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+


-------------------------
DEC700 and DEC2700 series
-------------------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
|**04-2025** Version 34                                                                                                                                   |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Download                                                                |SHA256 Checksum                                                                |
+=========================================================================+===============================================================================+
|:download:`Archive <files/A10_v34_bios.tar.gz>`                          |c1a9dbf2087f08c7e2278fbb20c5f7934b7806bdecdd7320496a5d01018f5d42               |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CVE Update.                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

--------------------------------
DEC600 and DEC2600 2.5GbE series
--------------------------------

.. Warning::

    This firmware is exclusive to the DEC600 and DEC2600 2.5 Gigabit series of the A8 version 2 boards. Do not install this firmware
    on older DEC600/DEC2600 devices that only support 1 Gigabit Ethernet.

.. Attention::

    The DEC600 and DEC2600 series (2.5GbE) use an image file that must be written to a USB drive as described in the
    `OPNsense installation instructions <../manual/install.html#installation-media>`__. Replace the OPNsense image in the instructions with the BIOS
    image and write it to the USB drive. After preparing the USB drive, you can ignore steps 1 to 3 and start from step 4
    of the installation instructions below.


+---------------------------------------------------------------------------------------------------------------------------------------------------------+
|**03-2024** Version 2                                                                                                                                    |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Download                                                                |SHA256 Checksum                                                                |
+=========================================================================+===============================================================================+
|:download:`Image <files/Coreboot_Deciso_A8V2.img.bz2>`                   |1f05ed6423dc45bf5c479a86e813ec2a87d73e77544eedd49f2343c5942d2218               |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CPU Frequency corrections and minor bugfixes                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

**Installation instructions**
=====================================================================================================================

Updating the UEFI firmware requires writing a bootable image to a USB drive on a separate machine.
Make sure you have an empty or unused USB drive before starting this procedure. Also make sure the USB
drive is FAT32 formatted.

.. warning::

    As a general warning, following this procedure is at your own risk.


**Step 1**

Download the latest BIOS archive file for your platform from the downloads section above.

**Step 2**


Verify the SHA256 checksum.

**Step 3**

Insert the USB drive into your computer and extract the archive to the USB drive. Make sure the file structure is as follows:

::

    USB drive:/
    ├── LATEST.FD
    ├── startup.nsh
    ├── H2OFFT-Sx64.efi
    ├── efi/
    │   ├── boot/
    │   │   ├── Bootx64.efi


**Step 4**

Safely remove the USB drive from the computer and plug it into the appliance.

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


**Hyper threading**
=====================================================================================================================

Selected models do support hyper threading, but as effectiveness depends on workload, we tend to disable it by default.
If you do want to enable it when supported,  enter the setup utility and search for the following menu item:

    AMD CBS -> Zen Common Options  -> Core/Thread Enablement  -> SMTEN

Select :code:`Auto` here to enable the feature.


**Microcode updates**
=====================================================================================================================

Microcode patches are distributed in our EFI firmware updates. If a Microcode update is required to address specific
issues which are deemed important enough by AMD/Intel, you can install the microcode update yourself in a timely
manner by using the :doc:`/manual/cpu-microcode` plugin.
