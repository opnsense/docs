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
**Synchronize groups**                         *Enable to read groups from RADIUS server - requires the
                                               CLASS attribute to return the designated (single*) group*
**Limit groups**                               *Select list of groups that may be considered during sync*
**Automatic user creation**                    *This offers the ability to automatically create the
                                               user when it doesn't exist - requires "Synchronize groups"
                                               to be enabled and actually return a group for a user.*
============================== =============== =========================================================

.. Note::
   RADIUS does not support a *memberOf* group concept by design. OPNsense uses the returned CLASS attribute
   instead to find a string containing the user's group membership. Since the **Synchronize groups**
   feature shares the same code of the LDAP server feature **Synchronize groups** the string defined as
   CLASS value must be prefixed with *CN=* (e.g. *CLASS="CN=MyVPN-Group"*)!

   *Additionally the group separator must be a line break (*\n*). Some RADIUS servers (e.g. MS NPS) will not
   support special characters in the string value, the return value is therefore limited to a single line 
   (which in turn translates into a single group).

Use the tester under :menuselection:`System --> Access --> Tester` to test the Radius server.

If you want to use the FreeRADIUS plugin set up the server as 127.0.0.1 and don't forget to add a **Client** in the FreeRADIUS configuration.
