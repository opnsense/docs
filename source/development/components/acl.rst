===================
Access Control List
===================

.. sidebar:: Access Control List

    .. image:: images/acl-finger-print.jpg

--------
Overview
--------

The current ACL system is targeted at delivering backwards compatibility
for legacy code and being able to extend this a little to add new
features without having to reimplement the whole system.

In the legacy system the access control is using the following steps to
determine if a page can be accessed by a user:

#. The user, stored in the config.xml file at system/user (one item per
   user)
#. One or more groups for that user, stored in system/group which
   contains priv sections.
#. A PHP file binding the priv section content to a page mask (including
   wildcards)

Our temporary solution is to keep the user and the group in place and replace the
PHP file with a simple config in the model which uses the same mask construction
there was in the old codebase. To bind priv to pages, edit models/OPNsense/Core/ACL\_Legacy\_Page\_Map.txt

--------------
Usage from PHP
--------------

Using the system from PHP is rather simple:

.. code-block:: php

    $acl = new OPNsense\Core\ACL();
    if ( $acl->isPageAccessible("user", "/firewall_rules.php") ) {
      print ( "/firewall_rules.php is accessible" ) ;
    }

-----------------------
Usage in Volt templates
-----------------------

The ACL scheme is bound to the default UI controller, and can be used by
using the acl keyword:

.. code-block:: jinja

    {% if acl.isPageAccessible(session.get('Username'),subMenuItem.Url)  %}
      this page is accessible
    {% endif %}
