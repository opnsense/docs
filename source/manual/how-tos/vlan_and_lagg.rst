========================================
VLAN and LAGG Setup
========================================

**Summary**

Connect your `OPNsense Appliance` successfully to a `Managed Switch` using OSI Layer 2 protocols like LAGG and VLAN.


.. contents:: Index


----------------------------
Introduction
----------------------------

A VLAN (Virtual Local Area Network) allows to create separate Layer 2 networks within the same physical switch.
This means you can segment a single physical network into multiple logical networks,
keeping different groups of devices isolated from each other even though they are connected to the same switch.

VLAN are usually categorized as `tagged` and `untagged`:

- | **Tagged VLAN:** Frames are sent with VLAN tags embedded in them. This allows multiple VLANs to be carried over a single network link,
    typically between switches or VLAN-aware devices. Tagged VLANs are used on **trunk ports** to identify which frame belongs to which VLAN.
- | **Untagged VLAN:** Frames are sent without VLAN tags. The switch port assigns incoming untagged frames to a default VLAN.
    Untagged VLANs are typically used on **access ports** connected to end devices that are not VLAN-aware, such as computers.


Each VLAN will represent its own isolated network, connected by a VLAN-aware router like the OPNsense.
Traffic that should cross VLAN boundaries must be routed and controlled via firewall rules. This is known as `Inter-VLAN-Routing`.

.. Note::

    Not all switches support VLANs. `Unmanaged Switches` only provide basic functionality.
    `Managed Switches` will support features like Link Aggregation (with LACP mode) and VLAN needed for this setup.


.. Attention::

    Do not mix tagged and untagged VLANs on the trunk connecting the `OPNsense Appliance` and the `Managed Switch`.
    Side effects include leaking Router Advertisements, DHCP, CARP and other broadcasts between tagged and untagged VLANs.
    This depends on the brand of the deployed switch, so avoiding untagged frames for trunk ports is the safest method.
    Additionally, the interface statistics of the untagged VLAN would show all traffic, which can be confusing.


.. Attention::

    Do not use a bridge interface to connect multiple ports to the same switch as this will create a network loop.
    Use a Layer 2 Link Aggregation protocol (LAGG) with LACP instead.


This guide will explain the best practice approach. Since switches from different vendors offer divergent configuration paths,
only a guideline can be provided.


----------------------------
Setup Overview
----------------------------

In our basic setup, we have a `Managed Switch` and an `OPNsense Appliance`.

We need isolate:

    - a LAN network with `PCs`, we assigned VLAN 5
    - a DMZ network with `Web Servers`, we assigned VLAN 20
    - a GUEST network with clients connecting to a `Guest Wifi`, we assigned VLAN 33

The OPNsense and the Switch are either connected with a single network cable,
or with multiple network cables via `Link Aggregation`.
The `Port Mode` describes the configuration of the `Managed Switch` ports.

===============  ================  ================  ======================================
VLAN Tagged      VLAN Untagged     Port Mode         Device
===============  ================  ================  ======================================
5,20,33          None              Trunk             Switch <-> OPNsense
None             5                 Access            Switch <-> PC01
None             5                 Access            Switch <-> PC02
None             20                Access            Switch <-> WebServer01
33               5                 Trunk             Switch <-> AccessPoint01
33               5                 Trunk             Switch <-> AccessPoint02
===============  ================  ================  ======================================

.. Tip::

    Most Access Points require their management network to be untagged, and additional SSIDs like `Guest Wifi` to be tagged.
    The trunk from `Managed Switch` to `Access Point` has to be configured in a mixed mode with an untagged (default) VLAN and a tagged VLAN.
    This is in contrast to the trunk that is connected to the OPNsense, which has no untagged (default) VLAN.

.. Tip::

    The `Access Port` of a `Managed Switch` will tag ingress frames with its configured VLAN, and strip egress frames of VLAN tags.

.. Tip::

    It is good practice to configure the ports of a `Managed Switch` only with VLANs that are needed for that specific port or LAGG. 
    This is called manual VLAN Pruning.

----------------------------
Configuration
----------------------------


1. Setup LAGG Interface (optional)
-------------------------------------------

See the section on `LAGG </manual/other-interfaces.html#lagg>`_ for more details.

.. Note::

    This step is optional. It will create an abstraction layer between the VLANs and the physical interfaces,
    making it easy to change or add more physical interfaces later. A LAGG can be created even with just a single member interface.
    If you have a simple office deployment, you can skip this step and use a physical interface directly.

    
.. Attention::

    The member interfaces of a LAGG must be unassigned before creation. Check in :menuselection:`Interfaces --> Assignments` and delete
    the assignment if necessary.


- | Go to :menuselection:`Interfaces --> Devices --> LAGG` and add a new entry:

=============================  ================================================================
**Option**                     **Value**
=============================  ================================================================
Parent                         Choose one or more interfaces, e.g., ``igc0`` and ``igc1``
Proto                          lacp (if your managed switch supports it)
Fast timeout                   Keep on default, disabled
Hash Layers                    Set to same as switch, if unknown leave empty
Description                    ``lagg0``
=============================  ================================================================

Afterwards, create the same LAGG interface on the `Managed Switch` and assign one or more physical interfaces to it. 
Connect the `OPNsense Appliance` and the `Managed Switch` via one or multiple network cables to establish the link layer.
Verify the status of the LAGG interface as up before continuing.



2. Add VLAN Interfaces
----------------------------

See the section on `VLAN </manual/other-interfaces.html#vlan>`_ for more details.

In our example setup we require tagged VLAN 5 (LAN), 20 (DMZ) and 33 (GUEST), and no untagged VLAN.
If you skipped Step 1, create the VLAN directly on a physical interface like ``igc0``.

- | Go to :menuselection:`Interfaces --> Devices --> VLAN` and add new entries:

=============================  ===============  ===============  ===============
**Option**                     **LAN**          **DMZ**          **GUEST**
=============================  ===============  ===============  ===============
Device                         ``vlan0.5``      ``vlan0.20``     ``vlan0.33``
Parent                         ``lagg0``        ``lagg0``        ``lagg0``
VLAN tag                       ``5``            ``20``           ``33``
Description                    ``vlan0.5``      ``vlan0.20``     ``vlan0.33``
=============================  ===============  ===============  ===============


- | Go to :menuselection:`Interfaces --> Assignments` and assign the new VLAN interfaces. The parent interface should stay unassigned.
    In rare cases, the parent interface can be assigned without a network configuration, to allow manual link speed overrides.
- | On the `Managed Switch`, create the same tagged VLANs on the LAGG or physical interface. Make sure there is no `Native-VLAN-ID` or `default VLAN`
    on the trunk port that connects to the OPNsense.

.. Tip::

    A good choice is using descriptive names for interfaces with a template like ``interface_vlan_description``.
    In our example this results in ``lagg0_vlan5_LAN``, ``lagg0_vlan20_DMZ`` and ``lagg0_vlan33_GUEST``.
    This improves administration, especially in large setups with multiple interfaces being parents to different VLAN.


.. Tip::

    If the Switch does not support removing the untagged VLAN from a trunk port, create a sacrificial VLAN
    that is used to blackhole untagged traffic. As example, set the `Native-VLAN-ID` or `default VLAN` of the trunk port to `3999`,
    and do not reuse this VLAN tag elsewhere in the same Layer 2 network.


3. Create Networks on VLANs
----------------------------

.. Note::

    The steps so far followed the `OSI Layer Model`:

    #. Connecting the `Physical Layer` (Layer 1) between `OPNsense Appliance` and `Managed Switch`
    #. Creating the `Data Link Layer` (Layer 2) with LAGG (optional) and VLAN
    #. Configuring the `Network Layer` (Layer 3) by setting IP addresses on the VLAN interfaces
    

To create connectivity between assigned VLAN interfaces via `Inter-VLAN-Routing`, configure a network on them.
It is good practice to embed the VLAN IDs into the layer 3 networks, if possible.

=============================  ==============================  ==============================  ==============================
**Description**                **lagg0_vlan5_LAN**             **lagg0_vlan20_DMZ**            **lagg0_vlan33_GUEST**
=============================  ==============================  ==============================  ==============================
IPv4 Configuration Type        ``Static IPv4``                 ``Static IPv4``                 ``Static IPv4``
IPv4 address                   ``192.168.5.1/24``              ``192.168.20.1/24``              ``192.168.33.1/24``
=============================  ==============================  ==============================  ==============================

.. Attention::

    Each VLAN interface requires a unique IPv4 and/or IPv6 network, conflicts will prevent `Inter-VLAN-Routing`.
    If you plan multiple sites that should be connected via VPN, you can reuse the same VLAN IDs, yet use
    unique IPv4 networks for each site of your organization.


With VLANs configured, `PCs` in `LAN`, `Web Servers` in `DMZ` and `Guest Wifi clients` in `GUEST` are isolated,
even though they are connected to the same switch.

The OPNsense is responsible to route packets between VLANs.

It is the default gateway in VLAN 5, 20 and 33.
It will receive packets with destination IP addresses to the other locally connected networks, and route according to its routing table.
Access can be controlled with `Firewall Rules`, essentially creating different security zones.

.. Note::

     Only routed traffic can be filtered by a central firewall. Devices in the same VLAN communicate directly by using ARP or NDP to discover their neighbors.
