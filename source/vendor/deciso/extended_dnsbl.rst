===========================
Deciso: Extended Blocklists
===========================

As part of the OPNsense Business Edition, Deciso offers the extended blocklists module as
part of the standard Business Edition installation. With this module you are able
to configure DNS blocking policies in a more fine-grained manner by specifying networks on which the blocklists
should apply.

The extended blocklists can be found under :menuselection:`Services->Unbound DNS->Extended Blocklists`.

Blocklists
----------------------------

Blocklists are configured in the same manner as with regular blocklists, except they are listed
in a grid, where multiple blocklists and multiple networks may be defined per grid entry to ease administration
for a large amount of networks. An optional description may be provided for your own reference.

Source networks are provided as IP addresses in CIDR notation, or singular IP addresses. The validation
for this field is strict, meaning that setting host bits in a CIDR notation is not allowed.

.. Note::

    If you'd like to use the extended blocklists module, keep in mind that the regular blocklists, if configured,
    are still active. They define a policy for all networks, and are given preference above the extended blocklists.
    Therefore it's possible that a conflict arises between blocklists for a specific network and regular blocklists.
    Please verify that the relevant blocklists are not configured in :menuselection:`Services->Unbound DNS->Blocklist`.

    If you're not sure if a policy would overlap in this manner, please use the tester as described below.

Custom
----------------------------

In the Custom tab you are able to configure custom domains to block, also per source network. The domains can either
be exact matches, or entered as a wildcard in a separate field. Wildcard entries will block every subdomain of
the configured domain name. It's not possible to block a first-level domain such as 'com'.

To prevent cluttering in the grid, the relevant domains and wildcards are not shown in the grid. Therefore
it's mandatory to add a description for your own reference so you can easily locate a custom policy. You can view
the blocked domains/wildcards by clicking "edit" on the grid entry.


Tester
----------------------------

If you'd like to verify whether a specified domain is correctly being blocked, or if you want to know
if a domain is part of a specific list, you can use the tester to see the policy that's applied to a DNS request.
Here you're able to enter a domain, as well as a source IP address to simulate a request from a specific address.
Note that no actual DNS request is sent if a domain were to pass, it's kept isolated as part of the blocklisting mechanism.

It's also possible to verify whether a domain overlaps with another policy. For example, if you configured the facebook blocklist,
the output would look something like this:

.. code-block:: json

    {
        "status": "OK",
        "action": "Block",
        "policy": {
            "bl": "ext_blf0",
            "wildcard": false,
            "source_net": [
                "192.168.2.0/24",
                "192.168.1.0/24",
                "10.0.0.0/8"
            ]
        }
    }

However, if you also enabled the facebook blocklist in the regular blocklist section, you would get:

.. code-block:: json

    {
        "status": "OK",
        "action": "Block",
        "policy": {
            "bl": "blf0",
            "wildcard": false,
            "collisions": [
                {
                    "bl": "ext_blf0",
                    "wildcard": false,
                    "source_net": [
                        "192.168.2.0/24",
                        "192.168.1.0/24",
                        "10.0.0.0/8"
                    ]
                }
            ],
            "source_net": []
        }
    }

which would tell you that a regular list is conflicting with an extended blocklist policy.
