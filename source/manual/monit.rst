=====
Monit
=====

OPNsense uses Monit for monitoring services. Monit has quite extensive monitoring capatibilities, which is why the
configuration options are extensive as well. This guide will do a quick walk through the setup, with the
configuration options explained in more detail afterwards, along with some caveats.

------------
Global setup
------------

Navigate to **Services->Monit->Settings**. On the “General Settings” tab, turn on Monit and fill in the details of your SMTP server. Save the changes.
Then, navigate to the “Alert settings” and add one for your e-mail address. If your mail server requires the “From” field
to be properly set, enter ``From: sender@example.com`` in the “Mail format” field. Save the alert and apply the changes.

---------------
Adding an alert
---------------

First, you have to decide what you want to monitor and what constitutes a failure. It helps if you have some knowledge
about how Monit alerts are set up. This is described in the
`Monit documentation <https://mmonit.com/monit/documentation/monit.html#ALERT-MESSAGES>`_.

If you have done that, you have to add the condition first. Navigate to the 'Service Test Settings' tab and look if the
condition you want to add already exists. If it doesn't, click the + button to add it.

Now navigate to the 'Service Test' tab and click the + icon. In the dialog, you can now add your service test. If you're done,
save it, then apply the changes.

The fields in the dialogs are described in more detail below.

-----------------
Settings overview
-----------------

Navigate to **Services->Monit->Settings**. You will see four tabs, which we will describe in more detail below

^^^^^^^^^^^^^^^^
General Settings
^^^^^^^^^^^^^^^^

Click 'advanced mode' to see all the settings.

+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Setting                       | Description                                                                                                           |
+===============================+=======================================================================================================================+
| Enable Monit                  | Turns Monit on or off.                                                                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Polling interval              | How often Monit checks the status of the components it monitors.                                                      |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Start delay                   | How long Monit waits before checking components when it starts.                                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Mail Server                   | A list of mail servers to send notifications to (also see below this table).                                          |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Mail Server Port              | The mail server port to use. 25 and 465 are common examples.                                                          |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Username                      | The username used to log into your SMTP server, if needed. Often, but not always, the same as your e-mail address.    |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Password                      | The password used to log into your SMTP server, if needed.                                                            |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Secure Connection             | Use TLS when connecting to the mail server.                                                                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| SSL Version                   | The TLS version to use. AUTO will try to negotiate a working version.                                                 |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Verify SSL Certificates       | Checks the TLS certificate for validity. If you use a self-signed certificate, turn this option off.                  |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Log File                      | The log file of the Monit process. This can be the keyword syslog or a path to a file.                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| State File                    | The state file of the Monit process.                                                                                  |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Eventqueue Path               | The path to the eventqueue directory.                                                                                 |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Eventqueue Slots              | The number of eventqueue slots.                                                                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Enable HTTPD                  | Turns on the Monit web interface. (Required to see options below.)                                                    |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Monit HTTPD Port              | The listen port of the Monit web interface service.                                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Monit HTTPD Access List       | The username:password or host/network etc. for accessing the Monit web interface service.                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| M/Monit URL                   | The M/Monit URL, e.g. https://user:pass@192.168.1.10:8443/collector                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| M/Monit Timeout               | When doing requests to M/Monit, time out after this amount of seconds.                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| M/Monit Register Credentials  | Automatically register in M/Monit by sending Monit credentials (see Monit Access List above).                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+

In the “Mail Server” settings, you can specify multiple servers. Monit will try the mail servers in order,
starting with the first, advancing to the second if the first server does not work, etc.
If no server works Monit will not attempt to send the e-mail again.

**Two things to keep in mind**:
the authentication settings are shared between all the servers, and the 'From:' address is set in the “Alert Settings”.

Authentication options for the Monit web interface are described in
https://mmonit.com/monit/documentation/monit.html#Authentication.

M/Monit is a commercial service to collect data from several Monit instances. To use it from OPNsense, fill in the
appropriate fields and add corresponding firewall rules as well.

^^^^^^^^^^^^^^
Alert Settings
^^^^^^^^^^^^^^

This lists the e-mail addresses to report to. Click the Edit icon of a pre-existing entry or the Add icon
(a plus sign in the lower right corner) to see the options listed below.

+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Setting                       | Description                                                                                                                            |
+===============================+========================================================================================================================================+
| Enable alert                  | Turns this alert on or off.                                                                                                            |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Recipient                     | The e-mail address to send this e-mail to.                                                                                             |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Not on                        | When off, notifications will be sent for events specified below. When on, notifications will be sent for events *not* specified below. |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Events                        | Events that trigger this notification (or that don't, if "Not on" is selected).                                                        |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Mail format                   | Can be used to control the mail formatting and from address. See below this table.                                                     |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Reminder                      | Send a reminder if the problem still persists after this amount of checks.                                                             |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Description                   | A description for this rule, in order to easily find it in the Alert Settings list.                                                    |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

“Mail format” is a newline-separated list of properties to control the mail formatting. It is also needed to correctly
set the From address. For example::

    From: sender@example.com
    Reply-To: support@example.com
    Subject: $SERVICE at $HOST failed


^^^^^^^^^^^^^^^^
Service Settings
^^^^^^^^^^^^^^^^

This lists the services that are set. There are some services precreated, but you add as many as you like. Click the Edit
icon of a pre-existing entry or the Add icon (a plus sign in the lower right corner) to see the options listed below.

+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Setting                       | Description                                                                                                                             |
+===============================+=========================================================================================================================================+
| Enable service checks         | Turns this service on or off.                                                                                                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Name                          | A name for this service, consisting of only letters, digits and underscore. More descriptive names can be set in the Description field. |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Type                          | The kind of object to check. 'Custom' allows you to use custom scripts.                                                                 |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Path                          | The path to the directory, file, or script, where applicable.                                                                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Program Timeout               | How often to run this check.                                                                                                            |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Start                         | The start script of the service, if applicable.                                                                                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Stop                          | The stop script of the service, if applicable.                                                                                          |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Tests                         | The condition to test on to determine if an alert needs to get sent. These conditions are created on the Service Test Settings tab.     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Description                   | A description for this service, in order to easily find it in the Service Settings list.                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

^^^^^^^^^^^^^^^^^^^^^
Service Test Settings
^^^^^^^^^^^^^^^^^^^^^

+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                       | Description                                                                                                                                       |
+===============================+===================================================================================================================================================+
| Name                          | The name of the test.                                                                                                                             |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Condition                     | A condition that adheres to the Monit syntax, see `the Monit documentation <https://mmonit.com/monit/documentation/monit.html#SERVICE-TESTS>`_    |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Action                        | What to do when the condition gets hit.                                                                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

There are some precreated service tests. Most of these are typically used for one scenario, like the
'Memory usage > 75%' test. Some, however, are more generic and can be used to test output of your own scripts.
These include:

+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Service Test                  | Description                                                                                                                             |
+===============================+=========================================================================================================================================+
| NonZeroStatus                 | The returned status code is not 0. (Scripts typically exit with 0 if there were no problems, and with non-zero if there were.)          |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ChangedStatus                 | The returned status code has changed since the last it the script was run.                                                              |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

------
Status
------

The Monit status panel can be accessed via **Services->Monit->Status**. For every active service, it will show the status,
along with extra information if the service provides it.