========================================
Zenarmor (Sensei): Hardware Requirements
========================================

Due to the nature of deep packet analysis and detailed drill-down reporting functionality, Zenarmor requires more hardware resources than a standard L3-L4 firewall.

 **Note**
 
    With the Sensei 1.5 release, you can offload your reporting database to an external system. This allows you to be able to run Zenarmor on systems with a constrained amount of RAM. 


It is recommended that you check if your Ethernet adapter functions well with netmap.

-------------
CPU & Memory
-------------

Because the analytics module relies on Elasticsearch to process large amounts of data, the amount of the memory available in the system is crucial for the overall performance of Zenarmor.

**Tip**

    If the number of active devices are more than 500 and the sustained WAN bandwidth is higher than 500 Mbps, we do not recommend deploying Zenarmor as a virtual guest since resources in virtual environments are generally shared between guest systems.

Below is the recommended minimum hardware requirements for Zenarmor based on the number of devices and the amount of sustained bandwidth:

=====================  =========================  ==================  ======================================================================
 **# Active Devices**  **Maximum WAN Bandwidth**  **Minimum Memory**  **Minimum CPU**
 0-50                  300 Mbps                   1 GB                A Dual-Core CPU (x86_64 compatible, single core PassMark score of 200)
 50-100                500 Mbps - 10 Kpps         4 GB                Intel Dual-Core i3 2.0 GHz (2 Cores, 4 Threads) or equivalent
 100-250               1 Gbps - 20 Kpps	          8 GB                Intel Dual-Core i5 2.2 GHz (2 Cores, 4 Threads) or equivalent
 250-1000              1-2 Gbps 40 Kpps           16 GB               Intel Dual-Core i5 3.20 GHz (2 Cores, 4 Threads) or equivalent
 1000-2000             1-2 Gbps                   32 GB               Intel Quad-Core i7 3.40 GHz (4 Cores, 8 Threads) or equivalent
 2000+                 2-4.5 Gbps                 64 GB               Intel Quad-Core i9 3.0 GHz (24 Cores, 48 Threads) or equivalent
=====================  =========================  ==================  ======================================================================

 **Note**
 
   Zenarmor requires at least 1 GB of memory. Installer will not continue if you have less than 1 GB of RAM. We recommend 8 GB memory to have an exceptional reporting experience with elasticsearch database. 

-----------------
Ethernet Adapter
-----------------

Zenarmor uses a FreeBSD subsystem called `netmap(4) <https://www.freebsd.org/cgi/man.cgi?query=netmap&sektion=4>`_ to access raw Ethernet frames. With FreeBSD 11 (OPNsense version <= 20.1) this software can be very particular in terms of proper driver compatibility. 

Intel based adapters, particularly em(4) and igb(4), are observed to perform well in terms of stability and performance. 

Sunny Valley Networks is sponsoring developments on this project so you can expect netmap(4) will better support a wide range of Ethernet drivers. 

-----------
Disk Space
-----------

Zenarmor uses `Elasticsearch <https://en.wikipedia.org/wiki/Elasticsearch>`_ or `MongoDB <https://www.mongodb.com/>`_ as its backend to store large data sets. Please allow at least 5 MB of disk space per hour per megabit/second throughput.

If you're running a 100 Mbps link \(about 100 users\) which is quite active during the daytime and idle rest of the day, you may calculate the space needed as follows:

.. code-block:: none

    5 MB x 12 hours x 100 Mbps = 6 GB per day.
    6 GB x 7 days a week = 42 GB per week.
    42 x 4 weeks a month = 164 GB per month.

As of `version 0.7.0 <https://www.sunnyvalley.io/docs/support/release-notes#07>`_, Zenarmor expires old report data to free up disk space for the most recent data based on the configured number of days of history to keep.
