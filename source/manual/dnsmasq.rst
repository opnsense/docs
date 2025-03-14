==================
Dnsmasq DNS & DHCP
==================

`DNSmasq` is a lightweight and easy to configure DNS forwarder and DHCP server.

It is considered the replacement for `ISC-DHCP` in small and medium sized setups,
and synergizes well with `Unbound DNS`, our standard enabled forward/resolver service.

---------------------------------
Considerations before deployment
---------------------------------

DNS Service
-----------------------------

Combining `DNSmasq` with `Unbound` can enable synergies, such as DHCP leases that have their hostnames registered in `DNSmasq` to be queried by `Unbound`.

Since `DNSmasq` does not restart on configuration changes and does not need custom scripts to register DNS, it is very resilient and easy to manage.

.. Note::

    `Unbound` is a recursive resolver, `DNSmasq` a non-resursive forwarding DNS server. This means `DNSmasq` always
    needs a recursive DNS resolver it can forward its queries to. This can be `Unbound`, or another DNS Service on the internet.


In the configuration examples further below, we will always combine `Unbound` with `DNSmasq`.

DHCP Service
-----------------------------

`DNSmasq` is the perfect DHCP server for small and medium sized setups. The configuration is straight forward, and since it can register the DNS names of leases,
it can replicate the simplicity known from consumer routers.

If HA for DHCP is a requirement, split pools can be configured for two `DNSmasq` instances. With a dhcp reply delay, the secondary instance will only answer when
the first instance is unresponsive.

For larger enterprise setups, `KEA DHCP` can be a viable alternative. It supports lease synchronisation via REST API, which means both DHCP servers keep track
of all existing leases and do not need split pools. It is also far more scalable if there are thousands of leases.

The tradeoff using `KEA DHCP` is a more complicated setup, especially when custom DHCP options are needed. DNS registration is also not possible.

With this in mind, pick the right choice for your setup. When in doubt, using `DNSmasq` can be the best choice.

-------------------------
General settings
-------------------------

Most settings are pretty straightforward here when the service is enabled, it should just start forwarding dns requests
when received from the network. DHCP requires at least one dhcp-range and matching dhcp-options.


DNS Settings
-------------------------

.. tabs::

   .. tab:: General

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================

      ========================================= ====================================================================================

   .. tab:: Hosts

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================

      ========================================= ====================================================================================

   .. tab:: Domains

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================

      ========================================= ====================================================================================


DHCP Settings
-------------------------

.. tabs::

   .. tab:: DHCP ranges

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================

      ========================================= ====================================================================================

   .. tab:: DHCP options

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================

      ========================================= ====================================================================================

   .. tab:: DHCP tags

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================

      ========================================= ====================================================================================

   .. tab:: DHCP options / match

      ========================================= ====================================================================================
      **Option**                                **Description**
      ========================================= ====================================================================================

      ========================================= ====================================================================================


-------------------------
Advanced settings
-------------------------

To configure options that are not available in the gui one can add custom configuration files on the firewall itself.
Files can be added in :code:`/usr/local/etc/dnsmasq.conf.d/`, these should use as extension .conf (e.g. custom-options.conf).
When more files are placed inside the directory, all will be included in alphabetical order.

.. Warning::
    It is the sole responsibility of the administrator which places a file in the extension directory to ensure that the configuration is
    valid.

.. Note::
    This method replaces the ``Custom options`` settings in the Dnsmasq configuration, which was removed in version 21.1.


The DHCP service in `Unbound` uses tags to determine which DHCP ranges and DHCP options to send.

Each interface sets a tag automatically when a DHCP broadcast is received. Choosing an interface in a DHCP range and DHCP option matches this tag.


---------------------------------
Configuration examples
---------------------------------


Combining `DNSmasq DNS` and `Unbound DNS``
------------------------------------------



Register hostnames of DHCP leases
------------------------------------------



Understanding DHCP tags
------------------------------------------



DHCP for simple networks
------------------------------------------



DHCP for small and medium sized HA setups
------------------------------------------
