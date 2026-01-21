============================
nginx: Local Website Hosting
============================

.. Warning::

    Even if you can host websites directly from OPNsense, it is not recommended for security reasons - especially when
    sending requests to a local PHP interpreter. Do NOT consider using the feature to serve PHP content locally in
    enterprise networks. It is intended for home users who want to save money by saving power and know what they are
    doing. If you do not know how to handle a web server properly, do not enable this feature.
    
Prepare
=======

First of all, a directory has to be created. For example `/srv/web_application1`. Please note that this directory must be
accessible by nginx and PHP (both running as `www`).

For example, you can chmod it (+rx for directories, +r for files for this user) or `chown` it.

.. code-block:: sh

    # create a directory
    mkdir -p /srv/web_application1
    cd /srv
    stat web_application1
    # Example Result:
    # 86 18009 drwxr-xr-x 2 root wheel 14050 512 "Aug 31 18:28:19 2018" 
    #  "Aug 31 18:28:19 2018" "Aug 31 18:28:19 2018" "Aug 31 18:28:19 2018"
    #  32768 8 0 web_application1
    #
    # as you can see, everyone can read (r) and switch into the directory (x))
    #
    # do this if the directory is not readable or executable:
    chmod +rx web_application1
    
.. Warning::

    Never use chmod 777 and be careful with write permissions. the most secure way is to
    change the owner to www (`chown www filename`) and give write permission only to the
    web server user (`chmod o+w filename`). The same is valid for directories. It would be
    a good idea not to execute anything in those directories (for example via a special
    location block in nginx).
    If you write your own applications, it is recommended to store such data outside of
    your web root.

When the directory exists, you can create a file in this directory. Let's say, it should be called test.php and should show
some information about PHP:


.. code-block:: sh

    cat > /srv/web_application1/test.php
    <?php phpinfo();

Press control + d to end the input.

.. Note::

    you can also use vim if you install vim-lite via pkg.

.. code-block:: sh

    # If needed, change the permission to make it readable:
    chmod +r test.php

.. Note::

    In a real world scenario, you would probably copy an archive (.tar.gz, .tar.xz, .tar.bz or .zip) via SFTP or SCP on the
    firewall and execute a command to extract it. Read the man pages for tar, the compression tool or unzip for more detailed
    instructions.

Configure Locations
===================

.. image:: images/nginx_edit_location_dialog.png

For a location, the following directives are important:

=============================== ======================================================================
Directive                       Description                                                           
=============================== ======================================================================
Match Type and URL Pattern      How to match the location and the pattern                             
File System Root                Directory of web application
Upstream Servers                Send it to a remote interpreter instead of using the local one        
Pass Request To PHP Interpreter Check if you want to enable PHP (runs locally as user www) or remotely
Router Script                   Sends all request to a specific script (entry point of application)   
=============================== ======================================================================


=============================== ============================
Directive                       Value
=============================== ============================
Match Type and URL Pattern      ~* .*.php or similar
File System Root                /srv/web_application1
Upstream Servers                empty
Pass Request To PHP Interpreter checked
Router Script                   empty
=============================== ============================


Configure HTTP Server
=====================

.. image:: images/nginx_edit_http_server_dialog.png

Configuring the HTTP server is simple. You need a hostname (for example website.test), a port (8080/TCP is the
HTTP alternative port, so it is good for testing. For production sites you should stick with the defaults).
Please select the previously created location to serve web content. Please also configure a root here,
because all requests, which do not match, will be handled by the server default. The default server will
just serve the static file.


Testing
=======

To test if you web server is running, you can paste call it by its IP and port.

.. Note::

    Please note that IPv6 addresses must be enclosed within square brackets like http://[::1]/ or http://[::1]:8080/.

.. code-block:: sh

    curl "http://192.168.0.1:8080/test.php"


Security Considerations
=======================

* This is nginx and not httpd. It will not care about your .htaccess files.
  Do not put secret data in unprotected directories. You can protect those directories by yourself,
  but make sure you don't forget them. Some application depend on this file.
* Do not overlap nor use OPNsense directories as root
* Do not upload badly maintained software. If your firewall gets compromised,
  it will become easy to compromise your hosts too.
* All your applications run under the same user (www)
* Watch out for advisories_
* Install updates ASAP
* Check your logs regularly.
* Consider hardening your directory and file access permission (like making directories and files read only
  for nginx and PHP)

.. _advisories: https://nginx.org/en/security_advisories.html

