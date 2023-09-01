==========================
Wazuh Agent
==========================

--------------------------------------
Introduction
--------------------------------------

`Wazuh <https://wazuh.com/>`__ is an open source unified XDR (Extended Detection and Response) and SIEM (Security Information en Event Management)
system capable of offering protection for endpoints and cloud workloads.

The Wazuh architecture is based on agents, running on the monitored endpoints, which collect information and are capable of
executing active responses directed by the manager.

The goal of this plugin is to offer an easily installable plugin to connect to the Wazuh manager.

.. Note::
  The scope of Wazuh on OPNsense is only to offer configurable agent support. We do not plan nor advise to run the Wazuh
  central components on OPNsense. Detailed information on how to install these on supported platforms are available directly from the
  `Wazuh website <https://documentation.wazuh.com/current/installation-guide/index.html>`__
  or you can use their cloud based offering available `here <https://wazuh.com/cloud/>`__


.. Warning::
  This plugin is provided "as-is" and with very limited [tier 3] community support from the OPNsense team. Using a SIEM/XDR system
  requires knowledge which usually is out of the (free) community support scope.


--------------------------------------
Installation
--------------------------------------

Installation of this plugin is rather easy, go to :menuselection:`System --> Firmware --> Plugins` and search for **os-wazuh-agent**,
use the [+] button to install it.

Next go to :menuselection:`Services --> Wazuh Agent --> Settings` to configure the service.


.. Tip::
    When the ossec log offers too limited insights when debugging issues, try to increase the debug level. You can find this setting under
    General settings when "advanced mode" is enabled.

--------------------------------------
Connecting the agent
--------------------------------------

To connect the agent to the manager, just fill in a hostname under **General Settings/Manager hostname**, make sure
the agent is marked enabled and optionally specify a connect password under **Authentication/Password**.

Next go to the manager to see if the agent registered itself.


--------------------------------------
Selecting which logs to ingest
--------------------------------------

Our Wazuh agent plugin supports syslog targets like we use in the rest of the product, so if an application sends
its feed to syslog and registers the application name as described in our `development documentation <https://docs.opnsense.org/development/backend/legacy.html#syslog>`__
it can be selected to send to Wazuh as well.

For Intrusion detection we can send the events as well using the same (eve) datafeed used in OPNsense, just mark the
**Intrusion detection events** in the general settings.

.. Note::
  Wazuh only supports `rfc3164 <https://datatracker.ietf.org/doc/html/rfc3164>`__ formatted syslog messages, for that reason
  we record a copy of the requested events into a file named :code:`/var/ossec/logs/opnsense_syslog.log` using that format.


--------------------------------------
Installing custom ossec.conf entries
--------------------------------------

Some Wazuh modules are directly selectable from the gui, but when a feature is needed, which is not offered in the
plugin, it's possible to add static sections manually.

You can add these in :code:`/usr/local/opnsense/service/templates/OPNsense/WazuhAgent/ossec_config.d/`, for example, to
add a custom json feed, add a file containing the following content in there:

.. code-block:: xml
  :linenos:
  :caption: /usr/local/opnsense/service/templates/OPNsense/WazuhAgent/ossec_config.d/099-my-feed.conf

  <localfile>
    <log_format>json</log_format>
    <location>/path/to/my/file.json</location>
  </localfile>


--------------------------------------
Use active responses
--------------------------------------

Wazuh supports `active responses <https://documentation.wazuh.com/current/user-manual/capabilities/active-response/index.html>`__
so the manager can direct defensive actions when needed. The plugin ships with one action named :code:`opnsense-fw` to
drop traffic from a specified source address.

.. Note::

  The opnsense-fw action is stateful and can add and delete addresses from the firewall, more context on these type
  of actions can be found in the `Wazuh <https://documentation.wazuh.com/current/user-manual/capabilities/active-response/custom-active-response-scripts.html>`__
  documentation.


To use this action, you need to add some configuration in the manager, starting with the definition of this action.

.. code-block:: xml
  :linenos:
  :caption: /var/ossec/etc/ossec.conf

  <ossec_config>
    <command>
      <name>opnsense-fw</name>
      <executable>opnsense-fw</executable>
      <timeout_allowed>yes</timeout_allowed>
    </command>
  </ossec_config>

After which you can use it in active-response rules, like this:

.. code-block:: xml
  :linenos:
  :caption: /var/ossec/etc/ossec.conf

  <ossec_config>
    <active-response>
      <disabled>no</disabled>
      <command>opnsense-fw</command>
      <location>defined-agent</location>
      <agent_id>001</agent_id>
      <rules_id>100201</rules_id>
      <timeout>180</timeout>
    </active-response>
  </ossec_config>


The official `documentation <https://documentation.wazuh.com/current/user-manual/capabilities/active-response/how-to-configure.html>`__
contains more information about the options available.

.. Tip::
  Active responses are logged into :menuselection:`Services --> Wazuh Agent --> Logfile / active-responses`, including
  the messages received from the manager.


To quickly test if an active-response can be executed on the agent, we advise to use the API console under :menuselection:`Wazuh --> Tools --> API console`.
Executing the :code:`opnsense-fw` command for address :code:`172.16.1.30` on agent :code:`001` can be done using:

.. code-block:: xml
  :linenos:

  PUT /active-response?agents_list=001
  {
    "command": "!opnsense-fw",
    "custom": false,
    "alert": {
      "data": {
        "srcip": "172.16.1.30"
      }
    }
  }


.. Tip::

  Wazuh offers quite some `proof of concept <https://documentation.wazuh.com/current/proof-of-concept-guide/index.html>`__ documents and blog posts,
  like `this <https://wazuh.com/blog/responding-to-network-attacks-with-suricata-and-wazuh-xdr/>`__
  document explaining how Suricata and Wazuh can be combined to respond to detected threats.

--------------------------------------
Test rule detection
--------------------------------------

In case log entries are being collected in :code:`/var/ossec/logs/opnsense_syslog.log` and no events are being collected
in the Manager, it's usually a good idea to check how Wazuh processes these lines.

The :menuselection:`Wazuh --> Tools --> Ruleset test` menu item in the manager offers an easy to use tool to inspect log
events.

