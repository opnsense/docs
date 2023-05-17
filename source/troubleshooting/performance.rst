=======================================
Performance
=======================================

Receive-side scaling
--------------------------------------------------



**Introduction**
=====================================================================================================================

RSS is used to distribute packets over CPU cores using a hashing function – either with support in the hardware which offloads the hashing for you, or in software.
The idea is to take as input the TCP 4-tuple (source address, source port, destination address, destination port) of a packet, hash this input using
an in-kernel defined key, and selecting the resulting values’ LSB as an index into a user-configurable indirection table.
The indirection table is loaded into the hardware during boot and is used by the NIC to decide which CPU to interrupt with a given packet.
All of this allows packets of the same origin/destination (a.k.a. flows) to be queued consistently on the same CPU.

.. Note::

    **By default, RSS will be disabled since it’s impact is quite far reaching.**

    Only enable this feature if you’re interested in testing it and seeing if it will increase your
    throughput under high load – such as when using IDS/IPS.

    Since we do not have every type of hardware available – nor the time to test all of them,
    no guarantee is given that a NIC driver will properly handle the kernel
    implementation or is even capable of using it.


The implementation of RSS is coupled with `PCBGROUP <https://www.freebsd.org/cgi/man.cgi?query=PCBGROUP>`__
– an implementation which introduces notions of CPU affinity for connections.
While the latter will be of lesser importance for OPNsense, since it specifically applies to connections
built up in userland using sockets (which is relevant to servers, not middleboxes),
the idea of distributing work on a lower level with hardware support provides a myriad of benefits.


**Network card / driver**
=====================================================================================================================

Assuming you are using a modern NIC which supports multiple hardware queues and RSS, the configuration of a NIC will decide how and on which queue packets
arrive on your system. This is also hardware dependent and will not be the same on every NIC. Should your driver support the option to enable/disable RSS,
a sysctl tunable will be available.

It is possible for a NIC to perform RSS without being able to configure it. Should you wish to know if it can be enabled/disabled:

.. code-block::

    sysctl -a | grep rss

should show any drivers exposing the option via a tunable.

It is also possible that a driver does not expose this ability to the user, in which case you’d want to look up whether the NIC/driver supports RSS at all using online
datasheets or a simple google search. For example, igb enables RSS by default, but does not reflect this in any configuration parameter. However, since it uses multiple queues:

.. code-block::

    # dmesg | grep vectors

    igb0: Using MSI-X interrupts with 5 vectors
    igb1: Using MSI-X interrupts with 5 vectors
    igb2: Using MSI-X interrupts with 5 vectors
    igb3: Using MSI-X interrupts with 5 vectors

It will most likely have some form of packet filtering to distribute packets over the hardware queues. In fact, igb does RSS by default.

For most NICs, RSS is the primary method of deciding which CPU to interrupt with a packet. NICs that do not implement any other type of filter and whose RSS feature
is missing or turned off, will most likely interrupt only CPU 0 at all times – which will reduce potential throughput due to cache line migrations and lock contention.
Please keep system-wide RSS disabled if this is the case.

The last but not least thing to consider is the fact that driver support with the in-kernel implementation of RSS is a must. Proper driver support will ensure the correct key
and indirection table being set in hardware. Drivers which support RSS according to the source code (but mostly untested):

*    em
*    igb -> tested & working
*    axgbe -> tested & working
*    netvsc
*    ixgbe
*    ixl
*    cxgbe
*    lio
*    mlx5
*    sfxge

**Kernel support**
=====================================================================================================================

Internally, FreeBSD uses `netisr <https://www.freebsd.org/cgi/man.cgi?format=html&query=netisr(9)>`__
as an abstraction layer for dispatching packets to the upper protocols.
Within the implementation, the default setting is to restrict packet processing to one thread only.
Since RSS now provides a way to keep flows local to a CPU, the following sysctls should be set in :menuselection:`System->Settings->Tunables`:

* net.isr.bindthreads = 1
* net.isr.maxthreads = -1

The first option causes threads to be bound to a CPU, the next one assigns a workstream to each core available.

Furthermore, the RSS implementation also provides a few necessary sysctls:

* net.inet.rss.enabled = 1

Makes sure RSS is enabled. This is disabled by default to prevent regressions on NICs that do not properly implement the RSS interface.

* net.inet.rss.bits = X

This one is dependent on the amount of cores you have.
By default the amount of bits here represent the amount of cores x 2 in binary.
This is done on purpose to provide load-balancing, though there is no current implementation for this so we
recommend setting this value to the amount of bits representing the number of CPU cores.
This means we use the following values:

- for 4-core systems, use ‘2’
- for 8-core systems, use ‘3’
- for 16-core systems, use ‘4’
- Etc.


.. Note::

    Remember to reboot the machine after changing :code:`net.inet.rss.enabled` as this option can only be set during boot.

**Validate settings**
=====================================================================================================================


If RSS is enabled with the 'enabled' sysctl, the packet dispatching policy will move from ‘direct’ to ‘hybrid’. This will directly dispatch a packet on the current context when allowed,
otherwise it will queue the packet on the bound CPU on which it came in on. Please note that this will increase the interrupt load as seen in ‘top -P’.
This simply means that packets are being processed with the highest priority in the CPU scheduler - it does not mean the CPU is under more load than normal.

The correct working of netisr can be verified by running:

.. code-block::

    netstat -Q

**Note regarding IPS**
=====================================================================================================================

When Suricata is running in IPS mode, Netmap is utilized to fetch packets off the line for inspection. By default, OPNsense has configured Suricata in such a way that the packet which
has passed inspection will be re-injected into the host networking stack for routing/firewalling purposes. The current Suricata/Netmap implementation limits this re-injection to one thread only.
Work is underway to address this issue since the new Netmap API (V14+) is now capable of increasing this thread count. Until then, no benefit is gained from RSS when using IPS.
