========================
CARP status
========================

---------------------
General
---------------------

The CARP (Common Address Redundancy Protocol) protocol is quite a powerful feature of the firewall, which
allows multiple machines to share IPv4 / IPv6 addresses among each other.

To determine if a host should be master, it listens on the network for carp broadcast packets and determines
if its priority is higher than the others on the network (the highest advertising frequency wins).

A higher advskew (Advertising Frequency Skew) will lower its advertisements and renders the node less attractive of
being a master.

Combined with the :code:`advskew` value, the system also uses the current demotion value (:code:`sysctl net.inet.carp.demotion`)
which will be added to its preset :code:`advskew` in the gui. This value informs the user about the health of the node.
When its value is :code:`0`, all is ok, when some cable is unplugged it will for example add a value to the "demotion counter".

The following demotion events are available by default in the kernel.

* Interface down (net.inet.carp.ifdown_demotion_factor)
* Error sending announcements (net.inet.carp.senderr_demotion_factor)
* Busy processing pfsync updates (net.pfsync.carp_demotion_factor)


------------------------
Custom service hooks
------------------------

In some cases the status of the node should be influenced by the services on the machine, for example when a
dynamic routing system isn't initialized yet, it might be better to wait before propagating as being a better alternative
in the cluster.

This mechanism should be comparable to what is available for pfsync (
when states are being synced, we propagate with a higher :code:`advskew`
using the value in :code:`net.pfsync.carp_demotion_factor`)

The idea of the service status hook is to register service check scripts into a single directory and validate
status as a whole (if any of the test scripts fail, we add a demotion factor for "services").

.. Note::

    Some inspiration for this hook came from how OpenBSD handles demotion in ospfd (https://man.openbsd.org/ospfd.conf.5 --> demote)

To create new tests, just add executable scripts in the following directory, which exits :code:`0` if all is good and
something other than 0 on issues (e.g. :code:`exit 1`).


::

    /usr/local/etc/rc.carp_service_status.d/<service_test>


.. Tip::

    Make sure test scripts are as lightweight as possible, so it wouldn't mind of they run more often than strictly
    needed.


.. Note::

    We use a high demotion value (:math:`2^{20}`) when one of the services fails its test, so we don't need to remember our current state
    (reading :code:`sysctl net.inet.carp.demotion` would be enough) and can use a bitwise :code:`and` to check if it's set.


A simple test which always reports service as being down, can be as simple as the following:

.. code-block:: csh
    :caption: /usr/local/etc/rc.carp_service_status.d/test_service

    #!/bin/sh

    exit 1


.........................
Trigger event
.........................

To ask the system to evaluate status again, we should call the :code:`carp_service_status` script,
using configd so we don't need to be root to trigger a test.

::

    configctl interface update carp service_status

.. Note::

    Services using this facility should emit this event themself after normal operation has proceeded.

.........................
Logging
.........................

Carp status changes are usually logged to syslog (:menuselection:`System --> Log Files --> General`), so does our carp
service status check.

When the test service example is installed, we would expect a log line which looks like the following after triggering an event:

::

    ....  OPNsense carp: carp demoted by 1048576 due to service disruption (services: test_service)

This informs the user about the amount of demotion and which services are responsible for it.

When service status is recovered again, it will send something like the following to syslog.

::

    ..... carp promoted by 1048576 due to service recovery
