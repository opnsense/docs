====================================
OpenVPN
====================================


---------------------------------
Assigned Interfaces
---------------------------------

While not strictly necessary, it is possible to assign individual interfaces for OpenVPN servers and clients alike. However doing
so may yield unexpected behaviour of firewall rules. Most notably, rules created on an assigned interface of an OpenVPN Roadwarrior
server are created with the :code:`reply-to` directive by default, which breaks client connectivity.

.. Tip::

    In cases as described above, it can be observed that incoming traffic matches and passes the corresponding firewall rule, but
    reply traffic is never sent back to the connected client. This can be verified via the Web GUI by going to
    :menuselection:`Firewall -> Log Files -> Live View` and optionally by performing a packet capture on the affected interface.

There are multiple ways to fix this problem. For most setups, it  will be sufficient to disable the automatically created IPv4 and
IPv6 Gateways under :menuselection:`System -> Gateways -> Single`. Doing so will also disable the automatic addition of the
:code:`reply-to` directive to rules created on the interface, and client connectivity will be restored.

Another option is to manually select the option "Disable Reply-To" on each firewall rule you generate on the assigned interface.
See :doc:`/manual/firewall` for further details.

The third option is to globally disable the generation of :code:`reply-to` completely as described in
:doc:`/manual/firewall_settings`. However this method can break Multi-WAN setups.

