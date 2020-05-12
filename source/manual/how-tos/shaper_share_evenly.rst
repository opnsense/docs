===================================================
Share internet bandwidth amongst users evenly
===================================================

For this example we presume an internet connection of 10 Mbps Download and 1 Mbps
Upload that we want to share evenly between all users.

.. nwdiag::
  :scale: 100%
  :caption: Shaping bandwidth evenly sample

    nwdiag {

      span_width = 90;
      node_width = 180;
      Internet [shape = "cisco.cloud"];
      pc [label="Connected PC's",shape="cisco.pc"];
      pc -- switchlan;

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

    }

To start go to :menuselection:`Firewall --> Traffic Shaper --> Settings`.

Step 1 - Create Upload and Download Pipes
-----------------------------------------
On the **Pipes** tab click the **+** button in the lower right corner.
An empty **Edit Pipe** screen will popup.

Create Pipe For Upload

====================== ================ ================================================
 **enabled**            Checked          *Check to enable the pipe*
 **bandwidth**          1                *Numeric value of the desired bandwidth*
 **bandwidth Metric**   Mbit/s           *Metric to use with the numeric value*
 **mask**               empty            *Select destination to share the bandwidth*
 **description**        PipeUp-1Mbps     *Free field, enter something descriptive*
====================== ================ ================================================


Create Pipe For Download

====================== ================== ================================================
 **enabled**            Checked            *Check to enable the pipe*
 **bandwidth**          10                 *Numeric value of the desired bandwidth*
 **bandwidth Metric**   Mbit/s             *Metric to use with the numeric value*
 **mask**               empty              *Select destination to share the bandwidth*
 **description**        PipeDown-10Mbps    *Free field, enter something descriptive*
====================== ================== ================================================

Step 2 - Create a Queues
------------------------
On the **Queues** tab click the **+** button in the lower right corner.
An empty **Edit queue** screen will popup.

Create Queue for Upload

====================== ================== ================================================
 **enabled**            Checked            *Check to enable the pipe*
 **pipe**               PipeUp-1Mbps       *Select our Pipe*
 **weight**             100                *Weight to use with the numeric value*
 **mask**               source             *Every source creates a match*
 **description**        QueueUp-1Mbps      *Free field, enter something descriptive*
====================== ================== ================================================

Create Queue for Download

====================== ================== ================================================
 **enabled**            Checked            *Check to enable the pipe*
 **pipe**               PipeDown-10Mbps    *Select our Pipe*
 **weight**             100                *Weight to use with the numeric value*
 **mask**               destination        *Every source creates a match*
 **description**        QueueDown-10Mbps   *Free field, enter something descriptive*
====================== ================== ================================================


Step 3 - Create Rules
----------------------
On the **Rules** tab click the **+** button in the lower right corner.
An empty **Edit rule** screen will popup.

Create a rule for traffic directed towards the internet (Upload).

====================== ================= =====================================================
 **sequence**            11               *Auto generated number, overwrite only when needed*
 **interface**           WAN              *Select the interface connected to the internet*
 **proto**               ip               *Select the protocol, IP in our example*
 **source**              192.168.1.0/24   *The source IP to shape, select the LAN network*
 **src-port**            any              *The source port to shape, leave on any*
 **destination**         any              *The destination to shape, leave on any*
 **dst-port**            any              *Use any of the destination port if static*
 **target**             QueueUp-1Mbps     *Select the Upload 1Mbps Queue*
 **description**        ShapeUpload       *Enter a descriptive name*
====================== ================= =====================================================


Create a rule for traffic coming from the internet (Download).

====================== ================= =====================================================
 **sequence**            21               *Auto generated number, overwrite only when needed*
 **interface**           WAN              *Select the interface connected to the internet*
 **proto**               ip               *Select the protocol, IP in our example*
 **source**              any              *The source address, leave on any*
 **src-port**            any              *The source port to shape, leave on any*
 **destination**         192.168.1.0/24   *The destination IP to shape, select LAN network*
 **dst-port**            any              *The destination port to shape, leave on any*
 **target**             QueueDown-10Mbps  *Select the Download 10 Mbps Queue*
 **description**        ShapeDownload     *Enter a descriptive name*
====================== ================= =====================================================

Now press |apply| to activate the traffic shaping rules.

*Screenshot Rules*

.. image:: images/shaping_rules_s2.png
    :width: 100%

.. |apply| image:: images/applybtn.png
