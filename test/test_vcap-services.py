from vcap_services import index

def test_load_from_file():
    assert index.parse_credentials_from_file('s', {}) == {}


def test_load_from_vcap_services():
    assert index.load_from_vcap_services('conversation') == None
