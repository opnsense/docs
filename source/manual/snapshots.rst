=========
Snapshots
=========

.. contents:: Index

--------------
Quick Overview
--------------
*Snapshots* capture the base system at a given moment. They're useful for administration, as they introduce a fallback boot option when more risky operations like major upgrades or experimental configurations fail. If something goes wrong, it is quite simple to roll back to the previous working state.

These *Snapshots* leverage ZFS features, making them space-efficient and easy to manage. During the boot process, the latest and previous saved *Snapshots* can be chosen with *Option 8*, effectively switching between different system states.

.. Attention:: **Snapshots require ZFS as filesystem**. UFS will not work since it does not support file system level snapshots.

The *Snapshots* are differential. A new *Snapshot* is always the latest current running state. This means, there are no incremental *Snapshot* chains, as seen in other implementations such as Hypervisors.

.. Note:: Each Snapshot can be created and deleted as its own self contained entity with no other dependencies. For practical reasons, it is recommended to keep no more than two *Snapshots*. Snapshots can use a considerable amount of space if they are not cleaned up after use.

.. _snapshot-recommended-workflow:


--------------------
Recommended Workflow
--------------------

#. Create a new Snapshot
#. Activate the new Snapshot
#. Do administrative changes (e.g. firmware upgrade)
#. Reboot and test the changes:

* OPNsense works as expected: 
    * Remove the old *default* Snapshot
    * Rename the current active Snapshot to *default*
* OPNsense has issues: 
    * Select the old *default* Snapshot in the Boot Menu
    * After booting, delete the known faulty Snapshot

.. Tip:: This workflow ensures that the *default Snapshot* is always the *last known good state*.


--------
Tutorial
--------

As an example, there is a major upgrade to a new OPNsense version. To have the option of a quick rollback when things do not turn out as expected, creating a *Snapshot* before doing the changes is the best choice.

.. Note:: This is useful for *Hardware Appliances*. A virtualized OPNsense will have other recovery options that leverage the features of the Hypervisor itself, like creating VM level snapshots.

Snapshots can have the following states:

=========== ========================================================
Active      Description
=========== ========================================================
**N**       *Snapshot* is active right now
**R**       *Snapshot* will be active after reboot
**NR**      *Snapshot* is active and will be used on reboots
**-**       *Snapshot* is not active
=========== ========================================================

.. _snapshot-creating:


*******************
Creating a Snapshot
*******************

* | Go to :menuselection:`System --> Snapshots`
* | Select **+** to create a new *Snapshot*, use the default name
* | Activate the new *Snapshot* by clicking **✓** next to it
* | The OPNsense will write all future changes to the new Snapshot, marked as **Active R**


At this point, upgrade the OPNsense to a new version. These changes will all happen in the new Snapshot, leaving the *default* Snapshot as *last known good state*.


******************
Booting a Snapshot
******************

If the upgrade introduced some issues, the *default Snapshot* can be booted from the *OPNsense Boot Menu*.

.. Note:: If the Hardware Appliance does not have *VGA*, using *Serial* is the best choice to expose the *Boot Menu*.

* | Boot the OPNsense, at the start of the boot sequence the *Boot Menu* will show up
* | Press the *Space Bar* to pause it
* | Press ``8`` to choose ``8. Boot Environments`` which displays the current *Snapshots*
* | Press ``2`` to select a different *active Snapshot*, it should now display ``zfs:zroot/ROOT/default``
* | Press ``1`` to go back to the *main menu*
* | Press ``ENTER`` to select ``1. Boot Multi user [ENTER]``

.. Tip:: If there are more Snapshots, press ``2`` repeatedly to cycle through them.


*******************
Deleting a Snapshot
*******************

Now that the OPNsense has booted to its *last known good state* with the *default Snapshot*, it is time to clean up the *faulty Snapshot*.

* | Go to :menuselection:`System --> Snapshots`
* | Check that the *default Snapshot* is *Active N*
* | Press **✓** next to the *default Snapshot* so it is marked as *Active NR*
* | Press **🗑** next to the Snapshot that is currently *Active -*
* | At this point, the OPNsense is correctly configured back to the old *default* Snapshot state, marked as **Active NR**

.. Note:: :ref:`Creating a Snapshot <snapshot-creating>` can be repeated to retry the major upgrade. For other scenarios, refer to the :ref:`Recommended Workflow <snapshot-recommended-workflow>` for a quick overview.
