=================
Authoritative DNS
=================

.. contents:: Index

As part of the OPNsense Business Edition, Deciso offers a plugin for advanced DNS infrastructure requirements.

`OPNDNS` is based on `PowerDNS Authoritative <https://doc.powerdns.com/authoritative/>`__
and hosts DNS zones on OPNsense. It can manage static internal zones, reverse lookup zones,
and dynamic DNS updates from services such as :doc:`KEA DHCP </manual/kea>` using RFC2136.

It supports record types that are usually outside the scope of a recursive resolver, such as ``MX``, ``SRV`` and ``TXT``.

In a common setup, :doc:`Unbound DNS </manual/unbound>` remains the recursive resolver for clients and forwards
selected internal zones to this service.


--------------------------------
Considerations before deployment
--------------------------------


DNS role
--------

This service is not a recursive resolver. It only answers for zones configured locally.

It is intended primarily for internal authoritative DNS use cases, such as infrastructure zones,
reverse lookup zones and DHCP-driven dynamic updates. It is not meant to replace a dedicated public DNS
setup for internet-facing domains.

It should normally not replace :doc:`Unbound DNS </manual/unbound>` as the DNS server for clients.
Instead, keep Unbound on port ``53`` and forward selected internal zones to this service on another port,
for example ``53053``.

.. Note::

    Unbound resolves arbitrary DNS names for clients.
    This service only answers for zones it is authoritative for.


Records and RRsets
------------------

The GUI uses the term **record** for simplicity.

Technically, each record entry represents an RRset. An RRset is the combination of:

- one record name
- one record type
- one TTL
- one or more values

For example, two IPv4 addresses for the same host are stored as one ``A`` RRset with two values:

.. code-block:: text

    host1.internal. 300 IN A 192.168.1.10
    host1.internal. 300 IN A 192.168.1.11

In the GUI, this is entered as one record with ``host1`` as name, ``A`` as type, ``300`` as TTL,
and both IP addresses as separate values.


Zone types
----------

There are two zone types:

- ``static`` zones contain records managed through the GUI.
- ``allowupdate`` zones allow RFC2136 updates.

Static zones are intended for manually configured records, such as nameservers, infrastructure hosts,
service records and reverse lookup records.

Dynamic zones are intended for automatic updates, for example from :doc:`KEA DHCP </manual/kea>`.

.. Attention::

    Do not create manual records in dynamic zones unless you know exactly why they are needed.
    These zones are expected to be owned by RFC2136 update clients.


High availability
-----------------

A global role controls how the service behaves:

- ``Primary`` creates and manages zones and records.
- ``Secondary`` creates secondary zones and retrieves their contents from the configured peer.

The primary can allow one configured peer to transfer zones and can notify it when a zone changes.

.. Note::

    The HA design is intentionally simple. A single peer is configured globally and used for zone transfers
    and notifications.

    Using this service as a secondary for public DNS infrastructure is not recommended, even if it is technically possible.


----------------
General settings
----------------

Most settings are straightforward. Enable the service, choose the role, configure the listen port,
and optionally configure the HA peer.

.. tabs::

    .. tab:: General

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Enable**                                Enable the service.
        **Listen Port**                           Port used for DNS queries.
        **Role**                                  Choose whether this firewall acts as ``Primary`` or ``Secondary``.
        **Peer**                                  IP address and port of the peer DNS server. On a primary, this is used for
                                                  zone transfers and notifications. On a secondary, this is the primary server.
        **Disable HA sync**                       Prevent general settings from being synchronized between HA peers.
        ========================================= ====================================================================================

        .. Tip::

            When Unbound listens on port ``53``, configure this service on a different port such as ``53053``
            and forward the relevant zones from Unbound.

    .. tab:: SOA

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Primary nameserver**                    Primary nameserver used in the SOA record, for example ``ns1.internal``.
        **Responsible Mailbox**                   Responsible mailbox encoded as DNS name, for example ``hostmaster.internal``.
        **Refresh**                               Time in seconds after which a secondary checks the primary for zone updates.
        **Retry**                                 Time in seconds after which a secondary retries a failed refresh.
        **Expire**                                Time in seconds after which a secondary stops serving the zone if the primary
                                                  cannot be reached.
        **Minimum TTL**                           Minimum TTL used in the SOA record.
        ========================================= ====================================================================================

        .. Note::

            SOA records are generated automatically. They do not need to be created manually.

            If these settings are changed, existing zones must be deleted and recreated to receive updated SOA content.
            The serial is updated automatically on configuration changes and is used by secondary servers to detect updates.

    .. tab:: Log

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Log Level**                             Higher values log more details. Use high values only while debugging. Values can be
                                                  between 1 to 9.
        **Log DNS Queries**                       Log incoming DNS queries. This can generate large amounts of log data.
        **Log DNS Details**                       Log additional DNS packet details for debugging. This can be noisy.
        ========================================= ====================================================================================


-------------
Zone settings
-------------

Zones are configured in :menuselection:`Services --> Authoritative DNS --> Zones`.

.. tabs::

    .. tab:: Zones

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Zone Name**                             Name of the zone, for example ``internal`` or ``1.168.192.in-addr.arpa``.
        **Type**                                  ``static`` for GUI-managed zones, ``allowupdate`` for RFC2136 updates.
        **Allow Updates From**                    Network allowed to send RFC2136 updates. Only used with ``allowupdate`` zones.
        **Default TTL**                           Default time-to-live for records in this zone.
        **Description**                           Optional description for your reference.
        ========================================= ====================================================================================

        .. Attention::

            Zone names are stored without a trailing dot.

    .. tab:: Records

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Zone**                                  Zone this record belongs to.
        **Record Name**                           Record name. Use ``@`` for the zone apex or a relative name.
        **Type**                                  DNS record type, for example ``A``, ``AAAA``, ``NS``, ``MX``, ``PTR`` or ``TXT``.
        **TTL**                                   Optional record-specific TTL. If empty, the zone default is used.
        **Values**                                One or more record values. Use one value per line.
        **Description**                           Optional description for your reference.
        ========================================= ====================================================================================

        .. Note::

            A record entry with multiple values represents one RRset.

            Record names are relative to their zone and must not end with a trailing dot.

            Record values that reference DNS names should usually be fully qualified and end with a trailing dot.
            For example, ``NS``, ``MX``, ``CNAME`` and ``PTR`` targets should usually be entered as
            ``ns1.internal.`` instead of ``ns1.internal``.


----------------------
Configuration examples
----------------------

The following examples show a typical internal DNS setup with one forward zone and one reverse zone.

Unbound remains the DNS resolver for clients and forwards the local zones to this service.

The examples use:

- Forward zone: ``internal``
- Reverse zone for ``192.168.1.0/24``: ``1.168.192.in-addr.arpa``
- Nameservers: ``ns1.internal.`` and ``ns2.internal.``
- Listen port: ``53053``


Forward zone
--------------------

This example creates a static internal zone called ``internal``.

The zone contains two nameservers:

- ``ns1.internal.`` with IPv4 address ``192.168.1.2``
- ``ns2.internal.`` with IPv4 address ``192.168.1.3``

Go to :menuselection:`Services --> Authoritative DNS --> Settings --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53053``
**Role**                            ``Primary``
==================================  =======================================================================================================

Press **Apply**.

Go to :menuselection:`Services --> Authoritative DNS --> Settings --> SOA` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Primary nameserver**              ``ns1.internal``
**Responsible Mailbox**             ``hostmaster.internal``
**Refresh**                         ``10800``
**Retry**                           ``3600``
**Expire**                          ``604800``
**Minimum TTL**                     ``3600``
==================================  =======================================================================================================

Press **Apply**.

Go to :menuselection:`Services --> Authoritative DNS --> Zones` and add:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``internal``
**Type**                            ``static``
==================================  =======================================================================================================

Press **Save**.

Add the nameserver records for the new internal zone. If you do not use HA, you can skip the second nameserver value.

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Zone**                            ``internal``
**Name**                            ``@``
**Type**                            ``NS``
**TTL**                             ``300``
**Values**                          ``ns1.internal.``

                                    ``ns2.internal.``
==================================  =======================================================================================================

Press **Save**.

Create the A records for the nameservers.

.. tabs::

    .. tab:: ns1.internal

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Zone**                            ``internal``
        **Name**                            ``ns1``
        **Type**                            ``A``
        **TTL**                             ``300``
        **Values**                          ``192.168.1.2``
        ==================================  =======================================================================================================

        Press **Save**.

    .. tab:: ns2.internal

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Zone**                            ``internal``
        **Name**                            ``ns2``
        **Type**                            ``A``
        **TTL**                             ``300``
        **Values**                          ``192.168.1.3``
        ==================================  =======================================================================================================

        Press **Save** and **Apply**.

The zone now contains answers for ``internal.`` and both nameserver host records.

.. Tip::

    Test the result directly:

    .. code-block:: sh

        dig @127.0.0.1 -p 53053 internal NS
        dig @127.0.0.1 -p 53053 ns1.internal A
        dig @127.0.0.1 -p 53053 ns2.internal A

    If you do not have ``dig`` available yet, install it via ``pkg install bind-tools``.


Reverse zone
--------------------

A forward zone maps names to IP addresses.
A reverse zone maps IP addresses back to names.

Example:

- Forward zone: ``internal``
- Reverse zone for ``192.168.1.0/24``: ``1.168.192.in-addr.arpa``

Go to :menuselection:`Services --> Authoritative DNS --> Zones` and add:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``1.168.192.in-addr.arpa``
**Type**                            ``static``
==================================  =======================================================================================================

Press **Save**.

Here we reuse the nameservers of our static forward zone. If you do not use HA, you can skip the second nameserver value.

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Zone**                            ``1.168.192.in-addr.arpa``
**Name**                            ``@``
**Type**                            ``NS``
**TTL**                             ``300``
**Values**                          ``ns1.internal.``

                                    ``ns2.internal.``
==================================  =======================================================================================================

Press **Save**.

Create the reverse records (PTR) for the nameservers.

.. tabs::

    .. tab:: ns1 reverse record

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Zone**                            ``1.168.192.in-addr.arpa``
        **Name**                            ``2``
        **Type**                            ``PTR``
        **TTL**                             ``300``
        **Values**                          ``ns1.internal.``
        ==================================  =======================================================================================================

        Press **Save**.

    .. tab:: ns2 reverse record

        If you do not use HA, you can skip this record.

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Zone**                            ``1.168.192.in-addr.arpa``
        **Name**                            ``3``
        **Type**                            ``PTR``
        **TTL**                             ``300``
        **Values**                          ``ns2.internal.``
        ==================================  =======================================================================================================

        Press **Save** and **Apply**.

.. Tip::

    Test the reverse lookup directly:

    .. code-block:: sh

        dig @127.0.0.1 -p 53053 -x 192.168.1.2
        dig @127.0.0.1 -p 53053 -x 192.168.1.3


Forwarding from Unbound
-----------------------

Clients should normally query :doc:`Unbound DNS </manual/unbound>` on port ``53``.
Unbound can then forward only the locally hosted zones.

This keeps the client setup simple while separating recursive and authoritative DNS duties.

Go to :menuselection:`Services --> Unbound DNS --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53``
==================================  =======================================================================================================

Press **Apply**.

Go to :menuselection:`Services --> Unbound DNS --> Query Forwarding` and add forwarding entries for the zones.

.. tabs::

    .. tab:: Forward zone

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Domain**                          ``internal``
        **Server IP**                       ``127.0.0.1``
        **Server Port**                     ``53053``
        ==================================  =======================================================================================================

        Press **Save** and add the next entry.

    .. tab:: Reverse zone

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Domain**                          ``1.168.192.in-addr.arpa``
        **Server IP**                       ``127.0.0.1``
        **Server Port**                     ``53053``
        ==================================  =======================================================================================================

        Press **Save** and **Apply**.

When a client queries Unbound for ``ns1.internal.``, the request is forwarded to ``127.0.0.1:53053``.
The local service answers for the zone and Unbound returns the response to the client.

.. Note::

    Forwarding only applies to the configured domains.
    Internet DNS resolution continues to be handled by Unbound normally.


Dynamic DNS with KEA DHCP (RFC2136)
-----------------------------------

:doc:`KEA DHCP </manual/kea>` can register client FQDNs through dynamic DNS updates using RFC2136.

This example registers DHCP clients in forward and reverse zones.

The example uses:

- Parent zone: ``internal``
- Forward zone: ``dhcp.internal``
- Reverse zone: ``1.168.192.in-addr.arpa``
- Nameservers: ``ns1.internal.`` and ``ns2.internal.``
- DHCP subnet: ``192.168.1.0/24``
- DHCP pool: ``192.168.1.100 - 192.168.1.199``
- DNS server: ``127.0.0.1``
- DNS server port: ``53053``

Go to :menuselection:`Services --> Authoritative DNS --> Zones` and add:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``dhcp.internal``
**Type**                            ``allowupdate``
**Allow Updates From**              ``127.0.0.1`` ``192.168.1.3``
==================================  =======================================================================================================

Press **Save**.

.. Note::

    The IP address ``192.168.1.3`` represents the secondary DNS server in an HA setup.
    You can omit this address when HA is not used.

    By default, PowerDNS forwards RFC2136 updates received by a secondary zone to
    the configured primary server. Allowing the secondary DNS server here lets the
    primary accept those forwarded updates.

    This is useful when Kea is active on the backup OPNsense node. Kea sends its
    updates to the local secondary server, which then forwards them to the primary
    server where the update is applied.


Then add an NS record for the zone. If you do not use HA, you can skip the second nameserver value.

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Zone**                            ``dhcp.internal``
**Name**                            ``@``
**Type**                            ``NS``
**TTL**                             ``300``
**Values**                          ``ns1.internal.``

                                    ``ns2.internal.``
==================================  =======================================================================================================

Press **Save**.

.. Note::

    This example reuses the nameservers from the already configured ``internal`` zone.

    The nameserver host records, such as ``ns1.internal.`` and ``ns2.internal.``, are defined in the parent zone.
    The dynamic ``dhcp.internal`` zone only references them with its own NS record.

Go to :menuselection:`Services --> Authoritative DNS --> Zones` and add a new reverse zone.
If you already created the reverse zone earlier just change it accordingly.

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``1.168.192.in-addr.arpa``
**Type**                            ``allowupdate``
**Allow Updates From**              ``127.0.0.1``
==================================  =======================================================================================================

Press **Save**.

Then add an NS record for the reverse zone if they do not already exist. If you do not use HA, you can skip the second nameserver value.

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Zone**                            ``1.168.192.in-addr.arpa``
**Name**                            ``@``
**Type**                            ``NS``
**TTL**                             ``300``
**Values**                          ``ns1.internal.``

                                    ``ns2.internal.``
==================================  =======================================================================================================

Press **Save** and **Apply**.

.. Note::

    The reverse zone also uses the same nameservers.

    The PTR records themselves are created dynamically by KEA through RFC2136 updates.
    The NS record only defines which nameservers are responsible for the reverse zone.

.. Attention::

    Do not forget to add forwards from Unbound for these zones.

Go to :menuselection:`Services --> KEA DHCP --> KEA DHCPv4`, select a subnet and enable advanced mode.

==================================  =======================================================================================================
**Option**                          **Value**
==================================  =======================================================================================================
Subnet                              ``192.168.1.0/24``
Pools                               ``192.168.1.100 - 192.168.1.199``

**DHCP option data**
Auto collect option data            Unchecked
Routers                             ``192.168.1.1``
DNS servers                         ``192.168.1.1``
Domain name                         ``dhcp.internal``

**Dynamic DNS**
DNS forward zone                    ``dhcp.internal.``
DNS reverse zone                    ``1.168.192.in-addr.arpa.``
DNS qualifying suffix               ``dhcp.internal.``
DNS server                          ``127.0.0.1``
DNS server port                     ``53053``
Override no update                  ``X``
Override client update              ``X``
Update on renew                     ``X``
==================================  =======================================================================================================

.. Attention::

    The zones and qualifying suffix must end with a trailing dot.

    If you want to update both IPv4 and IPv6 records of dual stack hosts, set conflict resolution mode to ``no-check-with-dhcid``.

    If certain hosts should get registered with custom hostnames, create a host reservation for them.

Go to :menuselection:`Services --> KEA DHCP --> DDNS Agent` and set:

==================================  =======================================================================================================
**Option**                          **Value**
==================================  =======================================================================================================
Enabled                             ``X``
Bind address                        ``127.0.0.1``
Bind port                           ``53001``
==================================  =======================================================================================================

Press **Apply**.

.. Note::

    This example does not use a TSIG key.
    The communication is local and ``Allow Updates From`` restricts which clients can update the zone.

For a general DHCP setup, see :doc:`KEA DHCP </manual/kea>`.


High availability setup
-----------------------

This example uses two OPNsense firewalls:

- Primary: ``192.168.1.2``
- Secondary: ``192.168.1.3``

The primary manages the zones and allows the secondary to transfer them.


Primary
~~~~~~~

Go to :menuselection:`Services --> Authoritative DNS --> Settings --> General` on the primary and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53053``
**Role**                            ``Primary``
**Peer**                            ``192.168.1.3:53053``
**Disable HA sync**                 ``X``
==================================  =======================================================================================================

Press **Apply**.

Create static and dynamic zones on the primary as usual.
It manages the records and increases the zone serial on each **Apply** or when an RFC2136 client updates a record.


Secondary
~~~~~~~~~

Go to :menuselection:`Services --> Authoritative DNS --> Settings --> General` on the secondary and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53053``
**Role**                            ``Secondary``
**Peer**                            ``192.168.1.2:53053``
**Disable HA sync**                 ``X``
==================================  =======================================================================================================

Press **Apply**.

For a secondary server, records are not managed locally.
The zone contents are received from the primary through zone transfer.

Add ``Authoritative DNS`` to :menuselection:`System --> High Availability --> Settings --> Services to synchronize`.
The zones on the secondary are created when HA synchronization is triggered in
:menuselection:`System --> High Availability --> Status`.

After the first sync, the secondary performs an AXFR zone transfer.
Further changes are announced through NOTIFY messages.

It is recommended to transfer zones over the same link used for HA sync.
TCP must be allowed between both nodes on the configured listen port.

.. Attention::

    The secondary is read-only. Records sync automatically via standard DNS zone transfers, you do not need any cron jobs for the HA sync.

    RFC2136 updates must be sent to the primary. During failover, the secondary continues to serve the latest transferred zone state.


------------
Good to know
------------


Trailing dots
-------------

Zone names are stored without a trailing dot:

.. code-block:: text

    internal
    1.168.192.in-addr.arpa

Record names are relative to the zone and must not end with a trailing dot.

Record values that reference DNS names should usually be fully qualified and end with a trailing dot:

.. code-block:: text

    ns1.internal.

For example:

- Record name: ``ns1``
- Record value: ``ns1.internal.``


SOA records
-----------

An SOA record defines basic authority and timing information for a zone.
It contains the primary nameserver, responsible mailbox, zone serial and refresh timers used by secondary servers.

SOA records are generated automatically from the SOA settings.

They cannot be created manually as records in the GUI.
To regenerate SOA content, delete and recreate the zone.


NS records
----------

NS records define which nameservers are responsible for a zone.

Configure NS records explicitly for every zone.

For a zone named ``internal``, a simple setup could use:

.. code-block:: text

    internal. 300 IN NS ns1.internal.
    internal. 300 IN NS ns2.internal.

Additional zones can use the same nameservers.

Nameservers should also have matching address records.
For reverse lookups, create corresponding PTR records as well.


Serial handling
---------------

When static zone content changes, the zone serial is increased so that secondary servers can detect updates.

Secondary systems should not manage records directly.


DHCP search domain
------------------

Clients can resolve short hostnames when DHCP provides a search domain.

For example, if :doc:`KEA DHCP </manual/kea>` sends ``dhcp.internal`` as the domain name,
a client may resolve ``host1`` as ``host1.dhcp.internal``.

.. Note::

    Short name resolution depends on the client resolver behavior and the DHCP options it receives.

    DNS itself still stores and answers for fully qualified names. The search domain is only applied by the client.


Firewall rules
--------------

If clients or peers query the service directly, allow TCP and UDP traffic to the configured listen port.

For zone transfers, TCP must be allowed between primary and secondary.

.. Tip::

    DNS queries commonly use UDP.
    Zone transfers require TCP.


Testing
-------

Test direct queries before configuring Unbound forwarding.

.. code-block:: sh

    dig @127.0.0.1 -p 53053 internal SOA
    dig @127.0.0.1 -p 53053 internal NS
    dig @127.0.0.1 -p 53053 ns1.internal A
    dig @127.0.0.1 -p 53053 -x 192.168.1.2

If direct queries work but client queries fail, check the Unbound forwarding configuration first.

If you do not have ``dig`` available yet, install it via ``pkg install bind-tools``.


Log and diagnostics
-------------------

If queries do not return the expected result, check:

- service status
- listen port
- Unbound forwarding entries
- firewall rules
- zone existence
- expected records
- relative record names
- trailing dots in record values where required

.. Attention::

    A query for ``host.internal`` only reaches the local zone when Unbound has a forwarding entry for ``internal``.

    Without forwarding, Unbound tries to resolve the name normally and does not automatically know about the locally hosted zone.
