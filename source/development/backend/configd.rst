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
|                       |                        |    - stream_output (return result in streaming mode)   |
+-----------------------+------------------------+--------------------------------------------------------+
| errors                | text [no]              | :code:`errors:no` ignores the scripts exit code        |
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


-----------------------------
Extending the Environment
-----------------------------

Configd's own configuration can be found in the `configd.conf <https://github.com/opnsense/core/blob/master/src/opnsense/service/conf/configd.conf>`__ file.
In some cases it can be practical to extend the envrionment with additional settings for the configd actions to use.

To add environment variables, create a new config file in the :code:`conf/configd.conf.d/` directory
using the :code:`.conf` extension containing an :code:`[environment]` section.
For example, to add a proxy server (for the firmware updater), use settings like these:

.. code-block::
    :caption: /usr/local/opnsense/service/conf/configd.conf.d/proxy.conf

    [environment]
    HTTP_PROXY=http://proxy-adddress:8080
    HTTPS_PROXY=http://proxy-adddress:8080



.. Note::

    After changing the configd configuration, don't forget to restart the configd service via the gui or `service configd restart` (as root).

.. Warning::

    When using the same settings as already specified in the base configuration, these settings will be overwritten. The parsing order
    of configuration files is to read all vendor shipped properties first and read additional files next. Last property found is the one
    being used (e.g. specifying a new :code:`PATH` in the environment, will overwrite the one being shipped in our :code:`configd.conf`.)

