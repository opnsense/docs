====================================
Gateways and monitoring
====================================

The address you are trying to monitor should be reachable using the interface the gateway is attached to, either
directly or using a static route (check :menuselection:`System --> Routes --> Status`).

---------------------------------
dpinger:.. sendto error: XXX
---------------------------------

Usually found in :menuselection:`System --> Log Files --> General`, every code has a meaning, usually explained in
`errno.h <https://github.com/opnsense/src/blob/master/sys/sys/errno.h>`__ (:code:`man errno`)

Some common ones are explained in the :ref:`errno` section.

------------------------------------------
arpresolve: can't allocate llinfo for..
------------------------------------------

This message usually means that the configured gateway lies outside the configured subnets for this firewall (for IPv4).

.. Tip::

    Double check the subnets of your interface and virtual IP's, you can also use :menuselection:`Interfaces --> Overview`
    for a quick list of all configured addresses.
