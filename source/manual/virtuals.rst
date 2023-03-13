==================================
Virtual & Cloud based Installation
==================================

------------
Local/Server
------------
Installing OPNsense on a virtual machine can be done by using the DVD ISO image.
Full instructions are available in chapter :doc:`install` .

General tips
------------
For optimum performance and compatibility, these guides are given:

* Minimum required RAM is 1 GB
* Minimum recommended virtual disk size of 8 GB
* Disable all off-loading settings in :menuselection:`Interfaces --> Settings`

.. image:: images/disableoffloading.png

------------------

VMware ESXi
-----------
VMware offers full instructions for installing FreeBSD, these can be found
`here <https://partnerweb.vmware.com/GOSIG/FreeBSD_13x.html>`__.

To install the VMware tools just goto :menuselection:`System --> Firmware --> Plugins` and install
**os-vmware** by clicking on the **+** sign next to it.

.. image:: images/os-vmware.png

.. Note::

        While other network setups may work fine, the e1000 driver seems to work
        best, certainly when utilizing the traffic shaper.

------------------

Xen
---
To install the Xen tools just goto :menuselection:`System --> Firmware --> Plugins` and install
**os-xen** by clicking on the **+** sign next to it.

.. image:: images/os-xen.png

------------------

HyperV
------
HyperV Generation 1 and 2 are supported out of the box, no additional drivers
or tools are needed.

KVM
---
**i440FX chipset**
OPNsense on KVM works with virtio disks and network devices (confirmed on QEMU 5.0).

**Q35 chipset**
As of 22.1.x, OPNsense is based on FreeBSD 13.0, which includes support for the virtualized Q35 chipset and newer
generation of KVM virtio devices.
Note that this was a relatively recent addition to FreeBSD, so it may not be as well tested as the i440 support.

Others
------
OPNsense can be installed on all virtual machines that support FreeBSD (such as Bhyve, VirtualBox).

------------------

------
Hosted
------
For hosted installations where you can't install using the DVD ISO an alternative
approach is available in the form of **opnsense-bootstrap**.

opnsense-bootstrap
------------------
opnsense-bootstrap(8) is a tool that can completely reinstall a running system
in place for a thorough factory reset or to restore consistency of all the OPNsense
files. It can also wipe the configuration directory, but won't do that by default.

It will automatically pick up the latest available version and build a chain of
trust by using current package fingerprints -> CA root certificates -> HTTPS -> OPNsense
package fingerprints.

What it will also do is turn a supported stock FreeBSD release into an OPNsense
installation.  Both UFS and ZFS installations are supported.

opnsense bootstrap is available for our
`github source repository <https://github.com/opnsense/update/tree/master/bootstrap>`__

------------------

--------------------
Amazon AWS EC2 Cloud
--------------------
.. image:: how-tos/images/amazon-web-services.png
    :height: 80px

Installing OPNsense into the Amazon cloud can be a daunting task as no console is
offered. Luckily an easy to install AMI is also available in the aws marketplace.

See also our how-to for :doc:`how-tos/installaws`.


--------------------
Microsoft Azure
--------------------
.. image:: how-tos/images/Azure.png
    :height: 80px

OPNsense is also available in the Microsoft Azure Marketplace as an easy installable virtual appliance.

See also our how-to for :doc:`how-tos/installazure`.

-------------
Common Issues
-------------
Some common issues have been reported for different virtual environments.
You can find known solutions to these problems below.

If you problem is not listed always try the General tips as mentioned in the
article first.

------------------

File copy failed during installation
------------------------------------
This issue is most likely caused by low memory setting. Make sure your virtual
OPNsense installation has a minimum of 1 GB of RAM.

------------------

Disk Errors on VMware
-----------------------
This issue can be caused by a defective drive. Changing drive mode to IDE has
been reported to help for certain ESXi versions.

------------------

NAT issues on XenServer
-----------------------
This issue has been reported to be solved by disabling checksum offloading on both
OPNsense domU and Vifs.

------------------

Traffic Shaper does not work on VMware
--------------------------------------
If you are using vmxnet3 drivers try to switch to E1000.
