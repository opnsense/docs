=============
API Reference
=============

Introduction
------------

The OPNsense API calls are structured in the form: 

.. code-block:: sh

     https://opnsense.local/api/<module>/<controller>/<command>/[<param1>/[<param2>/...]]

There are two HTTP verbs used in the OPNsense API:

    - ``GET``  Retrieves data from OPNsense
    - ``POST``  Creates new data, updates existing data or executes an action

The body of the HTTP POST request and response is an 'application/json' object.

The $key and $secret parameters are used to pass the API credentials using curl. You need to set these parameters with your own API credentials before using them in the examples:

.. code-block:: sh

    key=w86XNZob/8Oq8aC5r0kbNarNtdpoQU781fyoeaOBQsBwkXUt
    secret=XeD26XVrJ5ilAc/EmglCRC+0j2e57tRsjHwFepOseySWLM53pJASeTA3

Core API
--------

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

    curl -k -u "$key":"$secret" https://10.1.0.205/api/core/firmware/getfirmwareconfig -v

.. code-block:: sh

    curl -k -u "$key":"$secret" https://opnsense.local/api/core/firmware/status -v

.. code-block:: sh

    curl -d '' -k -u "$key":"$secret" https://10.1.0.205/api/core/firmware/changelog/18.1 -v


Menu
~~~~

.. csv-table::
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","core","menu","search",""

Packages
~~~~~~~~
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


----------------------

CaptivePortal
~~~~~~~~~~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","captiveportal","service","reconfigure",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","captiveportal","service","addtemplate",""
   "``POST``","captiveportal","service","deltemplate","$uuid"
   "``GET``","captiveportal","service","gettemplate","$fileid"
   "``GET``","captiveportal","service","searchtemplates",""
   "``GET``","captiveportal","service","searchtemplates","$uuid"
   "``POST``","captiveportal","service","settemplate","$uuid"
   "``POST``","captiveportal","settings","addzone",""
   "``POST``","captiveportal","settings","delzone","$uuid"
   "``GET``","captiveportal","settings","getzone","$uuid"
   "``GET``","captiveportal","settings","searchzones",""
   "``POST``","captiveportal","settings","setzone","$uuid"
   "``POST``","captiveportal","settings","togglezone","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","captiveportal","service","saveTemplate",""
   "","captiveportal","session","disconnect",""
   "","captiveportal","session","list",""
   "","captiveportal","session","zones",""
   "","captiveportal","voucher","dropExpiredVouchers",""
   "","captiveportal","voucher","dropVoucherGroup",""
   "","captiveportal","voucher","expireVoucher",""
   "","captiveportal","voucher","generateVouchers",""
   "","captiveportal","voucher","listProviders",""
   "","captiveportal","voucher","listVoucherGroups",""
   "","captiveportal","voucher","listVouchers",""

----------------------

Cron
~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","cron","service","reconfigure",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","cron","settings","addjob",""
   "``POST``","cron","settings","deljob","$uuid"
   "``GET``","cron","settings","getjob","$uuid"
   "``GET``","cron","settings","searchjobs",""
   "``POST``","cron","settings","setjob","$uuid"
   "``POST``","cron","settings","togglejob","$uuid/$enabled"

----------------------

IDS
~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","ids","settings","get",""
   "``POST``","ids","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","ids","service","reconfigure",""
   "``POST``","ids","service","restart",""
   "``POST``","ids","service","start",""
   "``GET``","ids","service","status",""
   "``POST``","ids","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","ids","settings","adduserrule",""
   "``POST``","ids","settings","deluserrule","$uuid"
   "``GET``","ids","settings","getruleset","$uuid"
   "``GET``","ids","settings","getuserrule","$uuid"
   "``GET``","ids","settings","searchinstalledrules",""
   "``GET``","ids","settings","searchuserrule",""
   "``POST``","ids","settings","setrule","$uuid"
   "``POST``","ids","settings","setruleset","$uuid"
   "``POST``","ids","settings","setuserrule","$uuid"
   "``POST``","ids","settings","togglerule","$uuid/$enabled"
   "``POST``","ids","settings","toggleruleset","$uuid/$enabled"
   "``POST``","ids","settings","toggleuserrule","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","ids","service","dropAlertLog",""
   "","ids","service","getAlertInfo",""
   "","ids","service","getAlertLogs",""
   "","ids","service","queryAlerts",""
   "","ids","service","reloadRules",""
   "","ids","service","updateRules",""
   "","ids","settings","getRuleInfo",""
   "","ids","settings","getRulesetproperties",""
   "","ids","settings","listRuleClasstypes",""
   "","ids","settings","listRulesets",""
   "","ids","settings","setRulesetproperties",""

----------------------

Proxy
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","proxy","settings","get",""
   "``POST``","proxy","settings","set",""
   "``GET``","proxy","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","proxy","service","reconfigure",""
   "``POST``","proxy","service","restart",""
   "``POST``","proxy","service","start",""
   "``GET``","proxy","service","status",""
   "``POST``","proxy","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","proxy","settings","addremoteblacklist",""
   "``POST``","proxy","settings","delremoteblacklist","$uuid"
   "``GET``","proxy","settings","getremoteblacklist","$uuid"
   "``GET``","proxy","settings","searchremoteblacklists",""
   "``POST``","proxy","settings","setremoteblacklist","$uuid"
   "``POST``","proxy","settings","toggleremoteblacklist","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","proxy","service","downloadacls",""
   "","proxy","service","fetchacls",""
   "","proxy","settings","fetchRBCron",""

----------------------

Routes
~~~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","routes","routes","reconfigure",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","routes","routes","addroute",""
   "``POST``","routes","routes","delroute","$uuid"
   "``GET``","routes","routes","getroute","$uuid"
   "``GET``","routes","routes","searchroute",""
   "``POST``","routes","routes","setroute","$uuid"
   "``POST``","routes","routes","toggleroute","$uuid/$disabled"

----------------------

TrafficShaper
~~~~~~~~~~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","trafficshaper","service","reconfigure",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","trafficshaper","settings","addpipe",""
   "``POST``","trafficshaper","settings","addqueue",""
   "``POST``","trafficshaper","settings","addrule",""
   "``POST``","trafficshaper","settings","delpipe","$uuid"
   "``POST``","trafficshaper","settings","delqueue","$uuid"
   "``POST``","trafficshaper","settings","delrule","$uuid"
   "``GET``","trafficshaper","settings","getpipe","$uuid"
   "``GET``","trafficshaper","settings","getqueue","$uuid"
   "``GET``","trafficshaper","settings","getrule","$uuid"
   "``GET``","trafficshaper","settings","searchpipes",""
   "``GET``","trafficshaper","settings","searchqueues",""
   "``GET``","trafficshaper","settings","searchrules",""
   "``POST``","trafficshaper","settings","setpipe","$uuid"
   "``POST``","trafficshaper","settings","setqueue","$uuid"
   "``POST``","trafficshaper","settings","setrule","$uuid"
   "``POST``","trafficshaper","settings","togglepipe","$uuid/$enabled"
   "``POST``","trafficshaper","settings","togglequeue","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","trafficshaper","service","flushreload",""

----------------------

Diagnostics
~~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","diagnostics","netflow","getconfig",""
   "``GET``","diagnostics","netflow","setconfig",""
   "``POST``","diagnostics","netflow","setconfig",""

.. csv-table:: Diagnostics
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","diagnostics","activity","getActivity",""
   "","diagnostics","dns","reverse",""
   "","diagnostics","firewall","log",""
   "","diagnostics","interface","flushArp",""
   "","diagnostics","interface","getArp",""
   "","diagnostics","interface","getInterfaceNames",""
   "","diagnostics","interface","getNdp",""
   "","diagnostics","interface","getRoutes",""
   "","diagnostics","netflow","cacheStats",""
   "","diagnostics","netflow","isEnabled",""
   "","diagnostics","netflow","reconfigure",""
   "","diagnostics","networkinsight","export",""
   "","diagnostics","networkinsight","getInterfaces",""
   "","diagnostics","networkinsight","getMetadata",""
   "","diagnostics","networkinsight","getProtocols",""
   "","diagnostics","networkinsight","getServices",""
   "","diagnostics","networkinsight","timeserie","FlowInterfaceTotals/bps/"
   "","diagnostics","networkinsight","top","FlowDstPortTotals/"
   "","diagnostics","systemhealth","getInterfaces",""
   "","diagnostics","systemhealth","getRRDlist",""
   "","diagnostics","systemhealth","getSystemHealth",""

Plugin API
----------
acmeclient
~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","acmeclient","settings","get",""
   "``POST``","acmeclient","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","acmeclient","service","configtest",""
   "``POST``","acmeclient","service","reconfigure",""
   "``POST``","acmeclient","service","restart",""
   "``POST``","acmeclient","service","start",""
   "``GET``","acmeclient","service","status",""
   "``POST``","acmeclient","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","acmeclient","accounts","add",""
   "``POST``","acmeclient","accounts","del","$uuid"
   "``GET``","acmeclient","accounts","get","$uuid"
   "``GET``","acmeclient","accounts","search",""
   "``POST``","acmeclient","accounts","set","$uuid"
   "``POST``","acmeclient","accounts","toggle","$uuid/$enabled"
   "``POST``","acmeclient","actions","add",""
   "``POST``","acmeclient","actions","del","$uuid"
   "``GET``","acmeclient","actions","get","$uuid"
   "``GET``","acmeclient","actions","search",""
   "``POST``","acmeclient","actions","set","$uuid"
   "``POST``","acmeclient","actions","toggle","$uuid/$enabled"
   "``POST``","acmeclient","certificates","add",""
   "``POST``","acmeclient","certificates","del","$uuid"
   "``GET``","acmeclient","certificates","get","$uuid"
   "``GET``","acmeclient","certificates","search",""
   "``POST``","acmeclient","certificates","set","$uuid"
   "``POST``","acmeclient","certificates","toggle","$uuid/$enabled"
   "``POST``","acmeclient","validations","add",""
   "``POST``","acmeclient","validations","del","$uuid"
   "``GET``","acmeclient","validations","get","$uuid"
   "``GET``","acmeclient","validations","search",""
   "``POST``","acmeclient","validations","set","$uuid"
   "``POST``","acmeclient","validations","toggle","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","acmeclient","certificates","revoke",""
   "","acmeclient","certificates","sign",""
   "","acmeclient","service","signallcerts",""
   "","acmeclient","settings","fetchCronIntegration",""
   "","acmeclient","settings","fetchHAProxyIntegration",""

----------------------

arpscanner
~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","arpscanner","settings","get",""
   "``POST``","arpscanner","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","arpscanner","service","check",""
   "``POST``","arpscanner","service","reload",""
   "``POST``","arpscanner","service","start",""
   "``GET``","arpscanner","service","status",""
   "``POST``","arpscanner","service","stop",""

----------------------

cicap
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","cicap","antivirus","get",""
   "``POST``","cicap","antivirus","set",""
   "``GET``","cicap","general","get",""
   "``POST``","cicap","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","cicap","service","reconfigure",""
   "``POST``","cicap","service","restart",""
   "``POST``","cicap","service","start",""
   "``GET``","cicap","service","status",""
   "``POST``","cicap","service","stop",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","cicap","service","checkclamav",""

----------------------

clamav
~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","clamav","general","get",""
   "``POST``","clamav","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","clamav","service","reconfigure",""
   "``POST``","clamav","service","restart",""
   "``POST``","clamav","service","start",""
   "``GET``","clamav","service","status",""
   "``POST``","clamav","service","stop",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","clamav","service","freshclam",""
   "","clamav","service","version",""

----------------------

collectd
~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","collectd","general","get",""
   "``POST``","collectd","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","collectd","service","reconfigure",""
   "``POST``","collectd","service","restart",""
   "``POST``","collectd","service","start",""
   "``GET``","collectd","service","status",""
   "``POST``","collectd","service","stop",""

----------------------

freeradius
~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","freeradius","eap","get",""
   "``POST``","freeradius","eap","set",""
   "``GET``","freeradius","general","get",""
   "``POST``","freeradius","general","set",""
   "``GET``","freeradius","ldap","get",""
   "``POST``","freeradius","ldap","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","freeradius","service","reconfigure",""
   "``POST``","freeradius","service","restart",""
   "``POST``","freeradius","service","start",""
   "``GET``","freeradius","service","status",""
   "``POST``","freeradius","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","freeradius","client","addclient",""
   "``POST``","freeradius","client","delclient","$uuid"
   "``GET``","freeradius","client","getclient","$uuid"
   "``GET``","freeradius","client","searchclient",""
   "``POST``","freeradius","client","setclient","$uuid"
   "``POST``","freeradius","client","toggleclient","$uuid"
   "``POST``","freeradius","user","adduser",""
   "``POST``","freeradius","user","deluser","$uuid"
   "``GET``","freeradius","user","getuser","$uuid"
   "``GET``","freeradius","user","searchuser",""
   "``POST``","freeradius","user","setuser","$uuid"
   "``POST``","freeradius","user","toggleuser","$uuid"

----------------------

ftpproxy
~~~~~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","ftpproxy","service","reload",""
   "``POST``","ftpproxy","service","restart",""
   "``POST``","ftpproxy","service","start",""
   "``GET``","ftpproxy","service","status",""
   "``POST``","ftpproxy","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","ftpproxy","settings","addproxy",""
   "``POST``","ftpproxy","settings","delproxy","$uuid"
   "``GET``","ftpproxy","settings","getproxy","$uuid"
   "``GET``","ftpproxy","settings","searchproxy",""
   "``POST``","ftpproxy","settings","setproxy","$uuid"
   "``POST``","ftpproxy","settings","toggleproxy","$uuid"

----------------------

haproxy
~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","haproxy","settings","get",""
   "``POST``","haproxy","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","haproxy","service","configtest",""
   "``POST``","haproxy","service","reconfigure",""
   "``POST``","haproxy","service","restart",""
   "``POST``","haproxy","service","start",""
   "``GET``","haproxy","service","status",""
   "``POST``","haproxy","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","haproxy","settings","addacl",""
   "``POST``","haproxy","settings","addaction",""
   "``POST``","haproxy","settings","addbackend",""
   "``POST``","haproxy","settings","adderrorfile",""
   "``POST``","haproxy","settings","addfrontend",""
   "``POST``","haproxy","settings","addhealthcheck",""
   "``POST``","haproxy","settings","addlua",""
   "``POST``","haproxy","settings","addserver",""
   "``POST``","haproxy","settings","delacl","$uuid"
   "``POST``","haproxy","settings","delaction","$uuid"
   "``POST``","haproxy","settings","delbackend","$uuid"
   "``POST``","haproxy","settings","delerrorfile","$uuid"
   "``POST``","haproxy","settings","delfrontend","$uuid"
   "``POST``","haproxy","settings","delhealthcheck","$uuid"
   "``POST``","haproxy","settings","dellua","$uuid"
   "``POST``","haproxy","settings","delserver","$uuid"
   "``GET``","haproxy","settings","getacl","$uuid"
   "``GET``","haproxy","settings","getaction","$uuid"
   "``GET``","haproxy","settings","getbackend","$uuid"
   "``GET``","haproxy","settings","geterrorfile","$uuid"
   "``GET``","haproxy","settings","getfrontend","$uuid"
   "``GET``","haproxy","settings","gethealthcheck","$uuid"
   "``GET``","haproxy","settings","getlua","$uuid"
   "``GET``","haproxy","settings","getserver","$uuid"
   "``GET``","haproxy","settings","searchacls",""
   "``GET``","haproxy","settings","searchactions",""
   "``GET``","haproxy","settings","searchbackends",""
   "``GET``","haproxy","settings","searcherrorfiles",""
   "``GET``","haproxy","settings","searchfrontends",""
   "``GET``","haproxy","settings","searchhealthchecks",""
   "``GET``","haproxy","settings","searchluas",""
   "``GET``","haproxy","settings","searchservers",""
   "``POST``","haproxy","settings","setacl","$uuid"
   "``POST``","haproxy","settings","setaction","$uuid"
   "``POST``","haproxy","settings","setbackend","$uuid"
   "``POST``","haproxy","settings","seterrorfile","$uuid"
   "``POST``","haproxy","settings","setfrontend","$uuid"
   "``POST``","haproxy","settings","sethealthcheck","$uuid"
   "``POST``","haproxy","settings","setlua","$uuid"
   "``POST``","haproxy","settings","setserver","$uuid"
   "``POST``","haproxy","settings","togglebackend","$uuid/$enabled"
   "``POST``","haproxy","settings","togglefrontend","$uuid/$enabled"
   "``POST``","haproxy","settings","togglelua","$uuid/$enabled"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","haproxy","statistics","counters",""
   "","haproxy","statistics","info",""
   "","haproxy","statistics","tables",""

----------------------

helloworld
~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","helloworld","settings","get",""
   "``POST``","helloworld","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","helloworld","service","reload",""
   "``POST``","helloworld","service","test",""

----------------------

iperf
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","iperf","instance","get",""
   "``POST``","iperf","instance","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","iperf","service","reconfigure",""
   "``POST``","iperf","service","restart",""
   "``POST``","iperf","service","start",""
   "``GET``","iperf","service","status",""
   "``POST``","iperf","service","stop",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","iperf","instance","query",""

----------------------

lldpd
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","lldpd","general","get",""
   "``POST``","lldpd","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","lldpd","service","reconfigure",""
   "``POST``","lldpd","service","restart",""
   "``POST``","lldpd","service","start",""
   "``GET``","lldpd","service","status",""
   "``POST``","lldpd","service","stop",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","lldpd","service","neighbor",""

----------------------

mdnsrepeater
~~~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","mdnsrepeater","settings","get",""
   "``POST``","mdnsrepeater","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","mdnsrepeater","service","restart",""
   "``POST``","mdnsrepeater","service","start",""
   "``GET``","mdnsrepeater","service","status",""
   "``POST``","mdnsrepeater","service","stop",""

----------------------

monit
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","monit","settings","get","general"
   "``POST``","monit","settings","set","general"

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","monit","service","configtest",""
   "``POST``","monit","service","reconfigure",""
   "``POST``","monit","service","restart",""
   "``POST``","monit","service","start",""
   "``GET``","monit","service","status",""
   "``POST``","monit","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","monit","settings","add","test"
   "``POST``","monit","settings","add","service"
   "``POST``","monit","settings","add","alert"
   "``POST``","monit","settings","del","test/$uuid"
   "``POST``","monit","settings","del","service/$uuid"
   "``POST``","monit","settings","del","alert/$uuid"
   "``GET``","monit","settings","get","test/$uuid"
   "``GET``","monit","settings","get","service/$uuid"
   "``GET``","monit","settings","get","alert/$uuid"
   "``GET``","monit","settings","search","test"
   "``GET``","monit","settings","search","alert"
   "``GET``","monit","settings","search","service"
   "``POST``","monit","settings","set","service/$uuid"
   "``POST``","monit","settings","set","test/$uuid"
   "``POST``","monit","settings","set","alert/$uuid"
   "``POST``","monit","settings","toggle","alert/$uuid"
   "``POST``","monit","settings","toggle","service/$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","monit","settings","notification",""
   "","monit","status","get","html"

----------------------

nodeexporter
~~~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","nodeexporter","general","get",""
   "``POST``","nodeexporter","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","nodeexporter","service","reconfigure",""
   "``POST``","nodeexporter","service","restart",""
   "``POST``","nodeexporter","service","start",""
   "``GET``","nodeexporter","service","status",""
   "``POST``","nodeexporter","service","stop",""

----------------------

nut
~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","nut","settings","get",""
   "``POST``","nut","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","nut","service","reconfigure",""

----------------------

openconnect
~~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","openconnect","general","get",""
   "``POST``","openconnect","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","openconnect","service","reconfigure",""
   "``POST``","openconnect","service","restart",""
   "``POST``","openconnect","service","start",""
   "``GET``","openconnect","service","status",""
   "``POST``","openconnect","service","stop",""

----------------------

postfix
~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","postfix","antispam","get",""
   "``POST``","postfix","antispam","set",""
   "``GET``","postfix","general","get",""
   "``POST``","postfix","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","postfix","service","reconfigure",""
   "``POST``","postfix","service","restart",""
   "``POST``","postfix","service","start",""
   "``GET``","postfix","service","status",""
   "``POST``","postfix","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","postfix","domain","adddomain",""
   "``POST``","postfix","domain","deldomain","$uuid"
   "``GET``","postfix","domain","getdomain","$uuid"
   "``GET``","postfix","domain","searchdomain",""
   "``POST``","postfix","domain","setdomain","$uuid"
   "``POST``","postfix","domain","toggledomain","$uuid"
   "``POST``","postfix","recipient","addrecipient",""
   "``POST``","postfix","recipient","delrecipient","$uuid"
   "``GET``","postfix","recipient","getrecipient","$uuid"
   "``GET``","postfix","recipient","searchrecipient",""
   "``POST``","postfix","recipient","setrecipient","$uuid"
   "``POST``","postfix","recipient","togglerecipient","$uuid"
   "``POST``","postfix","sender","addsender",""
   "``POST``","postfix","sender","delsender","$uuid"
   "``GET``","postfix","sender","getsender","$uuid"
   "``GET``","postfix","sender","searchsender",""
   "``POST``","postfix","sender","setsender","$uuid"
   "``POST``","postfix","sender","togglesender","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","postfix","service","checkrspamd",""

----------------------

proxysso
~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","proxysso","settings","get",""
   "``POST``","proxysso","settings","set",""

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","proxysso","service","createkeytab",""
   "","proxysso","service","deletekeytab",""
   "","proxysso","service","getchecklist",""
   "","proxysso","service","showkeytab",""
   "","proxysso","service","testkerblogin",""

----------------------

proxyuseracl
~~~~~~~~~~~~

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","proxyuseracl","settings","addacl",""
   "``POST``","proxyuseracl","settings","delacl","$uuid"
   "``GET``","proxyuseracl","settings","getacl","$uuid"
   "``GET``","proxyuseracl","settings","searchacl",""
   "``POST``","proxyuseracl","settings","setacl","$uuid"
   "``POST``","proxyuseracl","settings","toggleacl","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","proxyuseracl","settings","updownACL",""

----------------------

quagga
~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","quagga","bgp","get",""
   "``POST``","quagga","bgp","set",""
   "``GET``","quagga","general","get",""
   "``POST``","quagga","general","set",""
   "``GET``","quagga","ospf6settings","get",""
   "``POST``","quagga","ospf6settings","set",""
   "``GET``","quagga","ospfsettings","get",""
   "``POST``","quagga","ospfsettings","set",""
   "``GET``","quagga","rip","get",""
   "``POST``","quagga","rip","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","quagga","service","reconfigure",""
   "``POST``","quagga","service","restart",""
   "``POST``","quagga","service","start",""
   "``GET``","quagga","service","status",""
   "``POST``","quagga","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","quagga","bgp","addaspath",""
   "``POST``","quagga","bgp","addneighbor",""
   "``POST``","quagga","bgp","addprefixlist",""
   "``POST``","quagga","bgp","addroutemap",""
   "``POST``","quagga","bgp","delaspath","$uuid"
   "``POST``","quagga","bgp","delneighbor","$uuid"
   "``POST``","quagga","bgp","delprefixlist","$uuid"
   "``POST``","quagga","bgp","delroutemap","$uuid"
   "``GET``","quagga","bgp","getaspath","$uuid"
   "``GET``","quagga","bgp","getneighbor","$uuid"
   "``GET``","quagga","bgp","getprefixlist","$uuid"
   "``GET``","quagga","bgp","getroutemap","$uuid"
   "``GET``","quagga","bgp","searchaspath",""
   "``GET``","quagga","bgp","searchneighbor",""
   "``GET``","quagga","bgp","searchprefixlist",""
   "``GET``","quagga","bgp","searchroutemap",""
   "``POST``","quagga","bgp","setaspath","$uuid"
   "``POST``","quagga","bgp","setneighbor","$uuid"
   "``POST``","quagga","bgp","setprefixlist","$uuid"
   "``POST``","quagga","bgp","setroutemap","$uuid"
   "``POST``","quagga","bgp","toggleaspath","$uuid"
   "``POST``","quagga","bgp","toggleneighbor","$uuid"
   "``POST``","quagga","bgp","toggleprefixlist","$uuid"
   "``POST``","quagga","bgp","toggleroutemap","$uuid"
   "``POST``","quagga","ospf6settings","addinterface",""
   "``POST``","quagga","ospf6settings","delinterface","$uuid"
   "``GET``","quagga","ospf6settings","getinterface","$uuid"
   "``GET``","quagga","ospf6settings","searchinterface",""
   "``POST``","quagga","ospf6settings","setinterface","$uuid"
   "``POST``","quagga","ospf6settings","toggleinterface","$uuid"
   "``POST``","quagga","ospfsettings","addinterface",""
   "``POST``","quagga","ospfsettings","addnetwork",""
   "``POST``","quagga","ospfsettings","addprefixlist",""
   "``POST``","quagga","ospfsettings","delinterface","$uuid"
   "``POST``","quagga","ospfsettings","delnetwork","$uuid"
   "``POST``","quagga","ospfsettings","delprefixlist","$uuid"
   "``GET``","quagga","ospfsettings","getinterface","$uuid"
   "``GET``","quagga","ospfsettings","getnetwork","$uuid"
   "``GET``","quagga","ospfsettings","getprefixlist","$uuid"
   "``GET``","quagga","ospfsettings","searchinterface",""
   "``GET``","quagga","ospfsettings","searchnetwork",""
   "``GET``","quagga","ospfsettings","searchprefixlist",""
   "``POST``","quagga","ospfsettings","setinterface","$uuid"
   "``POST``","quagga","ospfsettings","setnetwork","$uuid"
   "``POST``","quagga","ospfsettings","setprefixlist","$uuid"
   "``POST``","quagga","ospfsettings","toggleinterface","$uuid"
   "``POST``","quagga","ospfsettings","togglenetwork","$uuid"
   "``POST``","quagga","ospfsettings","toggleprefixlist","$uuid"

.. csv-table:: Diagnostics
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","quagga","diagnostics","generalroutes",""
   "","quagga","diagnostics","generalroutes6",""
   "","quagga","diagnostics","log",""
   "","quagga","diagnostics","ospfdatabase",""
   "","quagga","diagnostics","ospfinterface",""
   "","quagga","diagnostics","ospfneighbor",""
   "","quagga","diagnostics","ospfoverview",""
   "","quagga","diagnostics","ospfroute",""
   "","quagga","diagnostics","ospfv3database",""
   "","quagga","diagnostics","ospfv3interface",""
   "","quagga","diagnostics","ospfv3neighbor",""
   "","quagga","diagnostics","ospfv3overview",""
   "","quagga","diagnostics","ospfv3route",""
   "","quagga","diagnostics","showipbgp",""
   "","quagga","diagnostics","showipbgpsummary",""
   "","quagga","diagnostics","showrunningconfig",""

----------------------

redis
~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","redis","settings","get",""
   "``GET``","redis","settings","set",""
   "``POST``","redis","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","redis","service","reconfigure",""
   "``POST``","redis","service","restart",""
   "``POST``","redis","service","start",""
   "``GET``","redis","service","status",""
   "``POST``","redis","service","stop",""

----------------------

relayd
~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","relayd","settings","get","general"

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","relayd","service","configtest",""
   "``POST``","relayd","service","reconfigure",""
   "``POST``","relayd","service","restart",""
   "``POST``","relayd","service","start",""
   "``GET``","relayd","service","status",""
   "``POST``","relayd","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","relayd","settings","del","tablecheck/$uuid"
   "``POST``","relayd","settings","del","protocol/$uuid"
   "``POST``","relayd","settings","del","virtualserver/$uuid"
   "``POST``","relayd","settings","del","table/$uuid"
   "``POST``","relayd","settings","del","host/$uuid"
   "``GET``","relayd","settings","get","host/$uuid"
   "``GET``","relayd","settings","get","tablecheck/$uuid"
   "``GET``","relayd","settings","get","virtualserver/$uuid"
   "``GET``","relayd","settings","get","table/$uuid"
   "``GET``","relayd","settings","get","protocol/$uuid"
   "``GET``","relayd","settings","search","host/"
   "``GET``","relayd","settings","search","virtualserver/"
   "``GET``","relayd","settings","search","protocol/"
   "``GET``","relayd","settings","search","tablecheck/"
   "``GET``","relayd","settings","search","table/"
   "``POST``","relayd","settings","set","virtualserver/$uuid"
   "``POST``","relayd","settings","set","host/$uuid"
   "``POST``","relayd","settings","set","table/$uuid"
   "``POST``","relayd","settings","set","protocol/$uuid"
   "``POST``","relayd","settings","set","tablecheck/$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","relayd","status","sum",""
   "","relayd","status","toggle",""

----------------------

rspamd
~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","rspamd","settings","get",""
   "``POST``","rspamd","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","rspamd","service","reconfigure",""
   "``POST``","rspamd","service","restart",""
   "``POST``","rspamd","service","start",""
   "``GET``","rspamd","service","status",""
   "``POST``","rspamd","service","stop",""

----------------------

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

----------------------

siproxd
~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","siproxd","general","get",""
   "``POST``","siproxd","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","siproxd","service","reconfigure",""
   "``POST``","siproxd","service","restart",""
   "``POST``","siproxd","service","start",""
   "``GET``","siproxd","service","status",""
   "``POST``","siproxd","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","siproxd","domain","adddomain",""
   "``POST``","siproxd","domain","deldomain","$uuid"
   "``GET``","siproxd","domain","getdomain","$uuid"
   "``GET``","siproxd","domain","searchdomain",""
   "``POST``","siproxd","domain","setdomain","$uuid"
   "``POST``","siproxd","domain","toggledomain","$uuid"
   "``POST``","siproxd","user","adduser",""
   "``POST``","siproxd","user","deluser","$uuid"
   "``GET``","siproxd","user","getuser","$uuid"
   "``GET``","siproxd","user","searchuser",""
   "``POST``","siproxd","user","setuser","$uuid"
   "``POST``","siproxd","user","toggleuser","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","siproxd","domain","set",""
   "","siproxd","service","showregistrations",""
   "","siproxd","user","set",""

----------------------

telegraf
~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","telegraf","general","get",""
   "``POST``","telegraf","general","set",""
   "``GET``","telegraf","input","get",""
   "``POST``","telegraf","input","set",""
   "``GET``","telegraf","output","get",""
   "``POST``","telegraf","output","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","telegraf","service","reconfigure",""
   "``POST``","telegraf","service","restart",""
   "``POST``","telegraf","service","start",""
   "``GET``","telegraf","service","status",""
   "``POST``","telegraf","service","stop",""

----------------------

tinc
~~~~

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","tinc","service","reconfigure",""
   "``POST``","tinc","service","restart",""
   "``GET``","tinc","service","start",""
   "``POST``","tinc","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","tinc","settings","delhost","$uuid"
   "``POST``","tinc","settings","delnetwork","$uuid"
   "``GET``","tinc","settings","gethost","$uuid"
   "``GET``","tinc","settings","getnetwork","$uuid"
   "``GET``","tinc","settings","searchhost",""
   "``GET``","tinc","settings","searchnetwork",""
   "``POST``","tinc","settings","sethost",""
   "``POST``","tinc","settings","sethost","$uuid"
   "``POST``","tinc","settings","setnetwork",""
   "``POST``","tinc","settings","setnetwork","$uuid"
   "``POST``","tinc","settings","togglehost","$uuid/$enabled"
   "``POST``","tinc","settings","togglenetwork","$uuid/$enabled"

----------------------

tor
~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","tor","general","get",""
   "``POST``","tor","general","set",""
   "``GET``","tor","relay","get",""
   "``POST``","tor","relay","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","tor","service","reconfigure",""
   "``POST``","tor","service","restart",""
   "``POST``","tor","service","start",""
   "``GET``","tor","service","status",""
   "``POST``","tor","service","stop",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","tor","exitacl","addacl",""
   "``POST``","tor","exitacl","delacl","$uuid"
   "``GET``","tor","exitacl","getacl","$uuid"
   "``GET``","tor","exitacl","searchacl",""
   "``POST``","tor","exitacl","setacl","$uuid"
   "``POST``","tor","exitacl","toggleacl","$uuid"
   "``POST``","tor","general","addhidservauth",""
   "``POST``","tor","general","delhidservauth","$uuid"
   "``GET``","tor","general","gethidservauth","$uuid"
   "``GET``","tor","general","searchhidservauth",""
   "``POST``","tor","general","sethidservauth","$uuid"
   "``POST``","tor","general","togglehidservauth","$uuid"
   "``POST``","tor","hiddenservice","addservice",""
   "``POST``","tor","hiddenservice","delservice","$uuid"
   "``GET``","tor","hiddenservice","getservice","$uuid"
   "``GET``","tor","hiddenservice","searchservice",""
   "``POST``","tor","hiddenservice","setservice","$uuid"
   "``POST``","tor","hiddenservice","toggleservice","$uuid"
   "``POST``","tor","hiddenserviceacl","addacl",""
   "``POST``","tor","hiddenserviceacl","delacl","$uuid"
   "``GET``","tor","hiddenserviceacl","getacl","$uuid"
   "``GET``","tor","hiddenserviceacl","searchacl",""
   "``POST``","tor","hiddenserviceacl","setacl","$uuid"
   "``POST``","tor","hiddenserviceacl","toggleacl","$uuid"
   "``POST``","tor","socksacl","addacl",""
   "``POST``","tor","socksacl","delacl","$uuid"
   "``GET``","tor","socksacl","getacl","$uuid"
   "``GET``","tor","socksacl","searchacl",""
   "``POST``","tor","socksacl","setacl","$uuid"
   "``POST``","tor","socksacl","toggleacl","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","tor","service","circuits",""
   "","tor","service","get",""
   "","tor","service","streams",""

----------------------

wol
~~~

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","wol","wol","addHost",""
   "","wol","wol","delHost",""
   "","wol","wol","getHost",""
   "","wol","wol","getwake",""
   "","wol","wol","searchHost",""
   "","wol","wol","set",""
   "","wol","wol","setHost",""
   "","wol","wol","wakeall",""

----------------------

zabbixagent
~~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","zabbixagent","settings","get",""
   "``POST``","zabbixagent","settings","set",""
   "``GET``","zabbixagent","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","zabbixagent","service","reconfigure",""
   "``POST``","zabbixagent","service","restart",""
   "``POST``","zabbixagent","service","start",""
   "``GET``","zabbixagent","service","status",""
   "``POST``","zabbixagent","service","stop",""

----------------------

zabbixproxy
~~~~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","zabbixproxy","general","get",""
   "``POST``","zabbixproxy","general","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","zabbixproxy","service","reconfigure",""
   "``POST``","zabbixproxy","service","restart",""
   "``POST``","zabbixproxy","service","start",""
   "``GET``","zabbixproxy","service","status",""
   "``POST``","zabbixproxy","service","stop",""

----------------------

zerotier
~~~~~~~~

.. csv-table:: Settings
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","zerotier","settings","get",""
   "``POST``","zerotier","settings","set",""

.. csv-table:: Service
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``GET``","zerotier","settings","status",""

.. csv-table:: Resources
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "``POST``","zerotier","network","add",""
   "``POST``","zerotier","network","del","$uuid"
   "``GET``","zerotier","network","get","$uuid"
   "``GET``","zerotier","network","search",""
   "``POST``","zerotier","network","set","$uuid"
   "``POST``","zerotier","network","toggle","$uuid"

.. csv-table:: Other
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

   "","zerotier","network","info",""

