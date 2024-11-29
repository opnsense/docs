===========================
[Interface] Groups
===========================

To simplify rulesets, you can combine interfaces into **Interface Groups** and add policies which will be applied to
all interfaces in the group.

Since interface groups are processed before normal interfaces, you should not have issues with overlapping rules in
the interface tabs itself. More details about processing order can be found  :ref:`here <Firewall_Rule_Processing_Order>`


.. Note::

    For multiwan setups be careful with groups. Since groups are not bound to a specific interface, they will
    use the normal routing system to determine the next hop when applied on WAN type interfaces (:code:`reply-to` is not used here).


--------------------
Settings
--------------------

=====================================================================================================================

====================================  ===============================================================================
Name                                  The technical name of the group. Has some restrictions which also apply
                                      to the underlying operating system.
Description                           A user friendly description, informational use only
Members                               Member interfaces
====================================  ===============================================================================


For a deployment strategy visit `Security Zones </manual/how-tos/security-zones.html>`_
