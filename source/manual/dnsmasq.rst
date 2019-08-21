==============
Dnsmasq DNS
==============

Dnsmasq is a lightweight, easy to configure, DNS forwarder, which can be used to answer to dns queries
from your network.

Similar functionality is also provided by "Unbound DNS", our standard enabled forward/resolver service.

In some cases people prefer to use dnsmasq or combine it with our default enabled resolver (Unbound).

.. Note::

    Since OPNsense 17.7 Unbound has been our standard DNS service, the main reason for Dnsmasq being shipped
    in our product is for compatibility. Although there are some use-cases that require Dnsmasq specifically,
    most users better opt for Unbound.

-------------------------
General settings
-------------------------

Most settings are pretty straightforward here, enable the service, listen on a port (53 when empty) and
assign interfaces to listen to.
You can register dhcp static mappings as well, so the forwarder will know internally defined hosts.


-------------------------
Host overrides
-------------------------

Here you define static hostnames, which allow you to reply a specific address when being asked.

-------------------------
Domain Overrides
-------------------------

If a specific domain should be answered by a different DNS server, you can configure it here.
