==========================
Configure Spamhaus DROP
==========================
The Spamhaus Don't Route Or Peer Lists
  DROP (Don't Route Or Peer) and DROPv6 are advisory "drop all traffic" lists,
  consisting of netblocks that are "hijacked" or leased by professional spam or
  cyber-crime operations (used for dissemination of malware, trojan downloaders,
  botnet controllers). The DROP and DROPv6 lists are a tiny subset of the SBL,
  designed for use by firewalls and routing equipment to filter out the malicious
  traffic from these netblocks.

  *Source :* https://www.spamhaus.org/drop/

For this How-To we will use the Alias feature and a firewall block rule.
The lists for this example are located here:

 * `DROP list <https://www.spamhaus.org/drop/drop.txt>`__
 * `DROPv6 list <https://www.spamhaus.org/drop/dropv6.txt>`__


-------------------------------------
Step 1 - Create an Alias for Spamhaus
-------------------------------------
Go to :menuselection:`Firewall --> Aliases --> All` and press the **Add a new alias** button in the
top right corner of the form.

Enter the following data:

+-----------------+-----------------------------------------+-----------------------------+
| **Name**        | spamhaus_drop                           | *Name of our alias*         |
+-----------------+-----------------------------------------+-----------------------------+
| **Description** | Spamhaus DROP                           | *Freely chosen description* |
+-----------------+-----------------------------------------+-----------------------------+
| **Type**        | URL Table (IPs)                         | *URL type*                  |
+-----------------+-----------------------------------------+-----------------------------+
| **Content**     | https://www.spamhaus.org/drop/drop.txt  | *Don't Route Or Peer List*  |
+-----------------+-----------------------------------------+-----------------------------+

Set the refresh frequency to 1 for each day.

Press **Save** and then **Add a new alias**.

+-----------------+-----------------------------------------+-------------------------------------+
| **Name**        | spamhaus_dropv6                          |  *Name of our alias*                |
+-----------------+-----------------------------------------+-------------------------------------+
| **Description** | Spamhaus DROPv6                          | *Freely chosen description*         |
+-----------------+-----------------------------------------+-------------------------------------+
| **Type**        | URL Table (IPs)                         | *URL type*                          |
+-----------------+-----------------------------------------+-------------------------------------+
| **Content**     | https://www.spamhaus.org/drop/dropv6.txt | *Don't Route Or Peer List v6* |
+-----------------+-----------------------------------------+-------------------------------------+

Set the refresh frequency to 1 for each day.

Press **Save** and then **Apply changes**.

.. image:: images/spamhaus_drop_dropv6.png
    :width: 100%

---------------------------------------
Step 2 - Firewall Rules Inbound Traffic
---------------------------------------
We will block incoming connections and outgoing connections for the drop and dropv6 lists.
To do so we will start with inbound traffic on the WAN interface.
Go to :menuselection:`Firewall --> Rules` Select the **WAN** tab and press the **+** icon in the
lower right corner.


Enter the following configuration and leave all other parameters on default values:

=================== ============== =============================================
 **Action**          Block          *Choose block to drop the incoming traffic*
 **Interface**       WAN            *Should be the default value*
 **TCP/IP Version**  IPv4           *For our example we use IPv4*
 **Source**          spamhaus_drop  *Our alias for the DROP list*
 **Category**        Spamhaus       *Freely chosen Category*
 **Description**     Block DROP     *Freely chosen description*
=================== ============== =============================================

**Save** and repeat this action for the DROPv6 list:

=================== =============== =============================================
 **Action**          Block           *Choose block to drop the incoming traffic*
 **Interface**       WAN             *Should be the default value*
 **TCP/IP Version**  IPv4            *For our example we use IPv4*
 **Source**          spamhaus_dropv6  *Our alias for the DROP list*
 **Category**        Spamhaus        *Freely chosen Category*
 **Description**     Block DROPv6     *Freely chosen description*
=================== =============== =============================================

.. image:: images/spamhaus_wan_rules.png
    :width: 100%


**Save**

----------------------------------------
Step 3 - Firewall Rules Outbound Traffic
----------------------------------------

Now do the same for outbound traffic traffic on the LAN interface.
Go to :menuselection:`Firewall --> Rules` Select the **LAN** tab and press the **+** icon in the
lower right corner.

=================== ============== =============================================
 **Action**          Block          *Choose block to drop the incoming traffic*
 **Interface**       LAN            *Should be the default value*
 **TCP/IP Version**  IPv4           *For our example we use IPv4*
 **Destination**     spamhaus_drop  *Our alias for the DROP list*
 **Category**        Spamhaus       *Freely chosen Category*
 **Description**     Block DROP     *Freely chosen description*
=================== ============== =============================================

**Save** and add the DROPv6 list:

=================== =============== =============================================
 **Action**          Block           *Choose block to drop the incoming traffic*
 **Interface**       LAN             *Should be the default value*
 **TCP/IP Version**  IPv6            *For our example we use IPv6*
 **Destination**     spamhaus_dropv6  *Our alias for the DROPv6 list*
 **Category**        Spamhaus        *Freely chosen Category*
 **Description**     Block DROPv6     *Freely chosen description*
=================== =============== =============================================

**Save** and **Apply changes**

.. image:: images/spamhaus_lan.png
    :width: 100%

**DONE**

---------------
Check pf Tables
---------------
To list the IP addresses that are currently in the DROP and DROPv6 lists go to
:menuselection:`Firewall --> Diagnostics --> Aliases` and select the list you want to see:

.. image:: images/spamhaus_pftable.png
    :width: 100%
