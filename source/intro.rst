============
Introduction
============

Welcome to the OPNsense documentation & wiki project!
The documentation is work in progress and is updated frequently.
If you would like to contribute in anyway, please take a look at our guide
how to :doc:`contribute`.

.. image:: ./images/opnsense_logo-zilver_grijs.png

------------------------------------
Welcome to OPNsense's documentation!
------------------------------------
`OPNsense® <https://opnsense.org>`__ is an open source,
easy-to-use and easy-to-build FreeBSD based firewall and routing platform.

**OPNsense** includes most of the features available in expensive commercial
firewalls, and more in many cases. It brings the rich feature set of commercial
offerings with the benefits of open and verifiable sources.

-----------------
Mission Statement
-----------------

  Give users, developers and businesses a friendly, stable and transparent
  environment. Make OPNsense the most widely used open source security platform.
  The project’s name is derived from open and sense and stands for:
  “Open (source) makes sense.”


.. image:: ./images/OPNsense-Deciso-Screenshot.jpg


-----------------
Reading guide
-----------------

While reading the documentation, it's good to know how the various topics are structured, what their purpose is and how
to find what you're looking for. Maybe even more important is what this documentation doesn't offer.

If you're looking for deeper insights about networking and best practices in designing them, this might not be the best
place to look. Most of our documents and how-to's focus on how to use functionality included in our software and/or one
of it's plugins. Quite some books are written about networking, there are (online) courses available and wikipedia
contains a lot of relevant articles as well. Some interesting reads include the fundamentals about the
`OSI model <https://en.wikipedia.org/wiki/OSI_model>`__, `IP addressing <https://en.wikipedia.org/wiki/IP_address>`__,
`routing <https://en.wikipedia.org/wiki/IP_routing>`__ and `network address translation <https://en.wikipedia.org/wiki/Network_address_translation>`__.
Likely these resources are more suitable for learning about general network concepts.
Although we do try to include some context in our documents, there are often assumptions made about the readers
knowledge on (basic) networking.

Like many products and projects, ours grows over time, functionality extends and changes, which sometimes makes it difficult
to find what you need for the version you're using. Although we try to keep our documentation up to date, sometimes text
doesn't reflect reality anymore. If that's the case and you think you found an omission, don't hestitate to open
a report using one of our templates on `GitHub <https://github.com/opnsense/docs/issues/new/choose>`__ or a pull request
of course if you're able to.

Always assume the text is intended for the latest version of our product, in time we might
add a version selector in the documentation, but given OPNsense is a security product, we advise to keep it up to date
anyway to protect yourself against the latest threats.

The releases section contains the changelogs for all versions we published over the years, if there are remarks
for an upgrade, this is a useful resource to collect the details.

Installation and setup is all about getting you started using one of the target options available.

The next sections should be quite familiair when working with OPNsense, as they reflect the options in the
menu of the product. In case you're not yet used to OPNsense, you can always use the search input in the left corner of
the screen to find your topic.

Both community and third-party plugins have their own area available, although they eventually register into the
same menu structure, it's good to know about possible differences between add-ons and standard functionality.
The level of support may differ between core functionality, as also explained in the "Support options" section,
feature requests and bugs maybe treated different as well (a lot of questions for a plugin which is being developed
by a single person, maybe less active than a group of people improving a plugin together for example).

When it comes to building software on top of OPNsense or extending existing functionality, the development
chapter is the one to read. It explains all about our architecture, coding style, how to hook into available facilities and
much more.

Some pointers when it comes to troubleshooting can be found in the section with the same name, it explains a bit
about our issue workflow and some tips we collected over the years.

Last but not least our documentation includes some pages around project relations, legal guidelines and
ways to contribute to the project.


-------------------

-----------
Feature set
-----------

The feature set of OPNsense includes high-end features such as forward caching
proxy, traffic shaping, intrusion detection and easy OpenVPN client setup.
The latest release is based on a recent FreeBSD for long-term support and uses a
newly developed MVC-framework based on Phalcon. OPNsense’s focus on security
brings unique features such as easy to use one time password authentication for various components.

The robust and reliable update mechanism gives OPNsense the ability to provide
important security updates in a timely fashion.

----------------------

----------------------
OPNsense Core Features
----------------------

- Traffic Shaper
- Captive portal

  - Voucher support
  - Template manager
  - Multi zone support

- Forward Caching Proxy

  - Transparent mode supported
  - Blacklist support

- Virtual Private Network

  - Site to site
  - Road warrior
  - IPsec
  - OpenVPN

- High Availability & Hardware Failover

  - Includes configuration synchronization & synchronized state tables
  - Moving virtual IPs

- Intrusion Detection and Inline Prevention

  - Built-in support for Emerging Threats rules
  - Simple setup by use of rule categories
  - Scheduler for period automatic updates

- Built-in reporting and monitoring tools

  - System Health, the modern take on RRD Graphs
  - Packet Capture
  - Netflow

- Support for plugins
- DNS Server & DNS Forwarder
- DHCP Server and Relay
- Dynamic DNS
- Backup & Restore

  - Encrypted cloud backup to Google Drive and Nextcloud
  - Configuration history with colored diff support
  - Local drive backup & restore

- Stateful inspection firewall
- Granular control over state table
- 802.1Q VLAN support
- and more…
