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

    Not all switches support VLAN. `Unmanaged Switches` only provide basic functionality.
    `Managed Switches` will support features like LACP and VLAN needed for this setup.


.. Attention::

    Do not mix tagged and untagged VLAN on the trunk connecting the `OPNsense Appliance` and the `Managed Switch`. 
    Side effects include leaking Router Advertisements, DHCP, CARP and other broadcasts between tagged and untagged VLAN.
    This depends on the brand of the deployed switch, so avoiding untagged frames for trunk ports is the safest method.


.. Attention::

    Do not use a bridge interface to connect multiple ports to the same switch as this will create a network loop.
    Use a Layer 2 Link Aggregation protocol like LACP instead.


This guide will explain the best practice approach. Since switches from different vendors offer divergant configuration paths,
only a guideline can be provided.


----------------------------
Setup Overview
----------------------------

In our basic setup, we have a `Managed Switch` and an `OPNsense Appliance`, along with a `Computer` and a `Printer` that should be in separate VLANs.
The OPNsense and the Switch are connected with two network cables via `Link Aggregation`.
The `Port Mode` describes the configuration of the `Managed Switch` ports.

===============  ================  ================  ===================
VLAN Tagged      VLAN Untagged     Port Mode         Device
===============  ================  ================  ===================
1,20             None              Trunk             Switch <-> OPNsense
None             1                 Access            Switch <-> Computer
None             20                Access            Switch <-> Printer
===============  ================  ================  ===================


----------------------------
Configuration
----------------------------


1. Setup LAGG interface
-------------------------

See the section on `LAGG </manual/other-interfaces.html#lagg>`_ for more details.

.. Note::

    This step is optional but highly recommended. It will create an abstraction layer between the VLAN and the physical interfaces,
    making it easy to change or add more physical interfaces later. A LAGG can be created even with just a single member interface.

    
.. Attention::

    The member interfaces of a LAGG must be unassigned before creation. Check in :menuselection:`Interfaces --> Assignements` and delete
    the assignement if necessary.


- | Go to :menuselection:`Interfaces --> Other Types --> LAGG` and add a new entry:

=============================  ================================================================
**Option**                     **Value**
=============================  ================================================================
Parent                         Choose one or more interfaces, e.g., ``igc0`` and ``igc1``
Proto                          lacp
Fast timeout                   Enable if switch supports it (recommended)
Hash Layers                    Set to same as switch, if unknown leave empty
Description                    ``lagg0``
=============================  ================================================================

Afterwards, create the same LAGG interface on the `Managed Switch` and assign one or more physical interfaces to it. 
Connect the `OPNsense Appliance` and the `Managed Switch` via one or multiple network cables to establish the link layer. 
Verify the status of the LAGG interface as up before continuing.

.. Note::

    If multiple switches are in a `Stack` configuration, using aggregation protocols like `MLAG (Multi-chassis Link Aggregation)`
    can be required on the switch side.    


2. Add VLAN Interfaces
----------------------------

See the section on `VLAN </manual/other-interfaces.html#vlan>`_ for more details.

In our example setup we require tagged VLAN 1 and 20, and no untagged VLAN.
If you skipped Step 1, create the VLAN directly on a physical interface.

- | Go to :menuselection:`Interfaces --> Other Types --> VLAN` and add new entries:

=============================  ================================================================
**Option**                     **Value**
=============================  ================================================================
Device                         ``vlan0.1``
Parent                         ``lagg0``
VLAN tag                       ``1``
Description                    ``vlan0.1``
=============================  ================================================================

=============================  ================================================================
**Option**                     **Value**
=============================  ================================================================
Device                         ``vlan0.20``
Parent                         ``lagg0``
VLAN tag                       ``20``
Description                    ``vlan0.20``
=============================  ================================================================

- | Go to :menuselection:`Interfaces --> Assignements` and assign the new VLAN interfaces. The parent interface should stay unassigned.
    In rare cases, the parent interface can be assigned without a network configuration, to allow manual link speed overrides.
- | On the `Managed Switch`, create the same tagged VLAN on the LAGG or physical interface. Make sure there is no `Native-VLAN-ID` on the trunk port.

.. Tip::

    A good choice is using descriptive names for interfaces with a template like ``interface_vlan_description``.
    In our example this results in ``lagg0_vlan1_LAN`` and ``lagg0_vlan20_PRINTER``.
    This improves administration, especially in large setups with multiple interfaces being parents to different VLAN.


.. Tip::

    If the Switch does not support setting the `Native-VLAN-ID` to `None`, create a sacrificial VLAN that is used to blackhole untagged traffic.
    As example, set the `Native-VLAN-ID` to `3999`, ensuring this tag is not used elsewhere.


3. Create Networks on VLANs
----------------------------

.. Note::

    The steps so far followed the `OSI Layer Model`:

    #. Connecting the `Physical Layer` (Layer 1) between `OPNsense Appliance` and `Managed Switch`
    #. Creating the `Data Link Layer` (Layer 2) with LAGG and VLAN
    #. Configuring the `Network Layer` (Layer 3) by setting IP addresses on the VLAN interfaces
    

To create connectivity between assigned VLAN interfaces via `Inter-VLAN-Routing`, configure a network on them.
In our example, we want the `Computer` to talk to the `Printer` via routing.

- | Go to :menuselection:`Interfaces --> lagg0_vlan1_LAN` and set the `IPv4 Configuration Type` to `Static IPv4`,
    assign an `IPv4 address` like ``192.168.1.1/24``
- | Go to :menuselection:`Interfaces --> lagg0_vlan20_PRINTER` and assign an `IPv4 address` like ``192.168.100.1/24``

.. Attention::

    Each VLAN interface requires a unique IPv4 and/or IPv6 network, conflicts will prevent `Inter-VLAN-Routing`.


With VLAN configured, the example `Computer` and `Printer` can not communicate directly, even though they are connected to the same switch.
The OPNsense is responsible to route packets between VLAN. It is the default gateway in both VLAN 1 and VLAN 20 and will receive packets
to be routed to the other connected network. Access can be controlled with `Firewall Rules`, essentially creating different security zones.

.. Note::

     Only routed traffic can be filtered by a central firewall. Devices in the same VLAN communicate directly by using ARP or NDP to discover their neighbors.
