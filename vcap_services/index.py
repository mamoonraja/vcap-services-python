import os
import json

def load_from_vcap_services(service_name):
    vcap_services = os.getenv('VCAP_SERVICES')
    if vcap_services is not None:
        services = json.loads(vcap_services)
        if service_name in services:
            return services[service_name][0]['credentials']
    else:
        return None

def parse_credentials(service_label, credentials):
    key = 'watson_' + service_label + '_'
    creds = {}
    if credentials is not None:
        cred_keys = credentials.keys()
        filtered_keys = list(filter(lambda x: x.find(key) != -1, cred_keys))
        for k in filtered_keys:
            creds[k.replace(key, '')] = credentials[k]
    return creds

def get_credentials_from_file(service_label, credentials_from_local_config=None):
    creds = {}
    kube_tag = 'service_watson_' + service_label
    creds_from_vcap = load_from_vcap_services(service_label)
    if credentials_from_local_config is not None:
        creds = parse_credentials(service_label, credentials_from_local_config)
    elif creds_from_vcap is not None:
        creds = creds_from_vcap
    elif os.getenv(kube_tag) is not None:
        creds = json.loads(os.getenv(kube_tag))
    return creds
