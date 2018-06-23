========================
Bootup / autorun options
========================

-------
syshook
-------

OPNsense offers an easy method to plug in custom scripts during boot stages and assorted system events.

Syshook scripts should be installed in:

::

    /usr/local/etc/rc.syshook.d/<subdir>/

They can contain any executable file (e.g. shell scripts) in the following subdirectories:

- backup
    - scripts used for peroidic backup and restore
- carp
    - scripts used for CARP MASTER / BACKUP events
- early
    - start script before system network startup
- start
    - start script after system network startup
- stop
    - stop script before normal system shutdown

File names can use a number prefix "XX-" to retain a particular order.  "20-" is typically used for core scripts, while "50-" is used for plugins.

Example (vmware guestd start, filename /usr/local/etc/rc.syshook.d/early/50-vmware)

::

    #!/bin/sh

    export vmware_guest_vmblock_enable="YES"
    export vmware_guest_vmhgfs_enable="YES"
    export vmware_guest_vmmemctl_enable="YES"
    export vmware_guest_vmxnet_enable="YES"

    /usr/local/etc/rc.d/vmware-kmod start

Do not forget to set executable permissions on your syshook files.

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
