=================
OpenConnect Setup
=================

------------
Introduction
------------

OpenConnect is a SSL VPN client initially created to support Cisco's AnyConnect SSL VPN.
It has since been ported to support the Juniper SSL VPN which is now known as Pulse Connect Secure.
Palo Altos Global Protect will also be supported in future and of course the own OpenConnect Server.


---------------------
Step 1 - Installation
---------------------

Go to :menuselection:`System --> Firmware --> Plugins` and search for **os-openconnect**.
Install the plugin as usual, refresh and page and the you'll find the client via
:menuselection:`VPN --> OpenConnect`.

--------------
Step 2 - Setup
--------------

The setup of the client is very simple. Just tick **Enable** and fill out **VPN Server**,
**Username** and **Password**. Be sure that the FQDN matches the name in the certificate 
or you will receive an error. Also wildcard certificates can produce errors.

Once enabled, a new interface will be available for specifying firewall rules;
:menuselection:`Firewall --> Rules --> OpenConnect` will appear.

------------------------------
Step 3 - Troubleshoot problems
------------------------------

To troubleshoot connection problems it's best to login via CLI and start OpenConnect manually:

# /usr/local/etc/rc.d/opnsense-openconnect start

Look out for errors like


``To trust this server in future, perhaps add this to your command line: --servercert sha256:9f97a3395d18093a14f0d8e768dabee231af34d9ba35432dfe838d58dd633333``
    
Now the field **Certificate Hash** comes into play, so please insert the string above without
the hash size and set this one in field **Certificate Hash Type**.
