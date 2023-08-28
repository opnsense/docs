==========================
Reflection and Hairpin NAT
==========================

.. contents:: Index

------------------------------------
Networks used in this How-To section
------------------------------------

=========  ===================  ===============================  ======================================
Interface  IPv4 Subnet          Hosts                            Gateway
=========  ===================  ===============================  ======================================
WAN        ``203.0.113.0/24``   ``203.0.113.1`` - OPNsense       ``203.0.113.254`` - OPNsense
DMZ        ``172.16.1.0/24``    ``172.16.1.1`` - Webserver       ``172.16.1.254`` - OPNsense
LAN        ``192.168.1.0/24``   ``192.168.1.1`` - Client         ``192.168.1.254`` - OPNsense
=========  ===================  ===============================  ======================================

--------------------
NAT - Quick Overview
--------------------

Because there are not enough available IPv4 addresses, a workaround called *NAT* (Network Address Translation) was implemented into the IPv4 Standard. It basically enables a router like the OPNsense to translate IPv4 addresses to other IPv4 addresses. Most of the time it is used to translate the limited external IPv4 address space to the shared internal IPv4 address space (RFC 1918, ``192.168.0.0/16`` - ``172.16.0.0/12`` - ``10.0.0.0/8``) and vice versa.

.. Note::

    SNAT - Source Network Address Translation
        * Changes the source IP of a packet
        * `Firewall --> NAT --> Outbound` using the option *Translation / target* in a rule
    DNAT - Destination Network Address Translation
        *  Changes the destination IP of a packet
        * `Firewall --> NAT --> Port Forward` using the option *Redirect target IP* in a rule
    PAT - Port Address Translation
        *  Changes the destination port of a packet
        * `Firewall --> NAT --> Port Forward` using the option *Redirect target port* in a rule

If you create a DNAT rule, you enable all clients in the WAN access to an internal IPv4 address. The OPNsense acts like a translator, translating IPv4 addresses between client and server. The OPNsense writes all translations into a file called the NAT table. It knows exactly how traffic should flow back and forth with the translations in place.

.. Warning::
    NAT is not a security feature. It only acts as a translator. If you want security, you need firewall rules in addition.

------------------------------------------
Introduction to Reflection and Hairpin NAT
------------------------------------------

For example, you have a Webserver ``example.com`` with the internal IP ``172.16.1.1`` in your DMZ. It has a public DNS Record of ``example.com in A 203.0.113.1``.

Your internal client ``192.168.1.1`` can't reach the Webserver if it resolves the DNS A-Record ``203.0.113.1``. When the OPNsense receives the packet from the client ``192.168.1.1`` with the destination IP ``203.0.113.1``, it chooses **itself** as the target, and **not** ``172.16.1.1``. That's because the external IPv4 address ``203.0.113.1`` is mapped to the WAN interface of the OPNsense.

That's where Reflection NAT comes into play. It creates NAT rules which help your internal client ``192.168.1.1`` to communicate with your webserver ``203.0.113.1``, by using the OPNsense as the "translator" to the actual destination ``172.16.1.1``.

.. Attention::
    You should choose your preferred Reflection NAT method from the three possible choices presented here. They're exclusive to each other, picking one method and sticking to it will prevent mistakes.

    * :ref:`Method 1 <nat-method1>` - Creating **manual** Port-Forward NAT (DNAT), **manual** Outbound NAT (SNAT), and **automatic** firewall rules
    * :ref:`Method 2 <nat-method2>` - Creating **automatic** Port-Forward NAT (DNAT), **manual** Outbound NAT (SNAT), and **manual** firewall rules
    * :ref:`Method 3 <nat-method3>` - Creating **automatic** Port-Forward NAT (DNAT), **automatic** Outbound NAT (SNAT), and **manual** firewall rules

.. Note::
    * **Reflection NAT:** The client and the server are in different subnets (layer 2 broadcast domains) and the OPNsense routes traffic between them. They can't communicate directly by resolving ARP requests. You only need DNAT.
    * **Hairpin NAT:** The client and the server are in the same subnet (layer 2 broadcast domain). They can communicate directly with each other by resolving ARP requests. You need SNAT and DNAT.
    
.. Note::
    When using IPsec, NAT only matches on policy based VPN. NAT on VTI interfaces won't match.

-------------
Best Practice
-------------

The best way to do Reflection NAT in the OPNsense is **not** to use the legacy Reflection options in :doc:`/manual/firewall_settings`. Creating the NAT rules manually with :ref:`Method 1 <nat-method1>` prevents unwanted traffic and makes auditing easy. There will be no hidden rules. All rules will be perfectly visible in the GUI and .xml config exports.

----------------------------
Start of the How-To Section:
----------------------------

The goal is to access the Webserver ``172.16.1.1`` on port ``443`` with it's external IP ``203.0.113.1`` from a client in WAN, LAN and DMZ.


.. _nat-method1:

Method 1 - Creating manual Port-Forward NAT (DNAT), manual Outbound NAT (SNAT), and automatic firewall rules
------------------------------------------------------------------------------------------------------------

Go to :menuselection:`Firewall --> Settings --> Advanced`
    Disable *Reflection for port forwards*, *Reflection for 1:1* and *Automatic outbound NAT for Reflection*

.. _nat-method1-portforward:
    
Go to :menuselection:`Firewall --> NAT --> Port Forward`
    Select **+** to create a new Port Forward rule.
    
    =========================  ================================
    Interface:                  Select ``WAN``, ``DMZ`` and ``LAN`` - Select all interfaces in which clients are that should access the webserver. This will create a linked Firewall rule in :menuselection:`Firewall --> Rules --> Floating` which allows the traffic.
    Protocol:                   Select ``TCP``
    Source:                     Select ``Any``
    Source port range:          Select ``Any``
    Destination:                Input ``203.0.113.1`` - It's the external IPv4 address of the webserver.
    Destination port range:     Input ``443`` - Or select the alias ``HTTPS``
    Redirect target IP:         Input ``172.16.1.1`` - It's the Webserver's internal IPv4 address in the DMZ.
    Redirect target port:       Input ``443`` - Or select the alias ``HTTPS``
    Description:                Input ``Reflection NAT Rule Webserver 443`` - Add a description because the linked *Filter rule association* will use that as its name and the :menuselection:`Firewall --> Rules --> Floating` rule will have it in the description.
    NAT reflection:             Use system default
    =========================  ================================
    
.. Tip::
    Reading the DNAT rule like a sentence makes it clearer:

    If a packet is received by the OPNsense on any of the interfaces ``WAN``, ``DMZ`` and ``LAN`` with protocol ``TCP`` from the source IP ``ANY`` and the source port range ``ANY`` to destination
    IP ``203.0.113.1`` and destination port ``443`` --> rewrite the destination IP to ``172.16.1.1`` and the destination port to ``443``.

.. Note::    
    The automatic linked floating firewall rule will allow traffic to the destination IP ``172.16.1.1`` because NAT rules match before Firewall rules. That means the firewall receives the packet and the NAT rule converts the destination from ``203.0.113.1`` to ``172.16.1.1`` first, before passing the packet to the firewall filter.

.. Attention::
    Now you have Reflection NAT. The traffic from the internal LAN client ``192.168.1.1`` and any WAN client reaches the Webserver.
    But there is a caveat - any DMZ client and the Webserver itself are still unable reach the external IP ``203.0.113.1``. For that you need Hairpin NAT, which involves an additional SNAT rule.

.. _nat-method1-outbound:
    
Go to :menuselection:`Firewall --> NAT --> Outbound`
    Select *Hybrid outbound NAT rule generation* and save. That way you can have manual outbound rules in conjunction with automatic IP-Masquerading rules. You could also choose *Manual outbound NAT rule generation*. Please make sure that you create your own IP-Masquerading rules with the *manual outbound NAT* enabled. 
    
    
    Select **+** to create a new Port Forward rule.
     
    =========================  ================================
    Interface:                 Select ``DMZ`` - It's the interface of the subnet the Webserver is in.
    Protocol:                  Select ``TCP``
    Source Address:            Select ``DMZ net`` - It's the alias for the DMZ Network ``172.16.1.0/24``
    Source Port:               Select ``Any``
    Destination Address:       Input ``172.16.1.1`` - It's the Webserver's internal IPv4 address in the DMZ.
    Destination Port:          Input ``443`` - Or select the alias ``HTTPS``
    Translation/target:        Select ``DMZ address`` - It's the alias for the OPNsense Interface IPv4 address ``172.16.1.254`` in the DMZ Network.
    Description:               Input ``Hairpin NAT Rule Webserver 443``
    =========================  ================================

.. Tip::
    Reading the SNAT rule like a sentence makes it clearer:

    If a packet is received by the OPNsense on the interface ``DMZ`` with protocol ``TCP`` from the source net ``172.16.1.0/24`` and the source port ``ANY`` to destination IP ``172.16.1.1`` and destination port ``443`` --> rewrite the source ip to ``172.16.1.254`` and answer from the OPNsense ``DMZ`` interface.

.. Note::
    Now all DMZ clients (and the Webserver itself) can reach the Webserver with its external IP. 
    
    * You need this additional SNAT rule to avoid asynchronous traffic between clients and servers in the same layer 2 broadcast domain. TCP traffic won't work otherwise.

Repeat :ref:`Method 1 <nat-method1>` until all additional servers are reachable.    

If you encounter any issues, check :ref:`Troubleshooting NAT Rules <troubleshooting-nat-rules>` for a few tips.

.. Warning::
    The following methods are not adviced, but are still explained in order to prevent misconfigurations. There is more information in :doc:`/manual/firewall_settings`.

.. _nat-method2:

Method 2 - Creating Automatic Port-Forward NAT (DNAT), Manual Outbound NAT (SNAT), and Manual firewall rules
------------------------------------------------------------------------------------------------------------

Go to :menuselection:`Firewall --> Settings --> Advanced`
    Enable *Reflection for port forwards* to create automatic rules for all entries :menuselection: `Firewall --> NAT --> Port Forward` that have ``WAN`` as interface.

.. _nat-method2-portforward:
    
Go to :menuselection:`Firewall --> NAT --> Port Forward`
    Create the NAT rule as in :ref:`Method 1 - Port Forward <nat-method1-portforward>` but change the following things:
    
    * Make sure that your *Port Forwarding* rule specifies only ``WAN`` as interface.

.. _nat-method2-floating:

Go to :menuselection:`Firewall --> Rules --> Floating`    
    =========================  ================================
    Action:                    Select ``Pass``
    Interface:                 Select ``WAN``, ``DMZ`` and ``LAN`` - Select all interfaces in which clients are that should access the webserver.
    Protocol:                  Select ``TCP``
    Source:                    Select ``Any``
    Destination:               Input ``172.16.1.1`` - It's the Webserver's internal IPv4 address in the DMZ. NAT matches before firewall.
    Destination port range:    Input ``443`` - Or select the alias ``HTTPS``
    Description:               Input ``Reflection NAT Rule Webserver 443``
    =========================  ================================

Go to :menuselection:`Firewall --> NAT --> Outbound`
    Create the NAT rule as in :ref:`Method 1 - Outbound <nat-method1-outbound>`

.. _nat-method3:

Method 3 - Creating Automatic Port-Forward NAT (DNAT), Automatic Outbound NAT (SNAT), and Manual firewall rules
---------------------------------------------------------------------------------------------------------------

Go to :menuselection:`Firewall --> Settings --> Advanced`
    Enable *Reflection for port forwards* to create automatic rules for all :menuselection: `Firewall --> NAT --> Port Forward` that have ``WAN`` as interface.
    Enable *Automatic outbound NAT for Reflection* to create automatic SNAT rules.

Go to :menuselection:`Firewall --> NAT --> Port Forward`
    Create the NAT rule as in :ref:`Method 2 - Port Forward <nat-method2-portforward>`

Go to :menuselection:`Firewall --> Rules --> Floating`
    Create the floating firewall rule as :ref:`Method 2 - Floating <nat-method2-floating>`

.. _troubleshooting-nat-rules:    

-------------------------
Troubleshooting NAT Rules
-------------------------

.. Tip::
    * Open SSH shell:
    * Display all loaded and active NAT rules:
    * ``pfctl -s nat``
    * "rdr" means :menuselection:`Firewall --> NAT --> Port Forward` rules.
    * "nat" means :menuselection:`Firewall --> NAT --> Outbound` rules.
    
.. Tip::    
    * Displays all NAT rules in the OPNsense debug:
    * ``cat /tmp/rules.debug | grep -i nat``
    * If there are more rules here than in ``pfctl -s nat``, it means you forgot to hit apply somewhere.
    
.. Tip::    
    * Look at the default drops of the firewall live log in :menuselection:`Firewall --> Log Files --> Live View`
    * Turn on logging of the NAT and Firewall rules you have created, and check if they match in :menuselection:`Firewall --> Log Files --> Live View`. NAT rules have the label "NAT" and blue color and firewall rules have the label "Description you gave your rule" and either green or red color.
    * In ":menuselection:`Firewall --> Diagnostics --> Sessions` you can check if there is a session between your internal client and your internal server, and which rule matches to it.
    * Use tcpdump on the client, the opnsense and the server, and test if the traffic goes back and forth between the devices without any mistakes. Look for TCP SYN and SYN ACK. If there are only SYN then the connection isn't established and there are mistakes in your rules.
