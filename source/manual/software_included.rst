=======================
Included software
=======================

OPNsense® comes with a lot of features included in the base system, for some situations you may need additional software, which
is either provided via a plugin or only as a binary package (without user interface).

This chapter aims to provide some details on the components included in the system, where to find them and how to
install them when not installed by default.


The operating system
....................................

The basic ( `FreeBSD <https://www.freebsd.org/>`__) system contains a kernel and a base package, which provide the
bare essentials for the system to be able to boot and do its work.

Both components are updated using :code:`opnsense-update`, which is explained in more detail
`here <https://docs.opnsense.org/manual/opnsense_tools.html#opnsense-update>`__.


Plugins
....................................

Plugins are packages offered by OPNsense®, which can be installed directly via the user interface and often come
with setup options accessible for the end-user.

Since OPNsense® is a community driven project, the amount of (community/commercial) support available on these plugins
can be different.

.. Note::

    The plugin repository is maintained by the project, when plugins are not kept up to date by its maintainer, they will
    be removed at some point in time.
    (a good example for such a plugin would be if one requires python 2 and we stop shipping it due to upstream deprecation)


Packages (pkg)
....................................

Binary software is installed using pkg, which uses our software repository (available via multiple mirrors).
All installed software can be found via the user interface :menuselection:`System -> Firmware ->Packages`, but in some situations
people want to install additional software via the command line of the machine itself.

To find a full list of all software available, you can use the following command:

.. code-block:: sh

    pkg rquery '%n (%v)'


If, for example you would like to install the gnu `nano <https://www.nano-editor.org/>`__ editor, you can do so using the following command:

.. code-block:: sh

    pkg install nano


.. Note::

    OPNsense® is a firewall distribution, we aim to keep our footprint as small as possible. This means that we don't build
    all the software available in the world. If you need a specific package for your use-case, you could always ask via
    a support ticket on `GitHub <https://github.com/opnsense/tools/issues>`__, but note that packages not used by our core system or
    a supported plugin would not be guaranteed in the future (build contents may change over time).


.. Warning::

    Adding (FreeBSD, ..)  repositories in :code:`/usr/local/etc/pkg/repos/` manually is not supported and usually lead to unexpected
    issues. Before reporting any type of issue with such setups, we kindly ask you to revert to a standard setup first.

The ports tree
....................................

In case your using software, which is not supplied by us, you can always build these packages yourself.
It's best to use our build system to facilitate this, you can do so using the following commands

.. code-block:: sh

    opnsense-code src ports tools
    cd /usr/ports/your/port
    make install


To update a package, the following command can be used instead:

.. code-block:: sh

    opnsense-code src ports tools
    cd /usr/ports/your/port
    make reinstall


.. Note::

    There are a lot of resources available about building ports packages, such as `https://www.freebsd.org/ports/ <https://www.freebsd.org/ports/>`__ and
    the pointers in our documentation and tools.
    We consider building custom software a feature not usable for beginners, before creating support tickets, make sure you have
    the necessary skillsets needed to perform such tasks.
