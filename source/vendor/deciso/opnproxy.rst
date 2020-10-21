======================================
Deciso: Proxy access management
======================================

As part of the OPNsense Business Edition, Deciso offers a plugin to add fine grained access control to your existing
web proxy setup.

One of the features often requested is to easily (dis)allow (groups of) users access to certain domain or url parts,
the :code:`OPNProxy` plugin addition offers this functionality at ease.

Installation
---------------------------

Installation of this plugin is rather easy, go to :menuselection:`System --> Firmware --> Plugins` and search for **os-OPNProxy**,
use the [+] button to install it.

Next go to :menuselection:`Services --> Web Proxy --> Access control` to start configuring polcies.

.. Note::

    Redis is required for this plugin to operate, when accessing the access control settings page for the first time you will be pointed to the correct
    setting to enable it directly. (just enable and apply should be enough)

General
---------------------------

In order to utilise user/group based policies, the proxy needs to be able to inspect the traffic and know the identity of the
user.

Since most of the internet is being encrypted nowadays, you would need to enable some sort of ssl inspection in between.
When setting "Enable SSL inspection" in :menuselection:`Services -> Webproxy -> Administration -> Forward Proxy`
you are able to use a "man-in-the-middle" approach (where the proxy intercepts traffic and is able to filter it).
A disadvantage of this option is that your clients would need to trust the firewalls certificate (CA selected in "CA to use").
When enabled full paths can be filtered.

A bit lighter option would be to use SSL inspection with "Log SNI information only" enabled,
in which case the firewall would know which domain you are trying to visit, but can not inspect the content of the request (or response for that matter).

.. Note::

    When enabling "Log SNI information only", only domain based policies will be usable for SSL/TLS based requests.

The standard authentication options available in OPNsense apply, which can be configured in
:menuselection:`Services -> Webproxy -> Administration -> Forward Proxy -> Authentication settings`. Please make sure
to import/add the users in OPNsense in order to user their authorisation settings (existence and group membership).


.. Note::

    Standard (global) policies take precedence over the ones defined in the access control plugin, this includes
    "SSL no bump sites" when full TLS/SSL inspection is used.
    (it's not possible to block no bump sites in full inspection mode)


Policy types
---------------------------

Part of OPNproxy is a standard list of categorized locations, which can be easily added to a policy, these type of policies
are the default ones. You will find categories here like :code:`adult`, :code:`advertisements`, :code:`malware` and many others.

In some cases however our defaults are not enough, for this reason we also offer the posibility to push your own list of
domains and locations into a custom policy.

Every policy contains what to match (either a standard category or a list of domains and paths), what to do (allow or deny)
and an audience (the users and/or groups the policy applies to).

Since both users and groups can be selected within the same policy, we choose to prefix users with a :code:`*`.

.. Tip:

    For easy administration it's generally a good idea to use groups in policies instead of users.

Prioritisation within our access control is quite easy and should cover all possible scenarios, below the order in which
decisions are made:

1.  No policy, default allow. When authentication is properly setup, this means that access depends on supplying valid credentials.
2.  Explicit allow, the closest matching policy (see text below) returns accept, access will be granted (also when another policy returns deny)
3.  Explicit deny, the closest matching policy returns deny, access will be denied


Closest matching explained
.............................

One of the key features of our access control system is a method to find the best suitable policy for the requested domain
or url.

This means that if someone defines two ACL's one denying access to all google.nl subdomains (:code:`.google.nl`) and
one allowing access to the favicon on the page :code:`www.google.nl/favicon.ico`, only access to favicon.ico is allowed on
the google.nl website.

If one of our default policies contains a website you still want to allow, you can easily add the domain (with or without path)
to another policy to still grant access. This is one of the main reasons we prioritise :code:`allow` over :code:`deny` in these
policies.


Custom policies
---------------------------

Custom policies are defined as lists of domains with optional paths using one line per item.
When domain policies should include subdomains, they should be prefixed with a point (.), e.g. :code:`.nl` matches
all dutch top level domains.

Some companies use very strict policies, in which case one should only be allowed to access specific domains. For this case
we added a special wildcard (:code:`*`). When set in a policy it will mark the absolute top level domain.

.. Tip::

    If one should only be allowed to access pkg.opnsense.org you would create two policies, one containing a deny policy
    on :code:`*` and one containing an allow policy on :code:`pkg.opnsense.org`.


Using the policy tester
---------------------------

When doubting if a specific location would be accessible by a user, one can always use the included ACL tester.
Although mainly used for debugging purposes, it will easily inform you about the decision the webproxy will take
when using our acl's.

The policy tester contains two fields and a test button, just enter a username followed by a url (e.g. https://www.google.nl/)
and hit the test button. Depending on settings it will return a response like:

.. code-block:: json

  {
    "message": "ERR message=\"reason:c1380754-e14b-4dc7-bcf9-96307450c025 policy_type:custom\" user=\"root\"\n",
    "user": {
      "uid": "root",
      "id": "0",
      "applies_on": [
        "u:root",
        "g:admins"
      ]
    },
    "policy": {
      "action": "deny",
      "id": "c1380754-e14b-4dc7-bcf9-96307450c025",
      "applies_on": [
        "g:admins"
      ],
      "policy_type": "custom",
      "description": "test_custom2",
      "path": "/",
      "wildcard": true,
      "domain": "google.nl"
    }
  }


Which informs you about all settings relevant for the lookup, the message returned (to squid), the user found and the policy matched
using the rules described earlier.
