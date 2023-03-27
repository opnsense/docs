=====================================
Access / Servers / Radius
=====================================

Configuring a Radius server for user authentication in services like vpn or captive portal
is easy just go to :menuselection:`System --> Access --> Servers` and click on **Add server** in the top right corner.

Fill in the form:

============================== =============== =========================================================
**Descriptive name**            radius_test    *Enter a descriptive name*
**Type**                        Radius         *Select Radius*
**Hostname or IP address**      10.10.10.1     *Enter the IP of your Radius server*
**Shared Secret**               secret         *Shared secret for your Radius server*
**Services offered**            Authentication *Select Authentication,for Captive portal + accounting*
**Authentication port value**   1812           *Port number, 1812 is default; for accounting it's 1813*
**Authentication Timeout**      5              *Timeout for Radius to respond on requests*
**Synchronize groups**                         *Enable to Synchronize groups, requires the option above*
**Limit groups**                               *Select list of groups that may be considered during sync**
**Automatic user creation**                    *When groups are automatically synchronized,
                                               this offers the ability to automatically create the
                                               user when it doesn't exist.*
============================== =============== =========================================================

Use the tester under :menuselection:`System --> Access --> Tester` to test the Radius server.

If you want to use the FreeRADIUS plugin set up the server as 127.0.0.1 and don't forget to add a **Client** in the FreeRADIUS configuration.
