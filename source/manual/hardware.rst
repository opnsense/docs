=======================
Hardware sizing & setup
=======================

The **hardware setup** requires a careful preparation and selection of
the standard PC hardware components for the intended installation of
OPNsense.

⚠ Computer hardware with the open source security software OPNsense®
pre-installed can be purchased directly from various (online) stores.

.. TIP::
  The OPNsense development team encourages everyone looking for a turn-key solution
  to buy from `Deciso <https://www.deciso.com>`__ or one of the other partners listed on our partner page.
  **Listed partners make significant contributions back to the project.**

--------------------------------
Supported hardware architectures
--------------------------------

OPNsense® is available for `x86-64 <https://en.wikipedia.org/wiki/X86-64>`__ (amd64) bit microprocessor architectures.
Full installs on `SD memory cards <https://en.wikipedia.org/wiki/Secure_Digital>`__,
`solid-state disks (SSD) <https://en.wikipedia.org/wiki/Solid-state_drive>`__ or `hard disk drives
(HDD) <https://en.wikipedia.org/wiki/Hard_disk_drive>`__ are intended for OPNsense.

While supported devices range from embedded systems to rack-mounted servers,
the hardware must be capable of running 64-bit `operating
systems <https://en.wikipedia.org/wiki/operating_system>`__.

---------------------
Hardware requirements
---------------------

For substantially narrowed OPNsense® functionality there is the basic
specification. For full functionality there are minimum, reasonable and
recommended specifications.

.. rubric:: Minimum
   :name: minimum

The minimum specification to run all OPNsense standard features that do
not need disk writes. Means that you can run all standard features, except
for the ones that require disk writes, e.g. a caching proxy (cache) or intrusion detection
and prevention (alert database).

+------------------+--------------------------------------------------------------------------+
| Processor        | 1 GHz dual-core CPU                                                      |
+------------------+--------------------------------------------------------------------------+
| RAM              | 2 GB                                                                     |
+------------------+--------------------------------------------------------------------------+
| Install method   | Serial console or video (VGA)                                            |
+------------------+--------------------------------------------------------------------------+
| Install target   | SD or CF card with a minimum of 4 GB, use nano images for installation.  |
+------------------+--------------------------------------------------------------------------+

Table:  *Minimum hardware requirements*

.. rubric:: Reasonable
   :name: reasonable

The reasonable specification to run all OPNsense standard features.
Means that every feature is functional, but perhaps not with a lot of users
or high loads.

+------------------+--------------------------------------------------------------------------+
| Processor        | 1 GHz dual-core CPU                                                      |
+------------------+--------------------------------------------------------------------------+
| RAM              | 4 GB                                                                     |
+------------------+--------------------------------------------------------------------------+
| Install method   | Serial console or video (VGA)                                            |
+------------------+--------------------------------------------------------------------------+
| Install target   | 40 GB SSD, a minimum of 2 GB memory is needed for the installer to run.  |
+------------------+--------------------------------------------------------------------------+

Table:  *Reasonable hardware requirements*

.. rubric:: Recommended
   :name: recommended

The recommended specification to run all OPNsense standard features.
Means that every feature is functional and fits most use cases.

+------------------+---------------------------------+
| Processor        | 1.5 GHz multi-core CPU          |
+------------------+---------------------------------+
| RAM              | 8 GB                            |
+------------------+---------------------------------+
| Install method   | Serial console or video (VGA)   |
+------------------+---------------------------------+
| Install target   | 120 GB SSD                      |
+------------------+---------------------------------+

Table:  *Recommended hardware requirements*

.. rubric:: Hardware guide
   :name: hardware-guide

The hardware required for your local OPNsense will be determined by the
intended minimum `throughput <#throughput>`__ and feature set.

---------------------
Impact of Feature set
---------------------

While most features do not affect hardware dimensioning, a few features
have a massive impact on it. These include:

`Squid <https://en.wikipedia.org/wiki/Squid_(software)>`__ 
    A caching web proxy which can be used for web-content control.
    These packages rely strongly on CPU load and disk-cache writes.

`Captive portal <https://en.wikipedia.org/wiki/Captive_portal>`__
    Settings with hundreds of simultaneously served captive portal users
    will require more CPU power in all the hardware specifications
    displayed below.

`State transition tables <https://en.wikipedia.org/wiki/State_transition_table>`__
    It is a known fact that each state table entry requires about 1 kB
    (kilobytes) of RAM. The average state table, filled with 1000
    entries, will occupy about 1 MB (megabytes) of
    `RAM <https://en.wikipedia.org/wiki/Random-access_memory>`__.
    OPNsense usage settings with hundreds of thousands of connections
    will require memory accordingly.

|

----------
Throughput
----------

The main hardware factors of the OPNsense setup involved are CPU, RAM,
mass storage (disc), the number and quality of network interfaces.

+-------------------+-----------------------+-------------+------------------------+
| Throughput (Mbps) | Hardware requirements | Feature set | Users / Networks       |
+===================+=======================+=============+========================+
| 11-150            | Basic spec.           | narrowed    | adjusted (10-30)       |
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

FreeBSD is the base of OPNsense. All FreeBSD drivers
are included in the OPNsense kernel, and the hardware compatibility is
the same.

.. Tip::
    If you are looking to buy new hardware then take a look at our `partner page <https://opnsense.org/partners>`__
    as these partners contribute back to OPNsense and sell hardware that is know to work well.

For further help and support, see

-  `FreeBSD 14.1 Hardware Compatibility
   List <https://www.freebsd.org/releases/14.1R/hardware/>`__
-  `OPNsense Forum <https://forum.opnsense.org/>`__

.. rubric:: List of references
   :name: list-of-references

-  Schellevis, Jos; *Hardware requirements*; `OPNsense > Get
   started <https://opnsense.org/users/get-started/>`__ (2015)
-  McKusick, Marshall; Neville-Neil, George V; Warson, Robert NM; *The
   Design and Implementation of the FreeBSD Operating System* (2015);
   Addison-Wesley, New Jersey; ISBN 978-0321968975
