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
    if len(response['rows']) == 0:
        # create a new rule, identified by rule_description allowing traffic from
        # 192.168.0.0/24 to 10.0.0.0/24 using TCP protocol
        data = {"rule" :
                    {
                    "description": rule_description,
                    "source_net": "192.168.0.0/24",
                    "protocol": "TCP",
                    "destination_net": "10.0.0.0/24"
                    }
                }
        r = requests.post(
            "%s/api/firewall/filter/addRule" % remote_uri, auth=(api_key, api_secret), verify=False, json=data
        )
        if r.status_code == 200:
            print("created : %s" % json.loads(r.text)['uuid'])
        else:
            print("error : %s" % r.text)

    else:
        for row in response['rows']:
            print ("found uuid %s" % row['uuid'])
