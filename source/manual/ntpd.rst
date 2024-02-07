==============
Network Time
==============

OPNsense ships with a standard `NTPd <http://doc.ntp.org/current-stable/>`__ server,
which synchronizes time with upstream servers and provides time to connected clients.

A newly installed firewall comes with NTP enabled on all interfaces (firewall blocks all non LAN access in this case),
forwarding queries to one of the :code:`X.opnsense.pool.ntp.org` upstreams (:code:`X` is any of 0,1,2,3).

-------------------------
General settings
-------------------------

In most cases the default setup is ready to use, below you will find some of the general options which can be configured.

=====================================================================================================================

.. Attention::

    NTPd syncs the local clock to remote NTP servers and listens for incoming client queries using the selected interfaces.
    The interface selection must therefore include a WAN type interface so that normal routing to the internet can take place.
    Only selecting a LAN type interface will likely work due to outbound NAT rules, however, if CARP is configured, it is
    possible that such NAT rules will translate to the address of the CARP VIP, causing asymmetric routing for secondary nodes.

    Unless you are sure that you want to use a specific interface, it is recommended to keep the default of listening
    on all interfaces and use the firewall rules to constrain access to the NTP service.
    See `Listen interfaces <settingsmenu.html#listen-interfaces>`__ for more information.

====================================  ===============================================================================
Interface(s)	                      Interfaces to listen on. This interface selection is also used for outgoing
                                      queries. when no interfaces are selected it listens on all interfaces with a
                                      wildcard. Selecting all interfaces will explicitly listen on only the
                                      interfaces/IPs specified. Interfaces without an IP address will not be shown.
Time servers                          Servers to use, comes with two toggles:

                                      * Prefer
                                          Marks the server as preferred.
                                      * Do not use
                                          Marks the server as unused, except for display purposes.
                                          The server is discarded by the selection algorithm.
Orphan mode                           Orphan mode allows the system clock to be used when no other
                                      clocks are available. The number here specifies the stratum reported
                                      during orphan mode and should normally be set to a number high enough to
                                      insure that any other servers available to clients are
                                      preferred over this server.
NTP graphs                            Enable RRD graphs of NTP statistics, which can be viewed in
                                      :menuselection:`Reporting --> Health`
Syslog logging                        Extend logging with peer and/or system messages
Statistics logging                    Enable statistical logging in :code:`/var/log/ntp`, doesn't come with a
                                      user interface
Access restrictions                   Within the access restriction row, you can set various options which
                                      limit the use of ntpd and in some cases instruct ntpd how to handle
                                      rejected clients.
Leap seconds                          You can manually supply ntpd with a leap seconds file, more detailed info
                                      on the contents of those files can be found
                                      `here <http://support.ntp.org/bin/view/Support/ConfiguringNTP#Section_6.14.>`__
====================================  ===============================================================================


.. Note::

    NTPs is disabled if no Time servers are configured. There is no separate enable/disable toggle.


-------------------------
GPS
-------------------------

If you own a gps receiver, which supports NMEA, you can use it as a reference clock and configure it in this section.
For some brands settings are preconfigured, you can also use custom settings.


-------------------------
PPS
-------------------------

If your GPS receiver supports PPS (Pulse Per Second) output or you have a separate PPS signal available, you
can configure the serial port to use along with some other settings here.


-------------------------
Status
-------------------------

The status page can be used to query the health of the upstream time sources, it shows the following characteristics.


========================================================================================================================

====================================  ==================================================================================
Status                                Human readable status of the upstream
Server                                Upstream source
Ref ID                                Source IP address or
                                      `kiss code: <http://doc.ntp.org/4.2.6p5/decode.html#kiss>`__
Stratum                               NTP uses a hierarchical, semi-layered system of time sources
                                      (`wikipedia <https://en.wikipedia.org/wiki/Network_Time_Protocol#Clock_strata>`__)
                                      This field shows the stratum of the upstream source
                                      (lower usually means closer to the actual time source)
Type                                  Type of time source, one of:

                                      * u: unicast or manycast client
                                      * b: broadcast or multicast client
                                      * p: pool source
                                      * l: local (reference clock)
                                      * s: symmetric (peer)
                                      * A: manycast server
                                      * B: broadcast server
                                      * M: multicast server
When                                  time in seconds, minutes, hours, or days since the last packet was
                                      received, or '-' if a packet has never been received
Poll                                  poll interval in seconds
Reach                                 reach shift register (octal), when set to :code:`377` all 8 bits are set and thus
                                      no responses have been lost. Convert to bits to inspect which tries failed.
                                      (e.g. :code:`257` --> :code:`10101111` means the last four responses
                                      where received and two where lost within the last 8 tries)
Delay                                 roundtrip delay in milliseconds
Offset                                offset time in milliseconds of the server relative to this host
Jitter                                indicates the difference, in milliseconds, between two samples
====================================  ==================================================================================
