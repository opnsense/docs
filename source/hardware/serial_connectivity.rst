.. _serial:

====================================
Serial Console connectivity
====================================

The following device families offer a mini-usb connection which can be used for serial communication:

* DEC600 series
* DEC2600 series
* DEC700 series
* DEC2700 series
* DEC800 series
* DEC3800 series

Supplied with the firewall is a mini-usb to usb cable, use this to connect the to your PC (Windows, Linux, Mac)
next start your terminal program (Putty, screen, etc).

The baudrate should be set to :code:`115200,8N1`

.. _legacy_uart:

**Legacy UART vs. UEFI serial**
=====================================================================================================================

Starting from OPNsense 22.1 (22.4 for the business edition), support for legacy serial UART0 communication is dropped, 
since the upgrade to FreeBSD 13-STABLE required a switch to the UEFI serial protocol.
Prior to this, only legacy serial UART0 was possible. Should you connect your Deciso appliance with a serial line 
and get limited output / no output from the point of handover to the OS, it is important your BIOS settings are updated 
to disable legacy UART.

While in the BIOS, go to Setup Utility --> AMD CBS --> FCH Common Options --> UART Configuration Options --> UART 0 Legacy Options.
and make sure this setting is set to **Disabled**.
