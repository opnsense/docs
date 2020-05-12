==============
Log Files
==============

When troubleshooting problems with your firewall, it is very likely you have to check
the logs available on your system. In the UI of OPNsense, the log files are generally grouped
with the settings of the component they belong to. The log files can be found here:

================ ======================================================== =============================================================================
 **Live View**    :menuselection:`Firewall --> Log Files --> Live View`    *View firewall logs in realtime, smart filtering can be applied*
 **Plain View**   :menuselection:`Firewall --> Log Files --> Plain View`   *Just the plain contents how **pf** logs into **filter.log** *
================ ======================================================== =============================================================================

Live View
---------

Live view updates itself in realtime if a rule is matched that has logging enabled or one of the global logging options is enabled under:
:menuselection:`System --> Settings --> Logging`

For better troubleshooting you can provide a filter string. This filter may include regular expressions.
Lets assume one logging entry as one single string without special separators.

So for just displaying packets that match DNS replies from wan to your lan clients in segment 192.168.1.0/24, you have to use:

.. code-block:: sh

    WAN.*:53.*192.168.1

or to be even more correct

.. code-block:: sh

    WAN.*:53.*192\.168\.1\.

==========  ====================== ===================== ======================  ========================
 **WAN**     **.***                 **:53**               **.***                  **192\.168\.1\.**
 Interface   1 or more characters   first match of port   1 or more characters    destination ip address
==========  ====================== ===================== ======================  ========================
