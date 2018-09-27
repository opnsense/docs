===========
BIND Plugin
===========

-------
History
-------

The history of the Bind plugin was a user request on OPNsense subreddit to create a 
plugin with a full-featured DNS server, also able to manage zonefiles with the most
popular ressource records. In the beginning the plugin was build with only general 
features so the community can contribute and adding wished features with a friendly
review of the OPNsense Team.

At the time of writing the plugin is able to be used as a local resolver and as a 
nice replacement for pfBlockerNG or PiHole, since it is offering a DNSBL feature
via BIND Reverse Policy Zones.

For version 2.0 it is planned to offer full zone-file management.

------------
Installation
------------

First of all, go to **System->Firmware->Plugins** and install **os-bind**.
You will finde the plugin at **Services->BIND**.

----------------
General Settings
----------------

:Enable c-icap service:
    Enable the C-ICAP service to handle ICAP requests.
:Timeout:
    The time after which the socket will be closed.
:Max keepalive timeout:
    The time after which the socket will be closed if it stays inactive.
:Start servers:
    The count of the server processes which will be spawned.
:Max servers:
    Limit the count of processes
:Listen address:
    The address in which the server should be bound.
    This address is usually the loopback address (\:\:1 for IPv6 or
    127.0.0.1 for IPv4). The default value is \:\:1.
:Server admin:
    This field should be set to an email address which acts as a contact
    for users, who are having issues with the server.
    A good idea would be an address, which converts the mails to your internal
    ticket system.
:Servername:
    If you want to override the server name (displayed on error pages),
    you can enter it here.

    
---------
Antivirus
---------

.. image:: images/c-icap_av.png

:Enable ClamAV:
    Enables the virus
    -scan plugin of c-icap-modules using ClamAV
:Scan for filetypes:
    The type of files which should be analyzed.
    You should scan as many file types as possible but keep in mind that
    scanning requires resources which have to be available.
:Send percentage data:
    Amount of Data of the original file which should be included in the preview.
    More Data will have better scanning results and is better for security while
    a lower value improves performance.
:Allow 204 response:
    A 204 response has the advantage, that the data don't have
    to be sent over the wire again. In case of a preview, no more data
    will be sent to the ICAP server and the data will be forwarded to
    the client. In case of all data has been received by the ICAP server,
    the data does not need to be sent back. Please note, that the ICAP client
    has to support 204 responses.
:Pass on error:
    In case the scan fails, the file can be passed through.
    This is less secure but keeps the business running in case of failure.
    Keep in mind that this may put your network at risk.

