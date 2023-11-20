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

.. note::

     When using Postman to test an API call, use the 'basic auth' authorization type. The $key and $secret parameters go into Username/Password respectively.

.. note::

    Always make sure the owner of the key is authorized to access the resource in question, the "Effective Privileges" set on the user
    shows which resources are accessible. (Edit reveals the endpoints assigned to each resource).

    ACL's are explained in :doc:`development/components/acl </development/components/acl>`).

Required parameters and expected responses
------------------------------------------------

Our auto-generated api documentation can only collect endpoints and their most likely call method (:code:`GET`, :code:`POST`),
Since almost 99% of our endpoints are actually being used by the gui, it's not very complicated to find their
parameters, you just need a browser and open an inspect pane. Calls being executed from the gui can easily be found
by filtering the requests starting with :code:`/api/`.

For exampe, when looking at the search grid in :menuselection:`System --> Diagnostics --> Services`, pressing the reload
button will execute a :code:`POST` to :code:`https://my.firewall/api/core/service/search` containing the following raw
json data:

::

    {"current":1,"rowCount":7,"sort":{},"searchPhrase":""}


And returns a structure similar to:

::

    {
        "total": 10,
        "rowCount": 7,
        "current": 1,
        "rows": [
            {
            "id": "configd",
            "locked": 1,
            "running": 1,
            "description": "System Configuration Daemon",
            "name": "configd"
            },
            ....
        ]
    }


A lot of endpoints use the same shared model classes underneath and will thus look quite similar. If classes are bound to
a model, the documentation will point to it. Here you can find the standard types to expect, without specific application
specific validations.

When more detailed information is needed, best read the  :doc:`Architecture </development/architecture>` documentation to
understand how different areas of the system interact.


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
