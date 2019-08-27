==================================
Gateway groups / Multi WAN
==================================
Multi WAN scenarios are commonly used for failover or load balancing, but combinations
are also possible with OPNsense.

.. blockdiag::
   :desctable:

   blockdiag {
      WAN_primary -- OPNsense;
      OPNsense -- WAN_backup;
      internet -- WAN_primary;
      WAN_backup -- internet;
      internet [shape="cloud"];
      WAN_primary [shape="cisco.modem",label=""];
      WAN_backup [shape="cisco.modem",label=""];

   }

------------
WAN Failover
------------
WAN failover automatically switches between WAN connections in case of connectivity
loss (or high latency) of your primary ISP. As long as the connection is not good
all traffic will be routed of the next available ISP/WAN connection and when
connectivity is fully restored so will the routing switch back to the primary ISP.


------------------
WAN Load Balancing
------------------
Load balancing can be used to split the load between two (or more) ISPs. This
enhances the total available bandwidth and/or lowers the load on each ISP.

The principle is simple: Each WAN connection (gateway) gets a portion of the traffic.
The traffic can be divided equally or weighted.

------------------------------
Combining Balancing & Failover
------------------------------
It is also possible to combine Load Balancing with Failover in such scenarios
you will have 2 or more WAN connections for Balancing purposes and 1 or more for
Failover. OPNsense offers 5 tiers (Failover groups) each tier can hold multiple
ISPs/WAN gateways.

-------------
Configuration
-------------
For a how to configure read:

.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/multiwan
