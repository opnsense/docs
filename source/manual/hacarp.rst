=====================================
High Availability & Hardware Failover
=====================================
OPNsense utilizes the Common Address Redundancy Protocol or CARP for hardware
failover. Two or more firewalls can be configured as a failover group. If one
interface fails  on the primary or the primary goes offline entirely, the
secondary becomes active.

Utilizing this powerful feature of OPNsense creates a fully redundant firewall
with automatic and seamless fail-over. While switching to the backup network
connections will stay active with minimal interruption for the users.

.. image:: images/light_bulbs.png
    :width: 100%

------------------
Automatic failover
------------------

If the primary firewall becomes unavailable, the secondary firewall will take
over without user intervention and minimal interruption.

-------------------------
Synchronized state tables
-------------------------

The firewall’s state table is replicated to all failover configured firewalls.
This means the existing connections will be maintained in case of a failure,
which is important to prevent network disruptions.

-----------------------------
Configuration synchronization
-----------------------------

OPNsense includes configuration synchronization capabilities. Configuration
changes made on the primary system are  automatically synchronized to the
secondary firewall.

-----------------
Configure HA CARP
-----------------

For detailed setup guide see: :doc:`/manual/how-tos/carp`
