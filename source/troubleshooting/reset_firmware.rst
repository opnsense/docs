=======================================
Reset firmware configuration
=======================================

In cases where the firmware configuration is corrupt in the `config.xml` file, we can reset that section of our configuration using the following
command:


.. code-block:: sh

    pluginctl -f system.firmware

Which shows the current data stored and asks for removal, choose :code:`Y` here to drop that part and circle back to
the :menuselection:`System --> Firmware` section to store the configuration again.

