==============================================================
CPU Microcode updates [AMD/Intel]
==============================================================

--------------------------------------
Introduction
--------------------------------------

Processor manufactures like AMD and Intel often release microcode updates to increase stabilty and security of their products.
Microcode updates can close the gap in between BIOS/EFI updates, which are generally less frequently available,
to fix issues found after product release.

This document describes the two plugins available in OPNsense and how to verify the microcode version being used
on the system at hand.

.. note::

    Microcode patches are shipped in our package repository. If there is a new patch level available, it will
    automatically be applied on a system update while the plugin is installed.

--------------------------------------
Installation
--------------------------------------

Installation of this plugin is rather easy, go to :menuselection:`System --> Firmware --> Plugins` and search for **os-cpu-microcode-amd**
or **os-cpu-microcode-intel**, then use the [+] button to install it.

Reboot the machine to apply the new microcode.


--------------------------------------
[Expert] Check microcode version
--------------------------------------

After installing the machine, the microcode update is applied. You can validate the microcode version via the console by using the
following command:

::

    x86info -a | grep -i micro


Which should output something like:

::

    Microcode patch level: 0x800126f


Usually manufactures publish a list of patch levels, for example AMD's patches can be found in the linux `source <https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/amd-ucode/README>`__ tree.

