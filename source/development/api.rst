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

The $key and $secret parameters are used to pass the API credentials using curl. You need to set these parameters with your own API credentials before using them in the examples:

.. code-block:: sh

    key=w86XNZob/8Oq8aC5r0kbNarNtdpoQU781fyoeaOBQsBwkXUt
    secret=XeD26XVrJ5ilAc/EmglCRC+0j2e57tRsjHwFepOseySWLM53pJASeTA3

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
