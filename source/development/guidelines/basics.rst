=================
Basics and Future
=================

This article explains the basic coding guidelines that apply and put the
development effort into perspective by explaining the difficulties of legacy
code and the interaction/migration to new
`MVC-based <https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller>`_
code. It also explains guideline differences between new and legacy code.

--------
PHP code
--------
For PHP code the `PSR-12 <https://www.php-fig.org/psr/psr-12/>`_ coding standard applies.

------
Python
------
For Python code the Python Enhancement Proposals (PEPs) apply.
See the `Python Developer's Guide <https://www.python.org/dev/>`__ for detailed
information.

------------
Architecture
------------
Documentation is available about our :doc:`architecture </development/architecture>`
and used :doc:`components </development/components>`.

-----------------------
Safeguard user input
-----------------------

We aim to validate user input before injecting it in the configuration in order to provide a more user friendly
interface and prevent bad things to happen in the future.

Although we do understand that the perfect validation isn't always possible at once (too much referential constraints, not always as easy to catch)
it is a best practice to ask yourself if a specific input could be validated (if not now, what about the future).

The issue with user input impossible to validate is that it will bite you eventually, leading to future security issues waiting to happen
(for example a non authorized user can write commands that will be executed with elevated privileges, we saw this with openvpn for example).

For this reason we do not allow plain text configuration data to be stored in our configuration
(although some legacy components still use this `opnsense/core#d62015 <https://github.com/opnsense/core/commit/d62015df1cdb0c0711b488bd66ced631b9a4f37b>`__ )

.. Note::

    Feature requests for custom user inputs will be declined in our public repositories, defining what a feature should do
    also helps designing the right feature.


.. Tip::

    If custom input is needed, in most cases you can use hooks to include additional configuration data in the service,
    most services offer this type of support (either with predefined directories or via the template system).

    This prevents arbitrary users from adding undefined configuration data.


The different field types in our model system are aimed to help the developer safeguard his or her code for unexpected input.


-----------------
Ideal Development
-----------------
Our ideal OPNsense system looks like a standard FreeBSD system using our
pluggable user interface for management, which supports both real users as "machine"
users (REST).

When developing we want the code to be clean and coded as DRY (Don't Repeat Yourself)
as possible and do not want to invent the wheel when not needed.

The user interface should to be able to run as non-root user instead of root by
restructuring the way commands are passed to the system (configd).

----------------------------
Reality: Overdue Maintenance
----------------------------
In reality we forked a system that went without code maintenance for a very long
time and we needed to transition that into something more structured.

One of the first things (on the programming part of the system) we did was build
components around an existing framework (`Phalcon <https://phalconphp.com/>`_)
to create new modules, which could use validated configuration data (from the
config.xml), supply a RESTful API and generate HTML output using standard
templates (Volt).

We created the configd system, which can generate system configuration and
execute system calls using predefined templates. And then we started using those
new components for our first newly designed modules (like the proxy and the traffic shaper).
More information about the “to-be” architecture can be found in our
:doc:`architecture </development/architecture>` documentation.

---------
Strategy
---------
Knowing we can’t change the world in a single day and having a lot of legacy to
drag around with us, our strategy consists of three parts:

**1)** Cleanup and maintenance
Restructure old (legacy) code, basically all code in the src/www, src/etc/inc to
make it better readable, easier to use and remove unused / unnecessary parts. By
doing so we want to extend the lifetime of the old code a bit and make the
transition in new code easier eventually.

**2)** Detach
Move system configuration calls to configd where possible, which gives the
administrator the advantage of running those commands from the command line and
helps removing the need for root user access in the future. The ipsec VICI
implementation is one example of this stage.

**3)** Moving on
(re)build new parts, using our new modules, which provide a layered development
system to automatically support API calls from other systems and XML based model
templates to describe configuration data.

*See also:*

* :doc:`Hello World Module </development/examples/helloworld>`
* :doc:`Howto use the API </development/how-tos/api>`

Our guidelines somewhat depend of the stage the code is in, when writing new code,
all actions should use the API system for actually changing configuration and
performing configuration tasks. They should, of course, use the normal PSR coding
standards for PHP code and follow the Python PEPs.

When moving to the legacy part of the system, our goal is to stick as close to
PSR1/2 as possible, knowing it will never be perfect.
