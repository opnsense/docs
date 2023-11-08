=======================
Users & Groups
=======================

.. image:: images/usermanager_groups.png
   :width: 100%

With the local user manager in OPNsense one can add users and groups and define
the privileges for granting access to certain parts of the GUI (Web Configurator).

Adding Users
------------
To add a new user go to :menuselection:`System --> Access --> Users` and click on the **+** sign at
the bottom right corner of the form.

==================================================================================================

=========================== ============ =========================================================
**Disabled**                Unchecked    *Can be used to (temporarily) disable an account*
**Username**                John         *A unique username*
**Password**                secret       *A strong password*
**Full name**               John Doe     *Optional, Full username, for reference only*
**E-Mail**                  a@b.com      *Optional, users email, for reference only*
**Comment**                              *Optional, comment field, for reference only*
**Preferred landing page**  ui/page      *Optional, landing page to visit after login*
**Login shell**             /bin/csh     *The shell to use when logging in via the console.*
**Expiration date**                      *Optional, if account should expire enter as mm/dd/yyy*
**Group Membership**                     *Optional, select one or more groups*
**Effective Privileges**                 *Optional, additional grants for this user,*
                                         *usually these are being handled via a group*
**User Certificates**                    *Optional, check if a user certificate should be created*
**API keys**                             *Optional, when planning to use the API from*
                                         *another application, create keys for this user*
**OTP seed**                             *Optional, enter or generate a OTP seed (base32)*
**Authorized keys**                      *Optional, paste ssh key for ssh console access*
=========================== ============ =========================================================


Creating Groups
---------------
Go to :menuselection:`System --> Access --> Groups` and click on the **+** sign in the lower right
corner of the form.

Enter a **Group name** and a **Description** and add users to the group.

When users should access resources on this firewall via a group, connect the relevant ones via **Assigned Privileges**.
