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

-----------------
Services
-----------------

To register services, the *<plugin>_services()* function should return a structure containing its name, description and operating properties.

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

For a full list of supported service methods, please inspect *services.inc*


-----------------
Syslog
-----------------

To register syslog targets, the *<plugin>_syslog()* function should return a structure containing targets and definitions.

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



-----------------
Interface
-----------------

To register new (virtual) interfaces, create a function called *<plugin>_interfaces()*, which should return a named array containing the unique interface name as key (enc0 for ipsec for example).

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
Configure
-----------------

When your plugin needs configuration after boot, you can create a function called  *<plugin>_configure()* which will be called upon boot.
