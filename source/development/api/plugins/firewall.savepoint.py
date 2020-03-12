#!/usr/bin/env python3.7
import requests
import json

# key + secret from downloaded apikey.txt
api_key="3RhWOno+HwvtmT406I6zw8of8J6n9FOKlWK6U0B+K7stt/fDaJg7bjeF3QAshlScYqC+3o5THy3vQViW"
api_secret="uaBk27NKhQCZSDpfAlG6YJ473MzvsCNiED6kzbYuykzU05fCRkcJADhDm5nxbZt8yREC74ZpvD/vbcEx"

# define the basics, hostname to use and description used to identify our test rule
rule_description='OPNsense_fw_api_testrule_1'
remote_uri="https://192.168.1.1"

# search for rule
r = requests.get(
    "%s/api/firewall/filter/searchRule?current=1&rowCount=7&searchPhrase=%s" % (
        remote_uri, rule_description
    ),
    auth=(api_key, api_secret), verify=False
)

if r.status_code == 200:
    response = json.loads(r.text)
    if len(response['rows']) > 0:
        rule_uuid = response['rows'][0]['uuid']
        r = requests.post("%s/api/firewall/filter/savepoint" % remote_uri, auth=(api_key, api_secret), verify=False)
        if r.status_code == 200:
            sp_response = json.loads(r.text)
            # disable rule
            r = requests.post("%s/api/firewall/filter/toggleRule/%s/0" % (remote_uri, rule_uuid),
                              auth=(api_key, api_secret), verify=False
            )
            # apply changes, revert to sp_response['revision'] after 60 seconds
            r = requests.post("%s/api/firewall/filter/apply/%s" % (remote_uri, sp_response['revision']),
                              auth=(api_key, api_secret), verify=False
            )
            print("revert to revision %s in 60 seconds (%s changed)" % (sp_response['revision'], rule_uuid))
    else:
        print("rule %s not found" % rule_description)
