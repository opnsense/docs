===============
Using configd
===============

-------
General
-------

To add new services and system calls, which can be used from the frontend system or command line, you can create configd actions.

All available templates should be installed at the following location on
the OPNsense system:

::

    /usr/local/opnsense/service/conf/actions.d/


*Please note that all actions which should be accessible from the frontend should have a registered configd action, if possible use standard rc(8) scripts for service start/stop.*

-----------------
Naming convention
-----------------

Service templates should use distinctive names to identify your service and contain simple / clear actions.

For example, we will describe the template for ssh, which is installed by default.

**File name:**


::

    /usr/local/opnsense/service/conf/actions.d/actions_sshd.conf

Our ssh service has two actions available:

- restart
    - starts / restarts ssh service
- stop
    - stops / kills all ssh daemons


::

    [restart]
    command:/usr/local/etc/rc.sshd
    parameters:
    type:script
    message:starting sshd

    [stop]
    command:/bin/pkill -TERM sshd; exit 0
    parameters:
    type:script
    message:stop sshd


Between brackets [] you find the name of the action, the definition of the actual call is defined in the following parameter:value pairs.
When a service or module provides a lot of actions, it sometimes is practical to add another level of operation.

For example, the restart service call for this service will translate to: **sshd restart**

In case we have an action like **filter diag info**, you can create an actions_filter.conf which contains a section [diag.info].

-----------------
Action properties
-----------------


+-----------------------+------------------------+--------------------------------------------------------+
| Property              | Syntax                 | Description                                            |
+=======================+========================+========================================================+
| command               | text                   | shell command string to execute                        |
+-----------------------+------------------------+--------------------------------------------------------+
| parameters            | %s for every parameter | list of parameters to use, example : /i %s             |
+-----------------------+------------------------+--------------------------------------------------------+
| type                  | script|script_output   |  type of call:                                         |
|                       |                        |    - script (only return exit status)                  |
|                       |                        |    - script_output (return result)                     |
+-----------------------+------------------------+--------------------------------------------------------+
| message               | text                   | Message to send to syslog (you can use %s parameters)  |
+-----------------------+------------------------+--------------------------------------------------------+
| description           | text                   | User-friendly description, also allows GUI usage       |
+-----------------------+------------------------+--------------------------------------------------------+


-----------
Test action
-----------

To test a new configd action, please restart the configd service first using:

::

    service configd restart

Next use the supplied helper command to execute our action:

::

    configctl sshd restart
