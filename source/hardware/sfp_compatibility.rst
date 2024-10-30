====================================
SFP(+) Compatibility
====================================

Most OPNsense® appliances feature 10 Gigabit SFP+ cages powered by AMD® `axgbe` to allow
for flexible connectivity. Different SFP(+) transceiver modules can be used to connect to different types of
media (e.g. copper or fiber) depending on your needs.

Our enterprise & datacenter OPNsense® appliances may also feature 25 Gigabit capable SFP28 cages powered by Intel® `ice`.

Below you can find some general information as well as a list of tested SFP(+)/SFP28 transceiver modules
that are verified to work with OPNsense® appliances.

.. tip::

    If you are using an SFP(+)/SFP28 module on one of the OPNsense® appliances that is not listed below but is working
    properly, consider submitting a Pull Request to `our documentation <https://github.com/opnsense/docs>`__ to extend the list.
    Any contribution is welcome!

=====================================================================================================================

.. contents:: Table of Contents
    :local:


**General Information**
=====================================================================================================================

There are a lot of transceiver modules available on the market and they are usually one of the following types:

- Copper RJ45

Often used for connectivity up to a distance of 100 meters maximum and are
relatively inexpensive.

.. warning::

    RJ45 SFP+ modules (10GBASE-T) can run at high operating temperatures in comparison to Fiber or DAC modules. Only
    the datacenter level OPNsense® appliances are equipped with passive cooling for the SFP+ cages. If the ambient
    temperature does not exceed 50°C, RJ45 SFP+ modules can be used in all OPNsense® appliances without issue.

- Single-mode optical fiber (SMF)

Often used for communication across large distances (100+km) and usually connected with either Simplex-LC or
Duplex-LC OS2 patch cords. It can potentially carry more bandwidth than Multi-mode fiber, but the equipment
needed to use SMF is often more expensive in comparison to MMF.

- Multi-mode optical fiber (MMF)

Multi-mode fiber is the alternative for SMF (up to 550M for 10Gb/s), often used for backbone applications in
buildings and usually connected with OM3 Duplex-LC patch cords.

- Direct-Attach (DAC)

For short ranges (up to 10M), often a popular choice due to low cost and low latency.

.. attention::

    Most transceiver modules are available for purchase with a variety of different programming options for
    compatibility with different vendors. Unless specified otherwise, all modules are assumed to have
    the generic / MSA standard default programming.



**Axgbe**
=====================================================================================================================

.. note::

    10 Mbit/s is currently not supported by Axgbe.

--------------------------------------
1G Single-mode optical fiber
--------------------------------------

========= ============================== ======= =========================
Vendor    Type                           Speed        Notes
========= ============================== ======= =========================
BeanField 100BASE-BX0-D53                100Mb
FlexOptix S.B1312.20.DL BiDi LX          1G      Tested module rated for 20km,
                                                 other distances are assumed to function properly
FlexOptix S.B1312.10.D                   1G      Tested module rated for 10km,
                                                 other distances are assumed to function properly
FS        SFP-FE-BX                      100Mb
FS        SFP-GE-BX                      1G
MikroTik  S-53LC20D                      1G
TP-Link   1000Base-BX WDM Bi-Directional 1G
Ubiquiti  UACC-OM-SM-1G-S                1G
========= ============================== ======= =========================

--------------------------------------
1G Multi-mode optical fiber
--------------------------------------

========= ============================== ======= =========================
Vendor    Type                           Speed        Notes
========= ============================== ======= =========================
FlexOptix S.8512.02.D                    1G
========= ============================== ======= =========================

--------------------------------------
10G Single-mode optical fiber
--------------------------------------

========= ============================== ======= =========================
Vendor    Type                           Speed   Notes
========= ============================== ======= =========================
FlexOptix P.1396.10 SMF 1310nm Duplex-LC 10G     Tested module rated for 10km,
                                                 other distances are assumed to function properly
FlexOptix P.B1696.10.DA + P.B1696.10.AD  10G     Simplex-LC. Two complementary modules are needed.
FS        XGS-ONU-25-20NI                10G     XGSPON
Zaram     ZXOS11NPI                      10G     XGSPON
========= ============================== ======= =========================

--------------------------------------
10G Multi-mode optical fiber
--------------------------------------

============= ============================== ======= =========================
Vendor        Type                           Speed   Notes
============= ============================== ======= =========================
Cisco-Finisar SFP-10G-SR                     10G
FS            SFP-10GSR-85                   10G
FS            SFP-10/25GR-85                 10G
IBM-Finisar   FTLX8571D3BCL-IC               10G
Intel         AFBR-709DMZ-IN2                10G
Mellanox      MFM1T01A-SR                    10G
Ubiquiti      UF-MM-10G                      10G
Uptimed       UP-TR-SR-CI 10G                10G
============= ============================== ======= =========================

--------------------------------------
1G Copper RJ45
--------------------------------------

========== ============================== ============= =========================
Vendor     Type                           Speed         Notes
========== ============================== ============= =========================
FS         SFP-GB-GE-T                    10/100/1000Mb
HP (Aruba) Instant On                     1G
MikroTik   S-RJ01                         10/100/1000Mb
StarTech   GLCTST                         1G
Ubiquiti   UF-RJ45-1G                     10/100/1000Mb
========== ============================== ============= =========================

--------------------------------------
10G Copper RJ45
--------------------------------------

========== ============================== ============= =========================
Vendor     Type                           Speed         Notes
========== ============================== ============= =========================
FS         SFP-10G-T                      10G
Uptimed    UP-TR-10G-RJ45-CI              1/2.5/5/10G   Will always link at 10G on axgbe,
                                                        maximum speed is determined by link partner
FlexOptix  T.C96.02.KMF                   1/2.5/5/10G   Will always link at 10G on axgbe,
                                                        maximum speed is determined by link partner
========== ============================== ============= =========================

--------------------------------------
10G Direct-Attach
--------------------------------------

========== ============================== ============= =========================
Vendor     Type                           Speed         Notes
========== ============================== ============= =========================
Aruba      SFP+ DAC                       10G
Cisco      SFP-H10GB-CU1M                 10G
FS         SFPP-PC02                      10G
MikroTik   XS+DA0001                      10G           Rated for 1/10/25G, only links on 10G
Netgear    AXC761                         10G
Startech   DACSFP10G1M                    10G
Ubiquiti   UniFi 1m DAC                   10G
========== ============================== ============= =========================

**ICE**
=====================================================================================================================

--------------------------------------
25G Single-mode optical fiber
--------------------------------------

========= ============================== ======= =========================
Vendor    Type                           Speed   Notes
========= ============================== ======= =========================
FlexOptix P.B1625G.10.ADI                25G     Tested module rated for 10km,
                                                 other distances are assumed to function properly
========= ============================== ======= =========================

--------------------------------------
25G Multi-mode optical fiber
--------------------------------------

========= ============================== ======= =========================
Vendor    Type                           Speed   Notes
========= ============================== ======= =========================
FlexOptix P.8525G.01                     25G
FS        SFP28-25GSR-85                 25G
Uptimed   UP-SFP28-SR-CI                 25G
========= ============================== ======= =========================

--------------------------------------
25G Direct-Attach
--------------------------------------

========= ============================== ======= =========================
Vendor    Type                           Speed   Notes
========= ============================== ======= =========================
FlexOptix P.C3025G.H Passive             25G
FS        SFP-H25G-CU1M                  25G     With Intel compatibility
========= ============================== ======= =========================
