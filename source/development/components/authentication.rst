===================
Authentication
===================

.. sidebar:: Access Control List

    .. image:: images/acl-finger-print.jpg

--------
Concepts
--------

Authentication in OPNsense consists of three basic concepts, which are available throughout the entire system:

* Authenticators

  - These implement the method to use, for example Radius, Ldap, local authentication, etc

* Connections

  - A connection uses an authenticator and defines the properties needed, for example our Radius server available at our domain using specfic settings.

* Services

  - Some services require or support authentication, such as the webinterface, OpenVPN, etc. These may allow one or more connectors.

------------------------------
Authenticators & Connections
------------------------------


Services within OPNsense can use different authentication methods, for which connections can be configured in **System-->Access-->Servers**
(e.g. the method can be **radius** which is offered through a server at a location).
All of these methods use the same api defined in :code:`\OPNSense\Auth\IAuthConnector`, which comes with some simple to use handles.

If a class in :code:`\OPNSense\Auth` implements :code:`IAuthConnector` it is considered a viable authentication option
for the authenticator factory named :code:`AuthenticationFactory`.

The factory provides a layer of abstraction around the different authentication concepts, for example a server defined in
**System-->Access-->Servers** can be requested using a simple :code:`(new AuthenticationFactory())->get('name');`
This connects the authenticator to the configured servers and the response object is ready to handle authentication requests.


-----------------------------
Services
-----------------------------

We strive to use :code:`pam` to define our services, in which case we adopt to existing standards.
OPNsense comes with a pam module, which connects our service definitions with the services defined using pam.

A simple example of a service named **opnsense-auth-test** is defined as follows in a file with the name :code:`/etc/pam.d/opnsense-auth-test`

.. code-block:: sh

    auth		sufficient	pam_opnsense.so
    account		sufficient	pam_opnsense.so

To test authentication, you can use opnsense-auth-test for any configured service. The following example
tries to authenticate user *root* for service *opnsense-auth-test*.

.. code-block:: sh

    /usr/local/sbin/opnsense-auth-test -s opnsense-auth-test -u root

.. Note::

    **opnsense-auth-test** inherits from the standard system authentication used for console and webgui login.


Internally pam calls :code:`/usr/local/sbin/opnsense-auth` which then uses our factory class to perform authentication using
the connections defined in the service.

For this purpose we expose a *services* namespace in :code:`\OPNSense\Auth\Services` where the required options can be read
from the OPNsense configuration.

For every service defined in pam, the factory method :code:`getService()` expects a class implementing :code:`OPNsense\Auth\IService`

.. Note::

    Not every service uses pam already, in that case it is defined as a script handling the authentication. Conceptually
    it delivers the same functionally, but has some downsides in terms of required rights for the script.

The interface :code:`IService` is quite easy to read and should be self explanatory.
