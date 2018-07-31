=============
Using Aliases
=============
Aliases are named lists of networks, hosts or ports that can be used as one entity
by selecting the alias name in the various supported sections of the firewall.
These aliases are particularly useful to condense firewall rules and minimize
changes.

-----------
Alias Types
-----------
OPNsense offers the following alias types:

+------------+------------------------------------------------------+
| Type       | Description                                          |
+============+======================================================+
| Hosts      | Single hosts by IP or Fully Qualified Domain Name    |
+------------+------------------------------------------------------+
| Networks   | Entire network p.e. 192.168.1.1/24                   |
+------------+------------------------------------------------------+
| Ports      | Port numbers or a port range like 20:30              |
+------------+------------------------------------------------------+
| URL Tables | A table of ip addresses that can be fetched          |
+------------+------------------------------------------------------+
| GeoIP      | Select countries or whole regions                    |
+------------+------------------------------------------------------+

-----
Hosts
-----
Hosts can be entered as a single IP address or a fully qualified domain name.
When using a fully qualified domain name, the name will we resolved periodically
(default is each 300 seconds).

Sample
  Lets say we want to create an alias table for **www.youtube.com**

  .. image:: images/aliases_host.png
      :width: 100%

**Apply changes** and look at the content of our newly created pf table.
Go to **Firewall->Diagnostics->pfTables** and select our newly created youtube table.

.. image:: images/pftable_youtube.png
    :width: 100%

As you can see there are multiple ip addresses for this domain.

--------
Networks
--------
Networks are specified in Classless Inter-Domain Routing format (CIDR). Use the
the correct CIDR mask for each entry. For instance a /32 specifies a single IPv4 host,
or /128 specifies a single IPv6 host, whereas /24 specifies 255.255.255.0 and
/64 specifies a normal IPv6 network.

-----
Ports
-----
Ports can be specified as a single number or a range using a colon **:**.
For instance to add a range of 20 to 25 one would enter 20:25 in the **Port(s)**
section.

----------
URL Tables
----------
URL tables can be used to fetch a list of ip addresses from a remote server.
There are several IP lists available for free, most notably are the "Don't Route
Or Peer" lists from Spamhaus.

-----
GeoIP
-----
With GeoIP alias you can select one or more countries or whole continents to block
or allow. Use the *toggle all* checkbox to select all countries within the given
region.

This feature was reworked with 17.7.7 and supersedes the GeoIP blocking via IPS.

  .. image:: images/firewall_geoip_alias.png
      :width: 100%

--------------
Import Feature
--------------
To quickly add a list of aliases OPNsense also offers an import feature, where
you can paste or enter a list in text format.

Common examples are lists of IPs, networks, blacklists, etc.
The list may contain IP addresses, with or without CIDR prefix, IP ranges,
blank lines (ignored) and an optional description after each IP. e.g.:

.. code::

  172.16.1.2
  172.16.0.0/24
  10.11.12.100-10.11.12.200
  192.168.1.254 Home router
  10.20.0.0/16 Office network
  10.40.1.10-10.40.1.19 Managed switches

Spamhaus
--------

The Spamhaus Don't Route Or Peer Lists
  DROP (Don't Route Or Peer) and EDROP are advisory "drop all traffic" lists,
  consisting of netblocks that are "hijacked" or leased by professional spam or
  cyber-crime operations (used for dissemination of malware, trojan downloaders,
  botnet controllers). The DROP and EDROP lists are a tiny subset of the SBL,
  designed for use by firewalls and routing equipment to filter out the malicious
  traffic from these netblocks.

  *Source :* https://www.spamhaus.org/drop/

Downloads
 * `DROP list <https://www.spamhaus.org/drop/drop.txt>`__
 * `EDROP list <https://www.spamhaus.org/drop/edrop.txt>`__

----------------------------------
Using Aliases in pf Firewall Rules
----------------------------------
Aliases can be used in the firewall rules to make administration of large lists
easy. For instance we could have a list of remote ip's that should have access to
certain services, when anything changes we only need to update the list.

Lets create a simple alias list and assume we have 3 remote ip's that may access
the ipsec server for a site to site tunnel connection:

* 192.168.100.1
* 192.168.200.2
* 192.168.300.3

.. image:: images/alias_remote_ipsec.png
    :width: 100%

We call our list remote_ipsec and update our firewall rules accordingly.

.. image:: images/alias_firewall_rules.png
    :width: 100%

Notice the list icon to identify a rule with an alias (list).

--------
Advanced
--------
For hosts it is possible to use lists in lists. Per example you could have:

* critical_servers {10.0.1.1 , 10.0.1.2}
* other_servers {10.0.1.100 , 10.0.1.200}

Then concatenate both by defining a new list:

* servers { critical_servers , other_servers}.

The end result will be a list with all ip addresses in one alias list (servers).

------------------------------
Configure DROP and EDROP lists
------------------------------
To setup the DROP and EDROP lists in combination with the firewall rules, read:
:doc:`how-tos/edrop`
