========================
Overview
========================

The life of a service starts during the boot process, but with different hooks available, sometimes it is challenging
to find the correct one. This paragraph aims to explain the various integration spots availabe, which are
being explained in more detail in the rest of the chapter.


....................................
Bootup
....................................

After the kernel is loaded and the machine starts to boot, the following integration points are being executed
in sequence:

1.  :doc:`syshook/early </development/backend/autorun>`, simple shell scripts to run before any network services are loaded,
    can for example be used to load specific drivers.
2.  :doc:`plugins/device </development/backend/legacy>`, register and create devices, services like OpenVPN use this on
    our end to make sure :code:`tun` and :code:`tap` devices exist before doing further configuration.
3.  :doc:`plugins/configure/early </development/backend/legacy>`, configure :code:`early` event in bootup process, before normal services are being started (things like ssh and the webconfigurator use this spot)
4.  :doc:`plugins/firewall </development/backend/legacy>` allows for automatic firewall (nat) rule registration in cases where the service is able to ship its own rules. (some do this optionally for easy setup)
5.  :doc:`plugins/configure/vpn </development/backend/legacy>`, configure :code:`vpn` event, vpn type services are being configured here (e.g. IPsec, OpenVPN)
6.  :doc:`plugins/configure/bootup </development/backend/legacy>`, configure :code:`bootup` event, normal legacy service configuration, when not using the rc(8) system (for example: unbound, ntpd)
7.  :doc:`syshook/start </development/backend/autorun>`, simple shell scripts to run after all networking has been setup.
8.  :doc:`rc(8) </development/backend/autorun>`, regular `rc(8)` scripts (executed using the above :code:`the rc.syshook.d/start``)


.. Tip::

    Use :code:`pluginctl -c` to display available events and the plugins attached to them.


....................................
Normal operation
....................................

Now the system is booted and events may take place, some of the common integration points with their purpose are listed below:

*   :doc:`syshook/carp </development/backend/autorun>`, when a high-availability node changes roles from/to master or backup, these scripts
    are being executed. This offers the ability to prevent client services from connecting when in the wrong mode.
*   :doc:`plugins/configure/newwanip </development/backend/legacy>` will be triggered after an interface retrieves a new address.
*   :doc:`plugins/interface </development/backend/legacy>`  handles dynamic registration of new (virtual) interfaces.
*   :doc:`plugins/syslog </development/backend/legacy>` registers syslog facilities
*   :doc:`plugins/xmlrpc </development/backend/legacy>` registers configuration synchronisation points.

....................................
Shutdown (reboot)
....................................

When the system is shutdown or being rebooted, we can hook actions using the  :doc:`syshook/stop </development/backend/autorun>`
script directory. Services like the backup hook into this to flush contents before being terminated.
