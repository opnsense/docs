==========
Using IPv6
==========

.. image:: images/IPv6.png
   :width: 100%

OPNsense fully supports IPv6 for routing and firewall. However there are lots of
different options to utilize IPv6. Currently these scenario's are known to work:

* Native IPv6 only
* Dual Stack IPv4 + IPv6
* IPv6 <-> IP4v Tunnel broker

.. Warning::

  NAT64, IPv4 <-> IPv6 Network address translations, is currently not supported
  by FreeBSD.

-----------
Configuring
-----------

- :doc:`/manual/how-tos/IPv6_ZenUK`
- :doc:`/manual/how-tos/ipv6_tunnelbroker`
- :doc:`/manual/how-tos/ipv6_dsl`
