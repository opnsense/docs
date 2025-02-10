====================
CARP Troubleshooting
====================

This article aims to highlight common problems and pitfalls associated with a CARP setup.

-------
General
-------

- CARP events are logged in the kernel message buffer, and can be inspected using either `dmesg` using the shell, or the general system log, filtering on 'kernel' and 'carp'.
- CARP advertisement packets can be captured using tcpdump in a shell:

.. code-block:: sh

    tcpdump -ni <interface> -t vrrp -T carp

- One can increase the CARP logging verbosity by using the following command:

.. code-block:: sh

    sysctl net.inet.carp.log=2


---------------------------------
Backup node cannot reach internet
---------------------------------

This issue usually occurs when an administrator is trying to update the machine while in backup mode,
and while traffic from the LAN can reach the internet, the machine itself cannot. This is usually caused by a misconfigured outbound NAT rule.
If the source network of the rule is set to 'any', traffic originating from the firewall itself going to the internet is also translated
to the CARP VIP, meaning the return traffic is sent to the master firewall, which ignores the traffic as the packets are out of state.

The solution is to adjust the outbound NAT rule so that it only accepts traffic from the relevant source network, which is often any RFC1918 address.


-----------
Split-brain
-----------

In certain rare occasions, both the master and backup node may show a "master" state assumed in the virtual IP status overview for one or more VIPs.
In general, there may be multiple reasons this is happening:

- The advertisement packets contain a hash that does not match up with what the other node expects. This is caused by misconfigured virtual IPs.
  See `CARP Virtual IP type <../firewall_vip.html#carp>`__ for more information. This situation is logged to the system log if the verbosity has been increased.

This is solved by making sure that all of the CARP VIPs and IP aliases belonging to the same VHID are exactly the same, including missing IP addresses.

- Advertisement packets get lost en-route to the other node. This can happen due to network issues or misconfigured routing.

While CARP is meant to act on link state changes or general failures, it does not detect whether the advertisement packets reach the other node.
Since CARP is configured on a per-interface basis, a backup node may see advertisement packets on one interface from the master, but fail to see them
on another. In this case the backup node cannot switch all interfaces in unison to the master state.

To troubleshoot this, you can inspect the CARP traffic on the backup node using tcpdump.

In the default case of multicast, one should be able to see the source IP address of the master node in the advertisement packets. If instead the backup
source IP address is shown, it indicates the CARP traffic is not reaching the backup node. One can rule out multicast issues by switching to
unicast in the Virtual IP settings.

- Preemption is disabled in :menuselection:`System --> High Availability --> Settings`. Unless you know what you are doing,
  preemption should always be enabled unless you're running a routing-only platform.

----------------
Interface errors
----------------

Sometimes CARP will failover for seemingly unknown reasons. This is because CARP relies on multiple layers for reliable delivery of packets, any failure will often manifest as an interface error.
Interface errors can happen for various reasons, but are often associated with either protocol failures or NIC/driver failures. If CARP cannot send out
an advertisement packet on a particular interface due to an interface error, the CARP system will demote itself, hoping the backup node will take over.
On the OPNsense side, this is indicated in the Virtual IP Status page by a message showing "CARP has detected a problem ...".

If this happens, an event is logged in the general system log and show the reason for the failure, for instance, `send error 55`. If the backup firewall
takes over, the master node will cease sending its advertisement packets, thereby also eliminating its ability to see whether communication has
been restored. In such a scenario, the demotion will remain the same until rebooted or until manually reset by an administrator.

To manually switch back to the master node, you can use the following command:

.. code-block:: sh

    sysctl net.inet.carp.demotion=<signed demotion factor>

where `<X>` is the signed demotion factor. I.e. if the current demotion is `240`, one should use `-240`. If the current demotion is `-480`, one should use `+480`.

After applying this command, CARP will start sending out advertisement packets again, thereby ambiguously detecting that communication has been restored,
and will therefore subtract the old demotion factor again. An administrator should correct this a second time to reset the value to 0.

------------------------------
Synchronizing backup to master
------------------------------

A backup node should never contain settings for Configuration synchronization in :menuselection:`System --> High Availability --> Settings`. If this is the case
an adminstrator can accidentally synchronize the backup with the master, causing all kinds of configuration errors.

.. Tip::

    Configure the master node in a different theme to differentiate the two machines.



