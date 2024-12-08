===============================
Use the API for CRUD Operations
===============================


Overview
--------

There are several components which have API capabilities which allow for Create, Read, Update, Delete (CRUD) operations.
The following code examples detail how CRUD operations are used to configure the TrafficShaper pipe object

Resources
---------
API endpoints and supported method resources are located in :doc: `development/api </development/api>`

In each of these pages, links to the xml model reference are provided.
These are used for creating the JSON payloads for ``POST`` requests.

For the following examples, the following references are used:
 - API endpoint reference for `Trafficshaper <development/api/core/trafficshaper>`
 - Model file `Trafficshaper.xml <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/models/OPNsense/TrafficShaper/TrafficShaper.xml>`


Create a pipe
-------------

The following JSON blob defines a 2 Mbit pipe, with basic co_del functionality.

.. code-block:: json

    {"pipe": {"description":"MyPipe", "bandwidth": 2, "bandwidthMetric": "Mbit", "mask":"src-ip", "codel_enable": 1, "codel_ecn_enable": 0, "pie_enable": 0,"enabled": 0}}

This requires a ``POST`` operation to the API endpoint
Wrapping this in a curl command looks like this:

::
    curl -XPOST -H 'Content-Type: application/json" -k -u "w86XNZob/8Oq8aC5hxh2he+vLN00r0kbNarNtdpoQU781fyoeaOBQsBwkXUt":"puOyw0Ega3xZXeD26XVrJ5WYFepOseySWLM53pJASeTA3" https://10.211.55.100/api/trafficshaper/settings/addpipe
    -d '{ "pipe" : { "description":"MyPipe", "bandwidth": "2", "bandwidthMetric": "Mbit", "mask":"src-ip", "codel_enable": 1, "codel_ecn_enable": 0,"pie_enable": 0, "enabled": 0} }''

Provided that the JSON payload is correct and passes validation, the response will contain the following data payload:

.. code-block:: json

    {"result":"saved", "uuid":"84f51fc6-e330-4ab7-b71a-31b51495a664"}


Where uuid is the unique identifier of the object, which can then be used for other operations.


Read a pipe
-----------
To confirm that the pipe is created and review all the configured options of the pipe, the following API call is used:

::
    curl -k -u "w86XNZob/8Oq8aC5hxh2he+vLN00r0kbNarNtdpoQU781fyoeaOBQsBwkXUt":"puOyw0Ega3xZXeD26XVrJ5WYFepOseySWLM53pJASeTA3" \
    https://10.211.55.100/api/trafficshaper/settings/getpipe/84f51fc6-e330-4ab7-b71a-31b51495a664

This is a straightforward ``GET`` request, note the use of the UUID from the creation return.

.. note::
    The returned JSON blob is not the same format as the payload used for POST requests to the API


Update a pipe
-------------
The following json blob will be used to change the description of the pipe, and remove the mask:

.. code-block:: json

    {"pipe": { "description": "Renamed Pipe", "mask":"none" } }

This requires a ``POST`` to the ``setPipe`` endpoint:

::
    curl -XPOST  -H 'Content-Type: application/json" -k -u "w86XNZob/8Oq8aC5hxh2he+vLN00r0kbNarNtdpoQU781fyoeaOBQsBwkXUt":"puOyw0Ega3xZXeD26XVrJ5WYFepOseySWLM53pJASeTA3" \
    https://10.211.55.100/api/trafficshaper/settings/setpipe/84f51fc6-e330-4ab7-b71a-31b51495a664 -d '{ pipe : { "description":"Renamed Pipe", "mask":"none"}

Provided that the JSON payload is correct and passes validation, the response will contain the following data payload:

.. code-block:: json

    {"result":"saved", "uuid":"84f51fc6-e330-4ab7-b71a-31b51495a664"}


Delete a pipe
-------------
Deletion of the pipe is a ``POST`` operation, with an empty json string as the paylod.

::
     curl -XPOST -H 'Content-Type: application/json" -k -u "w86XNZob/8Oq8aC5hxh2he+vLN00r0kbNarNtdpoQU781fyoeaOBQsBwkXUt":"puOyw0Ega3xZXeD26XVrJ5WYFepOseySWLM53pJASeTA3" \
    https://10.211.55.100/api/trafficshaper/settings/delpipe/84f51fc6-e330-4ab7-b71a-31b51495a664 -d ""
