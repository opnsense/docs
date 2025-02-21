============================
PPPoE ISP Setup
============================

.. contents:: Index


----------------------------
Summary
----------------------------

This guide covers the configuration of a PPPoE setup that subscribes the OPNsense to a Provider Edge Router (PE).

Most providers require a VLAN tag in modern setups, this guide will focus on that. If your setup does not require,
set the PPPoE device directly on the parent interface.

See the section on `Point-to-Point </manual/other-interfaces.html#point-to-point>`_ for more details.


----------------------------
Setup Overview
----------------------------

Your ISP provides you the following information to connect via PPPoE:

- Username: ``123456789001@example.com``
- Password: ``HelloWorld``
- VLAN Tag: ``7``

We assume the default WAN interface is ``igc1``.

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

.. Tip:: If you do not plan to use this interface at all, you can also unassign it. Only the VLAN interface must be assigned for PPPoE to work.


2. VLAN Interface
----------------------------

Create a VLAN interface on the WAN interface.

- Go to :menuselection:`Interfaces --> Devices --> VLAN` and create a new VLAN interface with the following settings:

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

.. Note:: `Device` can optionally be left empty to auto assign the vlan device name.

- Next, go to :menuselection:`Interfaces --> Assignments` and assign the VLAN interface you just created.

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Device**                          ``vlan0.1.7``
**Description**                     ``igc1_vlan7_PPPoE``
==================================  =======================================================================================================

- Press **Add**


3. PPPoE Interface
----------------------------

Now, we create the Point-to-Point device that we attach to the prior created VLAN.

Go to :menuselection:`Interfaces --> Devices --> PPPoE` and create a new PPPoE interface with the following settings:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**Link Type**                       ``PPPoE``
**Link interface(s)**               ``vlan0.1.7``
**Username**                        ``123456789001@example.com``
**Password**                        ``HelloWorld``
==================================  =======================================================================================================

- Press **Save**

Go to :menuselection:`Interfaces --> igc1_vlan7_PPPoE` and validate the settings:

==================================  =======================================================================================================
Option                              Value
==================================  =======================================================================================================
**IPv4 Configuration Type**         ``PPPoE``
==================================  =======================================================================================================

- Press **Save** and **Apply**

Now the PPPoE connection should be up and running when connecting ``igc1`` to the ISP provided Modem or ONT.

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
