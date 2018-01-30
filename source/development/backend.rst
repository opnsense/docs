=======
Backend
=======

The OPNsense backend consists of several components (see Architecture for a full stack description).

Our core backend service (configd) is implemented using `Python <https://en.wikipedia.org/wiki/Python>`__. and provides two main features:

- Service interaction (using configd actions)
- Generation of configuration data (using templates)

Because some of the codebase still integrates with our legacy codebase, we provide additional plugin options for the following components:

- Services (the services status)
- Syslog (define syslog targets)
- Interface (register interfaces, firewall use etc.)
- Service configuration (legacy service configuration, new style uses configd templates)


Services which need to be executed at system startup can use rc(8) or our syshook system.

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   backend/*
