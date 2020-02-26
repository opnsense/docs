=======
Routing
=======

-------
General
-------

To retain backward compatibility with legacy code, we try to keep the
old pages at their original location. For the new code, we define two
root folders in the url:

-  /ui/ for the new user interface parts
-  /api/ used for webservices (REST)

This part of the routing is handled by lighthttpd using mod\_alias and mod\_rewrite.

----------------------
User interface Routing
----------------------

If you look at the controller directory in OPNsense, you will notice
there are different directory levels under the root controller directory
in /usr/local/opnsense/mvc/app/controllers. To support different apps
and vendors eventually, we already used a structure which is
automatically used to setup the routing.

At the first level we use the vendor of the app, in our case that will
always be OPNsense.

The next level is used to name the topic (or app), for example we use
Sample for our example application.

Finally you may place your standard Phalcon classes for controllers in
that directory, so if you want to create a page helloworld, that should
come with a controller helloworldController.php (and a indexAction to
define the index action for that page).

The complete path of the helloworld page would eventually be:

::

  /usr/local/opnsense/mvc/app/controllers/OPNsense/Sample/helloworldController.php

When publishing the page, the vendor part of the controller is not used in the
mapping, so in this example the helloworld index page will be at:

::

  https://{url}/ui/sample/helloworld/

All the parts of the url are automatically converted to lower-case, so **S**\ample
will be mapped to **s**\ample.

This routing is setup via the index page of our new code base and uses

::

  /usr/local/opnsense/mvc/app/config/services.php

to wire it all together.

-----------
API routing
-----------

Routing for API functions is quite similar to routing UI components,
just create a Api directory under the app path and place a controller
class to handle the request. The only major difference is that it's
handled by a separate PHP file (called api.php) instead of the
index.php file used to configure the ui part, details of the routing can
be found in /usr/local/opnsense/mvc/app/config/services\_api.php .

If our sample app needs an API to echo something back via a controller called
tools it could be put into a file called:

::

  /usr/local/opnsense/mvc/app/controllers/OPNsense/Sample/Api/toolsController.api

And called via the following url:

::

  https://{host}}/api/sample/tools/echo

When the controller has a method called echoAction.
