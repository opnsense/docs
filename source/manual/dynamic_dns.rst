.. |br| raw:: html

    <br>

===========
Dynamic DNS
===========

Normally, a hostname is tied to a fixed IP address. This works well if the server the hostname is used for has a
static IP address. However, a static IP address is not always an option. In order to tie a hostname to a dynamic
IP address, a Dynamic DNS service can be used.

-------------------------------
Setting up a dynamic IP address
-------------------------------

In the web interface, go to :menuselection:`Services --> Dynamic DNS`. In the upper right corner, click **Add**.

A form will now appear with the following fields:

======================= =======================================================================================================================================================================
  Field                  Explanation
======================= =======================================================================================================================================================================
  Enable                 Enable this rule (allows turning entries off without removing them).
  Service type           The provider of your Dynamic DNS Service. If you use one not in the list, select “Custom” or “Custom (v6)”.
  Interface to monitor 	 This will usually be WAN.
  Hostname               Enter the complete host/domain name. For example: *myhost.dyndns.org*
  MX                     Set this option only if you need a special MX record. Not all services support this. Note: with a dynamic DNS service you can only use a hostname, not an IP address.
  Wildcards 	         Enable Wildcard
  Verbose logging 	     Enable verbose logging
  Username               Username is required for all types except Namecheap, FreeDNS and Custom Entries.
  Password
  Description            A description to easily identify this rule in the overview.
======================= =======================================================================================================================================================================

If you select “Custom” or “Custom (v6)” under “Service type”, more fields will appear:

=============================== =============================================================================================================================================================================================================================
  Field                          Explanation
=============================== =============================================================================================================================================================================================================================
 Interface to send update from   Most likely to be the same as “Interface to monitor”.
 CURL options                    Options passed to the ``curl`` command. These include `Verify SSL peer  <https://curl.haxx.se/libcurl/c/CURLOPT_SSL_VERIFYPEER.html>`_ and `Force IPv4 resolving <https://curl.haxx.se/libcurl/c/CURLOPT_IPRESOLVE.html>`_.
 Update URL                      An URL to let the Dynamic DNS provider know your IP address has changed. See the “full help” for information on how to use it.
 Result Match                    Can be used to verify the reply from the server, in order to distinguish confirmations from errors. See the “full help” for information on how to use it.
=============================== =============================================================================================================================================================================================================================

^^^^^^^^^^^^^^^^^^^^^^
Provider-specific info
^^^^^^^^^^^^^^^^^^^^^^

+------------------------------+------------------------------------------------------------------------------------------+
| Provider                     | Specifics                                                                                |
+==============================+==========================================================================================+
| Custom / Custom (v6)         | Username and Password fields represent HTTP Basic Authentication username and passwords. |
+------------------------------+------------------------------------------------------------------------------------------+
| Duck DNS                     | Username field: Enter your Token. |br|                                                   |
|                              | Password field: Leave empty.                                                             |
+------------------------------+------------------------------------------------------------------------------------------+
| FreeDNS (freedns.afraid.org) | Password field: Enter your “Authentication Token”.                                       |
+------------------------------+------------------------------------------------------------------------------------------+
| he.net tunnelbroker          | Hostname field: Enter your “Tunnel ID”.
+------------------------------+------------------------------------------------------------------------------------------+
| Route 53                     | Username field: Enter your “Access Key ID”. |br|                                         |
|                              | Password field: Enter your “Secret Access Key”.                                          |
+------------------------------+------------------------------------------------------------------------------------------+
