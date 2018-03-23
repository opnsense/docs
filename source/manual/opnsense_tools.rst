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

Example:
--------
A minor update also updated the kernel and you experience some driver issues with your NIC.
Open your browser and go to 

https://pkg.opnsense.org/FreeBSD:11:amd64/18.1/sets/

Here you can see all the kernels for version 18.1. Be aware to change the version if you driver a newer version.
As an example you updated from 18.1.4 to 18.1.5 you have now installed kernel-18.1.5. 
To revert back to the last stable you can see kernel-18.1 so the syntax would be:


# opnsense-update -kr 18.1

# /usr/local/etc/rc.reboot


Where -k only touches the kernel and -r takes the version number.


To switch back to the current kernel just use

# opnsense-update -k

# /usr/local/etc/rc.reboot

------------------


opnsense-revert
---------------
The opnsense-revert utility offers to securely install previous versions of packages
found in an OPNsense release as long as the selected mirror caches said release.
For a complete list of options look at the manpage on the system.

Example 1:
----------
The latest update of OPNsense to version 18.1.5 did da minor jump for the IPSec package stronswan.
From this moment your VPNs are unstable and only a restart helps.

To check if the update of the package is the reason you can easily revert the package
to it's previous state while running the latest OPNsense version itself

# opnsense-revert -r 18.1.4 strongswan

With this command you will on e.g. 18.1.5 while reverting the package strongswan to it's version it was in 18.1.4.


Example 2:
----------
The previous revert of strongswan was not the solution you expected so you try to completely revert to the previous
OPNsense version:

# opnsense-revert -r 18.1.4 opnsense

Be aware to also check if there were kernel updates like above to also downgrad the kernel if needed!


------------------



opnsense-patch
--------------
The opnsense-patch utility treats all arguments as upstream git repository commit hashes,
downloads them and finally applies them in order.
Patches can also be reversed by reapplying them, but multiple patches must be given in reverse order to succeed.
For a complete list of options look at the manpage on the system.


Example 1:
----------
You need a special feature for a plugin and ask in Github for it.
A developer adds it and ask you to install the patch df45fdac for testing.

# opnsense-patch -c plugins df45fdac

The -c changes the default core to plugin repo and adds the patch to the system. 
If it doesn't fix your issue of make it even worse, you can just reapply the command 
to revert it.

It is also possible to add patches from differnt users, just add -a githubusername before -c

