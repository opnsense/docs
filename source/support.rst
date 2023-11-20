===============
Support Options
===============

.. image:: images/support-1024x492.jpg


Software Support Levels
------------------------

OPNsense is used in infrastructures of all sizes, in some cases it is very important to know what to expect when running into
issues, certainly if part of the knowledge to maintain the infrastructure needs to be acquired from third parties.

Our platform is easily extendable, which encourages people to work on components not directly supported by us but very valuable
to our users.

In order to offer clarity for all involved, we decided to explain how we treat the components available in this chapter.

We currently distinct three different tiers of support, ranging from Critical to Community, where critical is always directly supported
by the OPNsense® Core Team and Community you may safely assume the core team has no (or very limited) involvement.

.. Tip::

    When designing infrastructures and in need of commercial support from the creators of OPNsense for community plugins,
    you can always contact us and discuss options.


If community plugins are very popular it is possible to promote in terms of support options, but in order to grow out of
the community tier some conditions have to be met.

* The software should be usable and understandable.
* Maintainability of the plugin should be good (code quality, following best practices)
* Documentation should be available and at least explain the purpose of the component including the most common settings.

These are the tiers in question:

Critical (Tier 1)
============================================
* Core team develops and supports
* Compiler errors or functional failures block git merges and releases
* Functionality is part of the standard installation or an officially supported plugin

Supplemental (Tier 2)
=====================================================
* Core team develops and supports or the functionality is deemed to be important enough to invest their time into bringing the plugin to its desired state in the long run.
* Compiler errors or functional failures block git merges
* Functionality problems such as 'known issues' might still go into releases
* Features require user to install the plugin / functionality not installed by default

Community (Tier 3)
============================
- Tier 3 is community supported, this means the OPNsense core development team won't support it to avoid overloading the team
- When accepting a Tier 3 feature into the code base, it will come with a number of limits and conditions:

  *  Submitter must commit to maintaining it:

    - Make sure code compiles and correctly functions after OPNsense and/or external (e.g. library) changes
    - Support users when they encounter problems (forum / git issue tracker – all related issues will be assigned to the maintainer)

- The code is offered as plugin and will not be part of the default OPNsense installation. The OPNsense core team will not be responsible for QA
- If the feature get lots of traction, and/or if the team just considers it very useful, it may get 'promoted' to being officially supported (Tier 2)
- The feature will be removed if the submitter stops maintaining it and no-one steps up to take over



Community
---------
If you need help with OPNsense you can always try the community options first.
When resorting to community support it is important to understand that anyone
helping you is doing so for free and at their own time. Even though your issue or
question may not be answered fully, it would be nice to thank the people who
help you.

To receive community support, the following options are available:

* Start searching this documentation & wiki
* The `OPNsense forum <https://forum.opnsense.org>`__
* Ask online users on `IRC Libera Chat <https://libera.chat/>`__ #opnsense
* Open a GitHub ticket (`core <https://github.com/opnsense/core/issues>`__, `plugins <https://github.com/opnsense/plugins/issues>`__) using one of our templates

.. Note::

    When a Github ticket is opened, it often is being tagged "support", but its status may change over time when more details
    are known. Triaging issues takes time, the easier one can replicate an issue on a clean install, the higher the chance
    tickets are being solved.


Commercial
----------

As we build and maintain the software used by individuals and companies all around the globe, we are able to help you
out when it comes to network design choices, solving issues and custom development around OPNsense.

Extended professional support services are available for an annual fee.
You can find our options in `the OPNsense webshop <https://shop.opnsense.com/product-categorie/support/>`__
or you may `contact us <https://shop.opnsense.com/contact-us/>`__ directly.


List of available community plugins
---------------------------------------------------------------

Below you will find the plugins available in the standard (community) version of OPNsense categorised by support tier
as described at the support levels section.


.. csv-table:: Tier 2
  :header: "Name", "Description"

   "devel/debug", "Add several debugging tools to enable full stack traces on crash reports and extended syntax checks for development activities."
   "net/firewall", "This package extends the standard OPNsense firewall system with endpoints for machine to machine management tasks. Gui components are initially only intended to ease testing and to explain current functionality."
   "net/frr", "FRRouting (FRR) is an IP routing protocol suite for Linux and Unix platforms which includes protocol daemons for BGP, IS-IS, LDP, OSPF, PIM, and RIP."
   "net/relayd", "relayd is a daemon to relay and dynamically redirect incoming connections to a target host.  Its purposes is to run as a load-balancer.  The daemon is able to monitor groups of hosts for availability, which is determined by checking for a specific service common to a host group.  When availability is confirmed, Layer 3 and/or layer 7 forwarding services are set up by relayd."
   "security/etpro-telemetry", "Todays cybersecurity engineers need timely and accurate data about eminent threats and how they spread around the globe. With this data cybersecurity researchers and analysts can improve the detection of malicious network traffic. The times when we could rely on just firewall rules for our protection are long gone. Additional layers of security are desperately needed to guard against these attacks."
   "security/stunnel", "Stunnel is a proxy designed to add TLS encryption functionality to existing clients and servers without any changes in the programs' code."
   "security/tinc", "tinc is a Virtual Private Network (VPN) daemon that uses tunnelling and encryption to create a secure private network between hosts on the Internet."
   "sysutils/git-backup", "This package adds a backup option using git version control."
   "sysutils/vmware", "The Open Virtual Machine Tools (open-vm-tools) are the open source implementation of VMware Tools. They are a set of guest operating system virtualization components that enhance performance and user experience of virtual machines. As virtualization technology rapidly becomes mainstream, each virtualization solution provider implements their own set of tools and utilities to supplement the guest virtual machine. However, most of the implementations are proprietary and are tied to a specific virtualization platform."

.. csv-table:: Tier 3
  :header: "Name", "Description"

   "benchmarks/iperf", "iperf3 is a tool for measuring the achievable TCP, UDP, and SCTP throughput along a path between two hosts.  It allows the tuning of various parameters such as socket buffer sizes and maximum attempted throughput.  It reports (among other things) bandwidth, delay jitter, and datagram loss.  iperf was originally developed by NLANR/DAST."
   "databases/redis", "Redis is an open source, advanced key-value store.  It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets and sorted sets."
   "devel/grid_example", "The goal of the 'grid_example' plugin is to showcase the capabilities of the OPNsense plugin framework in relation to the grid/table system."
   "devel/helloworld", "The goal of the 'Hello world' plugin is to showcase the capabilities of the OPNsense plugin framework.  It will control a program on the system named 'testConnection.py'. It will send an email using plain SMTP and will respond with a JSON message about the result of the attempt."
   "dns/bind", "BIND implements the DNS protocols. The DNS protocols are part of the core Internet standards. They specify the process by which one computer can find another computer on the basis of its name. The BIND software distribution contains all of the software necessary for asking and answering name service questions."
   "dns/ddclient", "ddclient is a Perl client used to update dynamic DNS entries for accounts on many dynamic DNS services."
   "dns/dnscrypt-proxy", "A flexible DNS proxy, with support for modern encrypted DNS protocols such as DNSCrypt v2 and DNS-over-HTTPS."
   "dns/rfc2136", "Support for RFC-2136 based dynamic DNS updates using Bind"
   "emulators/qemu-guest-agent", "QEMU Guest Agent for FreeBSD"
   "ftp/tftp", "tftp-hpa is portable, BSD derived tftp server.  It supports advanced options such as blksize, blksize2, tsize, timeout, and utimeout. It also supported rulebased security options."
   "mail/postfix", "Postfix attempts to be fast, easy to administer, and secure. The outside has a definite Sendmail-ish flavor, but the inside is completely different."
   "mail/rspamd", "Rspamd is fast, modular and lightweight spam filter. It is designed to work with big amount of mail and can be easily extended with own filters written in lua."
   "misc/theme-cicada", "The cicada theme - grey/orange - Designed and created by remic-webdesign@chello.at"
   "misc/theme-rebellion", "A suitably dark theme."
   "misc/theme-tukan", "The tukan theme - blue/white - Designed and created by remic-webdesign@chello.at"
   "misc/theme-vicuna", "The vicuna theme - dark anthrazit - Designed and created by rene@team-rebellion.net"
   "net-mgmt/collectd", "collectd is a daemon which collects system and application performance metrics periodically and provides mechanisms to store the values in a variety of ways, for example in RRD files."
   "net-mgmt/lldpd", "LLDP is an industry standard protocol designed to supplant proprietary Link-Layer protocols such as EDP or CDP. The goal of LLDP is to provide an inter-vendor compatible mechanism to deliver Link-Layer notifications to adjacent network devices."
   "net-mgmt/net-snmp", "Simple Network Management Protocol (SNMP) is a widely used protocol for monitoring the health and welfare of network equipment (eg. routers), computer equipment and even devices like UPSs. Net-SNMP is a suite of applications used to implement SNMP v1, SNMP v2c and SNMP v3 using both IPv4 and IPv6."
   "net-mgmt/netdata", "Netdata is distributed, real-time, performance and health monitoring for systems and applications. It is a highly optimized monitoring agent you install on all your systems and containers."
   "net-mgmt/nrpe", "nrpe is used to execute Nagios plugins on remote hosts and report the results to the main Nagios server. From the Nagios homepage:"
   "net-mgmt/telegraf", "Telegraf is the Agent for Collecting & Reporting Metrics & Data. Telegraf has plugins or integrations to source a variety of metrics directly from the system it’s running on, pull metrics from third-party APIs, or even listen for metrics via a StatsD and Kafka consumer services. It also has output plugins to send metrics to a variety of other datastores, services, and message queues, including InfluxDB, Graphite, OpenTSDB, Datadog, Librato, Kafka, MQTT, NSQ, and many others."
   "net-mgmt/zabbix-agent", "Zabbix is an enterprise-class open source distributed monitoring solution."
   "net-mgmt/zabbix-proxy", "Zabbix is an enterprise-class open source distributed monitoring solution."
   "net/chrony", "An alternative to native ntpd daemon. In some edge cases chrony works better in virtual environments."
   "net/freeradius", "FreeRADIUS includes a RADIUS server, a BSD licensed client library, a PAM library, and an Apache module. In most cases, the word FreeRADIUS refers to the RADIUS server."
   "net/ftp-proxy", "Ftp-proxy is a proxy for the Internet File Transfer Protocol.  FTP control connections are being redirected into the proxy, after which the proxy connects to the server on behalf of the client."
   "net/google-cloud-sdk", "This plugin installs the Google Cloud SDK. The SDK may be used on the CLI or in conjunction with the Let's Encrypt plugin."
   "net/haproxy", "HAProxy is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications. It is particularly suited for web sites crawling under very high loads while needing persistence or Layer7 processing."
   "net/igmp-proxy", "Igmpproxy is a simple multicast routing daemon based on mrouted. It uses IGMP forwarding to dynamically route multicast traffic."
   "net/mdns-repeater", "mdns-repeater is a Multicast DNS repeater. Multicast DNS uses the 224.0.0.251 address, which is 'administratively scoped' and does not leave the subnet."
   "net/ntopng", "ntopng is the next generation version of the original ntop, a network traffic probe that monitors network usage. ntopng is based on libpcap and it has been written in a portable way in order to virtually run on every Unix platform, MacOSX and on Windows as well."
   "net/radsecproxy", "A generic RADIUS proxy that in addition to usual RADIUS UDP transport, also supports TLS (RadSec), as well as RADIUS over TCP and DTLS. The aim is for the proxy to have sufficient features to be flexible, while at the same time to be small, efficient and easy to configure."
   "net/realtek-re", "This is the official driver from Realtek and can be loaded instead of the FreeBSD driver built into the GENERIC kernel if you experience issues with it (eg. watchdog timeouts), or your card is not supported."
   "net/shadowsocks", "A secure socks5 proxy, designed to protect your Internet traffic."
   "net/siproxd", "Siproxd is a proxy/masquerading daemon for the SIP protocol. It handles registrations of SIP clients on a private IP network and performs rewriting of the SIP message bodies to make SIP connections work via an masquerading firewall (NAT). It allows SIP software clients (like kphone, linphone) or SIP hardware clients (Voice over IP phones which are SIP-compatible, such as those from Cisco, Grandstream or Snom) to work behind an IP masquerading firewall or NAT router."
   "net/sslh", "Manage SSLH, the SSL/SHH multiplexer via the OPNsense web UI."
   "net/tayga", "TAYGA is an out-of-kernel stateless NAT64 implementation that uses the TUN driver to exchange IPv4 and IPv6 packets with the kernel. It is intended to provide production-quality NAT64 service for networks where dedicated NAT64 hardware would be overkill."
   "net/udpbroadcastrelay", "udbproadcastrelay is a UDP multicast relayer. Its intended use is to rebroadbcast udp packets on a specific port across interfaces, be those interfaces physical or VLAN."
   "net/upnp", "Mini UPnPd is a lightweight implementation of a UPnP IGD daemon. This is supposed to be run on your gateway machine to allow client systems to redirect ports and punch holes in the firewall."
   "net/vnstat", "vnStat is a console-based network traffic monitor for Linux and BSD that keeps a log of network traffic for the selected interface(s). It uses the network interface statistics provided by the kernel as information source. This means that vnStat won't actually be sniffing any traffic and also ensures light use of system resources."
   "net/wireguard", "WireGuard® is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform and widely deployable. It is currently under heavy development, but already it might be regarded as the most secure, easiest to use, and simplest VPN solution in the industry."
   "net/wireguard-go", "WireGuard® is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN. WireGuard is designed as a general purpose VPN for running on embedded interfaces and super computers alike, fit for many different circumstances. Initially released for the Linux kernel, it is now cross-platform and widely deployable. It is currently under heavy development, but already it might be regarded as the most secure, easiest to use, and simplest VPN solution in the industry."
   "net/wol", "wol implements Wake-On-LAN functionality in a small program. It wakes up hardware that is Magic Packet compliant."
   "net/zerotier", "ZeroTier can be used for on-premise network virtualization, as a peer to peer VPN for mobile teams, for hybrid or multi-data-center cloud deployments, or just about anywhere else secure software defined virtual networking is useful."
   "security/acme-client", "This plugin contains a full ACME protocol implementation based on the acme.sh project.  According to the authors, it's probably 'the easiest and smallest and smartest shell script' to automatically issue and renew the free certificates from Let's Encrypt."
   "security/clamav", "ClamAV(r) is an open source (GPL) anti-virus engine used in a variety of situations including email scanning, web scanning, and end point security. It provides a number of utilities including a flexible and scalable multi-threaded daemon, a command line scanner and an advanced tool for automatic database updates."
   "security/crowdsec", "Crowdsec is an open-source, lightweight software, detecting peers with aggressive behaviors to prevent them from accessing your systems. Its user friendly design and assistance offers a low technical barrier of entry and nevertheless a high security gain."
   "security/intrusion-detection-content-et-open", "IDS Proofpoint ET open ruleset duplicates rule files which are being delivered empty in ET Pro Telemetry edition so both can be installed."
   "security/intrusion-detection-content-et-pro", "Proofpoint ET Pro is a timely and accurate rule set for detecting and blocking advanced threats using your existing network security appliances, such as next generation firewalls (NGFW) and network intrusion detection / prevention systems (IDS/IPS)"
   "security/intrusion-detection-content-pt-open", "The Attack Detection Team searches for new vulnerabilities and 0-days, reproduces it and creates PoC exploits to understand how these security flaws work and how related attacks can be detected on the network layer."
   "security/intrusion-detection-content-snort-vrt", "The Snort Subscriber Rule Set refer to rules that have been developed, tested and approved by the Talos Security Intelligence and Research Team (Talos). The Snort Subscriber Ruleset released after March 7th, 2005 are governed by the Snort Subscriber Rule Set License Agreement."
   "security/maltrail", "Maltrail is a malicious traffic detection system, utilizing publicly available (black)lists containing malicious and/or generally suspicious trails, along with static trails compiled from various AV reports and custom user defined lists, where trail can be anything from domain name, URL, IP address or HTTP User-Agent header value. Also, it uses advanced heuristic mechanisms that can help in discovery of unknown threats."
   "security/openconnect", "OpenConnect is an SSL VPN client initially created to support Cisco's AnyConnect SSL VPN. It has since been ported to support the Juniper SSL VPN which is now known as Pulse Connect Secure."
   "security/softether", "SoftEther VPN ('SoftEther' means 'Software Ethernet') is one of the world's most powerful and easy-to-use multi-protocol VPN software. It runs on Windows, Linux, Mac, FreeBSD and Solaris."
   "security/tor", "Tor is a connection-based low-latency anonymous communication system which addresses many flaws in the original onion routing design."
   "security/wazuh-agent", "Wazuh is a free and open source platform used for threat prevention, detection, and response. It is capable of protecting workloads across on-premises, virtualized, containerized, and cloud-based environments."
   "sysutils/apcupsd", "Apcupsd, short for APC UPS daemon, can be used for controlling all APC UPS models. It can monitor and log the current power and battery status, perform automatic shutdown, and can run in network mode in order to power down other hosts on a LAN."
   "sysutils/api-backup", "Provide the functionality to download the config.xml"
   "sysutils/apuled", "LED control for PC Engines APU platform OPNsense plugin Cloudfence 2019 - JCC"
   "sysutils/dmidecode", "Dmidecode reports information about your system's hardware as described in your system BIOS according to the SMBIOS/DMI standard. This information typically includes system manufacturer, model name, serial number, BIOS version, asset tag as well as a lot of other details of varying level of interest and reliability depending on the manufacturer. This will often include usage status for the CPU sockets, expansion slots (e.g. AGP, PCI, ISA) and memory module slots, and the list of I/O ports (e.g. serial, parallel, USB)."
   "sysutils/hw-probe", "Send anonymized hardware diagnostics to https://bsd-hardware.info"
   "sysutils/lcdproc-sdeclcd", "LCDproc setup for SDEC LCD devices found in Watchguard FireBox firewall appliances."
   "sysutils/mail-backup", "Send a config.xml via mail, optionally encrypted via PGP."
   "sysutils/munin-node", "Munin network-wide graphing framework (node)"
   "sysutils/nextcloud-backup", "This package adds a backup option using an existing NextCloud instance."
   "sysutils/node_exporter", "Prometheus exporter for hardware and OS metrics exposed by *NIX kernels, written in Go with pluggable metric collectors."
   "sysutils/nut", "The primary goal of the Network UPS Tools (NUT) project is to provide support for Power Devices, such as Uninterruptible Power Supplies, Power Distribution Units, Automatic Transfer Switch, Power Supply Units and Solar Controllers."
   "sysutils/puppet-agent", "Puppet lets you centrally manage every important aspect of your system using a cross-platform specification language that manages all the separate elements normally aggregated in different files, like users, cron jobs, and hosts, along with obviously discrete elements like packages, services, and files."
   "sysutils/smart", "The smartmontools package contains two utility programs (smartctl and smartd) to control and monitor storage systems using the Self-Monitoring, Analysis and Reporting Technology System (S.M.A.R.T.) built into most modern ATA and SCSI hard disks.  It is derived from the smartsuite package, and includes support for ATA/ATAPI/SATA disks and SCSI disks and tape devices."
   "sysutils/virtualbox", "These additions are for installation inside a FreeBSD guest."
   "sysutils/xen", "FreeBSD VM tools for Citrix XenServer and XCP"
   "vendor/sunnyvalley", "This plugin adds a proprietary repository to install Zenarmor (previously Sensei), a plugin for OPNsense, complementing the firewall with state of the art next generation firewall features."
   "www/c-icap", "c-icap is an implementation of an ICAP server. It can be used with HTTP proxies that support the ICAP protocol to implement content adaptation and filtering services."
   "www/cache", "Add and enable caching for the web GUI to accelerate requests."
   "www/nginx", "NGINX is a high performance edge web server with the lowest memory footprint and the key features to build modern and efficient web infrastructure."
   "www/web-proxy-sso", "Allow to use the web proxy with Single Sign-On against an Active Directory instead of using a bundled authentication."
