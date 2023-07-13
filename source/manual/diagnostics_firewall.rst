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

The following fields are available in the grid:

==========================================================================================================================

========================= ================================================================================================
Dir                       Direction (in :code:`->` or out :code:`<-`)
Proto                     Protocol in question
Source                    Source address and port
Gateway                   Address and port this session is being translated too using NAT
Destination               Destination address and port
State                     State at source:destination, see tables in States section
Age (sec)                 The number of seconds since the state is created
Expires (sec)             The number of seconds left before the state expires.
Pkts                      Number of packets processed by the state
Bytes                     Number of bytes processed by the state
Rule                      Rule this state (most likely) belongs to
========================= ================================================================================================



-----------------------------------------
States
-----------------------------------------

Insight into the state table (pf), offers the ability to search for specific states and removal.
It is also possible to reset all states and/or the source tracking tables from here, especially the state table
reset should be used with care as it drops all active connections.

If you use the grid search input to look for states, or you used the **Inspect** button on the firewall rules page and
opened the state view, you will see a button that allows you to kill all states that matched the criteria.

.. Note::

    The state table tries to connect states to rules, but since these are refered to by rule number (sequence) in :code:`pf(4)`
    these aren't always accurate after changes to the rules.

The following fields are available in the grid:

==========================================================================================================================

========================= ================================================================================================
State id                  Unique internal identifier describing the state and the origin (creator)
Int                       Bound to which interface, by default this is all unless " Bind states to interface" is set
                          in :menuselection:`Firewall->Settings->Advanced`
Dir                       Direction (in :code:`->` or out :code:`<-`)
Proto                     Protocol in question
Source                    Source address and port
Nat                       Address and port this session is being translated too using NAT
Destination               Destination address and port
State                     State at source:destination,
                          see next tables for lists of states and their explanations available
Rule                      Rule this state (most likely) belongs to
Command                   Button to drop a specific state (State id)
========================= ================================================================================================


List of available TCP states (as defined by `RFC 793 <https://www.rfc-editor.org/rfc/rfc793>`__)
==========================================================================================================================

========================= ================================================================================================
LISTEN                    Represents waiting for a connection request from any remote TCP and port.
SYN_SENT                  Represents waiting for a matching connection request after having sent a connection request.
SYN_RCVD                  Represents waiting for a confirming connection request acknowledgment
                          after having both received and sent a connection request.
ESTABLISHED               Represents an open connection, data received can be delivered to the user.
                          The normal state for the data transfer phase of the connection.
FIN_WAIT_1                Represents waiting for a connection termination request from the remote TCP,
                          or an acknowledgment of the connection termination request previously sent.
FIN_WAIT_2                Represents waiting for a connection termination request from the remote TCP.
CLOSE_WAIT                Represents waiting for a connection termination request from the local user.
CLOSING                   Represents waiting for a connection termination request acknowledgment from the remote TCP.
LAST_ACK                  Represents waiting for an acknowledgment of the connection termination request
                          previously sent to the remote TCP (which includes an acknowledgment of
                          its connection termination request).
TIME_WAIT                 Represents waiting for enough time to pass to be sure the remote TCP received the
                          acknowledgment of its connection termination request.
CLOSED                    Represents no connection state at all
==========================================================================================================================

List of available UDP/Other states (man `pf.conf(5) <https://www.freebsd.org/cgi/man.cgi?pf.conf(5)>`__)
==========================================================================================================================

========================= ================================================================================================
NO_TRAFFIC                No traffic for this direction
SINGLE                    The state if the source host sends more than one packet but the destination host has never sent one back.
MULTIPLE                  The state if both hosts have sent packets.
========================= ================================================================================================


-----------------------------------------
Statistics
-----------------------------------------

Various detailed statistics gathered from `pfctl <https://www.freebsd.org/cgi/man.cgi?query=pfctl>`__,
such as packet counters per interface, memory limits, configured timeouts and detailed active rules.
