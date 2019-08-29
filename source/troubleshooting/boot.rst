====================================
Boot
====================================

-----------------------------
hangs at "booting..."
-----------------------------

On some serial connected devices the console settings are different, in which case you would
not be able to start the installer.

If you can reach the loader prompt, you could try to change some kernel parameters before booting.



::

    set hint.uart.0.flags=0x0
    set hint.uart.1.flags=0x10
    set comconsole_speed=115200
    set comconsole_port=0x2F8
    set console=comconsole
    boot

.. Note::

    To enter the loader prompt press :code:`3` when the OPNsense boot menu is visible


After installation, you could persist these settings in :menuselection:`System --> Settings --> Tunables`
