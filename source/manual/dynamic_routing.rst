======================
Dynamic Routing (FRR)
======================

Dynamic Routing (using routing protocols) is supported via an external plugin.
Routing protocols support your network equipment in finding the best available path for your packets.
We use Free Range Routing (`FRR <https://frrouting.org/>`__) to implement the various available protocols for
dynamic routing.

These routing protocols are used to:

* Improve fault tolerance (if a connection breaks, a new route will be found if possible)
* Simplify administration (you have to add fewer routes manually)

It is not adviseable to use dynamic routing in the following scenario's:

* When your network is small (so it would be better to use static routes)
* If you are working in a highly isolated environment, where you have to be in control of everything happening in your network

Routing Protocols supported by the plugin include:

* RIPv1 and RIPv2
* OSPFv2 and v3
* BGPv4

.. Warning::
    Not all routing protocols will work in any setup because they may have to be direct neighbors.
    Consider the limitations of a routing protocol before using it.

.. Warning::
    It's strongly advised to increase the kern.ipc.maxsockbuf value via **Tunables**. Go to :menuselection:`System --> Settings --> Tunables` and check if there
    is already a tunable for maxsockbuf and set it to 16777216 if it's lower. Otherwise add a new one with
    name above and the specified value.

.. Warning::
    Disabling a running routing daemon can be dangerous as it can lead to an inaccessible machine.
    If you want to disable a running routing daemon, make sure, you don't lose routes which are
    required by your connection to this machine (for example when using SSH).


------------
Installation
------------

First of all, select Plugins in the menu:

.. image:: images/menu_plugins.png

On this page, you can install the FRR plugin by clicking the `+` icon:

.. image:: images/plugins_frr.png

----------------
General setup
----------------

In order to use one or more of the protocols included, one has to enable the plugin in
:menuselection:`Routing --> General`. Without any other service enabled this makes sure the zebra service is being
configured, which is the coordinating master service which handles generic features such as logging and acccess to kernel
routing.

.. Tip::

    By default logging should be enabled, which sends messages to the local logging and offers remote logging over syslog.
    Always make sure to choose a sensible log level (default is Notifications) and check the log in
    :menuselection:`Routing --> Diagnostics -> Log`


.. Note::

    Since OPNsense doesn't support a form of configuration reloading at the moment, there might be a temporary loss
    of service when saving settings. Normally this is only a small glitch, but in high traffic areas it might
    something to take under consideration when performing maintenance.


------------------------------------------------
Dynamic routing and high availability
------------------------------------------------

In enterprise networks there's often a need to make sure services are protected for all sorts of failures, dynamic
routing helps a lot in this case to provide a proper path for packets to travel, but these nodes themselved might
need to be configured more resilient to prevent single points of failures on the edges of your network.

In OPNsense high availability and failover is organised around :doc:`carp <hacarp>`, which makes it a logical choice to
combine both technologies here as well.

A couple of different strategies are supported to combine both technologies, ranging from disable the daemon when in carp mode
to more fine grained control of how routes are propogated when a machine is in backup mode.

CARP failover mode
..............................

The most simple mode available, when a mode reaches backup state, it will shutdown the services, when it's going to master
it will start them all.

.. Note::

    Due to the nature of this option, it can't be combined with other carp options available.

OSPF: CARP demote
.............................

This option registers a :doc:`status monitor </development/backend/carp>` on top of the FRR logging feed to detect changes in link status,
when OSPF can't find its neighbors it will make this machine less attractive by increasing the demotion factor.

The feature is inspired by OpenBSD's handling of carp demotion in ospfd (https://man.openbsd.org/ospfd.conf.5).

.. Note::

    Since the relevant neighbor negotiation messages are only being logged when the log level is configured to debug,
    the log will be more loud when using this feature. When using a lower log level the status monitor is not expected
    to catch any relevant events.


OSPF: Influence interface cost based on CARP status
......................................................................

FRR natively does not support interaction with carp status as the variant in openbsd does
(carp note in “depend on” keyword https://man.openbsd.org/ospfd.conf.5), this is where our next option comes into play.

Using the interface settings of an OSPF interface you can choose to adjust costs for that interface based on the carp status of the
selected virtual address. Go to :menuselection:`Routing --> OSPF -> Interface` and choose an interface, here you will find the
following options that influence behaviour:

* Depend on (carp)

  * Select a virtual address that this interface relies on. When this target is not in **MASTER** mode, the selected interface is considered **demoted**

* Cost (when demoted)

  * Adjust the cost to this value when going to demoted state, usually one would use a high value here to prefer other routes first

* Cost

  * The standard cost, when provided will be used when in normal conditions. If it's left blank FRR defaults will be used, which it will also rollback to when going back to master mode.


------
How To
------

.. toctree::
   :maxdepth: 2
   :titlesonly:

   how-tos/dynamicrouting_howto
   how-tos/dynamicrouting_ospf
   how-tos/dynamicrouting_rip
