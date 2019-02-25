=======================
nginx: Header Hardening
=======================

.. Note::

    Except some specific configuration directives, this is **NOT**
    specific to the nginx plugin. Please note that you can also debug your
    frontend code this way.


Background Information
======================

HTTP headers can control, what a web application is allowd to do and what it is
not. This can be used to harden the web application against some **client side risks**.


Testing Web Applications Using A Local Proxy
============================================

Configuration of Firefox
------------------------

For this tests, you should install and configure FoxyProxy_.

.. _FoxyProxy: https://addons.mozilla.org/de/firefox/addon/foxyproxy-standard/

After it is installed, click on the proxy settings and add a new one:

.. image:: images/zap_foxyproxy.png

As a proxy, enter localhost (or 127.0.0.1 in case localhost does not work) and
the port 8080. Save the settings.


Downloading A Proxy Software For Testing
----------------------------------------

Well known Test tools are:

* OWASP ZAP (https://github.com/zaproxy/zaproxy)
* Burp (https://portswigger.net/burp)
* mitmproxy (https://mitmproxy.org/)


When it is downloaded, you usually have to unpack it into a fitting directory.``
When it is unpacked, you need to run it. In case of ZAP, doubleclick the
``zap.sh`` or ``zap.bat`` depending on your operating system.

Next regenerate and export the certificate under
``Tools -> Options -> Dynamic SSL certificates`` and import it into the Firefox
key store (Preferences -> Data Protection & Security -> Show Certificates) with
full trust.

Start Testing
-------------

Click on the FoxyProxy icon and select the localhost proxy defined first.
Next just use the application as usual. If you click the red button,
can stop the request in ZAP and it allows you to edit it:

.. image:: images/zap_request.png

When you are done, just click one of the play buttons to disable halting or wait
for the next request / response to edit that as well. For example the response
could look like this one:

.. image:: images/zap_response.png

You can see a lot of important information here like the used protocol (HTTP/1.1),
the Status 200, which means it was successful and a lot of headers.
Some of those headers impact security and ZAP will try to make a recommendation,
which may not be always correct but it may help you to find some (forgotten)
issues:

.. image:: images/zap_warnings.png

The colors of the flags show how high the risk is rated so the more red it is,
the more impact it has on security. The left view conteins a list of the
findings, the right view a detailed description of them.
Based on this information, you have to decide your further actions.


Testing Web Applications Using Developer Tools
==============================================


When you right click on the web site, you can inspect the element but the
opening tools also have a tab for networking.

.. image:: images/firefox_devtools_network.png

The network tab works like the main view of the proxy.
You can see which headers are sent and which ones are received.
The advantage here is that you get some errors on the console tab (for example
if the CSP has an error). The disadvantage of the console is, that is is not so
easy to intercept and modify data.


Inject Missing Headers Via The nginx Plugin
===========================================

Security headers in the nginx plugin can be injected by creating a new security
header configuration:

.. Image:: images/nginx_security_headers.png

If you set a setting here, it will override what the webserver sets.
You can inject this security setting into a location or HTTP server.

You can read about the headers in the Mozilla Wiki_ or in the RFCs.

.. _Wiki: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

.. Warning::

   Not all headers are supported by all browsers.
