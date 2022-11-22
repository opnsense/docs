=============
API Reference
=============

Introduction
------------

The OPNsense API calls are structured in the form:

.. code-block:: sh

     https://opnsense.local/api/<module>/<controller>/<command>/[<param1>/[<param2>/...]]

There are two HTTP verbs used in the OPNsense API:

    - ``GET``  Retrieves data from OPNsense
    - ``POST``  Creates new data, updates existing data or executes an action

The body of the HTTP POST request and response is an 'application/json' object.

Authentication
--------------

The $key and $secret parameters are used to pass the API credentials using curl. You need to set these parameters with your own API credentials before using them in the examples:

.. code-block:: sh

    key=w86XNZob/8Oq8aC5r0kbNarNtdpoQU781fyoeaOBQsBwkXUt
    secret=XeD26XVrJ5ilAc/EmglCRC+0j2e57tRsjHwFepOseySWLM53pJASeTA3

.. note::

     When using Postman to test an API call, use the 'basic auth' authorization type. The $key and $secret parameters go into Username/Password respectively.

Authorization
-------------

When using the API, the user for which the $key and $secret were issued, may require specific privileges granted to use the API modules and their controllers.
Such privileges, if any, are explicitly mentioned in the API documentation, alongside each method.

In case of doubts, however, you can grep through the source code. For example, for the `sslh` module,
the privileges can be found in https://github.com/opnsense/plugins/blob/master/net/sslh/src/opnsense/mvc/app/models/OPNsense/Sslh/ACL/ACL.xml (you may need to choose a tag that is relevant to the OPNsense version you use).

The corresponding privilege name that needs to be granted is denoted by the `<name>` element. For the `sslh` module and "any" controller (as denoted by the "`/*`" wildcard),
it is `Services: SSLH`:

.. code-block:: xml

    <acl>
       <page-services-sslh>
          <name>Services: SSLH</name>
          <patterns>
             <pattern>ui/sslh/*</pattern>
             <pattern>api/sslh/*</pattern>
          </patterns>
      </page-services-sslh>
    </acl>


Core API
--------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   api/core/*

Plugins API
------------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   api/plugins/*


Business edition API
------------------------

The business edition comes packed with some additional features which could also be used
for integration purposes from third-party applications. The most relevant ones will be explained in this section.


.. toctree::
  :maxdepth: 2
  :titlesonly:
  :glob:

  api/be/*
