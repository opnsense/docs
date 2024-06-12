==================================================
Fighting Bufferbloat with FQ_CoDeL
==================================================

Bufferbloat in simple terms of words is an increase of latency caused by network devices due to excessive **buffering** of traffic. The more traffic is buffered the longer it takes to be processed which causes unwanted latency. This is mostly seen by the end-user as lags in games, video & call stuttering.

In order to combat Bufferbloat we can take advantages of AQM/SQM algorithms which can significaly improve exprerience on end-user side.

One of such AQM is **FQ_CoDeL** e.g. **Fair/Flow Queueing Controlled Delay**


Important parameters of FQ_CODEL
--------------------------------
========================= =====================================================================================================================================================================================================================
 **quantum**              *Should be set to the value of Interface MTU. Number of bytes a queue can serve before being moved to the tail of old queues list (1514 default, 1500+14B hardware header, max 9000)*
 **target**               *Minimum acceptable persistent queue delay (5ms default). Does not drop packets directly after packets sojourn time becomes higher than target time but waits for interval time (100ms default) before dropping.*   
 **interval**             *Drops or Marks packets (if Codel ECN is enabled) when queue delay becomes high (default 100ms)*    
 **limit**                *Size of all queues managed by instance (default 10240, max 20480).It is the hard limit on the real queue size in packets*
 **flows**                *Sets the number of queues into which the incoming packets are classified (default 1024, max 65536)*
 **(FQ-)CoDel ECN**       *Enables (disabled by default) packet marking (instead of dropping) for ECN-enabled TCP flows when queue delay becomes high*           
========================= =====================================================================================================================================================================================================================


BW provided by ISP
------------------
+----------------+----------+-----------------+
|                | Download |      Upload     |
+================+==========+=================+
|      Mbit/s    |   530    |        30       |
+----------------+----------+-----------------+



To start go to :menuselection:`Firewall --> Shaper --> Pipes`. Select the *advanced mode*


Step 1a - Create Download Pipe
------------------------------
On the **Pipes** tab click the **+** button in the lower right corner.
An empty **Edit Pipe** screen will popup.

Create Pipe For Download
""""""""""""""""""""""""
========================= ================= ===========================================================================================================
 **enabled**              Checked           *Check to enable the pipe*
 **bandwidth**            495               *Numeric value of the bandwidth target is 85% of ISP advertized BW, which needs to be tuned per use-case*
 **bandwidth Metric**     Mbit/s            *Metric to use with the numeric value*
 **queue**                (empty)           *Not needed we will specify queue as object binded to this Pipe*
 **mask**                 (none)            *Leave empty*
 **scheduler type**       FQ_CoDel          *This will be the AQM we will use. Enables FQ_CoDeL in scheduler*
 **Enable CoDel**         (empty)           *Don't click this option we will use FQ as selected above*
 **(FQ-)CoDel target**    (empty)           *Can be tuned (default 5ms)*
 **(FQ-)CoDel interval**  (empty)           *Can be tuned but usually the default value is enough*
 **(FQ-)CoDel ECN**       Checked           *Click this option to enable packet marking ECN for ECN enabled flows*
 **FQ-CoDel quantum**     (empty)           *Refferres to MTU, should be set no more and no less than is your WAN MTU. For Ethernet let it default*
 **FQ-CoDel limit**       (empty)           *Can be tuned*
 **FQ-CoDel flows**       (empty)           *Can be tuned (default 1024). Usually left on default*
 **description**          Download          *Free field, enter something descriptive*
========================= ================= ===========================================================================================================

.. Note::

        Queue in pipe is a pipe object; parameter, that defines example FiFo for that Pipe. It's used for dynamic Queue creation.
        Queue parameter = size, in slots or KBytes (default 50), too large queue size can introduce queuing delay

.. Note::

        495 Mbps, reason we are setting lower BW is to overtake the Queueing before ISP.
        We usually take 85% of the Provided BW which we tune depending on the average 
        possible throughput that can be always reached

.. Note::

        You can use Ookla speedtest before applying any shaper and run several tests to 
        create such average possible throughput


Step 1b - Create Upload Pipe
----------------------------
On the **Pipes** tab click the **+** button in the lower right corner.
An empty **Edit Pipe** screen will popup.

Create Pipe For Upload
""""""""""""""""""""""""
========================= ================= ===============================================================================================================================================================
 **enabled**              Checked           *Check to enable the pipe*
 **bandwidth**            30                *Numeric value of the bandwidth target is 85% of ISP advertized BW, which needs to be tuned per use-case*
 **bandwidth Metric**     Mbit/s            *Metric to use with the numeric value*
 **queue**                (empty)           *Not needed we will specify queue as object binded to this Pipe*
 **mask**                 (none)            *Leave empty*
 **scheduler type**       FQ_CoDel          *This will be the AQM we will use. Enables FQ_CoDeL in scheduler*
 **Enable CoDel**         (empty)           *Don't click this option we will use FQ as selected above*
 **(FQ-)CoDel target**    (empty)           *Can be tuned (default 5ms)*
 **(FQ-)CoDel interval**  (empty)           *Can be tuned but usually the default value is enough*
 **(FQ-)CoDel ECN**       Checked           *Click this option to enable packet marking ECN for ECN enabled flows*
 **FQ-CoDel quantum**     (empty)           *Refferres to MTU, should be set no more and no less than is your WAN MTU. For Ethernet let it default*
 **FQ-CoDel limit**       (empty)           *Can be tuned*
 **FQ-CoDel flows**       (empty)           *Can be tuned (default 1024). Usually left on default*
 **description**          Upload            *Free field, enter something descriptive*
========================= ================= ===============================================================================================================================================================

.. Note::

        Queue in pipe is a pipe object; parameter, that defines example FiFo for that Pipe. It's used for dynamic Queue creation.
        Queue parameter = size, in slots or KBytes (default 50), too large queue size can introduce queuing delay

.. Note::

        30 Mbps, usually asymmetric don't have problem with upload set to advertized ISP BW.
        If we see latency or have symmetric we are setting lower BW to overtake the Queueing before ISP.
        We usually take 85% of the Provided BW which we tune depending on the average 
        possible throughput that can be always reached

.. Note::

        You can use Ookla speedtest before applying any shaper and run several tests to 
        create such average possible throughput


Step 2a - Create Download Queue
-------------------------------
On the **Queues** tab click the **+** button in the lower right corner.
An empty **Edit queue** screen will popup.

Create Queue For Download
""""""""""""""""""""""""
========================= ================== =============================================================================================================
 **enabled**              Checked            *Check to enable the queue*
 **pipe**                 Download           *Select our Pipe*
 **weight**               100                *Weight has no use in FQ_CoDeL, it will ignore it thus set to 100*
 **mask**                 (none)             *No need for MASK, FQ_CoDeL handles flows into individual queues. Flow > hash > Buckets > Queues*
 **Enable CoDel**         (empty)            *Don't click this option we will use FQ as selected in Pipe*
 **(FQ-)CoDel target**    (empty)            *In queue configuration needs to be empty. This is used for CoDeL in Queue*
 **(FQ-)CoDel interval**  (empty)            *In queue configuration needs to be empty. This is used for CoDeL in Queue*
 **(FQ-)CoDel ECN**       (empty)            *No need, ECN specified in Scheduler(Pipe). This is used for CoDeL in Queue*
 **description**          Download-Queue     *Free field, enter something descriptive*
========================= ================== =============================================================================================================

.. Note::

        Due to the way FQ_CoDeL works, the BW set in the Pipe will be shared across flows


Step 2b - Create Upload Queue
-----------------------------
On the **Queues** tab click the **+** button in the lower right corner.
An empty **Edit queue** screen will popup.

Create Queue For Upload
""""""""""""""""""""""""
========================= ================== =============================================================================================================
 **enabled**              Checked            *Check to enable the queue*
 **pipe**                 Upload             *Select our Pipe*
 **weight**               100                *Weight has no use in FQ_CoDeL, it will ignore it thus set to 100*
 **mask**                 (none)             *No need for MASK, FQ_CoDeL handles flows into individual queues. Flow > hash > Buckets > Queues*
 **Enable CoDel**         (empty)            *Don't click this option we will use FQ as selected in Pipe*
 **(FQ-)CoDel target**    (empty)            *In queue configuration needs to be empty. This is used for CoDeL in Queue*
 **(FQ-)CoDel interval**  (empty)            *In queue configuration needs to be empty. This is used for CoDeL in Queue*
 **(FQ-)CoDel ECN**       Checked            *No need, ECN specified in Scheduler(Pipe). This is used for CoDeL in Queue*
 **description**          Upload-Queue       *Free field, enter something descriptive*
========================= ================== =============================================================================================================

.. Note::

        Due to the way FQ_CoDeL works, the BW set in Pipe will be shared across flows


Step 3a - Create Download Rule
------------------------------
On the **Rules** tab click the **+** button in the lower right corner.
An empty **Edit rule** screen will popup.

Create a Rule For Download
""""""""""""""""""""""""
====================== =================== ===========================================================================================================
 **enabled**             Checked            *Check to enable the rule*
 **sequence**            1                  *Auto generated number, overwrite only when needed*
 **interface**           WAN                *Select the interface connected to the internet*
 **interface2**          NONE               *Matches packets traveling to/from interface (1) to/from interface (2). Can be combined with direction.*
 **proto**               ip                 *Select the protocol, IP in our example*
 **source**              any                *The source address to shape, leave on any*
 **src-port**            any                *The source port to shape, leave on any*
 **destination**         any                *The destination IP to shape, leave on any*
 **dst-port**            any                *The destination port to shape, leave on any*
 **direction**           in                 *Matches incoming or outgoing packets or both (default). We want to shape Download e.g ingress on WAN* 
 **target**             Download-Queue      *Select the Download queue*
 **description**        Download-Rule       *Enter a descriptive name*
====================== =================== ===========================================================================================================


Step 3b - Create Upload Rule
----------------------------
On the **Rules** tab click the **+** button in the lower right corner.
An empty **Edit rule** screen will popup.

Create a Rule For Upload
""""""""""""""""""""""""
====================== =================== ===========================================================================================================
 **enabled**             Checked            *Check to enable the rule*
 **sequence**            2                  *Auto generated number, overwrite only when needed*
 **interface**           WAN                *Select the interface connected to the internet*
 **interface2**          NONE               *Matches packets traveling to/from interface (1) to/from interface (2). Can be combined with direction.*
 **proto**               ip                 *Select the protocol, IP in our example*
 **source**              any                *The source address to shape, leave on any*
 **src-port**            any                *The source port to shape, leave on any*
 **destination**         any                *The destination IP to shape, leave on any*
 **dst-port**            any                *The destination port to shape, leave on any*
 **direction**           out                *Matches incoming or outgoing packets or both (default). We want to shape Upload e.g egress on WAN** 
 **target**             Upload-Queue        *Select the Upload queue*
 **description**        Upload-Rule         *Enter a descriptive name*
====================== =================== ===========================================================================================================


Now press |apply| to activate the traffic shaping rules.


Test for Bufferbloat
--------------------------------
There are several sites which can test & give you a rating for bufferbloat. You should run a test before and after implementing FQ_CoDeL.

* https://www.waveform.com/tools/bufferbloat
* http://www.dslreports.com/speedtest
* https://speed.cloudflare.com/

Bellow is a test run after applying above FQ_Codel configuration with Tuning.


*Screenshot after configuring Shaper with FQ_CoDel*

.. image:: images/bufferbloat_test_post_config_tuning.png
    :width: 100%

.. |apply| image:: images/applybtn.png


FQ-CoDel Tuning
----------------------------

FQ-CoDel specifically CoDel is designed to be *no knobs* algorithm, by default this is true at 10Gbit/s speeds. So it's worth to try to tune some parameters to better combat Bufferbloat on WAN from end users perspective.

*FQ-CoDel parameters to Tune and their out of the box default settings*

+----------------+----------------------------+
|FQ_C Parameter  |           Default          |
+================+==========+=================+
|     quantum    |            1514            |
+----------------+----------+-----------------+
|     target     |            5               |
+----------------+----------+-----------------+
|     interval   |            100             |
+----------------+----------+-----------------+
|     limit      |            10240           |
+----------------+----------+-----------------+
|     flows      |            1024            |
+----------------+----------+-----------------+
|     ECN        |            OFF             |
+----------------+----------+-----------------+

.. Note::

        We tune these parameters in Pipe. 
        Specifically in the Scheduler that is activated for a specific Pipe when choosing FQ_CoDel


quantum
"""""""
Quantum is one of these parameters that were constantly discussed what should be the proper value. Within the internet there is a lot of discussion that it should be set to 300 per 100Mbit/s of BW.
**This however is wrong.**

Quantum specifies number of bytes a queue can serve before being moved to the tail of old. As we are doing Fair Queueing we want to aim to serve all queues equally.

**The proper value of Quantum should be no more or less than is the WAN MTU.**

.. Note::

        At lower rates, below 100Mbit, setting the quantum to 300 ensures that more smaller packets get through faster than big ones. 
        It doesn't matter much at higher rates. The quantum should be set to the MTU or 300 if you have low bandwidth and the cpu power. 
        Setting the quantum lower causes more loops touching all the packets so it eats slightly more cpu
      
      
target & interval
""""""""""""""""""
Target is the acceptable minimum standing/persistent queue delay for each FQ-CoDel queue. This minimum delay is identified by tracking the local minimum queue delay that packets experience.
Target should be tuned to be at least the transmission time of a single MTU-sized packet at the WAN egress link speed. 

To do this we can run excessive ping, best during idle time of the network, to the HOP after your OPNsense and take the **average rtt round up as your Target**. In this case 12ms.

.. code-block::

    Example from the CLI of OPNsense

    traceroute 1.1.1.1
    traceroute to 1.1.1.1 (1.1.1.1), 64 hops max, 40 byte packets
    1  192.168.0.1  0.463 ms  0.453 ms  0.480 ms     <<<< LAN Interface of OPN
    2  10.205.5.1  10.879 ms  11.010 ms  11.079 ms   <<<< ISP directly connected Device to OPN WAN

    ping -s 1472 -c 1000 -D 10.205.5.1
    PING 10.205.5.1 (10.205.5.1) 1472(1500) bytes of data.
    1480 bytes from 10.205.5.1: icmp_seq=0 ttl=255 time=13.1 ms
    1480 bytes from 10.205.5.1: icmp_seq=1 ttl=255 time=10.4 ms

    --- 10.205.5.1 ping statistics ---
    1000 packets transmitted, 1000 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 7.800/11.429/45.992/4.796 ms

.. Note::

        Target is a good parameter for tune to prevent CoDel being too aggressive at low BW.
        Otherwise Target should be around 5-10% of Interval


Interval is used to ensure that the measured minimum delay does not become too stale. It's value is choose to give endpoints time to rach to a drop without being so long that response times suffer.

.. Note::

        Interval default 100ms works usually well (10ms-1s, excels at range 10ms-300ms).
        If you want to tune Interval it should to be set around the worst case RTT scenario through the bottleneck
        

limit
"""""""
Default limit size of 10240 packets is to much. The creators recommended value 1000 for sub 10Gbit/s connections. The default limit will never reached for sub 10Gbit/s WAN connections. Before that could happen FQ_CoDeL would already take action. So it's healthy to reduce limit.

The over-large packet limit leads to bad results during slow start on some benchmarks. Reducing it too low could impact new flow start.

However there is a problem with FQ_CoDel implementation in FreeBSD (as well OpenBSD), that causes CPU hogging and excessive logging, this is more visible when set to 1000. Which causes a backpush and additional unwanted latency.

**For now its best to have limit at default.**

.. Note::

        There is already a BUG opened for this and an email chain from one of the CoDeL creators. 
        This problem is overall affecting the performance, its not specific only to limit parameter, 
        and more so the more TCP flows are present


flows
"""""""
The "flows" parameter sets the number of queues into which the incoming packets are classified. Due to the stochastic nature of hashing, multiple flows may end up being hashed into the same slot.

This parameter can be set only at initialisation time in the current implementation (needs reboot of device), since memory has to be allocated for the hash table.

.. Warning::

        Setting too high number can cause the device to be stuck. Be careful with this one.


ECN
"""""""
Current best practice is to turn off ECN on uplinks running at less than 4Mbit (if you want good VOIP performance; a single packet at 1Mbps takes 13ms, and packet drops get you this latency back).

ECN IS useful on downlinks on a home router, where the terminating hop is only one or two hops away, and connected to a system that handles ECN correctly.

.. Note::

        If you are experiencing slow starts disable ECN


External references
............................................................

* https://www.rfc-editor.org/rfc/rfc8290.html
* https://www.rfc-editor.org/rfc/rfc8289#section-4.2
* https://man.freebsd.org/cgi/man.cgi?query=ipfw&apropos=0&sektion=8&manpath=FreeBSD+14.1-RELEASE&arch=default&format=html
* https://www.bufferbloat.net/projects/codel/wiki/Best_practices_for_benchmarking_Codel_and_FQ_Codel/
* https://forum.opnsense.org/index.php?topic=4949.msg20862#msg20862
* https://forum.opnsense.org/index.php?topic=39046.msg191251#msg191251
* https://www.man7.org/linux/man-pages/man8/tc-fq_codel.8.html
* https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=276890
* https://marc.info/?t=170776797300003&r=1&w=2
