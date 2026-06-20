Cloudflare Tunnel
=================

Introduction
------------

`Cloudflare Tunnel <https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/>`_
(formerly Argo Tunnel) allows you to expose self-hosted services to the internet
without opening inbound firewall ports or holding a public IP address. This makes
it well-suited for deployments behind CGNAT, ISPs that block inbound connections,
or networks where port forwarding is unavailable or undesirable.

The tunnel daemon (`cloudflared`) runs on the router, establishes outbound-only
connections to Cloudflare's edge, and forwards incoming HTTP/S and other proxied
traffic from Cloudflare to the backend services you configure in the Cloudflare
Zero Trust dashboard. Firewall policy for tunnelled services is enforced in
Cloudflare Access, not on OPNsense.

This plugin wraps the ``net/cloudflared`` FreeBSD port and requires a free
Cloudflare account with the Zero Trust dashboard enabled.

.. Warning::
    Traffic received via the Cloudflare Tunnel bypasses OPNsense firewall rules.
    Access control for tunnelled services must be enforced within Cloudflare Access.
    Backend services must also be reachable from the router's own IP address, as
    cloudflared forwards connections from the router itself.

Installation
------------

Install the ``os-cloudflared`` plugin from :menuselection:`System --> Firmware --> Plugins`.
Once installed, refresh the page — a new :menuselection:`Services --> Cloudflare Tunnel`
menu entry will appear.

To obtain a tunnel token:

1. Log in to the `Cloudflare Zero Trust dashboard <https://one.dash.cloudflare.com/>`_.
2. Navigate to :menuselection:`Networks --> Connectors`.
3. Click **Create a tunnel**, select **Cloudflared** as the connector type, and give
   the tunnel a name.
4. On the next page, copy the tunnel token (the long string shown in the install
   command). You only need the token itself — not the full command. The dashboard shows
   OS-specific install commands — ignore the OS selector and copy the long token string
   at the end of the command.

Settings
--------

Navigate to :menuselection:`Services --> Cloudflare Tunnel --> Settings`.

.. csv-table::
   :header: "Field", "Description"
   :widths: 20, 80

   "Enable", "Start the cloudflared service at boot and keep it running."
   "Tunnel Token", "Tunnel token from the Cloudflare Zero Trust dashboard."
   "Protocol", "Transport protocol used to reach Cloudflare's edge. **auto** (default) lets cloudflared choose. Force **quic** or **http2** only if you have a specific network requirement."
   "Post-Quantum Encryption", "Enable post-quantum cryptographic protection for the tunnel connection. Requires QUIC protocol."
   "Disable QUIC PMTU Discovery", "Disable Path MTU Discovery for QUIC connections. May improve reliability in environments where ICMP is filtered."
   "Log Level", "Verbosity of cloudflared logging. Defaults to **info**. Use **debug** for troubleshooting; **warn** or **error** for quieter operation."

QUIC UDP buffer sizes
---------------------

When running in **auto** or **quic** protocol mode, cloudflared relies on the
QUIC transport layer (via the ``quic-go`` library), which benefits significantly
from larger UDP receive buffers. FreeBSD's defaults are too small for high-throughput
QUIC and will result in a warning in the cloudflared log:

.. code-block:: text

    failed to increase receive buffer size (wanted: 7168 kiB, got 41 kiB).
    See https://github.com/quic-go/quic-go/wiki/UDP-Buffer-Sizes for details.

To suppress this warning and allow QUIC to operate at full throughput, set the
following tuneable values under :menuselection:`System --> Settings --> Tuneables`
to these values or higher:

.. csv-table::
   :header: "Tuneable", "Recommended value"
   :widths: 40, 60

   "kern.ipc.maxsockbuf", "16777216"
   "net.inet.udp.recvspace", "8388608"

.. Note::
    Even with optimal buffer sizes, sporadic ``Application error 0x0 (remote)``
    or ``failed to accept QUIC stream: timeout: no recent network activity`` entries
    may still appear in the log. These alone do not indicate packet corruption or a
    misconfiguration; enabling :menuselection:`Disable QUIC PMTU Discovery` may reduce
    their frequency.

Firewall considerations
-----------------------

cloudflared makes outbound-only connections to Cloudflare's edge on **TCP and UDP
port 7844**. On a default OPNsense configuration no extra firewall rules are
required.

If you have strict outbound floating rules (GeoIP blocks, blocklists, or a default
deny outbound policy), add a manual rule allowing traffic from **This Firewall** to
**any** on **TCP/UDP port 7844**.

**Multi-WAN users:** With multiple gateways configured, cloudflared traffic
originating from the router itself may fail to route entirely — not merely exit
via the wrong WAN. You must add an explicit policy-route rule to direct it:

1. Navigate to :menuselection:`Firewall --> Rules --> Floating`.
2. Add a rule matching **Source: This Firewall**, **Destination: any**,
   **Protocol: TCP/UDP**, **Destination port: 7844**.
3. Under :menuselection:`Gateway`, select the specific WAN gateway or gateway group
   through which the tunnel should exit.
4. Apply the rules.

.. Note::
    If you use Cloudflare Access policies on your tunnel, add a second floating rule
    with the same source and gateway matching **Protocol: TCP**, **Destination port: 443**,
    to allow JWT validation against your Cloudflare Access team domain.

Alternatively, enable :menuselection:`Disable force gateway` under
:menuselection:`Firewall --> Settings --> Advanced` if you want locally-originated
traffic to follow the routing table rather than be forced through a gateway, but be
aware that this may have unintended consequences for other traffic originating
from the firewall itself.

Startup and crash recovery
--------------------------

cloudflared will exit if it cannot resolve DNS when it first starts — for example,
on a fresh boot before upstream resolvers become reachable. The plugin registers a
``newwanip`` hook that automatically starts cloudflared (if it is not already
running) whenever the WAN interface receives a new IP address, providing recovery
in the common boot-order race.

Logging
-------

Navigate to :menuselection:`Services --> Cloudflare Tunnel --> Log File` to view
the cloudflared log via the standard OPNsense log viewer.

.. Note::
    The following warning appears at every startup and can be safely ignored::

        WRN ICMP proxy feature is disabled error="cannot create ICMPv4 proxy:
        ICMP proxy is not implemented on freebsd amd64 nor ICMPv6 proxy:
        ICMP proxy is not implemented on freebsd amd64"

    cloudflared's ICMP proxy enables ping and traceroute forwarding through the
    tunnel for WARP-based private network access. It is not implemented for
    FreeBSD, but has no effect on standard Cloudflare Tunnel operation.

cloudflared exposes a local metrics endpoint at ``http://localhost:2000/healthcheck``
which can be used to verify tunnel connectivity::

    fetch -qo - http://localhost:2000/healthcheck

.. Warning::
    The healthcheck may report ``{"connsCount":1}`` while the tunnel is still in
    the process of connecting — the connection count does not reliably indicate that
    the tunnel is fully established. Confirm tunnel status in the Cloudflare Zero
    Trust dashboard (:menuselection:`Networks --> Connectors`) or check the log for
    a ``Registered tunnel connection`` entry. See `cloudflared issue #1633
    <https://github.com/cloudflare/cloudflared/issues/1633>`_ for details.
