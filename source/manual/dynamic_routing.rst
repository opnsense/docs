===============
Dynamic Routing
===============

.. Warning::
    Disabling a running routing daemon can be dangerous as it can lead to an inaccessible machine.
    If you want to disable a running routing daemon, make sure, you don't lose routes which are
    required by your connection to this machine (for example when using SSH)

Dynamic Routing (using routing protocos) is supported via an external plugin. Routing protocols are used to make your network equipment find the best path where your packets should be sent to.

Routing protocols are used to

* improve fault tolerance (if a connection breaks, a new route will be found if possible)
* simplify administration (You have to add less routes manually)

You should not use routing protocols if

* your network is small (so it would be better to use static routes)
* you are working in a highly isolated environment, where you have to be in control of everything happening in your network

Routing Protocols supported by the plugin include:

* OSPFv2 and v3
* RIPv1 and RIPv2
* BGPv4

.. Warning::
    Not all routing protocols will work in any setup because they may have to be direct neighbors.
    Consider the limitations of a routing protocol before using it.

------------
Installation
------------

First of all, select Plugins in the menu:

.. image:: images/menu_plugins.png

On this page, you can install the quagga plugin by clicking the `+` icon:

.. image:: images/plugins_quagga.png


-------------
Configuration
-------------

* :doc:`how-tos/dynamicrouting_zebra`
* :doc:`how-tos/dynamicrouting_ospf`
* :doc:`how-tos/dynamicrouting_rip`


------
How To
------

* :doc:`how-tos/dynamicrouting_howto`

