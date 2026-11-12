===========================
Hostwatch
===========================

.. contents:: Index


--------------------
Overview
--------------------

The Hostwatch service offers a way to discover most neighbors on the network via their ARP and NDP messages.
When the daemon is activated, it builds a database of known neighbors and logs when IP address to MAC mappings change.

This can be useful to see how volatile a network is and if unknown new hosts appear.

Running the daemon improves some services that currently directly consume the ARP and NDP tables. The database has a persistent state,
can be queried faster, and for IPv6 will have a better picture of RFC 4941 addresses.

The following consumers use Hostwatch when it is running and fall back to the kernel ARP/NDP tables otherwise, depending on the address family:

* :doc:`Captive portal <captiveportal>`: collects client IP addresses.
* :doc:`MAC address aliases <aliases>`: resolve MAC addresses to IPv4 and IPv6 addresses.
* :doc:`Kea <kea>`: looks up clients' IPv6 link-local addresses for delegated prefix routes.


--------------------
Settings
--------------------

Settings can be found in :menuselection:`Interfaces --> Hostwatch --> Settings`

==============================================================================================================================================

=========================== ==================================================================================================================
**Enable**                  Enable the "hostwatch" service to discover network hosts.
**Interfaces**              Limit host discovery to the interfaces selected here.
**Promiscuous mode**        Listening for network packets not targeted directly at us.
**Verbose logging**         Verbosity mode, send more detailed information to the log.
**Expire/cleanup IPv4**     Remove IPv4 registrations after the configured number of seconds (minimum 3600, or 1 hour).
                            When unset, addresses are archived indefinitely and reported when seen again after a longer period of time.
**Expire/cleanup IPv6**     Remove IPv6 registrations after the configured number of seconds (minimum 3600, or 1 hour).
                            When unset, addresses are archived indefinitely and reported when seen again after a longer period of time.
**Ignore networks**         Ignore the selected networks.
=========================== ==================================================================================================================

.. Attention::

    The service will only listen on ethernet interfaces. Tunnel, loopback and similar interfaces are skipped since there is no ARP/NDP traffic.

.. Tip::

    Promiscuous mode is rarely needed. The firewall is in a central position and routes traffic between networks. The setting makes sense in a network
    where it would only be an observer.


--------------------
Hosts
--------------------

Open :menuselection:`Interfaces --> Hostwatch --> Hosts` to view discovered hosts.

If the host discovery service is enabled, you can see the contents of the database in this table. Otherwise, it will show the current contents of the
kernel ARP and NDP tables.

An interesting metric can be the **Last Seen** column, which shows hosts that have recently joined or not seen for a while.

The **Hostname** column tries to gather the current reverse DNS entry of each discovered host.

The **Statistics** column shows the number of active firewall states and the traffic observed for each discovered IP address.
These values come from the runtime firewall state table and are not persistent or intended as historical traffic accounting.

.. Hint::

    Restricted GUI users need the **Interfaces: Hostwatch** privilege to access this page. Grant
    **Interfaces: Diagnostics: DNS Lookup** to display hostnames and **Diagnostics: Show States** to display statistics.


--------------------
Log File
--------------------

Open :menuselection:`Interfaces --> Hostwatch --> Log File` to view the discovery log.

In the discovery log, you can find entries for new stations (hosts) and movements.

These logs have a simple structure, and could be consumed by an external syslog server for further processing (e.g., alerts for new stations).

If the log is busy with a lot of movements that look like flapping, something could be wrong in your network. Most common would be MAC address duplication,
or multiple hosts fighting for the same IP address.

.. Tip::

    To configure static IPv4/IPv6 to MAC address mappings, use :doc:`neighbors`.
