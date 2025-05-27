============================
Using plugins
============================

-------
General
-------

Plugins are located in the following location:

::

    /usr/local/etc/inc/plugins.inc.d/

And contain files with the extension ".inc".

All automatically registered functions start with the name of the file (without the extension), followed by the purpose.
For example *vpn_configure* would be the *configure* handle in a plugin file name vpn.inc.

With the use of these plugins, you have the ability to hook into different areas of the system, such as registration of
new interface types and making sure services are shown in the regular service overview.


.. Note::

    When plugins fail and cause PHP errors, these will be collected in :code:`/tmp/PHP_errors.log`, these plugins are not
    registered and executed when emitting such errors


-----------------
Services
-----------------

To register services, the :code:`<plugin>_services()` function should return a structure containing its name, description and operating properties.

::

    function myplugin_services()
    {
        $service = array();
        $service['name'] = 'myservice';
        $service['description'] = gettext('My service');
        $service['configd']['restart'] = array('myservice restart');
        $service['configd']['start'] = array('myservice start');
        $service['configd']['stop'] = array('myservice stop');
        $services[] = $pconfig;
        return $services;
    }



===========================  =================================================================================
**option**                   **Description**
===========================  =================================================================================
name                         Service identifier
id                           Optional identifier to suffix the service, only used in specific cases where
                             one "service" can actually be a list of them (e.g. :code:`openvpn`)
description                  User friendly description
pidfile                      Validate running based on specified pid file (instead of "name")
nocheck                      [boolean] ignore pid or process name and always report running
{type}                       Type could be one of :code:`configd`, :code:`php`, :code:`mwexec`
{type}.start                 Action to call when starting the service
{type}.stop                  Action to call when stopping the service
{type}.restart               Action to call when restarting the service
===========================  =================================================================================



To list all available services from the command line, you can use pluginctl (bundled with our core system).

::

    pluginctl -s


The same tool can also be used to execute the [re]start/stop operations, for the example above, a restart would look like:

::

    pluginctl -s myservice restart


-----------------
Configure
-----------------

The configure plugin can be used to catch certain events, such as :code:`bootup`, :code:`newwanip` and others.

A small sample of a registration is shown below, which registers the functions :code:`myplugin_configure()` on bootup
and :code:`myplugin_configure_vpn()` on vpn state change where the latter is accepting two (:2) parameters at most.
Note that the default number of arguments passed to the listeners is one (:1) which is the :code:`$verbose`  parameter
steering whether the function is allowed to print progress or not.  The maximum number of arguments passed depends
on the particular event provider.  For more details see below.

::

    function myplugin_configure()
    {
        return [
            'bootup' => ['myplugin_configure'],
            'vpn' => ['myplugin_configure_vpn:2'],
        ];
    }


To list all available hooks, you can use :code:`pluginctl` without parameters:

::

    pluginctl -c


Below you will find an incomplete list of the most common used events that are handled at the moment:

===========================  =================================================================================
**Event**                    **When**
===========================  =================================================================================
early                        Early in bootup process, before normal services are started
                             (things like ssh and the webconfigurator use this spot)
bootup                       Bootup, normal legacy service configuration, when not using the :code:`rc(8)` system
                             (for example: unbound, ntpd)
newwanip                     Triggered after configuration of a dynamic interface address, expects a maximum of three positional
                             parameters (:code:`$verbose` and :code:`$interfaces` and :code:`$family`). :code:`$interfaces`
                             is an array all relevant interfaces that require reloading or null for all.  $:code:`family` is the
                             address family type that triggered the event, either :code:`inet` for IPv4 or :code:`inet6` for IPv6.
vpn                          Triggered in multiple places that require a reload of the VPN based subsystems, expects a maximum
                             of two parameters (:code:`$verbose` and :code:`$interfaces`). :code:`$interfaces` is an array of
                             all relevant interfaces that require reloading or null for all.
===========================  =================================================================================


:code:`pluginctl`  can also be used to trigger a specific event, such as:

::

    pluginctl -c monitor



------------------
Firewall
------------------

To register firewall rules, create a function called :code:`<plugin>_firewall()`, this will pass a plugin object you
can use to generate new firewall rules.

A very simplified example of such a rule is included below:


::

    function myplugin_firewall(\OPNsense\Firewall\Plugin $fw) {
        $fw->registerFilterRule(500000, array("direction" => "in", "protocol" => "udp", "to_port" => 9999));
    }


:code:`configctl` can be used to reload the firewall and test your plugin:

::

    configctl filter reload


This will generate a rule like (in /tmp/rules.debug):

::

    pass in quick proto udp from {any} to {any} port {9999}


-----------------
Interface
-----------------

To register new (virtual) interfaces, create a function called :code:`<plugin>_interfaces()`, which should return a named array containing the unique interface name as key (enc0 for ipsec for example).

Every item should contain the following properties:

+-----------------------+------------------------+--------------------------------------------------------+
| **Property**          | **Syntax**             | **Description**                                        |
+=======================+========================+========================================================+
| enable                | boolean                | interface enabled, if so it will be saved in the config|
+-----------------------+------------------------+--------------------------------------------------------+
| descr                 | text                   | User readable description                              |
+-----------------------+------------------------+--------------------------------------------------------+
| networks              | array, [network, mask] | list of named arrays containing remote networks        |
+-----------------------+------------------------+--------------------------------------------------------+
| type                  | text                   | "none"                                                 |
+-----------------------+------------------------+--------------------------------------------------------+
| if                    | text                   | physical interface (e.g. enc0)                         |
+-----------------------+------------------------+--------------------------------------------------------+
| virtual               | boolean                | Virtual interface, true/false                          |
+-----------------------+------------------------+--------------------------------------------------------+

Example:

::

    function myplugin_interfaces()
    {
        global $config;

        $interfaces = array();
        if (isset($config['myplugin']['enable'])) {
            $oic = array("enable" => true);
            $oic['if'] = 'tun0';
            $oic['descr'] = 'myplugin';
            $oic['type'] = "none";
            $oic['virtual'] = true;
            $oic['networks'] = array();
            $interfaces['tun0'] = $oic;
        }

        return $interfaces;
    }


-----------------
Device
-----------------

To register virtual network devices types which can be used verbatim or manually assigned to interfaces,
the :code:`<plugin>_devices()` function should return a structure containing such devices and additional
definitions.

Device registration covers a number of aspects such as interfaces assignment page presentation, external
(re)configuration function, automatic configuration of assigned devices, and matching device name pattern
amongst others. Available settings are described below:


+-----------------------+------------------------+--------------------------------------------------------------+
| **Property**          | **Syntax**             | **Description**                                              |
+=======================+========================+==============================================================+
| function              | text                   | Calls function of that name with device name as argument     |
+-----------------------+------------------------+--------------------------------------------------------------+
| volatile              | boolean                | This interface can disappear so do not attempt boot recovery |
+-----------------------+------------------------+--------------------------------------------------------------+
| configurable          | boolean                | Assigned interface can set IPv4/IPv6 mode if true or missing |
+-----------------------+------------------------+--------------------------------------------------------------+
| pattern               | text                   | Regex to identify device names in bulk                       |
+-----------------------+------------------------+--------------------------------------------------------------+
| type                  | text                   | Unqiue type setting required for assignments page            |
+-----------------------+------------------------+--------------------------------------------------------------+
| names                 | array [ see below ]    | List of devices with individual names as associative keys    |
+-----------------------+------------------------+--------------------------------------------------------------+
| ...descr              | text                   | Descriptive text of device, e.g. for assignments page        |
+-----------------------+------------------------+--------------------------------------------------------------+
| ...ifdescr            | text                   | Verbatim description, e.g. as stored in config.xml           |
+-----------------------+------------------------+--------------------------------------------------------------+
| ...name               | text                   | Device name same as array key for convenient access          |
+-----------------------+------------------------+--------------------------------------------------------------+


Example:

::

    function my myplugin_devices()
    {
        $devices = [];

        $devices[] = [
            'function' => 'function_name_to_configure',
            'names' => ['dev0' => [
                'descr' => 'descriptive text',
                'ifdescr' => 'verbatim description',
                'name' => 'dev0',
            ]],
            'pattern' => '^dev',
            'volatile' => true,
            'type' => 'bridge',
        ];

        return $devices;
    }


-----------------
Syslog
-----------------

To register syslog targets, the :code:`<plugin>_syslog()` function should return a structure containing targets and definitions.

::

    function myplugin_syslog()
    {
        $logfacilities = array();
        $logfacilities['myplugin'] = array(
            'facility' => array('myplugin'),
        );
        return $logfacilities;
    }


.. Note::

    As of OPNsense 19.7 Syslog-NG is included in our base system, these files will only be used to identify applications
    for custom syslog remote targets in :menuselection:`System->Settings->Logging / targets`.


To test if a service registration functions properly, just restart the syslog facility:

::

    pluginctl -s syslogd restart


.. Note::

    In order to define local targets for Syslog-NG you can just add **local** filters (e.g. by creating
    :code:`src/opnsense/service/templates/OPNsense/Syslog/local/helloworld.conf`) which will be collected into
    one large syslog configuration.
    The readme on `GitHub <https://github.com/opnsense/core/blob/master/src/opnsense/service/templates/OPNsense/Syslog/local/README>`__
    describes the process.
    When running into issues, always make sure to manually restart syslog-ng first (:code:`service syslog-ng restart`), definition errors won't
    be written into any log. You will also have to restart the plugin (:code:`pluginctl -s syslog-ng restart`) for the syslog-ng configuration
    files to be regenerated.

.. Note::

    In case additional source sockets should be used by Syslog-NG you can add files in :code:`/usr/local/opnsense/service/templates/OPNsense/Syslog/sources/`
    containing definitions.
    The `001-local.conf <https://github.com/opnsense/core/blob/22.1.7/src/opnsense/service/templates/OPNsense/Syslog/sources/001-local.conf#L5>`__ file
    contains examples from jailed core services.

-----------------
XMLRPC (HA) sync
-----------------

When a configuration section should be exposed to High Availability sync, you can use the xmlrpc plugin hook.

If a plugin exposes a configuration section to ha sync, it can be enabled separately in the synchronization
settings :menuselection:`System->High Availability->Settings`.

A simple example to expose the configuration section Myplugin within the OPNsense xml path looks like this:

::

    function myplugin_xmlrpc_sync()
    {
        $result = array();
        $result[] = array(
            'description' => gettext('My Plugin'),
            'section' => 'OPNsense.Myplugin',
            'id' => 'myplugin',
            'services' => 'myplugin', // optional, in case a service with the same name exists
        );
        return $result;
    }


.. Note::


    If your plugin depends on other components in the system, make sure you enable synchronization for those as well.
