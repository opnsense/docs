===========
Diagnostics
===========

-----------------------------------------
Aliases
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
Sessions
-----------------------------------------

Utilises `pftop <https://www.freebsd.org/cgi/man.cgi?query=pftop>`__ to offer a detailed view on the active sessions
and their traffic counters.

-----------------------------------------
States
-----------------------------------------

Insight into the state table (pf), offers the ability to search for specific states and removal.
It is also possible to reset all states and/or the source tracking tables from here, especially the state table
reset should be used with care as it drops all active connections.

-----------------------------------------
Statistics
-----------------------------------------

Various detailed statistics gathered from `pfctl <https://www.freebsd.org/cgi/man.cgi?query=pfctl>`__,
such as packet counters per interface, memory limits, configured timeouts and detailed active rules.
