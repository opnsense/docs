shadowsocks
~~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","shadowsocks","general","get",""
   "``POST``","shadowsocks","general","set",""
   "``GET``","shadowsocks","local","get",""
   "``POST``","shadowsocks","local","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","shadowsocks","service","reconfigure",""
   "``POST``","shadowsocks","service","restart",""
   "``POST``","shadowsocks","service","start",""
   "``GET``","shadowsocks","service","status",""
   "``POST``","shadowsocks","service","stop",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","shadowsocks","localservice","reconfigure",""
   "","shadowsocks","localservice","status",""
