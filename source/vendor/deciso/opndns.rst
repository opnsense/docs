==========================
Authoritative DNS
==========================

.. contents:: Index

As part of the OPNsense Business Edition, Deciso offers a plugin for advanced DNS infrastructure requirements.

`OPNDNS` uses `PowerDNS Authoritative` to host DNS zones on OPNsense.

It can be used to manage internal static DNS zones, serve reverse lookup zones, and receive dynamic DNS updates
from services such as :doc:`KEA DHCP </manual/kea>` using RFC2136.

It can configure more record types than a DNS Recurser, e.g., MX, SRV and TXT records.

In a common setup, :doc:`KEA DHCP </manual/unbound>` remains the recursive DNS resolver for clients and forwards selected internal zones
to Authoritative DNS.


---------------------------------
Considerations before deployment
---------------------------------


DNS Service
-----------------------------

`PowerDNS Authoritative` is not a recursive resolver. It only answers for zones it is authoritative for.

This means it should normally not replace `Unbound DNS` as the DNS server for clients. Instead, `Unbound DNS` should continue to listen on port ``53``
and forward selected internal zones to Authoritative DNS running on another port, e.g. ``53053``.

.. Note::

    `Unbound` is a recursive resolver, `PowerDNS Authoritative` is an authoritative DNS server.
    PowerDNS answers only for configured zones and does not resolve arbitrary internet domains.


Static and Dynamic Zones
-----------------------------

There are two zone types:

- ``Static`` zones only consist of static records that are managed via the GUI.
- ``Dynamic`` (allowupdate) zones are a mix of static records and RFC2136 updates.

Static zones are intended for manually configured records such as nameservers, infrastructure hosts, service records, and reverse lookup records.

Dynamic zones are intended for automatic DNS updates, for example from `KEA DHCP`.


High Availability
-----------------------------

PowerDNS can be configured with a global role:

- ``Primary`` creates and manages zones and records.
- ``Secondary`` creates secondary zones and retrieves them from the configured primary server.

The primary server can allow zone transfers to one configured peer and send notifications to it when a zone changes.

.. Note::

    The HA design is intentionally simple. A single peer is configured globally and used for zone transfer and notification handling.
    It is not recommended to use the Authoritative DNS server as a secondary of a public DNS server, even if that is technically possible.


Installation
---------------------------

To install this plugin, go to :menuselection:`System --> Firmware --> Plugins` and search for **os-OPNDNS**,
the [+] button downloads and installs the software.

Next go to :menuselection:`Services --> Authoritative DNS --> Settings` to enable it.


-------------------------
General Settings
-------------------------

Most settings are straightforward. Enable the service, choose the role, configure the listen port, and optionally configure the HA peer.

.. tabs::

    .. tab:: General

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Enable**                                Enable Authoritative DNS.
        **Listen Port**                           The port used for responding to DNS queries.
        **Role**                                  Choose if this firewall acts as ``Primary`` or ``Secondary``.
        **Peer**                                  IP address and port of the peer DNS server. On a primary this is used for
                                                  zone transfers and notify handling. On a secondary this is used as the primary server.
        **Disable HA sync**                       Ignore the general settings from being synced between HA peers.
        ========================================= ====================================================================================

        .. Tip::

            When Unbound listens on port ``53``, configure Authoritative DNS on a different port such as ``53053`` and forward the relevant zones from Unbound.

    .. tab:: SOA

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Primary nameserver**                    The primary nameserver used in the SOA record, e.g. ``ns1.internal``.
        **Responsible Mailbox**                   The responsible mailbox encoded as DNS name, e.g. ``hostmaster.internal``.
        **Refresh**                               Time in seconds after which a secondary should check the primary for zone updates.
        **Retry**                                 Time in seconds after which a secondary should retry a failed refresh.
        **Expire**                                Time in seconds after which a secondary should stop serving the zone if the primary
                                                  cannot be reached.
        **Minimum TTL**                           Minimum TTL used in the SOA record.
        ========================================= ====================================================================================

        .. Note::

            SOA records are generated automatically by PowerDNS. They do not need to be created manually as RRsets.
            If you change settings here, you must manually delete and recreate zones to get updated SOA records.
            They cannot be manually configured since they have a serial that is updated automatically on configuration changes.
            That serial is the trigger if a zone should be transfered to a secondary DNS server.

-------------------------
Zone Settings
-------------------------

Zones are configured in :menuselection:`Services --> Authoritative DNS --> Zones`.

.. tabs::

    .. tab:: Zones

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Zone Name**                             Name of the zone, e.g. ``internal`` or ``1.168.192.in-addr.arpa``.
        **Type**                                  ``static`` for zones managed by the GUI, ``allowupdate`` for zones managed through RFC2136.
        **Allow Updates From**                    Network allowed to send RFC2136 updates for this zone. Only used when the zone type is ``allowupdate``.
        **Default TTL**                           Default time-to-live used for records in this zone.
        **Description**                           You may enter a description here for your reference.
        ========================================= ====================================================================================

        .. Attention::

            Zone names are stored without a trailing dot.

    .. tab:: RRsets

        ========================================= ====================================================================================
        **Option**                                **Description**
        ========================================= ====================================================================================
        **Zone**                                  Zone this record belongs to.
        **Record Name**                           Record name. Use ``@`` for the zone apex or the full relative record name.
        **Type**                                  DNS record type, e.g. ``A``, ``AAAA``, ``NS``, ``MX``, ``PTR``, ``TXT``.
        **TTL**                                   Optional record-specific TTL. If empty, the zone default is used.
        **Values**                                One or multiple record values. Use one value per line.
        **Description**                           You may enter a description here for your reference.
        ========================================= ====================================================================================

        .. Note::

            Some record values must be fully qualified DNS names and should end with a trailing dot.
            For example, NS, MX, CNAME and PTR targets should usually be entered as ``ns1.internal.`` instead of ``ns1.internal``.

        .. Attention::

            Record names are relative to their zone and must not end with a trailing dot.


---------------------------------
Configuration examples
---------------------------------

Static internal zone
--------------------------------------------------

In this example, Authoritative DNS hosts a static internal zone called ``internal``.

The zone contains two nameservers:

- ``ns1.internal.`` with IPv4 address ``192.168.1.2``
- ``ns2.internal.`` with IPv4 address ``192.168.1.3``

Unbound remains the resolver for clients and forwards the ``internal`` zone to Authoritative DNS.

- Go to :menuselection:`Services --> Authoritative DNS --> Settings --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53053``
**Role**                            ``Primary``
==================================  =======================================================================================================

- Press **Apply**

- Go to :menuselection:`Services --> Authoritative DNS --> Settings --> SOA` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Primary nameserver**              ``ns1.internal``
**Hostmaster**                      ``hostmaster.internal``
**Refresh**                         ``10800``
**Retry**                           ``3600``
**Expire**                          ``604800``
**Minimum TTL**                     ``3600``
==================================  =======================================================================================================

- Press **Apply**

Now create the static zone.

- Go to :menuselection:`Services --> Authoritative DNS --> Zones` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Type**                            ``static``
**Name**                            ``internal``
==================================  =======================================================================================================

- Press **Save**

Afterwards, create the NS records.

- Go to :menuselection:`Services --> Authoritative DNS --> RRsets` and add:

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

- Press **Save**

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

        - Press **Save**

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

        - Press **Save** and **Apply**

Now the zone contains authoritative answers for ``internal.`` and the two nameserver host records.

.. Tip::

    Test the result directly against Authoritative DNS:

    .. code-block:: sh

        dig @127.0.0.1 -p 53053 internal NS
        dig @127.0.0.1 -p 53053 ns1.internal A
        dig @127.0.0.1 -p 53053 ns2.internal A


Forward and reverse zones
--------------------------------------------------

A forward zone maps names to IP addresses. A reverse zone maps IP addresses back to names.

For example:

- Forward zone: ``internal``
- Reverse zone for ``192.168.1.0/24``: ``1.168.192.in-addr.arpa``

Create the reverse zone first.

- Go to :menuselection:`Services --> Authoritative DNS --> Zones` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``1.168.192.in-addr.arpa``
**Type**                            ``static``
==================================  =======================================================================================================

- Press **Save**

Create the NS record for the reverse zone.

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

- Press **Save**

Create PTR records for the nameservers.

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

        - Press **Save**

    .. tab:: ns2 reverse record

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Zone**                            ``1.168.192.in-addr.arpa``
        **Name**                            ``3``
        **Type**                            ``PTR``
        **TTL**                             ``300``
        **Values**                          ``ns2.internal.``
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**

.. Tip::

    Test the reverse lookup directly against Authoritative DNS:

    .. code-block:: sh

        dig @127.0.0.1 -p 53053 -x 192.168.1.2
        dig @127.0.0.1 -p 53053 -x 192.168.1.3


Forwarding from Unbound
--------------------------------------------------

Clients should normally query Unbound on port ``53``. Unbound can then forward only the zones hosted by Authoritative DNS.

This keeps the client setup simple and still allows PowerDNS to run as authoritative service.

- Go to :menuselection:`Services --> Unbound DNS --> General` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53``
==================================  =======================================================================================================

- Press **Apply**

- Go to :menuselection:`Services --> Unbound DNS --> Query Forwarding` and create entries for the zones hosted by Authoritative DNS.

.. tabs::

    .. tab:: Forward zone

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Domain**                          ``internal``
        **Server IP**                       ``127.0.0.1``
        **Server Port**                     ``53053``
        ==================================  =======================================================================================================

        - Press **Save** and add next

    .. tab:: Reverse zone

        ==================================  =======================================================================================================
        Option                              Value
        ==================================  =======================================================================================================
        **Domain**                          ``1.168.192.in-addr.arpa``
        **Server IP**                       ``127.0.0.1``
        **Server Port**                     ``53053``
        ==================================  =======================================================================================================

        - Press **Save** and **Apply**

When a client queries Unbound for ``ns1.internal.``, Unbound forwards the request to Authoritative DNS on ``127.0.0.1:53053``.
It answers authoritatively and Unbound returns the response to the client.

.. Note::

    This forwarding only applies to the configured domains. Internet DNS resolution continues to be handled by Unbound normally.


Dynamic DNS with KEA DHCP
--------------------------------------------------

KEA allows registering client FQDNs via dynamic DNS (RFC2136).

In this example, KEA registers DHCP clients in forward and reverse zones hosted by Authoritative DNS.

The example uses:

- Forward zone: ``dhcp.internal``
- Reverse zone: ``1.168.192.in-addr.arpa``
- DHCP subnet: ``192.168.1.0/24``
- DHCP pool: ``192.168.1.100 - 192.168.1.199``
- Authoritative DNS server: ``127.0.0.1``
- Authoritative DNS port: ``53053``

Create the forward dynamic zone.

- Go to :menuselection:`Services --> Authoritative DNS --> Zones` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``dhcp.internal``
**Type**                            ``allowupdate``
**Allow Updates From**              ``127.0.0.1``
==================================  =======================================================================================================

- Press **Save**

Create the reverse dynamic zone.

- Go to :menuselection:`Services --> Authoritative DNS --> Zones` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Name**                            ``1.168.192.in-addr.arpa``
**Type**                            ``allowupdate``
**Allow Updates From**              ``127.0.0.1``
==================================  =======================================================================================================

- Press **Save** and **Apply**

Configure the DHCPv4 subnet in KEA.

- Go to :menuselection:`Services --> KEA DHCP --> KEA DHCPv4` and select a subnet (enable advanced mode):

==================================  =======================================================================================================
**Option**                          **Value**
==================================  =======================================================================================================
Subnet                              ``192.168.1.0/24``
Pools                               ``192.168.1.100 - 192.168.1.199``

**DHCP option data**
Auto collect option data            (This must be unchecked)
Routers (gateway)                   ``192.168.1.1``
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

Next, enable the KEA DDNS Agent.

- Go to :menuselection:`Services --> KEA DHCP --> DDNS Agent` and set:

==================================  =======================================================================================================
**Option**                          **Value**
==================================  =======================================================================================================
Enabled                             ``X``
Bind address                        ``127.0.0.1``
Bind port                           ``53001``
==================================  =======================================================================================================

- Press **Apply**

.. Note::

    For this Authoritative DNS example, no TSIG key is configured. The communication is local and the `Allow Updates From` ACL prevents external
    clients from updating the zone.

.. Attention::

    Do not create manual RRsets (other than NS) in a dynamic zone unless you know exactly why they are needed.
    The zone is expected to be owned by RFC2136 update clients.

For a general KEA DHCP setup, see :doc:`KEA DHCP </manual/kea>`.


High Availability setup
--------------------------------------------------

In this example, two OPNsense firewalls run Authoritative DNS.

- Primary: ``192.168.1.2``
- Secondary: ``192.168.1.3``

The primary manages the zones and allows the secondary to transfer them.

Master
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Go to :menuselection:`Services --> Authoritative DNS --> Settings -> General` on the master and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53053``
**Role**                            ``Primary``
**Peer**                            ``192.168.1.3:53053``
**Disable HA sync**                 ``X`` (this prevents the general settings to be synced and overwrite the configuration of the backup)
==================================  =======================================================================================================

- Press **Apply**

Create static and dynamic zones on the Master as usual, it will manage these records and increase the zone serial on each `Apply`` or when an
RFC2136 client updates a record.

Backup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Go to :menuselection:`Services --> Authoritative DNS --> Settings -> General` on the backup and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**Listen Port**                     ``53053``
**Role**                            ``Secondary``
**Peer**                            ``192.168.1.2:53053``
**Disable HA sync**                 ``X`` (this prevents the general settings to be overwritten by the master)
==================================  =======================================================================================================

- Press **Apply**

For a secondary server, RRsets are not managed locally. The secondary receives zone contents from the primary through zone transfer.

The zones on the secondary will be created when the HA synchronization is triggered in :menuselection:`System --> High Availability --> Status`.
Do not forget to add `Authoritative DNS` to `Services to synchronize (XMLRPC Sync)`.

As soon as the first HA sync is done, there will be an AXFR zone transfer. Any further changes will be notified via NOTIFY messages.

It is recommended to do the zone transfers over the same link that runs the HA sync. 
For zone transfers, TCP must be allowed between primary and secondary on the configured listen port.

.. Attention::

    The secondary DNS server is read-only. RFC2136 updates will only happen on the primary DNS server, never on the secondary.
    When a failover happens, the secondary DNS server will continue to serve the transfered zones and records in the state since the last transfer.


---------------------------------
Good to know
---------------------------------

Authoritative only
-----------------------------

PowerDNS Authoritative does not resolve internet names.

Use Unbound for normal client DNS resolution and forward only selected zones to Authoritative DNS.


Trailing dots
-----------------------------

Zone names are stored without a trailing dot, e.g. ``internal`` or ``1.168.192.in-addr.arpa``.

Record names are relative to the zone and should not end with a trailing dot.

Record values that reference DNS names should usually be fully qualified and end with a trailing dot, e.g. ``ns1.internal.``.

.. Note::

    This distinction is important:

    - Record name: ``ns1``
    - Record value: ``ns1.internal.``


SOA records
-----------------------------

SOA records are generated automatically based on the configured SOA settings.

You cannot create SOA RRsets manually. If you want to regenerate the SOA RRsets, you must delete and recreate the zone.


NS records
-----------------------------

NS records should be configured explicitly for every static zone.

For an internal zone named ``internal``, a simple setup could use:

.. code-block:: text

    internal. 300 IN NS ns1.internal.
    internal. 300 IN NS ns2.internal.

Additional zones can use the same nameservers, as it is authoritative for all zones you create on it.

Do not forget, nameservers also need A and PTR records for their own names. Usually these are called `Glue Records`.


Serial handling
-----------------------------

When static zone content changes, the zone serial is increased so that secondary servers can detect updates.

Secondary systems should not manage RRsets directly.


Firewall rules
-----------------------------

If clients or peer servers query Authoritative DNS directly, firewall rules must allow TCP and UDP traffic to the configured listen port.

For zone transfers, TCP must be allowed between primary and secondary.

.. Tip::

    DNS queries commonly use UDP, but zone transfers require TCP.


Testing
-----------------------------

Authoritative DNS can be tested directly with ``dig`` before Unbound forwarding is configured.

Examples:

.. code-block:: sh

    dig @127.0.0.1 -p 53053 internal SOA
    dig @127.0.0.1 -p 53053 internal NS
    dig @127.0.0.1 -p 53053 ns1.internal A
    dig @127.0.0.1 -p 53053 -x 192.168.1.2

If direct queries work but client queries fail, check the Unbound query forwarding configuration first.


Log and diagnostics
-----------------------------

If Authoritative DNS does not answer as expected, check:

- The PowerDNS service status.
- The configured listen port.
- Whether Unbound forwards the correct zone.
- Whether firewall rules allow the query.
- Whether the zone exists and contains the expected RRsets.
- Whether record names are relative and record values use trailing dots where required.

.. Attention::

    A query for ``host.internal`` only reaches Authoritative DNS when Unbound has a forwarding entry for ``internal``.
    Without forwarding, Unbound will try to resolve the name normally and will not automatically know about the local authoritative zone.
