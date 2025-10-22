======================================
Scheduled jobs
======================================

Similar to the `cron <https://docs.opnsense.org/manual/settingsmenu.html#cron>`__ service, scheduled jobs can
execute certain predefined commands.
The difference is cron is used for periodic schedules, jobs handles one time planned events.

This feature is practical to plan automatic updates during maintenance slots or to shutdown the system if we know
electrical engineers are going to cut the power at a specific time.

A list of example commands can be found at the cron section of the manual.

======================================== =====================================================================================================
**Fieldname**                            **Purpose**
======================================== =====================================================================================================
Time                                     Date and time the action should be performed
Until (s)                                When scheduled, counts down to the moment of execution
Command                                  Configd command to execute
Parameters                               Optional parameters
Description                              Description to use for the job.
======================================== =====================================================================================================

