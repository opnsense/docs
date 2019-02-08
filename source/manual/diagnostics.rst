===========
Diagnostics
===========

In order to get more insight into your network, and to help solve problems, OPNsense contains several diagnostic tools.

The tools can be found in three places:

* **System -> Diagnostics**
* **Interfaces -> Diagnostics**
* **Firewall -> Diagnostics**

The following tools are available:

=================================================== ===========================================================================
 **System -> Diagnostics -> Activity**               Show executed commands
 **System -> Diagnostics -> Services**               Shows running services, allows starting/stopping/restarting
 **Interfaces -> Diagnostics -> ARP Table**          Show ARP table, which lists local connected IPv4 peers
 **Interfaces -> Diagnostics -> DNS Lookup**         Easy lookup of IPs and A records that belong to a hostname
 **Interfaces -> Diagnostics -> NDP Table**          Show NDP table, which lists local connected IPv6 peers
 **Interfaces -> Diagnostics -> Packet capture**     Capture packets travelling through an interface
 **Interfaces -> Diagnostics -> Ping**               Ping a hostname or IP address
 **Interfaces -> Diagnostics -> Port Probe**         Test if a host has a certain TCP port open and accepts connections on it
 **Interfaces -> Diagnostics -> Trace Route**        Trace route to a hostname or IP address
 **Firewall -> Diagnostics -> pfInfo**               General information and statistics for pf
 **Firewall -> Diagnostics -> pfTop**                Currently active pf states and routes
 **Firewall -> Diagnostics -> pfTables**             Shows IP addresses belonging to aliases
 **Firewall -> Diagnostics -> Sockets**              Shows listening sockets for IPv4 and IPv6
 **Firewall -> Diagnostics -> States Dump**          Currently active states
 **Firewall -> Diagnostics -> States Reset**         Delete active states and source tracking (cancels connections)
 **Firewall -> Diagnostics -> States Summary**       Show states sorted by criteria like source IP, destination IP, …
=================================================== ===========================================================================
