#!/usr/local/bin/python3
'''Compile Alerts and Alert rule'''

import json
from laceworksdk import LaceworkClient


def get_alert_rules(lw):
    '''alert_rules'''
    return_value = {}
    try:
        for alert_rule in lw.alert_rules.get()['data']:
            value = {}
            for key in ('name', 'description', 'severity'):
                value[key] = alert_rule['filters'][key]
            value['intgGuidList'] = alert_rule['intgGuidList']
            return_value[alert_rule['mcGuid']] = value
    except (KeyError):
        pass
    return return_value


def get_alert_channels(lw):
    '''alert_channels'''
    return_value = {}
    try:
        for alert_channel in lw.alert_channels.get()['data']:
            value = {}
            for key in ('name',):
                value[key] = alert_channel[key]
            return_value[alert_channel['intgGuid']] = value
    except (KeyError):
        pass
    return return_value


def get_resource_groups(lw):
    '''resource_groups'''
    return lw.resource_groups.get()


if __name__ == "__main__":

    # Instantiate a LaceworkClient instance
    lacework_client = LaceworkClient()

    alert_rules = get_alert_rules(lacework_client)
    # print(json.dumps(alert_rules))

    alert_channels = get_alert_channels(lacework_client)
    print(alert_channels)

    for ar in alert_rules.values():
        line = ''
        for field in ('name', 'description'):
            line += ',' + ar[field]
        for ac in ar['intgGuidList']:
            line += ',' + alert_channels[ac]['name']
        print(line)
    # resource_groups = get_resource_groups(lacework_client)
    # print(json.dumps(resource_groups))
