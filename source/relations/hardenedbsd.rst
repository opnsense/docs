===========
HardenedBSD
===========

.. image:: ./images/Logo-label-hardenedbsd.png

------------
Introduction
------------

HardenedBSD is a fork of FreeBSD, founded in 2014, that implements
exploit mitigations and security hardening technologies. The primary
goal of HardenedBSD is to perform a clean-room re-implementation of
the grsecurity patchset for Linux to HardenedBSD.

-----------------
Why Fork FreeBSD?
-----------------

Work on HardenedBSD began in 2013 when Oliver Pinter and Shawn Webb
started working on an implementation of Address Space Layout
Randomization (ASLR), based on PaX's publicly-available documentation,
for FreeBSD. At that time, HardenedBSD was meant to be a staging area
for experimental development on the ASLR patch. Over time, as the
process of upstreaming ASLR to FreeBSD became more difficult,
HardenedBSD naturally became a fork.


HardenedBSD completed its ASLR implementation in 2015 with the
strongest form of ASLR in any of the BSDs. Since then, HardenedBSD has
moved on to implementing other exploit mitigations and hardening
technologies. OPNsense, an open source firewall based on FreeBSD,
incorporated HardenedBSD's ASLR implementation in 2016.


HardenedBSD exists today as a fork of FreeBSD that closely follows
FreeBSD's source code. HardenedBSD syncs with FreeBSD every six hours.


-------------------
HardenedBSD's Goals
-------------------

HardenedBSD aims to provide the BSD community with a clean-room
reimplementation of the publicly-documented portions of the grsecurity
patchset for Linux.


-------------------
Who is HardenedBSD?
-------------------

HardenedBSD's core team consists of Oliver Pinter and Shawn Webb.
Contributions have been made by many individuals around the globe.


-------------------------
Cooperation with OPNsense
-------------------------

In May 2015, HardenedBSD announced collaboration with OPNSense. A
HardenedBSD-flavored version of OPNsense was published early on as a
proof-of-concept work. As the proof-of-concept proved stable, robust,
and scalable, OPNsense migrated to HardenedBSD with the support of
HardenedBSD's core team.
