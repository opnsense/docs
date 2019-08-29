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

Some common ones are explained below:

======  ==================== =================================================================================
XX      Name                 Description
======  ==================== =================================================================================
55      ENOBUFS              No buffer space available. An operation on a socket or pipe was not performed
                             because the system lacked sufficient buffer space or because a queue was full.
                             **Check connectivity from the machine itself using** :code:`ping`, most common
                             mistakes are misconfigured routes, interface issues (disconnected) and
                             policy based routing issues forcing traffic to the wrong target
                             (using :code:`reply-to`)
64      EHOSTDOWN            Host is down. A socket operation failed because the destination host was down.
                             **Expecting an (layer 2) ARP response but none was returned, often misconfigured
                             subnets or hosts are actually not accessible over L2**
65      EHOSTUNREACH         No route to host. A socket operation was attempted to an unreachable host
                             **The routing table is a good place to look**
                             (:menuselection:`System --> Routes --> Status`)
======  ==================== =================================================================================

------------------------------------------
arpresolve: can't allocate llinfo for..
------------------------------------------

This message usually means that the configured gateway lies outside the configured subnets for this firewall (for IPv4).

.. Tip::

    Double check the subnets of your interface and virtual IP's, you can also use :menuselection:`Interfaces --> Overview`
    for a quick list of all configured addresses.
