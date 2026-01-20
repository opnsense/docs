.. _serial:

====================================
Serial Console connectivity
====================================

The following device families offer a mini-usb connection which can be used for serial communication:

========= ============ =============================
Series     Formfactor   Range
========= ============ =============================
DEC6XX    Desktop      Entry level
DEC7XX    Desktop      Midrange
DEC8XX    Desktop      Enterprise
DEC26XX   Rack         Entry level
DEC27XX   Rack         Midrange
DEC38XX   Rack         Enterprise
DEC40XX   Rack         Enterprise / Datacenter
========= ============ =============================

Supplied with the firewall is a mini-usb to usb cable, use this to connect the to your PC (Windows, Linux, Mac)
next start your terminal program (Putty, screen, etc).

The baudrate should be set to :code:`115200,8N1`, more information about how to use the serial console is available in
our :doc:`serial access guide </manual/how-tos/serial_access>`

.. Note::

    The default configured settings in OPNsense for proper serial connectivity in
    :menuselection:`System->Settings->Administration` are as followed:

    ===================== =========================================
    setting               value
    ===================== =========================================
    Primary Console       Serial Console
    Secondary Console     None
    Serial Speed          115200
    USB-based serial      (unchecked)
    Console menu          (checked)
    ===================== =========================================

.. admonition:: Windows Tip

    On windows a COM port would be assigned after connecting the unit to usb, to find which one (COM1, COM2, .,) to
    use, keep the windows key pressed and hit :code:`R` (Windows+R) and execute the following command :code:`devmgmt.msc`
    to open the device manager.

    In the device manager all available ports are visible under the "Ports (COM & LPT)" section.




.. _legacy_uart:

**Legacy UART vs. UEFI serial**
=====================================================================================================================

Starting from OPNsense 22.1 (22.4 for the business edition) and the change to FreeBSD 13-STABLE, support for EFI
serial has changed, which requires EFI based systems to disable legacy support to prevent confusing the operating system.
Should you connect your Deciso appliance with a serial line and get limited output / no output from the point of
handover to the OS, it is important your BIOS settings are updated to disable legacy UART.

While in the BIOS, go to Setup Utility --> AMD CBS --> FCH Common Options --> UART Configuration Options --> UART 0 Legacy Options.
and make sure this setting is set to **Disabled**.
