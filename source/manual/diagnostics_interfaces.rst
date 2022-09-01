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
Netstat
---------------------

The netstat module contains a useful set of network status and statistics metrics, which are split into a number of
topics.


.. Tip::

    .. raw:: html

         Use the refresh <i class="fa fa-refresh fa-fw"></i> icon in the tab to refresh the data in it (selection won't change).


In order of relevance you can find the following information here:

........................
Interfaces
........................

This section contains all (physical and virtual) attached interfaces to the system containing metrics like the number of
packets and bytes send- and received per (hardware) address.

........................
Protocol
........................

Contains system wide statistics for each network protocol. Examples of statistics that can be found in this region are
the number of tcp listening connections, sent packets, duplicate packets, etc, etc.

........................
Sockets
........................

Displays network and unix domain sockets, this basically combines :code:`netstat` with :code:`sockstat` on FreeBSD
in order to provide insights into which process is listening were combined with metrics known by the system.

........................
Netisr
........................

Show statistics from the kernel network dispatch service, known as :code:`netisr(9)`.

........................
Memory
........................

Show statistics recorded by the memory management routines  (:code:`mbuf(9)`).
The network manages a private pool of memory buffers.

........................
Bpf
........................

Show statistics about :code:`bpf(4)` peers.
This includes information like how many packets have been matched, dropped and received by the bpf device,
also information about current buffer sizes and device states.

---------------------
Packet capture
---------------------

The packet capture module can be used to deep dive into traffic passing a (or multiple) network interfaces.
It has some options you can choose from, which are detailed below.

==============================================================================================================================================

=========================== ==================================================================================================================
Interface                   List of interfaces to start a capture on. A tcpdump process is started on each selected interface
Promiscuous                 When set, the system will capture all traffic present on the interface in stead
                            of the traffic heading to the firewall.
Address Family              Capture IPv4, IPv6 or both
Invert Protocol             Select all but the protocol selected below
Protocol                    The protocol to filter on
Host Address                This value is either the Source or Destination IP address or subnet in CIDR notation.
                            The packet capture will look for this address in either field.
                            Matching can be negated by preceding the value with ":code:`not`".
                            Multiple IP addresses or CIDR subnets may be specified as boolean expression.
                            If you leave this field blank, all packets on the specified interface will be captured.
                            Example: :code:`not 10.0.0.0/24 not and not 11.0.0.1`
Invert Port                 Select all but the port selected below
Port                        Port number to filter on (e.g. :code:`443` for standard https, :code:`22` for ssh)
Packet Length               The Packet length is the number of bytes of each packet that will be captured.
                            Default value is 0, which will capture the entire frame regardless of its size.
Count                       This is the number of packets the packet capture will grab (per selected interface).
                            Default value is 100. Enter 0 (zero) for no count limit.
Description                 Description to be displayed in "jobs" tab
=========================== ==================================================================================================================

Packet capture uses `tcpdump <https://www.tcpdump.org/>`__ and runs in the background.
After a capture is performed you can either look into it using the **View capture** button in the jobs tab or download the pcap file(s) to inspect it in an external tool, such as `Wireshark <https://www.wireshark.org/>`__.

The jobs tab contains all running or executed captures, the following options are available per capture job:

.. raw:: html

      <ul>
        <li> <i class="fa fa-fw fa-spinner fa-pulse"></i>Shows the capture is currently active </li>
        <li> <i class="fa fa-fw fa-remove"></i> Remove capture (stops capture when currently active) </li>
        <li> <i class="fa fa-fw fa-stop"></i> Stop the current capture </li>
        <li> <i class="fa fa-fw fa-play"></i> (Re)starts the current capture, removes previous results when executed before </li>
        <li> <i class="fa fa-fw fa-cloud-download"></i> Download a zip file containing all captured pcap files and a json file with selected options </li>
        <li> <i class="fa fa-fw fa-file"></i> View capture in high detail</li>
        <li> <i class="fa fa-fw fa-file-text"></i> View capture in medium detail</li>
        <li> <i class="fa fa-fw fa-file-o"></i> View capture in standard detail</li>
      </ul>

.. Tip::

      All view buttons can be used when the capture is still active, they will just show the details collected until now.


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
