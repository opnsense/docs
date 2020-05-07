==============================
Reserve dedicated bandwidth
==============================

**Reserve dedicated bandwidth for a realtime traffic such as (hosted) Voice Over IP (VOIP) server.**

In this scenario we will create a pipe dedicated for traffic going to and coming
from our realtime application. For the sample we presume a SIP trunk or hosted
Voice Over IP (VOIP) server.

For this example we presume a requirement of 4 uncompressed voice channels of 64 kbps,
resulting in a total bandwidth of 256 kbps. The internet connection in this example
has 10 Mbps Download and 1 Mbps Upload.



.. nwdiag::
  :scale: 100%
  :caption: Shaping hosted VOIP / SIP trunk sample

    nwdiag {

      span_width = 90;
      node_width = 180;
      Internet [shape = "cisco.cloud"];
      ip_phone [label="IP Phone",shape="cisco.ip_phone"];
      ip_phone -- switchlan;

      network LAN {
        switchlan [label="",shape = "cisco.workgroup_switch"];
        label = "LAN OPNsense";
        address ="192.168.1.x/24";
        fw1 [label="OPNsense",address="192.168.1.1/24"];
      }

      network WAN  {
        label = ".WAN OPNsense";
        fw1 [label="OPNsense", shape = "cisco.firewall", address="172.10.1.1/32"];
        Internet;
      }

      network SIPHOST {
        label = ".WAN SIP PROVIDER";
        Internet;
        sip_server [label="SIP/VOIP Server",shape="cisco.sip_proxy_werver", address="172.10.2.1/32"];
      }
    }

To start go to :menuselection:`Firewall --> Shaper --> Settings`.

Step 1 - Create Upload and Download Pipes
-----------------------------------------
On the **Pipes** tab click the **+** button in the lower right corner.
An empty **Edit Pipe** screen will popup.

Create Pipe For Upload (To our VOIP Server)

====================== ================ ================================================
 **enabled**            Checked          *Check to enable the pipe*
 **bandwidth**          256              *Numeric value of the desired bandwidth*
 **bandwidth Metric**   Kbit/s           *Metric to use with the numeric value*
 **mask**               (Empty)          *Used for auto queueing, empty for our sample*
 **description**        PipeUp-256kbps   *Free field, enter something descriptive*
====================== ================ ================================================

Create Pipe For Upload (Other Traffic = 1024 kbps - 256 kbps = 768 kbps)

====================== ================ ================================================
 **enabled**            Checked          *Check to enable the pipe*
 **bandwidth**          768              *Numeric value of the desired bandwidth*
 **bandwidth Metric**   Kbit/s           *Metric to use with the numeric value*
 **mask**               (Empty)          *Used for auto queueing, empty for our sample*
 **description**        PipeUp-768kbps   *Free field, enter something descriptive*
====================== ================ ================================================

Create Pipe For Download (From our VOIP Server)

====================== ================== ================================================
 **enabled**            Checked            *Check to enable the pipe*
 **bandwidth**          256                *Numeric value of the desired bandwidth*
 **bandwidth Metric**   Kbit/s             *Metric to use with the numeric value*
 **mask**               (Empty)            *Used for auto queueing, empty for our sample*
 **description**        PipeDown-256kbps   *Free field, enter something descriptive*
====================== ================== ================================================

Create Pipe For Download (Other Traffic = 10240 kbps - 256 kbps = 9984 kbps )

====================== =================== ================================================
 **enabled**            Checked             *Check to enable the pipe*
 **bandwidth**          9984                *Numeric value of the desired bandwidth*
 **bandwidth Metric**   Kbit/s              *Metric to use with the numeric value*
 **mask**               (Empty)             *Used for auto queueing, empty for our sample*
 **description**        PipeDown-9984kbps   *Free field, enter something descriptive*
====================== =================== ================================================

Step 2 - Create Rules
----------------------
On the **Rules** tab click the **+** button in the lower right corner.
An empty **Edit rule** screen will popup.

Create a rule for traffic directed towards the VOIP Server (Upload).

====================== ================= =====================================================
 **sequence**            11               *Auto generated number, overwrite only when needed*
 **interface**           WAN              *Select the interface connected to the internet*
 **proto**               ip               *Select the protocol, IP in our example*
 **source**              any              *The source IP to shape, leave on any*
 **src-port**            any              *The source port to shape, leave on any*
 **destination**        172.10.2.1        *The IP address of our VOIP server*
 **dst-port**            any              *Use any of the destination port if static*
 **target**             PipeUP-256kbps    *Select the Upload 256 kbps Pipe*
 **description**        ShapeVOIPUpload   *Enter a descriptive name*
====================== ================= =====================================================


Create a rule for traffic coming from the VOIP Server (Download).

====================== ================= =====================================================
 **sequence**            21               *Auto generated number, overwrite only when needed*
 **interface**           WAN              *Select the interface connected to the internet*
 **proto**               ip               *Select the protocol, IP in our example*
 **source**              172.10.2.1       *The IP address of our VOIP server*
 **src-port**            any              *The source port to shape, leave on any*
 **destination**         any              *The destination IP to shape, leave on any*
 **dst-port**            any              *The destination port to shape, leave on any*
 **target**             PipeDown256kbps   *Select the Download 256 kbps Pipe*
 **description**        ShapeVOIPDown     *Enter a descriptive name*
====================== ================= =====================================================

Create a rule for all other internet upload traffic

====================== ================= =====================================================
 **sequence**            31               *Auto generated number, overwrite only when needed*
 **interface**           WAN              *Select the interface connected to the internet*
 **proto**               ip               *Select the protocol, IP in our example*
 **source**              192.168.1.0/24   *The source IPs to shape, our LAN network*
 **src-port**            any              *The source port to shape, leave on any*
 **destination**         any              *the destination address, leave in any*
 **dst-port**            any              *Use any of the destination port if static*
 **target**             PipeUp-768kbps    *Select the Upload 768 kbps Pipe*
 **description**        ShapeUpload       *Enter a descriptive name*
====================== ================= =====================================================


Create a rule for all other internet download traffic

====================== =================== =====================================================
 **sequence**            41                 *Auto generated number, overwrite only when needed*
 **interface**           WAN                *Select the interface connected to the internet*
 **proto**               ip                 *Select the protocol, IP in our example*
 **source**              any                *The source IP to shape, leave on any*
 **src-port**            any                *The source port to shape, leave on any*
 **destination**         192.168.1.0/24     *The destination IPs to shape, our LAN network*
 **dst-port**            any                *The destination port to shape, leave on any*
 **target**             PipeDown-9984kbps   *Select the Download 256Kbps Pipe*
 **description**        ShapeDown           *Enter a descriptive name*
====================== =================== =====================================================

.. Note::

        Be aware of the sequence! It is important to make sure the right traffic
        is passed to the right pipe.


Now press |apply| to activate the traffic shaping rules.

*Screenshot Rules*

.. image:: images/shaping_rules_s1.png
    :width: 100%

.. |apply| image:: images/applybtn.png
