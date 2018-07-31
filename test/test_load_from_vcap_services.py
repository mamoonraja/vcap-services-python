import os
from vcap_services import load_from_vcap_services


dummy_VCAP_creds = {'username': 'Mo', 'password': 'Salah'}

def test_vcap_services_not_none():
    assert load_from_vcap_services('assistant') == dummy_VCAP_creds
    assert load_from_vcap_services('discovery') is None

def test_vcap_services_is_none():
    del os.environ['VCAP_SERVICES']
    assert load_from_vcap_services('assistant') is None
