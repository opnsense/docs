=============================================
IPS Bypass local traffic from inspection
=============================================

.. Note:: This tutorial explains how to bypass traffic between local attached networks. Following this tutorial will result in traffic only being inspected between external (WAN) networks and internal (LAN) networks. With bypass enabled, routing performance is improved significantly between local networks while IPS is used. 
.. Tip:: If you only have 1 interface selected in Intrusion Detection, you don't have to follow this tutorial. There won't be any performance benefit.
.. Warning:: Traffic between local networks won't be inspected anymore, so use this with care!

-------------
Prerequisites
-------------

- Some features described on this page were added in the latest version. Always keep your system up to date.
- Intrusion Detection should be **enabled** and **IPS mode** selected. 
- Only **internal networks** should be selected in **Interfaces** (LAN, OPT1 etc..), **not the WAN interface**.

-----------------
Create new Rules
-----------------

To start go to :menuselection:`Services --> Intrusion Detection --> Administration` and select the tab :menuselection:`User defined`.

Select **+** to add a new rule.

- Input the **Source IP** with CIDR-Suffix, e.g. ``10.0.0.0/8``
- Input the **Destination IP** with CIDR-Suffix, e.g. ``10.0.0.0/8``
- Select the **Action** as *Pass*
- Enable the **Bypass** checkbox
- Set the **Description** as "Bypass net 10.0.0.0 to 10.0.0.0"

Select **+** or **clone** to create additional new rules.

* Repeat the above steps to create rules between each of the RFC1918 Private IPv4 subnets, ``192.168.0.0/16``, ``172.16.0.0/12``, ``10.0.0.0/8``. Don't forget to adjust the description.

.. Note:: The finished ruleset for IPv4 should include the following rules:
    
    ==================  ==================  ==========  ==========  ======================================
    **Source IP**       **Destination IP**  **Action**  **Bypass**  **Description**
    ==================  ==================  ==========  ==========  ======================================
    10.0.0.0/8          10.0.0.0/8          Pass            X       Bypass net 10.0.0.0 to 10.0.0.0
    10.0.0.0/8          172.16.0.0/12       Pass            X       Bypass net 10.0.0.0 to 172.16.0.0
    10.0.0.0/8          192.168.0.0/16      Pass            X       Bypass net 10.0.0.0 to 192.168.0.0
    172.16.0.0/12       10.0.0.0/8          Pass            X       Bypass net 172.16.0.0 to 10.0.0.0
    172.16.0.0/12       172.16.0.0/12       Pass            X       Bypass net 172.16.0.0 to 172.16.0.0
    172.16.0.0/12       192.168.0.0/16      Pass            X       Bypass net 172.16.0.0 to 192.168.0.0
    192.168.0.0/16      10.0.0.0/8          Pass            X       Bypass net 192.168.0.0 to 10.0.0.0
    192.168.0.0/16      172.16.0.0/12       Pass            X       Bypass net 192.168.0.0 to 172.16.0.0
    192.168.0.0/16      192.168.0.0/16      Pass            X       Bypass net 192.168.0.0 to 192.168.0.0
    ==================  ==================  ==========  ==========  ======================================
    
.. Tip::

    - If you use IPv6 - e.g. with *Track Interface* or *Static IPv6* - create an additional rule. 
    - You can find your *IPv6 prefix* in :menuselection:`Interfaces --> Overview --> WAN` - e.g ``2001:db8:a:aa00::/56``.
    - You only have to create 1 rule, because all of the *Track IPv6 Interface - IPv6 Prefix ID* networks - e.g. ``2001:db8:a:aa01::/64``, ``2001:db8:a:aa02::/64`` - are already included in the ``/56`` Prefix.
    - Please note that this only works if your Prefix is static.

-------------------
Apply configuration
-------------------

Apply the configuration by pressing the **Apply** button at the bottom of
the form.

-------------------
External Resources
-------------------
- https://docs.suricata.io/en/suricata-6.0.0/rules/bypass-keyword.html
- https://docs.suricata.io/en/suricata-6.0.0/performance/ignoring-traffic.html
