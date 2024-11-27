Helloworld
~~~~~~~~~~

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","helloworld","service","reload",""
    "``POST``","helloworld","service","test",""

.. csv-table:: Service (SettingsController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","helloworld","settings","get",""
    "``POST``","helloworld","settings","set",""

    "``<<uses>>``", "", "", "", "*model* `HelloWorld.xml <https://github.com/opnsense/plugins/blob/master/devel/helloworld/src/opnsense/mvc/app/models/OPNsense/HelloWorld/HelloWorld.xml>`__"
