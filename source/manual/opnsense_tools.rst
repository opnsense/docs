==============
OPNsense Tools
==============

------------
Introduction
------------
The OPNsense project offers a bunch of tools to instantly patch the system,
revert a package to a previous (older version) state or revert the whole kernel. 

---------------
opnsense-update
---------------
The opnsense-update utility offers combined kernel and base system upgrades
using remotely fetched binary sets, as well as package upgrades via pkg.
For a complete list of options look at the manpage on the system.

Example 1:
----------
A minor update also updated the kernel and you experience some driver issues with your NIC.
Open your browser and go to 

https://pkg.opnsense.org/FreeBSD:11:amd64/18.1/sets/

Here you can see all the kernels for version 18.1. Be aware to change the version if you driver a newer version.
As an example you updated from 18.1.4 to 18.1.5 you have now installed kernel-18.1.5. 
To revert back to the last stable you can see kernel-18.1 so the syntax would be:

``
opnsense-update -kr 18.1
/usr/local/etc/rc.reboot
``

Where -k only touches the kernel and -r takes the version number.



------------------

VMware ESXi
-----------
VMware offers full instructions for installing FreeBSD, these can be found
`here <http://partnerweb.vmware.com/GOSIG/FreeBSD_11x.html>`__.

To install the VMware tools just goto **System->Firmware->Plugins** and install
**os-vmware** by clicking on the **+** sign next to it.

.. image:: images/os-vmware.png

.. Note::

        While other network setups may work fine, the e1000 driver seems to work
        best, certainly when utilizing the traffic shaper.

------------------

Xen
---
To install the Xen tools just goto **System->Firmware->Plugins** and install
**os-xen** by clicking on the **+** sign next to it.

.. image:: images/os-xen.png

------------------

HyperV
------
HyperV Generation 1 and 2 are supported out of the box, no additional drivers
or tools are needed.

Others
------
OPNsense can be installed on all virtual machines that support FreeBSD (such as
KVM, Bhyve, VirtualBox).

------------------

------
Hosted
------
For hosted installations where you can't install using the cdrom iso an alternative
approach is available in  the form of **opnsense-bootstrap**.

opnsense-bootstrap
------------------
opnsense-bootstrap(8) is a tool that can completely reinstall a running system
in place for a thorough factory reset or to restore consistency of all the OPNsense
files. It can also wipe the configuration directory, but won't do that by default.

It will automatically pick up the latest available version and build a chain of
trust by using current package fingerprints -> CA root certificates -> HTTPS -> OPNsense
package fingerprints.

What it will also do is turn a supported stock FreeBSD release into an OPNsense
installation, given that UFS was used to install the root file system.

opnsense bootstrap is available for our
`github source repository <https://github.com/opnsense/update/tree/master/bootstrap>`__

------------------

--------------------
Amazon AWS EC2 Cloud
--------------------
.. image:: how-tos/images/amazon-web-services.png
    :scale: 100%

Installing OPNsense into the Amazon cloud can be a dounting task as no console is
offered. As part of Deciso's support packages (see `OPNsense commercial Support
<https://opnsense.org/support-overview/commercial-support/>`__), deciso offer free
access to its OPNsense Amazon Machine Image (AMI).

See also our how-to for :doc:`how-tos/installaws`.

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
OPNsense installation has a minimum of 1GB of RAM.

------------------

Disk Errors on VMware
-----------------------
This issue can be caused by a defective drive. Changing drive mode to IDE has
been reported to help for certain ESXi versions.

------------------

Installation failure on KVM
---------------------------
If you are using virtio for the root disk then try switching to sata mode.

------------------

NAT issues on XenServer
-----------------------
This issue has been reported to be solved by disabling cheksum offloading on both
OPNsense domU and Vifs.

------------------

Traffic Shaper does not work on VMware
--------------------------------------
If you are using vmxnet3 drivers try to switch to E1000.
