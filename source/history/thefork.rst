==============
About the Fork
==============
Welcome to about the fork. This page is intended to explain the original motivation
for forking, but keep in mind that currently less than 10% of the original legacy code
base remains. As it stands today, OPNsense has evolved from being a fork to a whole new
security platform with leading innovations such as weekly security updates for
all components, a REST API, inline Intrusion Prevention and an intuitive modern user
interface.

.. sidebar:: Let's fork and lift the project!

    .. image:: images/fork-lift_new.jpg

-------------------
So why did we fork?
-------------------
Back in 2014, after having sponsored pfSense® for years, we felt that there was no other
option than to fork the project and to keep the spirit of the - original m0n0wall based
fork - alive. Below you can read about our original motivations and the birth of
OPNsense®.


Technical
---------

We had technical reasons to fork.
As much as we love the functionality/feature set of pfSense, we do not enjoy the
:doc:`code quality </development/guidelines/basics>` and dispersed development method. We like structure, achievable
goals set forth in a `roadmap <https://opnsense.org/about/road-map/>`__ with
regular releases and a decent :doc:`framework </development/architecture>`.

Security
--------
On the security part the main issue was the need to separate logic. The GUI
should not perform tasks that require root access, and potential security issues
should be fixed before they become a real problem.

Quality
-------
As for quality, all new features will be built using a solid :doc:`framework </development/architecture>` with a
Model View Controller. For this purpose we choose `Phalcon <https://phalcon.io/>`__ as it is the fastest
open source PHP framework available. And we will gradually migrate parts inherited
from pfSense to the new framework to avoid a big-bang approach.

Community
---------
A thriving community can only exist when people are willing to share. We want to
make it easier for people to join and help to build the community. With pfSense,
this has been rather difficult, as the tools to build it are difficult to use and
often do not work in the first few attempts. And since 2014 they are not
freely available any more, you need to apply for access with ESF. We believe a
good open source project has nothing to hide so access to the sources should be
there for all. It will remain a mystery why ESF made that move, as commit rights
and read rights are totally different.

.. Note::

   ESF has since changed their policy several times with different license models,
   including the ESF 6 clause license and the latest being a Apache style license.

Transparency
-------------
A real concern with pfSense is transparency. Since Netgate bought
the majority share of pfSense and renamed the company to ESF, it has been
difficult to understand the direction they want the project to go. Removing the
tools from GitHub without prior warning and using the brand name to fence off
competitors has scared quite a lot of people. Also the license had changed for
no apparent reason…

Restore a firm open source project
----------------------------------
With OPNsense, we have restored a stable project with clear goals and a very simple
license that is suitable for forking and making OEM versions. We think a community
project is there for all to use and work with.

-------------
First Release
-------------

Much work had already been done before the `first official release <https://opnsense.org/opnsense-version-15-1-released/>`__:

* The build-tools had been completely rewritten from the ground up
  with clear and easy to read build scripts that are portable and small,

* OPNsense is now a package that can be installed on top of our custom FreeBSD
  build (you can literally do pkg remove opnsense and you are left with an almost
  standard FreeBSD base system),

* The firmware upgrade process is now done with pkgng,

* Captive portal has been rewritten and does not make use of kernel patches anymore,

* New features (captive portal) have been implemented with a clear structure,

* The check_reload_status functionality, effectively the backend daemon starting
  and stopping components, has been fully rewritten in Python (configd),

*  Fully reworked the GUI to a modern Bootstrap based one that is also easier to
   customize if you want to.

--------------------------
Future Development & Focus
--------------------------

Moving forward the focus will remain on code quality and security.

.. Note::

   A lot of work has been done to improve the code quality and with weekly
   updates we have proven to be able to act quickly on known security threats.
   For current status of the project and future development see our `roadmap <https://opnsense.org/about/road-map/>`__.


Deciso's involvement
--------------------
That being said it is important to know that `Deciso <https://www.deciso.com/about-deciso/>`__ has been a long time sponsor
of pfSense and invested a lot of time and money into the project. Deciso helped
to make it a success in Europe. Until Netgate bought the company there was room
for many others like us, but that has changed unfortunately.

Closing thoughts
----------------
In the end it all boils down to the direction we will go both technical as well
as community involvement and transparency.

You are invited! Try OPNsense, be part of the community and help the project move
forward. OPNsense is rapidly becoming the number one open source firewall platform!
