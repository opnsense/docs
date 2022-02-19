==============================
Remote debugging the kernel
==============================

FreeBSD supports remote debugging using a serial interface.
Since most virtual solutions support serial interfaces it can be quite convenient to deploy a kernel and start a debug session
on another machine.

The setup assumes two (virtual) machines with a serial (rs232) connection in between.

.. blockdiag::
    :scale: 100%

    diagram init {
        build_vm [label = "Build VM"];
        test_vm [label = "Test VM"];
        build_vm -> test_vm;
    }



------------------------------
Configure and build a kernel
------------------------------

Use our toolchain described in detail `here <https://github.com/opnsense/tools>`__ and add the following options
to your :code:`SMP` file in :code:`/usr/tools/config/[VERSION]/SMP`


.. code-block:: sh

    #nomakeoptions DEBUG
    options        GDB                     # Support remote GDB.
    makeoptions    DEBUG=-g


Next clean and build a kernel

.. code-block:: sh

    make clean-obj,kernel kernel


-------------------------------------
Install the kernel on test vm
-------------------------------------


With the build finished, we should have a kernel package on the build machine available at the following location:

    :code:`/usr/local/opnsense/build/[Version]/[Architecture]/sets/kernel*.txz`


Copy this package to the test vm and install it using our :code:`opnsense-update` command:

.. code-block:: sh

      opnsense-update -ikfr [version] -l /location/from/


Where [version] is the version part of the kernel package, such as :code:`19.1.2`


-------------------------------------------
Configure the test vm
-------------------------------------------

To be able to connect to the test machine using :code:`kgdb`, you need to make sure some settings are set.


Edit :code:`/boot/device.hints` and change or add :code:`hint.uart.0.flags` to the following:

.. code-block:: sh

    hint.uart.0.flags="0xc0"


Also /boot/loader.conf.local should have a baud-rate configured for the serial device:

.. code-block:: sh

    comconsole_speed="115200"



-----------------------
Test your setup
-----------------------

Login to the test machine and force a debug session in gdb, using the following commands:

.. code-block:: sh

      # sysctl debug.kdb.current=gdb
      # sysctl debug.kdb.enter=1
      db> gdb
      Step to enter the remote GDB backend.
      db> c (continue)


Then go to the build machine, make sure gdb is installed (:code:`pkg install gdb`) and go to the directory where
the debug symbols are and start a session, ask a backtrace :code:`bt` and continue normal operation :code:`c`:

.. code-block: sh:

    # cd /usr/obj/usr/src/sys/SMP/
    # kgdb -r /dev/cuau0 ./kernel.debug
    (kgdb) bt
    (kgdb) c
