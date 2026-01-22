============================
PPPoE ISP Setup
============================

.. contents:: Index


----------------------------
Summary
----------------------------

This guide covers the configuration of a PPPoE setup that subscribes the OPNsense to a Provider Edge Router (PE).

Most providers require a VLAN tag in modern setups, this guide will focus on that. If your setup does not require VLANs,
set the PPPoE device directly on the parent interface.

See the section on `Point-to-Point </manual/other-interfaces.html#point-to-point>`_ for more details.


----------------------------
Setup Overview
----------------------------

Your ISP provides you the following information to connect via PPPoE:

- Username: 123456789001@example.com
- Password: HelloWorld
- VLAN Tag: 7

For this example setup, we assume the default WAN interface is ``igc1``.
Though this default interface can have different names depending on
your environment, e.g., ``igb1``, ``hn1``, ``vtnet1`` or similar.

----------------------------
Configuration
----------------------------


1. Parent Interface
----------------------------

The parent interface for the PPPoE connection is usually the WAN interface. This interface is assigned per default.

When using a VLAN, remove the IP configuration from it.

- Go to :menuselection:`Interfaces --> WAN` and set:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**IPv4 Configuration Type**         ``None``
**IPv6 Configuration Type**         ``None``
==================================  =======================================================================================================

- Press **Save** and **Apply**

.. Tip::

    The parent interface does not need to stay assigned in most cases. It is only needed to create the VLAN device in the next step.
    There are edge cases where the parent interface needs to stay assigned and enabled, such as manually spoofing the MAC address
    to comply with ISP requirements. This can happen if you replace a Customer Premises Router (CPE) with your own router and PPPoE
    authentication must use the MAC address of the CPE.


2. VLAN Device
----------------------------

Create a VLAN device on the WAN interface.

- Go to :menuselection:`Interfaces --> Devices --> VLAN` and create a new VLAN device with the following settings:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Device**                          ``vlan0.1.7``
**Parent interface**                ``igc1``
**VLAN tag**                        ``7``
**VLAN priority**                   Leave default
**Description**                     ``vlan0.1.7``
==================================  =======================================================================================================

- Press **Save** and **Apply**

.. Tip:: This device does not need to be assigned, it is only used to create the PPPoE device in the next step.


3. PPPoE Device
----------------------------

Now, we create the Point-to-Point device that we attach to the prior created VLAN device.

Go to :menuselection:`Interfaces --> Devices --> Point-to-Point` and create a new PPPoE device with the following settings:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Link Type**                       ``PPPoE``
**Link interface(s)**               ``vlan0.1.7``
**Description**                     ``igc1_vlan7_PPPoE``
**Username**                        ``123456789001@example.com``
**Password**                        ``HelloWorld``
==================================  =======================================================================================================

- Press **Save**

Go to :menuselection:`Interfaces --> Assignments` and assign the PPPoE device:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Device**                          ``pppoe0 (vlan0.1.7) - igc1_vlan7_PPPoE``
**Description**                     ``igc1_vlan7_PPPoE``
==================================  =======================================================================================================

Press **Add** to apply the changes.

Go to :menuselection:`Interfaces --> Assignments` and assign the PPPoE device:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Enable**                          ``X``
**IPv4 Configuration Type**         ``PPPoE``
==================================  =======================================================================================================

- Press **Save** and **Apply**

Now the PPPoE connection should be up and running when connecting the ``igc1`` port to the ISP provided Modem or ONT.

4. Logfiles
-------------------------------

The ``ppp`` log files can be found in :menuselection:`System --> Log Files --> General`.

.. Tip:: The Link Control Procol will reveal most Link Layer and Authorization issues. Filtering for these messages is the best way to troubleshoot Point-to-Point connections.

A successful LCP (Link Control Protocol) sequence should look like this:

::

    LCP: Open event
    LCP: state change Initial --> Starting
    LCP: LayerStart
    LCP: Up event
    LCP: state change Starting --> Req-Sent
    LCP: SendConfigReq #1
    LCP: rec'd Configure Request #105 (Req-Sent)
    LCP: SendConfigAck #105
    LCP: state change Req-Sent --> Ack-Sent
    LCP: rec'd Configure Ack #1 (Ack-Sent)
    LCP: state change Ack-Sent --> Opened
    LCP: auth: peer wants PAP, I want nothing
    LCP: LayerUp
    LCP: authorization successful
