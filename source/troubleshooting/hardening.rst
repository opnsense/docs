=======================================
System hardening vs performance
=======================================

OPNsense tends to choose more strict hardening options by default, so when comparing performance between upstream
standard FreeBSD it's good to know which settings differ and can have an impact on your measurements.
This document aims to describe (some of) the differences, so when you value performance over security it is more obvious
which toggles might be worthwhile to change.

Keep in mind that most of the settings will need a reboot and can be altered using system tunables in :menuselection:`System --> Settings --> Tunables`.


IPv4 random ID's [net.inet.ip.random_id]
--------------------------------------------------
control IP(v4) IDs generation behaviour.
This closes a minor information leak which allows remote observers to determine the rate of packet generation	on the machine by
watching the counter.  At	the same time, on high-speed links,	it can decrease	the ID reuse cycle greatly.
IPv6 flow IDs and fragment	IDs are	always random. (source :code:`man -S 4 inet`)

Our default is 1 (enabled).

Spectre and Meltdown
--------------------------------------------------

To mitigate some of the speculative execution vulnerabilities, there are a couple of settings available in FreeBSD.
More information about the various vulnerabilities and associated patches can be found `here <https://wiki.freebsd.org/SpeculativeExecutionVulnerabilities>`__

Meltdown mitigation using Page Table Isolation (PTI), although also enabled in FreeBSD it's worth to mention which setting is responsible
for enabling this feature. To disable PTI set :code:`vm.pmap.pti` to 0. Not all cpu's are vulnerable for Meltdown, in which case PTI can be disabled safely.

Spectre variant 2, the system offers IBRS-based mitigation on Intel CPUs.
The IBRS mitigation main disadvantage is the significant performance penalty.
In OPNsense IBRS is enabled (for Intel) by default by disabling (0) :code:`hw.ibrs_disable`, upstream FreeBSD standard is disabled (1).

User/group separation (security.bsd)
--------------------------------------------------

Freebsd offers a couple of toggles to tighten security for ordinary users, these likely don't impact performance
a lot, but these are the ones including descriptions that differ on our end (source :code:`sysctl -d security.bsd`).

================================================= =================================================================================
Setting                                             Description
================================================= =================================================================================
security.bsd.hardlink_check_gid [0->1]              Unprivileged processes cannot create hard links to files owned by other groups
security.bsd.hardlink_check_uid [0->1]              Unprivileged processes cannot create hard links to files owned by other users
security.bsd.unprivileged_proc_debug [1->0]         Unprivileged processes may use process debugging facilities
security.bsd.see_other_gids [1->0]                  Unprivileged processes may see subjects/objects with different real gid
security.bsd.see_other_uids [1->0]                  Unprivileged processes may see subjects/objects with different real uid
security.bsd.unprivileged_read_msgbuf [1->0]        Unprivileged processes may read the kernel message buffer
================================================= =================================================================================
