===========
Diagnostics
===========

In order to get more insight into your network, and to help solve problems, OPNsense contains several diagnostic tools.

The tools can be found in three places:

* :menuselection:`System --> Diagnostics`
* :menuselection:`Interfaces --> Diagnostics`
* :menuselection:`Firewall --> Diagnostics`

The following tools are available:

================================================================== ===========================================================================
 :menuselection:`System --> Diagnostics --> Activity`               Show executed commands
 :menuselection:`System --> Diagnostics --> Services`               Shows running services, allows starting/stopping/restarting
 :menuselection:`Interfaces --> Diagnostics --> ARP Table`          Show ARP table, which lists local connected IPv4 peers
 :menuselection:`Interfaces --> Diagnostics --> DNS Lookup`         Easy lookup of IPs and A records that belong to a hostname
 :menuselection:`Interfaces --> Diagnostics --> NDP Table`          Show NDP table, which lists local connected IPv6 peers
 :menuselection:`Interfaces --> Diagnostics --> Packet capture`     Capture packets travelling through an interface
 :menuselection:`Interfaces --> Diagnostics --> Ping`               Ping a hostname or IP address
 :menuselection:`Interfaces --> Diagnostics --> Port Probe`         Test if a host has a certain TCP port open and accepts connections on it
 :menuselection:`Interfaces --> Diagnostics --> Trace Route`        Trace route to a hostname or IP address
 :menuselection:`Firewall --> Diagnostics --> pfInfo`               General information and statistics for pf
 :menuselection:`Firewall --> Diagnostics --> pfTop`                Currently active pf states and routes
 :menuselection:`Firewall --> Diagnostics --> pfTables`             Shows IP addresses belonging to aliases
 :menuselection:`Firewall --> Diagnostics --> Sockets`              Shows listening sockets for IPv4 and IPv6
 :menuselection:`Firewall --> Diagnostics --> States Dump`          Currently active states
 :menuselection:`Firewall --> Diagnostics --> States Reset`         Delete active states and source tracking (cancels connections)
 :menuselection:`Firewall --> Diagnostics --> States Summary`       Show states sorted by criteria like source IP, destination IP, …
================================================================== ===========================================================================
