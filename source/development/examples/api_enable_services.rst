=============================
API enable standard services
=============================

OPNsense contains a simple wrapper which handles standard service actions like starting and stopping services.
For this example, we assume the HelloWorld example is created and the model exists.

Prerequisites
--------------------

The HelloWorld example forms the basis for this one, please make sure you read and try it first before starting with
this one.


Configd actions
--------------------


Since the example didn't contain a service, we're going to extend the configd template first.
Edit :code:`/usr/local/opnsense/service/conf/actions.d/actions_helloworld.conf` and expand with the following sections:

::

    [start]
    command:exit 0
    parameters:
    type:script
    message:hello world service start

    [stop]
    command:exit 0
    parameters:
    type:script
    message:hello world service stop

    [restart]
    command:exit 0
    parameters:
    type:script
    message:hello world service restart

    [reload]
    command:exit 0
    parameters:
    type:script
    message:hello world service restart

    [status]
    command: echo "hello world is running"
    parameters:
    type:script_output
    message:hello world service status

Next restart configd using :code:`service configd restart` and test these new calls using the following commands

::

    # configctl helloworld start
    OK
    # configctl helloworld stop
    OK
    # configctl helloworld status
    hello world is running
    # configctl helloworld restart
    OK


Our template only simulates a service, it doesn't actually do anything (:code:`exit 0`).

Update the service controller
---------------------------------


Next we change the existing controller to use :code:`ApiMutableServiceControllerBase`, which links the existing model to the service callouts defined.
The :code:`testAction` used in the HelloWorld example is left out to avoid confusion.

.. code-block:: php
    :caption: /usr/local/opnsense/mvc/app/controllers/OPNsense/HelloWorld/Api/ServiceController.php

    use OPNsense\Base\ApiMutableServiceControllerBase;

    class ServiceController extends ApiMutableServiceControllerBase
    {
        protected static $internalServiceClass = '\OPNsense\HelloWorld\HelloWorld';
        protected static $internalServiceTemplate = 'OPNsense/HelloWorld';
        protected static $internalServiceEnabled = 'general.enabled';
        protected static $internalServiceName = 'helloworld';

        protected function reconfigureForceRestart()
        {
            return 0;
        }
    }


The  service above defines the following static variables:

* $internalServiceClass
    * reference the model class, which is used to determine if this service is enabled (links the model to the service)
* $internalServiceTemplate
    * before starting the service it will call configd to generate configuration data, in this case it would execute the equivalent of :code:`configctl template reload OPNsense/HelloWorld` on the console
* $internalServiceEnabled
    * Which section of the model contains a boolean defining if the service is enabled (general.enabled)
* $internalServiceName
    * refers to the action template, where it can find start/stop/restart/status/reload actions (actions_helloworld.conf)


The :code:`reconfigureForceRestart` overwrite tells the controller if it should always stop the service before trying a start, some
services can be signaled to do a reconfigure without stopping.


Endpoints
---------------------------------

When deploying this controller into the HelloWorld module it would expose the following endpoints

.. csv-table::
   :header: "Method", "Endpoint"
   :widths: 4, 100

   "``POST``","/api/helloworld/service/stop"
   "``POST``","/api/helloworld/service/start"
   "``POST``","/api/helloworld/service/restart"
   "``POST``","/api/helloworld/service/reconfigure"
   "``GET``","/api/helloworld/service/status"
