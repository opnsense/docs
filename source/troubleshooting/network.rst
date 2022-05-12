====================================
Network
====================================


---------------------------------
Netmap (IPS, Sensei, ...)
---------------------------------

**General**

Netmap is a technology which enables fast packet processing while minimizing overhead, there are however some pitfalls
which may turn your network interface unreachable.

Before using this technology, always make sure you have access via another interface (or console) to your firewall
in case connectivity is dropped.

In order for netmap to function properly it is imperative that all sorts of driver / hardware  acceleration is disabled
(:menuselection:`Interfaces -> Settings`), this include :code:`VLAN Hardware Filtering` as well (which wasn't disabled pre 20.7).

Some drivers have may have additional tunables, which enable hardware acceleration, make sure to disable them as well
(.e.g intel ixl has :code:`hw.ixl.enable_head_writeback`, which we disable by default)

Below you will find a list of tunables which are know to be (partial) incompatible with netmap.

=========================================== =================================================================================
Tunable                                     Description
=========================================== =================================================================================
hw.ixl.enable_head_writeback                Intel :code:`ixl(4)` tunable for increased tx performance,
                                            OPNsense standard value is disabled.
dev.ax.<interface number>.sph_enable        AMD tunable to split header and payload into a separate buffer respectively,
                                            Netmap requires a uniform view of a packet. Disabled by default
                                            on OPNsense.
=========================================== =================================================================================

**Decoupling Netmap from an application**

It can be useful to split the functionality of Netmap and the application using it in order to determine whether it's
Netmap or the application at fault for connectivity issues. To aid in this, Netmap's :code:`bridge` utility has been
added to our pkg repository for easy installation and use. To avoid ambiguity, it has been renamed to :code:`netmap-bridge`.

You can install it by running :code:`pkg install netmap-bridge` (:code:`man netmap-bridge`).

:code:`netmap-bridge` provides a L2 software bridge between two interfaces, but can also be used to bridge an interface
and the host network stack like Suricata does. To replicate the behaviour of Suricata without actually running Suricata, run
:code:`netmap-bridge -i netmap:igb1`. Replace the interface as appropriate. While it is running, pass traffic as normal to 
determine if an original issue persists.

.. _errno:

---------------------------------
Common error codes
---------------------------------

Any piece of software that uses system calls to communicate over sockets use the standard interface 
`errno.h <https://github.com/opnsense/src/blob/master/sys/sys/errno.h>`__ (:code:`man errno`). If an error
is logged, a return code is associated to a specific reason of failure. Some common ones are explained below:

======  ==================== =================================================================================
XX      Name                 Description
======  ==================== =================================================================================
55      ENOBUFS              No buffer space available. An operation on a socket or pipe was not performed
                             because the system lacked sufficient buffer space or because a queue was full.
                             **Check connectivity from the machine itself using** :code:`ping`, most common
                             mistakes are misconfigured routes, interface issues (disconnected) and
                             policy based routing issues forcing traffic to the wrong target
                             (using :code:`reply-to`)
64      EHOSTDOWN            Host is down. A socket operation failed because the destination host was down.
                             **Expecting an (layer 2) ARP response but none was returned, often misconfigured
                             subnets or hosts are actually not accessible over L2**
65      EHOSTUNREACH         No route to host. A socket operation was attempted to an unreachable host
                             **The routing table is a good place to look**
                             (:menuselection:`System --> Routes --> Status`)
======  ==================== =================================================================================
