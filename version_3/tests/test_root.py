# tests/test_basic.py

def test_root_endpoint(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello, World!' in rv.data