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
2. Navigate to :menuselection:`Networks --> Tunnels`.
3. Click **Create a tunnel**, select **Cloudflared** as the connector type, and give
   the tunnel a name.
4. On the next page, copy the tunnel token (the long string shown in the install
   command). You only need the token itself — not the full command.

Settings
--------

Navigate to :menuselection:`Services --> Cloudflare Tunnel --> Settings`.

.. csv-table::
   :header: "Field", "Description"
   :widths: 20, 80

   "Enable", "Start the cloudflared service at boot and keep it running."
   "Tunnel Token", "The tunnel token from the Cloudflare Zero Trust dashboard. Stored in a root-readable file and passed to cloudflared via an environment variable (not on the command line)."
   "Protocol", "Transport protocol used to reach Cloudflare's edge. **auto** (default) lets cloudflared choose. Force **quic** or **http2** only if you have a specific network requirement."
   "Post-Quantum Encryption", "Enable post-quantum cryptographic protection for the tunnel connection. Requires QUIC protocol."
   "Disable QUIC PMTU Discovery", "Disable Path MTU Discovery for QUIC connections. May improve reliability in environments where ICMP is filtered."

Firewall considerations
-----------------------

cloudflared makes outbound-only connections to Cloudflare's edge on **TCP and UDP
port 7844**. On a default OPNsense configuration no extra firewall rules are
required.

If you have strict outbound floating rules (GeoIP blocks, blocklists, or a default
deny outbound policy), add a manual rule allowing traffic from **This Firewall** to
**any** on **TCP/UDP port 7844**.

**Multi-WAN users:** cloudflared may use any available gateway by default. If you
need its traffic to leave on a specific WAN, either:

* Add a manual outbound NAT or policy-route rule that pins traffic from the router
  itself to the desired gateway, or
* Enable :guilabel:`Disable force gateway` under
  :menuselection:`Firewall --> Settings --> Advanced` so that locally-originated
  traffic is not forced through the default gateway.

Startup and crash recovery
--------------------------

cloudflared will exit if it cannot resolve DNS when it first starts — for example,
on a fresh boot before upstream resolvers become reachable. The plugin registers a
``newwanip`` hook that automatically starts cloudflared (if it is not already
running) whenever the WAN interface receives a new IP address, providing recovery
in the common boot-order race.

For additional crash recovery — for example, if the tunnel drops for reasons
unrelated to a WAN change — you can add a periodic restart job:

1. Navigate to :menuselection:`System --> Settings --> Cron`.
2. Click **+** to add a new job.
3. In the **Command** dropdown, select **Restart Cloudflare Tunnel**.
4. Set the schedule as desired (e.g. every 5 minutes: ``*/5 * * * *``).
5. Leave the job **disabled** until you have confirmed the tunnel is stable; enable
   it only if you observe unrecovered drops.

.. Note::
    The cron restart is unconditional — it will bounce a healthy tunnel. Schedule
    it infrequently (no more than once every 5 minutes) and only enable it if you
    actually observe crashes that the ``newwanip`` hook does not recover.

Logging
-------

Navigate to :menuselection:`Services --> Cloudflare Tunnel --> Log File` to view
the cloudflared log via the standard OPNsense log viewer.
