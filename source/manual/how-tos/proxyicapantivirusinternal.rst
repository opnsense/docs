==================================================
Setup Anti Virus Protection using OPNsense Plugins
==================================================
OPNsense can offer HTTP and HTTPS protection by utilizing its highly flexible
proxy and the industry standard ICAP. An external engine from one of the known
vendors is used to offer maximum protection against malware, such as ransomware,
trojans and viruses. This protection can be further enhanced by the built-in Intrusion
Prevention System and Category Based Web filtering.

This How To will use the Plugins C-ICAP and ClamAV.

.. Note::
    The Anti Virus Engine can protect you against malicious websites and infected
    file downloads, it does not protect the local clients. Therefore it is always
    a good idea to install a client based solution as well to protect against other
    forms of infection such as through emails or usb stick if they are not analyzed
    as well.

.. Note::
    Note that there is still another attack vector called social engineering.
    Most attacks would fail without the help of an internal human whose trust
    is exploited. An active scanner is only a part of the security concept.

Step 1 - Setup the Proxy
------------------------
Start with setting up the proxy with its basic configuration, see :doc:`cachingproxy`.

Step 2 - Setup Transparent Mode
-------------------------------
To setup the transparent mode, see: :doc:`proxytransparent`.

Step 3 - Install and Configure the ClamAV and the C-ICAP plugins
----------------------------------------------------------------

.. Note::
    The defaults from c-icap and ClamAV (vendor defaults) are used.
    Please keep in mind that changing may affect security or performance.
    If you don't know how a setting is affecting your network,
    you should keep it at the default.

- :doc:`clamav`
- :doc:`c-icap`


Step 4 - Configure ICAP
-----------------------
To configure ICAP go to **Services->Proxy->Administration** And select **ICAP Settings**
for the **Forward Proxy** tab.

Select enable ICAP and filling the Request and Response URLs.
For the C-ICAP plugin, the default URLs will be:

======================== =========================
 **Request Modify URL**   icap://[::1]:1344/avscan
 **Response Modify URL**  icap://[::1]:1344/avscan
======================== =========================

Now click on **Apply**

Step 5 - Test using EICAR
-------------------------
To test if the engine is operational and functional go to http://www.eicar.org/85-0-Download.html
on this page you will find several files you can test.

First test the HTTP protocol version. If that works, test the HTTPS version if you
have also configured the transparent SSL proxy mode.

.. Warning::
    **IMPORTANT NOTE** :
    YOU DOWNLOAD THESE FILES AT YOUR OWN RISK!


**DONE**
