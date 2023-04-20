===========
BIND Plugin
===========

-------
History
-------

The history of the Bind plugin was a user request on OPNsense subreddit to create a
plugin with a full-featured DNS server, also able to manage zonefiles with the most
popular resource records. In the beginning the plugin was built with only general
features so the community can contribute and adding wished features with a friendly
review of the OPNsense team.

At the time of writing the plugin is able to be used as a local resolver and as a
nice replacement for pfBlockerNG or PiHole, since it is offering a DNSBL feature
via BIND Reverse Policy Zones.

------------
Installation
------------

First of all, go to :menuselection:`System --> Firmware --> Plugins` and install **os-bind**.
You will finde the plugin at :menuselection:`Services --> BIND`.

----------------
General Settings
----------------

:Enable BIND Daemon:
    Enable the BIND service.
:Listen IPs:
    Set the IP addresses the daemon should listen on.
:Listen IPv6:
    Set the IPv6 addresses the daemon should listen on.
:Listen Port:
    Set the port the daemon should listen on. Per default the port is 53530 to not
    interfere with existing Unbound/Dnsmasq setups. If you want to switch to BIND
    only, make sure to stop Unbound/Dnsmasq and switch to port 53 with both
    0.0.0.0 and :: as listening addresses set up.


:DNS Forwarders:
    A list of IP addresses BIND will forward unknown DNS request to. If empty BIND
    tries to resolve directly via the root servers.
:Logsize in MB:
    The amount for each logfile it can grow.
:Maximum Cache Size:
    This is the amount of RAM (in percent) the daemon can use for caching.
:Recursion:
    You have to set a list of networks via **ACL** tab to allow them using recursion
    against BIND.
:DNSSec Validation:
    Whether to enable or disable DNSSec validation.


-----
DNSBL
-----

:Enable DNSBL:
    Enable the DNSBL service. BIND will be configured for Reverse Policy Zones to
    blacklist domains. Choose below the lists to use for blacklist categories.
:Type of DNSBL:
    Here you can select the lists to use. Do not just select all and save. There are
    websites not loading content when nested ads are not loaded.
:Whitelist Domains:
    When a website is blocked due to a false positiv you can enter the domain name here
    so it is whitelisted before the blacklists come into play.

The Blacklists are downloaded and updated with every **Save** within BIND configuration.
For production use you can go to :menuselection:`System --> Settings --> Cron` and add a cronjob. On the
dropdown list you'll find the corret task under **Command**. Set the refresh interval
as you wish and save. This will trigger an update of the selected lists and reload
BIND.


----
ACLs
----

On tab ACLs you can create ACLs used for configuration options like **Recursion**. Add
a new ACL via **+**, give it a **Name** and add as many networks as you wish in **Network List**.
