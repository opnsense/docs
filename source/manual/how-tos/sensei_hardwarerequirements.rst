=====================
Sensei: Hardware Requirements
=====================

Due to the nature of packet analysis and granular drill-down reporting features, Sensei require more horsepower than a standard L3-L4 firewall.

.. Note::

    Sensei requires at least 4 GB of memory. Installer will not continue if you have less than 4 GB of RAM.

.. Note::

    A roadmap feature - Cloud reporting - will enable you to install Sensei to devices which have limited amount of memory. E.g. you'll be able to install Sensei to a Raspberry Pi. 

-----------------------------

CPU & Memory
------------

Because the analytics module relies on Elastic Search to do Big Data processing, amount of the memory available in the system is crucial for the performance of the whole product.

At least dual-core *(i5 or equivalent)* or preferably quad-core modern CPU *(i7 or equivalent)* would be advisable.

Recommended minimum hardware requirements for Sensei based on the number of users and the bandwidth:

+-----------------+--------------+-------------+----------------------+
| Number of Users | WAN Bandwith | Min. Memory | Min. CPU             |
+=================+==============+=============+======================+

======================= =====================   ====================   ====================================================================
 **Number of Users**    **WAN Bandwith**        **Min. Memory**         **Min. CPU**
 <25                    20 Mbps                 8 GB                    Intel Dual-Core i3 2.0 GHz (2 Cores, 4 Threads) or equivalent
 25-50	                50 Mbps - 10 Kpps       8 GB                    Intel Dual-Core i5 2.0 GHz (2 Cores, 4 Threads) or equivalent
 50-100	                100 Mbps - 20 Kpps      16 GB                   Intel Dual-Core i5 2.2 GHz (2 Cores, 4 Threads) or equivalent
 100-250                200 Mbps - 40 Kpps      16 GB                   Intel Dual-Core i7 2.0 GHz (2 Cores, 4 Threads) or equivalent
 250-1000               500 Mbps - 100 Kpps     32 GB                   Intel Quad-Core i7 3.40 GHz (4 Cores, 8 Threads) or equivalent
======================= =====================   ====================   ====================================================================

-----------------------------

Disk Space
------------

.. Note::

    Sensei uses `Elastic Search Engine <https://en.wikipedia.org/wiki/Elasticsearch>`_ as its backend to process the Big Data. Please spare at least 5 MB of disk space per hour per megabit/second throughput.

If you're running a 100 Mbps link \(about 100 users\) which is quite active during the daytime and idle rest of the day, you can calculate the space needed as follows:

.. code-block:: none

    5 MB x 12 hours x 100 Mbps = 6 GB per day.
    6 GB x 7 days a week = 42 GB per week.
    42 x 4 weeks a month = 164 GB per month.


.. Note::

    As of 0.7.0 ::italic::(`changelog <https://www.sunnyvalley.io/blog/what-s-cooking-for-0-7>`_) , Sensei retires reports data to open up space for the new coming data. After the configured timespan, existing reports data is automatically purged to save space for fresh data.
