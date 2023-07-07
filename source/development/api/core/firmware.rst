Firmware
~~~~~~~~
OPNsense has several API calls to get and set the firmware configuration:



.. csv-table::
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","core","firmware","audit",""
    "``POST``","core","firmware","changelog","$version"
    "``POST``","core","firmware","check",""
    "``POST``","core","firmware","connection",""
    "``GET``","core","firmware","get",""
    "``GET``","core","firmware","getOptions",""
    "``POST``","core","firmware","health",""
    "``GET``","core","firmware","info",""
    "``POST``","core","firmware","log","$clear"
    "``POST``","core","firmware","poweroff",""
    "``POST``","core","firmware","reboot",""
    "``POST``","core","firmware","resyncPlugins",""
    "``GET``","core","firmware","running",""
    "``POST``","core","firmware","set",""
    "``POST``","core","firmware","set",""
    "``POST``","core","firmware","status",""
    "``POST``","core","firmware","syncPlugins",""
    "``POST``","core","firmware","update",""
    "``POST``","core","firmware","upgrade",""
    "``GET``","core","firmware","upgradestatus",""

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

    "``POST``","core","firmware","details","$package"
    "``POST``","core","firmware","reinstall","$pkg_name"
    "``POST``","core","firmware","remove","$pkg_name"
    "``POST``","core","firmware","unlock","$pkg_name"
    "``POST``","core","firmware","install","$pkg_name"
    "``POST``","core","firmware","license","$package"
    "``POST``","core","firmware","lock","$pkg_name"


Examples:

.. code-block:: sh

    curl -d '' -k -u "$key":"$secret" https://opnsense.local/api/core/firmware/lock/os-xen -v

.. code-block:: sh

    curl -d '' -k -u "$key":"$secret" https://opnsense.local/api/core/firmware/license/acme.sh -v
