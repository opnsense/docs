============
Architecture
============

The main focus of the OPNsense project is to provide a secure and
manageable platform for all your security applications. This means high
quality software that is easily maintainable and bug free. We think that
having a framework with a clear separation of concerns is essential to
achieving these goals.

OPNsense is a fork of pfSense ®. The existing code base of pfSense ®
does not always apply a clear separation of concerns. This means we need
a transition of the old (legacy) code base to a new one with a clear
separation. We have chosen a gradual transition to avoid a big bang and
keep the product feature rich while increasing code quality. This
enables simple addition of new features with less bugs and shorter time
to market.

This article describes how this will be achieved.

-----------------------
High-level architecture
-----------------------

|OPNsense Components.svg|

As the above model shows there are two main areas in our stack, the
frontend implemented with PHP/Phalcon and the backend using a custom
service built in Python.

The frontend handles user interaction and communicates with the backend
service. Applying configuration changes, monitoring and controlling
services offered by OPNsense is done by the backend service.

By using a fully configurable backend service, we avoid hardcoding of
services and ease the implementation of new features.

The frontend stack delivers a model driven approach to handle
configuration data, including automatic validation.

Manipulation of the core configuration file is handled at the frontend
model; the backend service is merely a consumer of the information
provided.



---------------------
Frontend Architecture
---------------------

|OPNsense frontend.svg|

Routing
-------

The OPNsense framework uses standard components where possible; the
first layer initializes routing, which handles requests and
delivers them to the controller based on its url. User content is
generated using Volt templates (using Phalcon), which are picked by the controller.

For a detailed description on the routing principles used in OPNsense, visit Frontend
:doc:`/development/frontend/routing`.

Controllers and views
---------------------

Not all parts of the framework are implemented, but by deriving
all controllers from the base in the OPNsense project it’s easy to
extend and adapt to future needs. Documentation on how to implement
controllers, with the use of views, can be found at :doc:`/development/frontend/controller`.

Models
------

All models are defined by a combination of a class and an XML containing
a (nested) definition. More information on defining models can be found
at the frontend model page :doc:`/development/frontend/models`.

Communication
-------------

Communication to the backend service is handled via a unix domain
socket.

Core system
-----------

The core of OPNsense is powered by an almost standard FreeBSD ® system
extended with packages using the pkg system. GIT is used for version
control and the repositories are split into 4 parts:

-  src : the base (FreeBSD ®) system
-  ports : the ports collection containing third party software
-  core : the OPNsense gui and system configuration parts
-  tools : easy tools to build OPNsense

.. TIP::

   | For detailed information about the development workflow see:
   | :doc:`OPNsense development workflow </development/workflow>`


--------------------
Backend Architecture
--------------------


Middleware
--------------------------------------

|OPNsense backend.svg|

Configd, is responsible
for the core system interaction like starting and stopping of daemons
and generating configuration files for used services and applications.

The daemon listens on a unix domain socket and is capable of executing
actions defined in it’s own configuration directory
(“/usr/local/opnsense/service/conf/actions\_\*.conf”).

Currently there are four types of services implemented in the daemon:

-  script : execute external (rc) scripts, report back success or failure
-  script_output: execute external scripts, report back their contents, usually in json format
-  stream_output: open streams to backend components
-  inline : perform inline actions which are part of configd, most notable template generation and maintenance.

|
| Template generation is handled by Jinja2 (https://jinja.palletsprojects.com/en/stable/),
  more information on how to create application templates can be found
  at :doc:`/development/backend/templates`.



Operating stages
--------------------------------------

|OPNsense_operating_events.svg|

As all earlier layers describe how user input can be persisted and service information can be exchanged, we still
have a gap in our functionality when looking at the life of a firewall.
Until this point we have means to manually manage services and devices, including ways to collect information on demand,
but still in a rather isolated way (events triggered via the api layer).

This is where :doc:`syshooks <backend/autorun>` and :doc:`plugins <backend/legacy>` come into play,
these offer mechanisms to ensure different types of services can cooperate with the shared functionality available.

Between starting and stopping our firewall, we can identify three stages.
After power-on, we are booting, when this initial stage has been reached we end up with a running firewall with
all configured services available. During time, various events can happen, for example, someone pulling an network cable
and pushing it back in, this is the running stage.
Eventually, if someone decides to power-down or reboot the machine, we are entering shutdown stage, letting services know
we are ending operation.

Further details of each stage can be found in the :doc:`overview <backend/overview>` document.

To avoid endless dependency loops, services should prevent hooking on events that are not strictly required for operating.
For example, forcing a restart of a component when a network interface has changed is usually a sign of not
following best practices for designing network services.


.. |OPNsense Components.svg| image:: images/OPNsense_Components.svg
   :width: 600px
.. |OPNsense backend.svg| image:: images/OPNsense_backend.svg
   :width: 500px
.. |OPNsense frontend.svg| image:: images/OPNsense_frontend.svg
   :width: 600px
.. |OPNsense_operating_events.svg| image:: images/OPNsense_operating_events.svg
   :width: 700px
