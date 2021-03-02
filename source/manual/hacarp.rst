=====================================
High Availability
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


-----------------------------
Workflow
-----------------------------

Although its not required to synchronize the configuration from the master machine to the backup, a lot of people
would like to keep both systems (partially) the same.

To prevent issues spreading over both machines at the same time, we choose to only update on command (see the status page).

Our workflow looks like this:

.. blockdiag::
   :desctable:

   blockdiag {
      update1 [label="Master\nUpdate 1"];
      update2 [label="Master\nUpdate 2"];
      updaten [label="Master\nUpdate N"];
      sync [label="Synchronize\nBackup"];
      update1 -> update2 ;
      update2 -> updaten [label=".."];
      updaten -> sync;
   }

First commit all changes to the master, then update the backup while knowing the master is still properly configured.

.. Note::

    In case of an emergency, you should still be able to switch to the backup node when changes cause issues, since
    the backup machine is left in a known good state during the whole process.


-----------------------------
Automatic replication
-----------------------------

Although we advise to make sure to keep the backup machine intact during maintenance, some people prefer to keep
the backup in sync on periodic intervals. For this reason we added a cron action which you can schedule yourself
in :menuselection:`System -> Settings -> Cron` on the primary node.

To use this feature, add a new cron job containing the :code:`HA update and reconfigure backup` command and a
proper schedule, once a day outside office hours is usually a safe option.

.. Note::

    To prevent a non functional primary machine updating the active master, the :code:`HA update and reconfigure backup`
    will only execute if all carp interfaces are in :code:`MASTER` mode.


-----------------------------
Settings
-----------------------------

............................
Automatic failover
............................

If the primary firewall becomes unavailable, the secondary firewall will take
over without user intervention and minimal interruption.

Virtual IPs of the type CARP (:doc:`/manual/firewall_vip`) are required for this feature.


............................
Synchronized state tables
............................

The firewall’s state table is replicated to all failover configured firewalls.
This means the existing connections will be maintained in case of a failure,
which is important to prevent network disruptions.

.................................
Configuration synchronization
.................................

OPNsense includes configuration synchronization capabilities. Configuration
changes made on the primary system are synchronized on demand to the secondary firewall.


............................
Configure HA CARP
............................

For detailed setup guide see: :doc:`/manual/how-tos/carp`


-----------------------------
Status
-----------------------------

The status page connects to the backup host configured earlier and show all services running on the backup server.
With this page you can update the backup machine and restart services if needed.


.. Tip::

    .. raw:: html

         Use the refresh <i class="fa fa-refresh fa-fw"></i> button to update the backup node and restart all services at once.
