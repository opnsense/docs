====================================
Troubleshooting
====================================

.. image:: /troubleshooting/images/ask-blackboard-356079.jpg


Sometimes, even with all the hard work done to prepare your setup, issues occur.
Generally it's always good to check your logs (:menuselection:`System --> Log Files` or the ones found in the module your trying to setup),
but sometimes more help is needed.


General issue workflow
...........................

Before reporting issues, please make sure yours still exists on the latest version.
We generally advice to check the existing `issues <https://github.com/opnsense/core/issues>`__ and our `forum <https://forum.opnsense.org/>`__
before reporting new ones.

In case your issue was introduced after a (minor) upgrade, you can use `opnsense-revert <https://docs.opnsense.org/manual/opnsense_tools.html#opnsense-revert>`__
to downgrade specific packages installed on the system.

Using the firmware section (:menuselection:`System --> Firmware --> Status`) you can perform a health check on the system, on
the bottom of the status overview is a button named **Run an audit** which can be expanded to offer the **Health** selection.

When clicked this outputs something like the following:

.. code-block:: text

    ***GOT REQUEST TO AUDIT HEALTH***
    >>> Check installed kernel version
    Version 19.7.3 is correct.
    >>> Check for missing or altered kernel files
    No problems detected.
    >>> Check installed base version
    Version 19.7.3 is correct.
    >>> Check for missing or altered base files
    No problems detected.
    >>> Check for and install missing package dependencies
    Checking all packages: .......... done
    >>> Check for missing or altered package files
    Checking all packages: ....
    opnsense-19.7.4_1: checksum mismatch for /usr/local/etc/inc/auth.inc
    Checking all packages...
    Checking all packages......... done
    ***DONE***

When mismatches are reported, you can reinstall affected packages in the **Packages** section of the firmware screen.
In the case above you would reinstall opnsense, since the :code:`auth.inc` looks tainted.

.. Note::

    We advise to include the output of the health check if it seems to report issues when creating bug reports on GitHub.


.. Tip::

    Always try to be precise in issue reports, either if their about a possible bug or a feature request, it helps if
    intentions are absolutely clear. Our GitHub repositories use templates which should guide you through, we kindly
    ask you to use them (tickets not using our templates are treated as low priority).


Topics
...........................

Some of the common mistakes we have seen over the years, combined with pointers where to look for solutions can
be found in the list below.

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   troubleshooting/password_reset
   troubleshooting/webgui
   troubleshooting/boot
   troubleshooting/hardening
   troubleshooting/gateways
   troubleshooting/network
   troubleshooting/openvpn
   troubleshooting/performance
