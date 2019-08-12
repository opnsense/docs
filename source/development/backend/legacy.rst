====================
Using legacy plugins
====================

-------
General
-------

Legacy type plugins are located in the following location:

::

    /usr/local/etc/inc/plugins.inc.d/

And contain files with the extension ".inc".

All automatically registered functions start with the name of the file (without the extension), followed by the purpose.
For example *vpn_configure* would be the *configure* handle in a plugin file name vpn.inc.

With the use of these plugins, you have the ability to hook into different areas of the system, such as registration of
new interface types and making sure services are shown in the regular service overview.


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
and :code:`myplugin_configure()_vpn` on vpn state change where the latter is accepting two (2) parameters at most.


::

    function myplugin_configure()
    {
        return array(
            'bootup' => array('myplugin_configure')
            'vpn' => array('myplugin_configure_vpn:2')
        );
    }


To list all available hooks, you can use :code:`pluginctl` without parameters:

::

    pluginctl -c


Below you will find an incomplete list of the most common used events that are handled at the moment:

===========================  =================================================================================
Event                        When
===========================  =================================================================================
earlybootup                  Early in bootup process, before normal services are started
                             (things like ssh and the webconfigurator use this spot)
bootup                       Bootup, normal legacy service configuration, when not using the :code:`rc(8)` system
                             (for example: unbound, ntpd)
newwanip                     Triggered after configuration of a new interface address, expects a maximum of two positional
                             parameters (:code:`$verbose` and :code:`$interface`).
monitor                      Executed when there are changes that involve (dpinger) gateway monitoring.
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
| Property              | Syntax                 | Description                                            |
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
Syslog
-----------------

To register syslog targets, the :code:`<plugin>_syslog()` function should return a structure containing targets and definitions.

::

    function myplugin_syslog()
    {
        $logfacilities = array();
        $logfacilities['myplugin'] = array(
            'facility' => array('myplugin'),
            'remote' => 'myplugin',
        );
        return $logfacilities;
    }


.. Note::

    As of OPNsense 19.7 Syslog-NG is included in our base system and includes :code:`/usr/local/etc/syslog-ng.conf.d/*.conf`
    when started. When not depending on circular logs, you might want to consider adding templates there instead of
    using this legacy handler.


To test if a service registration functions properly, just restart the syslog facility:

::

    pluginctl -s syslogd restart



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
        );
        return $result;
    }


.. Note::


    If your plugin depends on other components in the system, make sure you enable synchronization for those as well.
