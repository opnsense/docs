Firmware
~~~~~~~~
OPNsense has several API calls to get and set the firmware configuration:

.. csv-table::
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","Core","Firmware","poweroff",""
   "``POST``","Core","Firmware","reboot",""
   "``GET``","Core","Firmware","running",""
   "``GET``","Core","Firmware","getFirmwareConfig",""
   "``GET``","Core","Firmware","getFirmwareOptions",""
   "``POST``","Core","Firmware","setFirmwareConfig",""
   "``GET``","Core","Firmware","info",""
   "``GET``","Core","Firmware","status",""
   "``POST``","Core","Firmware","audit",""
   "``POST``","Core","Firmware","upgrade",""
   "``GET``","Core","Firmware","upgradestatus",""
   "``POST``","Core","Firmware","changelog","$version"

Examples:

.. code-block:: sh

    curl -k -u "$key":"$secret" https://opnsense.local/api/core/firmware/getfirmwareconfig -v

.. code-block:: sh

    curl -k -u "$key":"$secret" https://opnsense.local/api/core/firmware/status -v

.. code-block:: sh

    curl -d '' -k -u "$key":"$secret" https://opnsense.local/api/core/firmware/changelog/18.1 -v


Packages
........
You can manage the packages and plugins in OPNsense, using these API calls:

.. csv-table::
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","Core","Firmware","install","$pkg_name"
   "``POST``","Core","Firmware","reinstall","$pkg_name"
   "``POST``","Core","Firmware","remove","$pkg_name"
   "``POST``","Core","Firmware","lock","$pkg_name"
   "``POST``","Core","Firmware","unlock","$pkg_name"
   "``POST``","Core","Firmware","details","$pkg_name"
   "``POST``","Core","Firmware","license","$pkg_name"

Examples:

.. code-block:: sh

    curl -d '' -k -u "$key":"$secret" https://opnsense.local/api/core/firmware/lock/os-xen -v

.. code-block:: sh

    curl -d '' -k -u "$key":"$secret" https://opnsense.local/api/core/firmware/license/acme.sh -v
