============================
OpenDNS
============================

`OpenDNS <https://www.opendns.com>`__ is a company and service that extends the Domain Name System (DNS) by adding features such as phishing
protection and optional content filtering in addition to DNS lookup, if its DNS servers are used.

When you are behind a static IP address, usually it should be enough to just enter the OpenDNS name servers in
:menuselection:`System --> Settings --> General`.

-------------------------
Settings
-------------------------

A minimum amount of settings is needed in order to register with OpenDNS.

=====================================================================================================================

====================================  ===============================================================================
Enabled                               If enabled, the firewall will signal OpenDNS about address changes
Username                              Username registered with OpenDNS
Password                              Associated password
Network                               The network name configured on the
                                      `Networks Dashboard <https://www.opendns.com/dashboard/networks/>`__ of
                                      OpenDNS under 'Manage your networks'.
                                      Used to update the node's IP address whenever the
                                      WAN interface changes its IP address.
====================================  ===============================================================================

.. Note::

    When disabling the service, please check your name servers in :menuselection:`System --> Settings --> General`,
    since this feature removed the previous ones.
