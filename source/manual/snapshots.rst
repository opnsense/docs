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

.. Note:: Each *Snapshot* can be created and deleted as its own self contained entity with no other dependencies. The size of each *Snapshot* will grow over time as the distance in bytes between the current *active Snapshot* and all stored *non-active Snapshots* grow.

.. _snapshot-recommended-workflow:


--------------------
Recommended Workflow
--------------------

#. Create a new Snapshot with the name ``known-good``
#. Do administrative changes (e.g. firmware upgrade)
#. Reboot and test the changes:

* OPNsense works as expected: 
    * Remove the **known-good** *Snapshot* and keep using the **default** *Snapshot*
* OPNsense has issues: 
    * Activate the **known-good** *Snapshot* either in the WebGUI or the Boot Menu
    * After rebooting, remove the bad **default** *Snapshot*
    * Rename the **known-good** *Snapshot* back to **default**

.. Tip:: *Snapshots* can also be used to safeguard against regressions introduced in configuration changes. Creating a new snapshot and activating it immediately, will make the system roll back automatically to the *last known good configuration* on reboot or power cycle.


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
* | Select **+** to create a new *Snapshot*, use ``known-good`` as name

At this point, upgrade the OPNsense to a new version. These changes will all happen in the current active **default** Snapshot, leaving the **known-good** Snapshot as *last known good configuration*.


******************
Booting a Snapshot
******************

If the upgrade introduced some issues, the **known-good** *Snapshot* can be activated from the WebGUI.

* If the WebGUI is available:

    * | Go to :menuselection:`System --> Snapshots`
    * | Select **✓** to activate the **known-good** *Snapshot*
    * | Reboot the OPNsense to roll back to the **known-good** *Snapshot*

.. Note:: In some cases, if the OPNsense does not boot to the WebGUI due to a software error, the *Boot Menu* can be used to roll back. If a *Hardware Appliance* does not have VGA, using the serial console is the best alternative.

* If the WebGUI is unavailable:

    * | Boot the OPNsense, at the start of the boot sequence the *Boot Menu* will show up
    * | Press the *Space Bar* to pause it
    * | Press ``8`` to choose ``8. Boot Environments`` which displays the current *Snapshots*
    * | Press ``2`` to select a different *active Snapshot*, it should now display ``zfs:zroot/ROOT/known-good``
    * | Press ``1`` to go back to the *main menu*
    * | Press ``ENTER`` to select ``1. Boot Multi user [ENTER]``

.. Tip:: If there are more Snapshots, press ``2`` repeatedly to cycle through them.


*******************
Deleting a Snapshot
*******************

Now that the OPNsense has booted either the **known-good** *Snapshot* or the **default** *Snapshot*, it is time to clean up to ensure a clear current system state.

* If the upgrade succeeded and **default** has been booted:

    * | Go to :menuselection:`System --> Snapshots`
    * | Check that the **default** *Snapshot* is *Active NR*
    * | Press **🗑** to delete the **known-good** *Snapshot*

* If the upgrade failed and **known-good** has been booted:

    * | Go to :menuselection:`System --> Snapshots`
    * | Check that the **known-good** *Snapshot* is *Active NR*
    * | Press **🗑** to delete the **default** *Snapshot*
    * | Press **✎** to rename the **known-good** *Snapshot* to **default**

At this point, the OPNsense is correctly configured at the *last known good configuration* state.

.. Tip:: Snapshots can be kept for a while after an upgrade, to have the option to roll back after a few days of testing in production. Please note that all configuration changes in that time will be lost when rolling back, so creating a configuration backup and importing it into the old system state can become a necessity.

.. Note:: :ref:`Creating a Snapshot <snapshot-creating>` can be repeated to retry the major upgrade. Refer to the :ref:`Recommended Workflow <snapshot-recommended-workflow>` for a quick overview.
