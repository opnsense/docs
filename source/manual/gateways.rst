=========
Gateways
=========


.. blockdiag::
   :desctable:

   blockdiag {
      OPNsense [shape="cisco.firewall", label=""];
      internet [shape="cloud"];
      private_net [shape="cloud", label="private net"];
      Gateway1 [shape="cisco.router", label=""];
      Gateway2 [shape="cisco.router", label=""];
      Gateway3 [shape="cisco.router", label=""];
      OPNsense -> Gateway1 -> internet;
      OPNsense -> Gateway2 -> internet [style = dotted];
      OPNsense -> Gateway3 -> private_net;

   }


Gateways define the possible routes that can be used to access other networks, such as the internet.
All different paths that are available to your firewall can be managed from this page, which can be found at :menuselection:`System->Gateways->Single`.

You can either define these gateways yourself, or they can be provided automatically from dynamical configured interfaces (e.g. dhcp), in which case they won't
have a predefined address.

When a gateway is generated automatically, you still have the ability to change its settings. Automatically generated gateways usually have
names like :code:`WAN_DHCP`.

In cases where you need to forward specific networks to a specific target, you can use static routes, which can be configured in
:menuselection:`System->Routes->Configuration` and are depended on the entries shown in the gateway page.

A specific kind of route is the :code:`default` route, this is where all traffic is being send when no other static route is configured.
There can only be one default at a time per ip protocol (ipv4, ipv6) in the system routing table.

----------------------------
Default gateways
----------------------------

Since there can only be one active default gateway, we need a method to figure out which one to use.
For both ip protocols (ipv4, ipv6), this is determined equally.

Gateways have priorities, ranging from :code:`1` [very important] to :code:`255` [least important], automatically generated
gateways will receive a low priority by default (which you can change manually).

Next there is a setting called :code:`upstream`, which marks the gateway as favourable for default gateway selection, there can be more
than one upstream configured at the same time.

When choosing a default, the algorithm will always sort :code:`upstream` gateways higher (more attractive) and will use the priority next.
If none of the gateways is explicitly chosen as upstream, the first non upstream is chosen.

In cases where gateway monitoring is configured, choosing a gateway also involves testing its current status and act accordingly when the
monitored address is not reachable.

By default the system only chooses a (new) default gateway on startup or when an interface is connected or disconnected. In many cases
you might want the default gateway also changed when the current gateway is not reachable anymore (via configured monitoring), in which
case you can enable "Gateway switching" in :menuselection:`System->Settings->General`

.. Tip::

    In case you have multiple (dynamic) gateways, which should fall over in a specific order on failure, just set a **priority** and **upstream** flag.
    (e.g. favour fiber optics above 4g) You choices should be reflected accordingly in the gateway grid (most important first).


----------------------------
Overview page
----------------------------

The overview page (:menuselection:`System->Gateways->Single`) shows all currently known gateways and their statuses in order of importance (most important on top).
When a gateway is considered "default" it will show **(active)** behind the name.

.. Note::

  The **(active)** status shown in the list reflects the current calculated default, which might differ from the machine routing if gateway switching is not enabled.
  You can always check the current active default in :menuselection:`System->Routes->Status`

.. Tip::

  When debugging dynamic gateway issues, always check if your expected gateway is actually in the list. The system will only consider
  items shown here.

----------------------
Settings
----------------------

Below you will find the most important settings that are available for a gateway item.

============================= =============================================================================
Disabled                      (temporary) disable this item
Name                          Unique name for this gateway
Description                   Optional description for this item
Interface                     The interface this gateway is connected to
Address Family                IP family (v4 or v6)
IP address                    Address of our gateway, empty/**dynamic** when dynamically generated.
Upstream Gateway              Upstream gateway, consider this gateway as default gateway candidate
Far Gateway                   Checkbox to allow the gateway to exist outside of the interface subnet.
Disable Gateway Monitoring    Disable monitoring (consider **online**)
Monitor IP                    Alternative address to monitor, always make sure the address is
                              actually reachable and using this interface (via a static gateway)
Mark Gateway as Down          Consider this gateway as down, so it can't be considered as default gateway
Priority                      Prioritizes this gateway, a lower value means more important.
============================= =============================================================================


---------------------------
Troubleshooting
---------------------------

Missing dynamic gateway
..........................

Most dynamic interface types write their current gateway into a file named :code:`/tmp/[interface]_router` or :code:`/tmp/[interface]_routerv6`.
When the expected gateway is not listed in the page, there might be an issue with the interface type (for example the remote server isn't providing one at the moment).


Gateway marked offline
.........................

When a gateway is marked offline, always check if the monitor address is reachable via the correct interface first.
You can use :menuselection:`Interfaces->Diagnostics->Ping` to test connectivity.
In case the monitor address is not in the same subnet as the interface,
also check if there's a static route (:menuselection:`System->Routes->Status`) available which sends the requested traffic to the correct upstream gateway.

There should always be a :code:`dpinger` process active, which you can check on the services page (:menuselection:`System->Diagnostics->Services`),
finally if all seems to be running you can deep dive into the packets leaving the interface,
if dpinger is active, there should be ICMP packets heading to your monitor address, which
you can inspect using :menuselection:`Interfaces->Diagnostics->Packet Capture`.
