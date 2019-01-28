=============
Serial Access
=============

Besides the web frontend, SSH and a locally connected monitor (if your device supports it), OPNsense can also be
controlled via serial. Accessing OPNsense via serial is similar to accessing via SSH, but unlike SSH, the system can
be accessed at any time, even when OPNsense is not running. This makes it especially useful for installing OPNsense,
as well as for emergency troubleshooting when you accidentally cut off internet access.

--------------------------------
Connecting to the serial console
--------------------------------

On Unix-like systems, you can connect to the serial console using the ``screen`` program, with a baud rate of 115200.
The device name can differ per system and per serial device. For example, on the Deciso DEC630, accessed from macOS,
the device is named ``/dev/tty.usbmodem1112421``. Entering the serial console thus involves opening a terminal and
executing the following instruction:

::

  screen /dev/tty.usbmodem1112421 115200

If OPNsense is running, you will now be asked for your username and password. The credentials are the same as those
used for SSH.

A thing to note is that, unlike SSH, you will not be able to scroll (but you can pipe the output through a pager like
``more`` or ``less``), and the screen won't always auto-update. If you connect and see no output, try pressing `Enter`
first before checking the other (more complex) possibilities.
