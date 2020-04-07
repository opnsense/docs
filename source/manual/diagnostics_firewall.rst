===========
Diagnostics
===========

-----------------------------------------
pfInfo
-----------------------------------------

Various detailed statistics gathered from `pfctl <https://www.freebsd.org/cgi/man.cgi?query=pfctl>`__,
such as packet counters per interface, memory limits, configured timeouts and detailed active rules.

-----------------------------------------
pfTop
-----------------------------------------

`pftop <https://www.freebsd.org/cgi/man.cgi?query=pftop>`__ displays the active packetfilter states and rules, and periodically updates this information.

-----------------------------------------
pfTables
-----------------------------------------

Detailed insight into loaded aliases and their content. When an alias has **Statistics** enabled, it will show these
too.

It's also possible to manually adjust the contents, using **Quick add address** or the delete button.

.. Note::

    When deleting items, keep in mind that the regular update process might put the address (or network) back in, since
    deletion isn't persistent.

.. Tip::

    Use "Find references" to check if an address would match any configured aliases, which is very practical for debugging
    purposes, since it will also check if an address fits a network (such as 10.0.0.2 fits in 10.0.0.0/24).


-----------------------------------------
States Dump
-----------------------------------------

Insight into the state table (pf), offers the ability to search for specific states and removal.

-----------------------------------------
States Reset
-----------------------------------------

Delete all active states and source tracking (cancels connections)

.. Warning::

    Handle with care, a state reset will discard all active connections, in which case clients might have to reconnect

-----------------------------------------
States Summary
-----------------------------------------

Show states sorted by criteria like source IP, destination IP, …
