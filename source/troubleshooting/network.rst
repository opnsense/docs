====================================
Network
====================================


---------------------------------
netmap (IPS, Sensei, ...)
---------------------------------

Netmap is a technology which enables fast packet processing while minimizing overhead, there are however some pittfals
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

=========================================== =================================================================================
