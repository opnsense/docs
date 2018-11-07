=======================
Hardware sizing & setup
=======================

The **hardware setup** requires a careful preparation and selection of
the standard PC hardware components for the intended installation of
OPNsense.

⚠ Computer hardware with the open source security software OPNsense®
pre-installed can be purchased directly from various (online) stores.

.. TIP::
  The OPNsense development team encourage everyone looking for a turn-key solution
  to buy from `Deciso <https://www.deciso.com>`__ or one of the other partners listed at our partner page.
  **Listed partners make significant contributions back to the project.**

--------------------------------
Supported hardware architectures
--------------------------------

OPNsense® is available for
`x86-32 <https://en.wikipedia.org/wiki/X86-32>`__ (i386) and
`x86-64 <https://en.wikipedia.org/wiki/X86-64>`__ (amd64) bit
microprocessor architectures. Full installs on `SD memory
cards <https://en.wikipedia.org/wiki/Secure_Digital>`__, `solid-state
disks (SSD) <https://en.wikipedia.org/wiki/Solid-state_drive>`__ or
`hard disk drives
(HDD) <https://en.wikipedia.org/wiki/Hard_disk_drive>`__ are intended
for OPNsense.

While the range of supported devices are from embedded systems to rack
mounted servers, we recommend to use a 64-bit versions of OPNsense, if
the hardware is capable of running 64-bit `operating
systems <https://en.wikipedia.org/wiki/operating_system>`__. It is
possible to install and run 32-bit (x86-32, i386) versions of OPNsense®
on 64-bit (x86-64, amd64) PC hardware, but we do not recommend it,
especially not for new deployments.

---------------------
Hardware requirements
---------------------

For substantially narrowed OPNsense® functionality there is the basic
specification. For full functionality there are minimum, reasonable and
recommended specifications.

.. rubric:: Minimum
   :name: minimum

The minimum specification to run all OPNsense standard features that do
not need disk writes, means you can run all standard features, expect
for the ones that require disk writes, e.g. a caching proxy (cache) or intrusion detection
and prevention (alert database).

+------------------+--------------------------------------------------------------------------+
| Processor        | 500 MHz single core cpu                                                  |
+------------------+--------------------------------------------------------------------------+
| RAM              | 512 MB                                                                   |
+------------------+--------------------------------------------------------------------------+
| Install method   | Serial console or video (vga)                                            |
+------------------+--------------------------------------------------------------------------+
| Install target   | SD or CF card with a minimum of 4 GB, use nano images for installation.  |
+------------------+--------------------------------------------------------------------------+

Table:  *Minimum hardware requirements*

.. rubric:: Reasonable
   :name: reasonable

The reasonable specification to run all OPNsense standard features,
means every feature is functional, but perhaps not with a lot of users
or high loads.

+------------------+--------------------------------------------------------------------------+
| Processor        | 1 GHz dual core cpu                                                      |
+------------------+--------------------------------------------------------------------------+
| RAM              | 1 GB                                                                     |
+------------------+--------------------------------------------------------------------------+
| Install method   | Serial console or video (vga)                                            |
+------------------+--------------------------------------------------------------------------+
| Install target   | 40 GB SSD, a minimum of 1 GB memory is needed for the installer to run.  |
+------------------+--------------------------------------------------------------------------+

Table:  *Reasonable hardware requirements*

.. rubric:: Recommended
   :name: recommended

The recommended specification to run all OPNsense standard features,
means every feature is functional and fits most use cases.

+------------------+---------------------------------+
| Processor        | 1.5 GHz multi core cpu          |
+------------------+---------------------------------+
| RAM              | 4 GB                            |
+------------------+---------------------------------+
| Install method   | Serial console or video (vga)   |
+------------------+---------------------------------+
| Install target   | 120 GB SSD                      |
+------------------+---------------------------------+

Table:  *Recommended hardware requirements*

.. rubric:: Hardware guide
   :name: hardware-guide

The hardware required for your local OPNsense, will be determined by the
intended minimum `throughput <https://en.wikipedia.org/wiki/>`__ and the
feature set.

---------------------
Impact of Feature set
---------------------

While most features do not affect hardware dimensioning, a few features
have massive impact on it. The candidates are:

`Squid <https://en.wikipedia.org/wiki/Squid_(software)>`__ 
    a caching web proxy which can be used for web-content control,
    respectively. These packages rely strongly on CPU load and
    disk-cache writes.

`Captive portal <https://en.wikipedia.org/wiki/Captive_portal>`__
    settings with hundreds of simultaneously served captive portal users
    will require more CPU power in all the hardware specifications
    displayed below.

`State transition tables <https://en.wikipedia.org/wiki/State_transition_table>`__
    it is a known fact, that each state table entry requires about 1 kB
    (kilobytes) of RAM. The average state table, filled with 1000
    entries will occupy about ~10 MB (megabytes) of
    `RAM <https://en.wikipedia.org/wiki/Random-access_memory>`__.
    OPNsense usage settings with hundred of thousands of connections
    will require memory accordingly.

|

----------
Throughput
----------

The main hardware-factors of the OPNsense setup involved are CPU, RAM,
mass storage (disc), the number and quality of network interfaces.

+-------------------+-----------------------+-------------+------------------------+
| Throughput (Mbps) | Hardware requirements | Feature set | Users / Networks       |
+===================+=======================+=============+========================+
| 1-10              | Basic spec.           | narrowed    | few (1-10)             |
+-------------------+-----------------------+-------------+------------------------+
| 11-150            | Minimum spec.         | reduced     | adjusted (10-30)       |
+-------------------+-----------------------+-------------+------------------------+
| 151-350           | Reasonable spec.      | all         | substantial (30-50)    |
+-------------------+-----------------------+-------------+------------------------+
| 350-750+          | Recommended spec.     | all         | substantial+ (50-150+) |
+-------------------+-----------------------+-------------+------------------------+
| Mbps (Mbit/s or Mb/s) - Megabit per second - 1,000,000 bits per second           |
+----------------------------------------------------------------------------------+

Network interface cards
    As the FreeBSD hardware-lists and -recommendations
    say, Intel® network interface cards (NIC) for
    `LAN <https://en.wikipedia.org/wiki/Local_area_network>`__
    connections are reliable, fast and not error-prone. Intel chipset
    NICs deliver higher throughput at a reduced `CPU
    load <https://en.wikipedia.org/wiki/Load_(computing)>`__.

.. rubric:: Supported hardware
   :name: supported-hardware

The FreeBSD 11.1-RELEASE is the base of OPNsense. All FreeBSD drivers
are included in the OPNsense kernel, and the hardware compatibility is
the same.

.. Tip::
    If you are looking to buy new hardware then take a look at our `partner page <https://opnsense.org/partners>`__
    as these partners contribute back to OPNsense and sell hardware that is know to work well.

For further help and support, see

-  `FreeBSD 11.1-RELEASE Hardware Compatibility
   List <https://www.freebsd.org/releases/11.1R/hardware.html>`__
-  `OPNsense Forum <https://forum.opnsense.org/>`__

.. rubric:: List of references
   :name: list-of-references

-  Schellevis, Jos; *Hardware requirements*; `OPNsense > Get
   started <https://opnsense.org/users/get-started/>`__ (2015)
-  McKusick, Marshall; Neville-Neil, George V; Warson, Robert NM; *The
   Design and Implementation of the FreeBSD Operating System* (2015);
   Addison-Wesley, New Jersey; ISBN 978-0321968975
