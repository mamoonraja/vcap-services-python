import os
import json

def load_from_vcap_services(service_name):
    vcap_services = os.getenv("VCAP_SERVICES")
    if vcap_services is not None:
        services = json.loads(vcap_services)
        if service_name in services:
            return services[service_name][0]["credentials"]
    else:
        return None

def parse_credentials_from_file(service_label, credentials):
    print(service_label, credentials)
    return {}

def get_creds_for_starter(service_label, credentials_from_file):
    if credentials_from_file != None:
        return parse_credentials_from_file(service_label, credentials_from_file)
