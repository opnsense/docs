==================================================
Control Plane Shaping
==================================================

Planes of Operation, is concept to describe and divide the functionality 
of a network device.

In essence the concept creates logical layers into which are categorized packets 
per their use and type.

There are 3 Planes:

1. **The control plane**
  
   Affect the operationability of the network.
  
   The control plane is the brain of the router. It consists of dynamic IP routing protocols (that is OSPF, IS-IS, BGP, and so on), 
   the RIB, routing updates, in addition to other protocols such as PIM, IGMP, ICMP, ARP, BFD, LACP, and so on. 
   In short, the control plane is responsible for maintaining sessions and exchanging protocol information with other router or network devices.

2. **The management plane**
     
   Affect the manageability of the network.
     
   The management plane is used to manage a device through its connection to the network. 
   Examples of protocols processed in the management plane include Simple Network Management Protocol (SNMP), 
   Telnet, File Transfer Protocol (FTP), Secure FTP, and Secure Shell (SSH). 
   These management protocols are used for monitoring and for command-line interface (CLI) access.

3. **The data plane**
     
   Affect the applications of the user.
     
   The data plane is the forwarding plane, which is responsible for the switching of packets through the router. 
   



Necessity of Control Plane Shaping
----------------------------------

Control plane is a necessary component for the network operation.
A congested state of the network, if control plane is not taken care of, will result in network disruptions. 
In order to guarantee operation and non-disruption in such events, we can take advantage of QoS in our case Shaping.

**Its necessary to understand Control plane as such, needs to be always taken care of, always in its own dedicated way.**

.. Attention::
    Control plane should not share a class (Pipe nor Queue) with any other traffic type.


Configuring Control plane for OPNsense
--------------------------------------

Configuration will take in account existence of already configured shaper as per how-tos/shaper_bufferbloat

In the configuration steps below, assume these tuned speeds:

+----------------+----------+-----------------+
|                | Download |      Upload     |
+================+==========+=================+
|      Mbit/s    |   495    |        30       |
+----------------+----------+-----------------+


Bandwidth allocation requirements for Control plane:

+----------------+----------+-----------------+
|    1% of BW    | Download |      Upload     |
+================+==========+=================+
|      Mbit/s    |    5     |       0.5       |
+----------------+----------+-----------------+

The 1% is the default lowest value. Its subjected to be increased if needed.

.. Attention::
    BW given to a different Pipe needs to be subtracted from already existing one.



Schedulers available for Control plane shaping:

+----------------+----------+-----------------+
|   Schedulers   |  Usable  |       Note      |
+================+==========+=================+
|      FIFO      |    NO    | No weight merit |
+----------------+----------+-----------------+
|       WFQ      |    YES   |   weight merit  |
+----------------+----------+-----------------+
|       DRR      |    NO    | causing latency |
+----------------+----------+-----------------+
|       QFQ      |    YES   |   weight merit  |
+----------------+----------+-----------------+
|    FQ_CoDel    |    NO    |AQM back-pressure|
+----------------+----------+-----------------+
|     FQ_PIE     |    NO    |AQM back-pressure|
+----------------+----------+-----------------+

In this example we will create a Shaper for the IPv6 Control plane.

To begin, go to :menuselection:`Firewall --> Shaper --> Pipes`. Select the *advanced mode*



Step 1a - Create Download Pipe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On the **Pipes** tab click the **+** button in the lower right corner.
An empty **Edit Pipe** screen pops up.

Create Control-plane-Pipe For Download
""""""""""""""""""""""""""""""""""""""
========================= =========================== ==============================================================================
Setting                   Default                     Description
========================= =========================== ==============================================================================
 **enabled**              Checked                     *Check to enable the pipe*
 **bandwidth**            5                           *Set initially to 1% of tuned BW, increase if needed*
 **bandwidth Metric**     Mbit/s                      *Metric associated with the bandwidth*
 **queue**                (empty)                     *Leave empty: queues are configured separately*
 **mask**                 (none)                      *Leave empty*
 **scheduler type**       WFQ                         *Default or QFQ, allows to use weights per queues*
 **Enable CoDel**         (empty)                     *Leave empty*
 **(FQ-)CoDel target**    (empty)                     *Leave empty*
 **(FQ-)CoDel interval**  (empty)                     *Leave empty*
 **(FQ-)CoDel ECN**       (empty)                     *Leave empty*
 **FQ-CoDel quantum**     (empty)                     *Leave empty*
 **FQ-CoDel limit**       (empty)                     *Leave empty*
 **FQ-CoDel flows**       (empty)                     *Leave empty*
 **description**          Control-plane-Pipe-Download *Free field, enter something descriptive*
========================= =========================== ==============================================================================

Step 1b - Create Upload Pipe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On the **Pipes** tab click the **+** button in the lower right corner.
An empty **Edit Pipe** screen pops up.

Follow the same process as for the Download pipe, 
entering the 1% of tuned bandwidth value
and entering "Control-plane-Pipe-Upload" for the **description**

Step 2a - Create Download Queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On the **Queues** tab click the **+** button in the lower right corner.
An empty **Edit queue** screen pops up.

Create Control-plane-IPv6-Queue For Download
""""""""""""""""""""""""""""""""""""""""""""
========================= ================================= ==============================================================================
 **enabled**              Checked                           *Check to enable the queue*
 **pipe**                 Control-plane-Pipe-Download       *Select our Pipe*
 **weight**               100                               *The higher weight the higher the ratio of BW a queue gets*
 **mask**                 (none)                            *Leave empty for a queue*
 **Enable CoDel**         (empty)                           *Leave empty for a queue*
 **(FQ-)CoDel target**    (empty)                           *Leave empty for a queue*
 **(FQ-)CoDel interval**  (empty)                           *Leave empty for a queue*
 **(FQ-)CoDel ECN**       (empty)                           *Leave empty for a queue*
 **description**          Control-plane-IPv6-Queue-Download *Free field, enter something descriptive*
========================= ================================= ==============================================================================

.. Note::

        Using WFQ or QFQ and weights, we can tell how much BW will get each control plane for each protocol gain.

Step 2b - Create Upload Queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On the **Queues** tab click the **+** button in the lower right corner.
An empty **Edit queue** screen pops up.

Follow the same process as for the Download queue, 
selecting the **"Control-plane-Pipe-Upload**,
and entering "Control-plane-IPv6-Queue-Upload" for the **description**

Step 3a - Create Download Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On the **Rules** tab click the **+** button in the lower right corner.
An empty **Edit rule** screen pops up.

Create a Control-plane-IPv6-Rule For Download
"""""""""""""""""""""""""""""""""""""""""""""
====================== ================================= ======================================================================================================
 **enabled**           Checked                           *Check to enable the rule*
 **sequence**          1                                 *Auto generated number, overwrite only when needed*
 **interface**         WAN                               *Select the interface connected to the internet*
 **proto**             ipv6-icmp                         *Select the protocol, ipv6-icmp in our example*
 **source**            any                               *The source address to shape, leave on any*
 **src-port**          any                               *The source port to shape, leave on any*
 **destination**       any                               *The destination IP to shape, leave on any*
 **dst-port**          any                               *The destination port to shape, leave on any*
 **direction**         in                                *Matches incoming or outgoing packets or both (default). We want to shape Download e.g ingress on WAN* 
 **target**            Control-plane-IPv6-Queue-Download *Select the Download queue*
 **description**       Control-plane-IPv6-Rule-Download  *Enter a descriptive name*
====================== ================================= ======================================================================================================

Step 3b - Create Upload Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On the **Rules** tab click the **+** button in the lower right corner.
An empty **Edit rule** screen pops up.

Follow the same process as for the Download rule, 
using the same values except:

- **sequence** (set to 2); 
- **direction** (set to "out")
- **target** (set to "Control-plane-IPv6-Queue-Upload");
- **description** (set to "Control-plane-IPv6-Rule-Upload")

.. Attention::
    The sequences needs to be at least 1 less than the default any rules or rules that would catch this traffic type 
    and you may need to adjust the other rule sequence values accordingly.

Step 4 - Finalizing the configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now press |apply| to activate the traffic shaping rules.

.. |apply| image:: images/applybtn.png

-----------------------


Additional Control plane per protocol
--------------------------------------
In case we need to create control plane of additional protocols such as BGP, PIM, etc.
We can use the already created "Control-plane-Pipe".
Simple add Queues with proper weights and Rules into this specific Pipe matching the traffic.


External references
-------------------

* https://www.ciscopress.com/articles/article.asp?p=2272154&seqNum=3
* https://www.computernetworkingnotes.com/ccna-study-guide/data-plane-control-plane-and-management-plane.html
* https://forum.opnsense.org/index.php?topic=46990.0
* https://man.freebsd.org/cgi/man.cgi?ipfw(8)
