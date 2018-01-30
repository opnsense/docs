========================
Bootup / autorun options
========================

-------
syshook
-------

OPNsense offers an easy method to plugin shell scripts during (early) boot stage.

Syshook scripts should be installed in :

::

    /usr/local/etc/rc.syshook.d/

They can contain regular shell scripts using the following extensions:

- start
    - start script after normal system startup
- early
    - start script before normal system startup.

Example (vmware guestd start, filename /usr/local/etc/rc.syshook.d/vmware.early)

::

    #!/bin/sh

    export vmware_guest_vmblock_enable="YES"
    export vmware_guest_vmhgfs_enable="YES"
    export vmware_guest_vmmemctl_enable="YES"
    export vmware_guest_vmxnet_enable="YES"

    /usr/local/etc/rc.d/vmware-kmod start


-----
rc(8)
-----

Part of the bootup process of OPNsense is probing the available rc(8) configuration files in */etc/rc.conf.d/*, when a daemon is enabled, the system will call the regular rc(8) start command.

In case the daemon needs some extra preparation, an additional "bootup" script can be provided, which will be run before executing normal "start".

Example (from a configured squid proxy server using */etc/rc.conf.d/squid*):

::

    squid_enable=YES
    squid_opnsense_bootup_run="/usr/local/opnsense/scripts/proxy/setup.sh"


The configd template system can be used to generate the necessary configuration file(s).
