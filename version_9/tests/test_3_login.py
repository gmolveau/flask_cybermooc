# tests/test_3_login_route.py

def test_login_empty_password(client):
    # testing errors
    empty_password = client.post("/api/v1/login", json={
        'username': 'testuser', 'password': ''
    })
    assert empty_password.status_code == 422

def test_login_empty_username(client):
    empty_username = client.post("/api/v1/login", json={
        'username': '', 'password': 'test_user'
    })
    assert empty_username.status_code == 422

def test_login_correct(client, global_data):
    correct = client.post("/api/v1/login", json={
        'username': 'testuser', 'password': 'test_user'
    })
    assert correct.status_code == 200
    json_data = correct.get_json()
    assert "token" in json_data
    global_data['token'] = json_data['token']

def test_login_admin(client, global_data):
    correct = client.post("/api/v1/login", json={
        'username': 'testadmin', 'password': 'testadmin'
    })
    assert correct.status_code == 200
    json_data = correct.get_json()
    assert "token" in json_data
    global_data['token_admin'] = json_data['token']

def test_login_wrong_username(client):
    wrong_username = client.post("/api/v1/login", json={
        'username': 'testusernot', 'password': 'test_user'
    })
    assert wrong_username.status_code == 404

def test_login_wrong_password(client):
    wrong_password = client.post("/api/v1/login", json={
        'username': 'testuser', 'password': 'test_user_wrong'
    })
    assert wrong_password.status_code == 401