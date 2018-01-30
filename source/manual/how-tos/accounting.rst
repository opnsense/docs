===============================
Setup FreeRADIUS for accounting
===============================

---------------------
Goal of this tutorial
---------------------

This tutorial can be used to test your Captive portal setup with radius
accounting, it's not intended to use for production setups (because we
only use simple flat files for everything). We used Ubuntu linux for
this setup, a different operating system might result in some paths
being different.

User limits on the OPNsense firewall are set right after login, the
Radius server should tell the firewall how much resources are left for
the user that logged in successfully. A normal login sequence look like
this:

[login] -> [send accounting start] -> [send interim updates while
connected] -> [on logout, send accounting stop]

-----
Setup
-----

To setup freeradius in ubuntu, execute the following command:

::

    apt-get install freeradius


Arrange client access
---------------------

Edit the file /etc/freeradius/clients.conf and append a block for your
network, as sample we will use 10.211.55.0/24.

.. code-block:: php

    client 10.211.55.0/24 {
        secret      = testing123
        shortname   = test-network
     }

Enable daily session limits
---------------------------

Enable daily session limits, which needs accounting to signal the
clients use.

-  In /etc/freeradius/sites-available/default uncomment daily in
   authorize and accounting sections.
-  in /etc/freeradius/radiusd.conf uncomment daily in the instantiate
   section
-  append to /etc/freeradius/dictionary


.. code-block:: c

    ATTRIBUTE       Daily-Session-Time      3000    integer
    ATTRIBUTE       Max-Daily-Session       3001    integer


-  uncomment sradutmp in the accounting section, to be able to use the
   radwho command.

--------------
Add test users
--------------

You can add your test users to /etc/freeradius/users, they should look
like this:

.. code-block:: c

    "test" Cleartext-Password := "test", Max-Daily-Session := 1800
            Framed-IP-Address = 10.211.55.100,
            Reply-Message = "Hello, %{User-Name}"


Make sure the second and third lines are indented by a single tab
character.

This should result in a user with a maxim use per day of 1800 seconds.

-----------
Test radius
-----------

For the initial test, it might be practical to debug the traffic going
in and out from Freeradius. The next steps help you start Freeradius in
debug mode, without output to console:


.. code-block:: c

    /etc/init.d/freeradius stop
    freeradius -X
