OPNBECore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: Resources (SyncController.php)  -- extends : ApiControllerBase
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","opncentral","sync","listServices",""
    "``GET``","opncentral","sync","listClasses",""
    "``GET``","opncentral","sync","metrics",""
    "``GET``","opncentral","sync","readConfig","$paths"
    "``POST``","opncentral","sync","reconfigure",""
    "``POST``","opncentral","sync","restartService",""


-----------------------
Sync API explained
-----------------------

The :code:`sync` API is being used to process central actions in parallell from the OPNcentral dashboard.
As explained in the documentation for OPNcentral, provisioning is able to detect change on the sections it may
distribute. In order to do this the :code:`listClasses` API action plays a large role here.


listClasses
.........................

The list classes endpoint provides insights into the different configuration items the target host understands
and how these are tied into services. It's also a key component in comparing configuration items.

.. code-block:: json

    {
      "classes": [
        {
          "description": "Aliases",
          "help": "Synchronize the aliases over to the other HA host.",
          "section": "OPNsense.Firewall.Alias",
          "services": [
            "pf"
          ],
          "md5": "942d6358fb4f17abed7cf4f5de6c5b24",
          "id": "aliases"
        },
      "runtime": 0.07380509376525879
    }


When the target firewall is 100% equal to the central node, the :code:`md5` values will match. In order to steer
specific overrides on the synchronisation action, it is possible to send a json encoded base64 structure as :code:`metadata`
post parameter (not available in the online documentation, advanced usage only).

readConfig
.........................

This endpoint is responsible for providing access to various parts of the configuration and mostly practical
to retrieve parts of the configuration.

Example usage of this endpoint is provided below.

.. code-block:: python

    import json
    import requests
    auth = {
      "key":"3RhWOno+HwvtmT406I6zw8of8J6n9FOKlWK6U0B+K7stt/fDaJg7bjeF3QAshlScYqC+3o5THy3vQViW",
      "secret":"uaBk27NKhQCZSDpfAlG6YJ473MzvsCNiED6kzbYuykzU05fCRkcJADhDm5nxbZt8yREC74ZpvD/vbcEx"
    }
    r = requests.get(
        'https://127.0.0.1/api/opncentral/sync/read_config/OPNsense.Firewall.Alias',
        auth=(auth['key'], auth['secret']),
        verify=False    # use for localhost testing only
    )
    print(r.text)


When executed, this will dump the contents of the configuration path :code:`OPNsense.Firewall.Alias` into a named array
with serialisable content.


reconfigure
.........................

The reconfigure action is the counterpart of the readConfig endpoint and accepts new configuration data specified in
the :code:`payload` attribute of the :code:`POST` request.

In some cases configuration merges have ways to handle local changes, which is documented in the "Provisioning classes"
section of the OPNcentral documentation.

After merging the new configuration, this endpoint also detects which services need to be restarted and will issue
a restart command automatically.

.. code-block:: python

    import json
    import requests
    auth = {
      "key":"3RhWOno+HwvtmT406I6zw8of8J6n9FOKlWK6U0B+K7stt/fDaJg7bjeF3QAshlScYqC+3o5THy3vQViW",
      "secret":"uaBk27NKhQCZSDpfAlG6YJ473MzvsCNiED6kzbYuykzU05fCRkcJADhDm5nxbZt8yREC74ZpvD/vbcEx"
    }

    payload = "<<dictionary type content from readConfig>>"

    r = requests.post(
        'https://127.0.0.1/api/opncentral/sync/reconfigure',
        auth=(auth['key'], auth['secret']),
        json={'payload': payload},
        verify=False,   # use for localhost testing only
        headers={'Content-Type': 'application/json; charset=UTF-8'}
    )

listServices
.........................

In order to gain insights on the active running services, you can use the listServices api action.
This will report all active services and their status.


restartService
.........................


The restart service action is also used in :menuselection:`Management: Status / Services` and offers the ability
to restart a list of selected services on the target host.

.. code-block:: python

    import json
    import requests
    auth = {
      "key":"3RhWOno+HwvtmT406I6zw8of8J6n9FOKlWK6U0B+K7stt/fDaJg7bjeF3QAshlScYqC+3o5THy3vQViW",
      "secret":"uaBk27NKhQCZSDpfAlG6YJ473MzvsCNiED6kzbYuykzU05fCRkcJADhDm5nxbZt8yREC74ZpvD/vbcEx"
    }

    r = requests.post(
        'https://127.0.0.1/api/opncentral/sync/restart_service',
        auth=(auth['key'], auth['secret']),
        json={'services':['cron']},
        verify=False,     # use for localhost testing only
        headers={'Content-Type': 'application/json; charset=UTF-8'}
    )

The example above will restart the :code:`cron` service.
