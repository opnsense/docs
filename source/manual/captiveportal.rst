=========================
Captive portal & GuestNET
=========================
A **Captive Portal** allows you to force authentication, or redirection to a click
through page for network access. This is commonly used on hotspot networks,
but is also widely used in corporate networks for an additional layer of security
on wireless or Internet access.

.. image:: images/hotspot_login.png

Overview and terminology
.........................


-----------------------------
Typical Applications
-----------------------------

* Guest Network
* Hotel & Camping Wi-Fi Access
* Bring Your Own Device (BYOD)

-------------------
Template Management
-------------------
OPNsense’s unique template manager makes setting up your own login page an easy
task. At the same time it offers additional functionalities, such as:

* URL redirection
* Option for your own Pop-up
* Custom Splash page

.. image:: images/captiveportal_template_folder.png

---------------
Zone Management
---------------
Different zones can be setup on each interface or multiple interfaces can share
one zone setup. Each Zone can use a different Captive Portal Template or share it
with another zone.

--------------
Authentication
--------------
Secure authentication via HTTPS or splash-only portal with URL redirection to a
given page Different sources can be used to authenticate a user in a zone:

* LDAP [Microsoft Active Directory]
* Radius
* Local user manager
* Vouchers / Tickets
* No authentication (Splash Screen Only)
* Multiple (a combination of above)

---------------
Voucher Manager
---------------
OPNsense's Captive Portal has an easy voucher creation system that exports the
vouchers to a csv file for use with your favorite application. The export allows
you to print vouchers by merging them with your Microsoft Word or LibreOffice template and
create a good looking handout with your logo and company style.

-----------------------
Timeouts & Welcome Back
-----------------------
Connection can be terminated after the user has been idle for a certain amount
of time (idle timeout) and/or force a disconnect when a number of minutes
have passed even if the user is still active (hard timeout). In case a user
reconnects within the idle timeout and/or hard timeout no login is required and
the user can resume its active session.

--------------------
Bandwidth Management
--------------------
The Built-in traffic shaper can be utilized to:

* Share bandwidth evenly
* Give priority to protocols port numbers and/or IP addresses

See also: :doc:`/manual/shaping`

-------------
Portal bypass
-------------
MAC and IP addresses can be white listed to bypass
the portal.


--------------------
Platform Integration
--------------------
Through the integrated REST API the captive portal application can be integrated
with other services. See: :doc:`/development/how-tos/api`


Administration
.........................

The Administration menu offers access to zone configuration and template management.

When creating a zone, a couple of options are available which we will try to explain briefly in the grid below:

========================================================================================================================================================

====================================  ==================================================================================================================
Enabled                               Enable the zone, which will install a network trap on the interfaces specified
Zone number                           Read-only sequence of the configured zone
Interfaces                            Interfaces which should be guarded by this captive portal
Allow inbound                         Select interfaces from which to allow inbound (stateful) traffic.
                                      This can be convenient if the zone in question contains machines/servers which should be
                                      accessible from other networks attached to this firewall.
Authenticate using                    Select an authenticator specified in :menuselection:`System --> Access --> Servers`
Always send accounting requests       [RADIUS only] This will make the captive portal always send accounting requests,
                                      rather than just when there is a need for accounting (e.g. when there is a daily session limit).
Enforce local group                   Restrict access to users in the selected (local)group, to validate group membership,
                                      see :menuselection:`System --> Access --> Groups`
Idle timeout (minutes)                Clients will be disconnected after this amount of inactivity. They may log in again immediately, though.
Hard timeout (minutes)                Clients will be disconnected after this amount of time, regardless of activity.
                                      They may log in again immediately, though.
Concurrent user logins                If this option is set, users can login on multiple machines at once.
                                      If disabled subsequent logins will cause machines previously logged in with the same username to be disconnected.
SSL certificate                       Certificate to use on the captive portal login system. Leave empty for HTTP only.
Hostname                              Hostname (of this machine) to redirect login page to, leave blank to use this interface IP address,
                                      otherwise make sure the client can access DNS to resolve this location.
                                      When using a SSL certificate, make sure both this name and the cert name are equal.
Allowed addresses                     Avoid authentication for addresses and subnets specified in this list
Allowed MAC addresses                 Avoid authentication for MAC addresses specified in this list
Extended pre auth data                Offer extended data to the login template before authentication (mac addresses for upstream use).
Custom template                       Template to use for the login page, specified in the templates tab.
====================================  ==================================================================================================================

.. raw:: html

    In the templates tab you can manage your templates, the default template can be fetched using the <i class="fa fa-fw fa-download"></i> button
    in the bottom right corner.
    <br/><br/>
    The file offered is a standard zip file, which can be unpacked locally and modified to your needs, the  new contents can be saved into a new
    zip file and uploaded in a new template (<i class="fa fa-fw fa-plus"></i>)


Sessions
.........................

Basic Real Time Reporting is Integrated using the sessions menu, this shows the following information for each zone.

* Live top IP bandwidth usage (Traffic Graph)
* Active Sessions
* Time left on Vouchers

Vouchers
.........................

Here you can create new vouchers for all voucher servers configured in :menuselection:`System --> Access --> Servers`


Examples
.........................

To setup a hotspot controller for business or hotel usage see:
:doc:`how-tos/guestnet`
