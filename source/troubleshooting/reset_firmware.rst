=======================================
Reset firmware configuration
=======================================

In cases where the firmware configuration is corrupt in the :code:`config.xml` file, we can reset that section of our configuration using the following
command (executed on a console or via SSH):


.. code-block:: sh

    pluginctl -f system.firmware

Which shows the current data stored and asks for removal, choose :code:`Y` here to drop that part and circle back to
the :menuselection:`System --> Firmware` section to store the configuration again.


.. Note::

    If our factory left a cache file which keeps a "factory-" plugin visible at all times, you can safely remove the reference using the following command:

    :code:`rm /usr/local/opnsense/version/factory-*`

