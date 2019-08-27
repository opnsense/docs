===========
Diagnostics
===========

The interface diagnostics page contains various tools to help debug network issues.

---------------------
ARP Table
---------------------

The `ARP <https://en.wikipedia.org/wiki/Address_Resolution_Protocol>`__ table module shows all MAC addresses known by this firewall.

==============================================================================================================================================

=========================== ==================================================================================================================
IP                          IPv4 address
MAC                         `MAC <https://en.wikipedia.org/wiki/MAC_address>`__ address
Manufacturer                Manufacturer looked up with the mac address above
Interface                   Associated interface
Interface name              The name of the interface if found
Hostname                    In case of a DHCPv4 client, the hostname when found in the leases file
=========================== ==================================================================================================================

---------------------
DNS Lookup
---------------------

Perform a quick dns lookup from the firewall.

---------------------
NDP Table
---------------------

Show addresses learned by the `Neighbor Discovery Protocol <https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol>`__ for IPv6.

==============================================================================================================================================

=========================== ==================================================================================================================
IPv6                        IPv6 address
MAC                         `MAC <https://en.wikipedia.org/wiki/MAC_address>`__ address
Manufacturer                Manufacturer looked up with the mac address above
Interface                   Associated interface
Interface name              The name of the interface if found
=========================== ==================================================================================================================


---------------------
Packet capture
---------------------

The packet capture module can be used to deep dive into traffic passing a (or multiple) network interfaces.
It has some options you can choose from, such as the interface to listen on, protocol you interested in and
host to track.

Packet capture uses `tcpdump <https://www.tcpdump.org/>`__ and runs in the background. After a capture is performed you can
either look into it using the **View capture** button or download the pcap file to inspect it in an external tool, such as `Wireshark <https://www.wireshark.org/>`__.

---------------------
Ping
---------------------

Use ping to establish if a remote host can be reached using ICMP.

---------------------
Port Probe
---------------------

Test if a host has a certain TCP port open and accepts connections on it.

---------------------
Trace Route
---------------------

Use `traceroute <https://www.freebsd.org/cgi/man.cgi?query=traceroute>`__ /  `traceroute6 <https://www.freebsd.org/cgi/man.cgi?query=traceroute6>`__
to measure the path traffic would follow when trying to reach a specific host.
