=============
System Wizard
=============

The system wizard guides you through the initial configuration of OPNsense. It opens automatically when
you first log in to the web interface on a new installation. You can also open it from
:menuselection:`System --> Wizard`.
The wizard assumes the default LAN/WAN setup. For other interface layouts, configure the settings directly
in the relevant pages of the web interface.

You can run the wizard again later to change individual settings. It loads the current configuration,
so you can adjust the desired options and apply the changes at the end.

The tabs below follow the wizard's steps. In the wizard, use **Next** to advance and the tabs to return
to earlier steps.

.. tabs::

   .. tab:: Welcome

      Start the setup or leave the wizard without applying changes.

      ============ ========================================================================================================
      **Option**   **Description**
      ============ ========================================================================================================
      **Next**     Begin the wizard. Changes take effect when you click Apply at the Finish step.
      **Abort**    Leave without applying the wizard settings.
      ============ ========================================================================================================

   .. tab:: General Information

      Set the firewall's identity, regional settings, and DNS preferences.

      ========================= ========================================================================================================
      **Option**                **Description**
      ========================= ========================================================================================================
      **Hostname**              Name of the firewall.
      **Domain**                Domain used by the firewall and for local DHCP/DNS registration.
      **Language**              Language of the web interface.
      **Timezone**              Local timezone used to display times, including log entries.
      **DNS Servers**           IPv4 or IPv6 addresses of DNS servers the firewall should use.
      **Override DNS**          Allow WAN DHCP/PPP to supply DNS servers.
      **Enable Resolver**       Enable Unbound DNS. See :doc:`/manual/unbound`.
      **Enable DNSSEC Support** Enable DNSSEC validation in Unbound.
      **Harden DNSSEC data**    Treat missing DNSSEC data for trust-anchored zones as bogus.
      ========================= ========================================================================================================

      .. Tip::

         Use an internal domain such as :code:`home.arpa`; avoid :code:`local`, which is reserved for mDNS.
         Choosing the correct timezone also makes logs easier to read.

   .. tab:: Network [WAN]

      Configure the connection to your upstream router or internet provider.

      ================================== ========================================================================================================
      **Option**                         **Description**
      ================================== ========================================================================================================
      **Disable WAN**                    Disable WAN if this interface is not needed.
      **Type**                           Choose DHCP to obtain an IPv4 address automatically, Static to enter an address and gateway,
                                         or PPPoE to connect using credentials supplied by your provider.
      **MAC (spoofed)**                  Override the MAC address if required by your provider; otherwise leave empty.
      **MTU**                            Set a specific MTU if required by your connection; otherwise leave empty.
      **MSS**                            Adjust TCP MSS clamping if required by your connection; otherwise leave empty.
      **IP Address**                     For Static, enter the WAN address and prefix length.
      **Gateway**                        For Static, enter the upstream gateway address.
      **DHCP hostname**                  For DHCP, enter a hostname if required by your provider.
      **PPPoE Username**                 Username supplied by your provider for PPPoE.
      **PPPoE Password**                 Password supplied by your provider for PPPoE.
      **PPPoE Service name**             Service name supplied by your provider, if required.
      **Block RFC1918 Private Networks** Block traffic from private, loopback, and Carrier-grade NAT address ranges on WAN.
      **Block bogon networks**           Block traffic from reserved or unassigned address ranges.
      ================================== ========================================================================================================

      .. Tip::

         When WAN sits behind another router and uses private address space, disable
         **Block RFC1918 Private Networks**.

   .. tab:: Network [LAN]

      Configure the firewall's address and DHCP service on the local network.

      ========================= ========================================================================================================
      **Option**                **Description**
      ========================= ========================================================================================================
      **Disable LAN**           Disable LAN only when it is not needed, such as in a WAN-only setup.
      **IP Address**            LAN address with its prefix length, for example :code:`192.168.1.1/24`.
      **Configure DHCP server** Configure Dnsmasq to assign IPv4 addresses to LAN clients. See :doc:`/manual/dnsmasq`.
      ========================= ========================================================================================================

      .. Tip::

         Choose a LAN subnet that differs from the WAN subnet. If you change the LAN address,
         you will need to reconnect at the new address after applying the wizard.

   .. tab:: Deployment type

      Select the options appropriate for your setup.

      =================================== ========================================================================================================
      **Option**                          **Description**
      =================================== ========================================================================================================
      **Optimize for Multiwan**           Enable force gateway and reply-to behavior for multiple internet connections.
                                          Leave disabled when using a single gateway. See :doc:`/manual/multiwan`.
      **Automatic DHCP/DNS registration** Forward DNS queries for your configured domain from Unbound to Dnsmasq to resolve DHCP clients by name.
                                          Requires both the DHCP server and Unbound resolver to be enabled in the wizard.
                                          See :doc:`/manual/dnsmasq`.
      **Optimize for IPsec**              Allow network interrupt processing to use all available CPUs, distributing processing across IPsec flows.
                                          This does not increase throughput for a single flow.
      **Enable ECMP routing**             Enable Equal-Cost Multipath routing. Routes must be configured separately.
                                          See :doc:`/manual/routes` for configuration and limitations, or :doc:`/manual/dynamic_routing` for FRR.
      =================================== ========================================================================================================

   .. tab:: Set initial password

      Set the password for the root account.

      ============================== ========================================================================================================
      **Option**                     **Description**
      ============================== ========================================================================================================
      **Root Password**              Enter a new password, or leave empty to keep the current password.
      **Root Password Confirmation** Repeat the new password, or leave empty when keeping the current password.
      ============================== ========================================================================================================

      .. Tip::

         On a fresh installation, replace the default password before putting the firewall into service.

   .. tab:: Finish

      Save your settings and complete the setup.

      ============ ========================================================================================================
      **Option**   **Description**
      ============ ========================================================================================================
      **Apply**    Save the settings and reconfigure the firewall.
      ============ ========================================================================================================

      If you changed the LAN address, reconnect to the web interface at the new address. LAN clients may need
      to renew their DHCP lease or update their static address to reach the new subnet.

      Once connected, check for updates under :menuselection:`System --> Firmware --> Status`.
