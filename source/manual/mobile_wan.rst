=================
Mobile Networking
=================

.. image:: images/OPNsense_4G_new.png
   :width: 100%

OPNsense supports 3G and 4G (LTE) cellular modems as failsafe or primary WAN
interface. Both USB and (mini)PCIe cards are supported.


-----------------
Supported Devices
-----------------
While all devices supported by FreeBSD will likely function under OPNsense their
configuration depends on a AT command string that can differ from device to device.
To make thing easier some of these strings are part of a easy selectable profile.

Tested devices by the OPNsense team include:

* **Huawei ME909u-521** (device cuaUx.0)
* **Huawei E220** (device cuaUx.0)
* **Sierra Wireless MC7304** (device cuaUx.2) [as of OPNsense 16.7]

.. Note::

  If you have tested a cellular modem that is not on this list, but does work then
  please report it to the project so we can list it and inform others.


-------------------------
Configure Cellular modems
-------------------------
Setting up and configuring a cellular modem is easy, see: :doc:`/manual/how-tos/cellular`

-------------------------
3G - 4G Cellular Failover
-------------------------
To setup Cellular Failover, just follow these two how-tos:

#. :doc:`/manual/how-tos/cellular`
#. :doc:`/manual/how-tos/multiwan`

.. Note:: Treat the cellular connection the same as a normal WAN connection.
