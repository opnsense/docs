===================
Access Control List
===================

.. sidebar:: Access Control List

    .. image:: images/acl-finger-print.jpg

--------
Overview
--------

The ACL system is targeted at delivering backwards compatibility
for legacy code and being able to extend this to add new
features without having to reimplement the whole system.

The following steps determine if a page can be accessed by a user:

#. The user, stored in the config.xml file at system/user may set "Effective Privileges" valid for that explicit entry, stored in <priv/> sections
#. One or more groups for that user, stored in system/group which contains priv sections as well.
#. An XML file (:code:`ACL.xml`) linking logical acl keys to uri patterns

Access controls for most legacy components are stored in models/OPNsense/Core/ACL/ACL.xml, most new components add their own
ACL's in the model belonging to the component. All stored :code:`ACL.xml` files combined determine the full set of options available
in the user/group manager. There is no expicit requirement which model services which ACL.

.. Note::

    When in need of a single ACL to match an explicit set of components (pages/api endpoints), one can add an ACL file easily
    for a module without further logic. 

---------------
ACL format
---------------

Each ACL file is stored in the model location (/usr/local/opnsense/mvc/app/models/) where :code:`ACL.xml` files
are stored in the location [VENDOR]/[MODULE]/ACL/ACL.xml. The format of the file is as follows:

.. code-block:: html

  <acl>
    <my-unique-acl-key>             <---- as stored for the user/group
       <name>My ACL name</name>     <---- name visible in the user manager
       <patterns>
          <pattern>path/to/my/module</pattern>      <--- list of uri's this ACL should unlock.
       </patterns>
    </my-unique-acl-key>
  </acL>


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
