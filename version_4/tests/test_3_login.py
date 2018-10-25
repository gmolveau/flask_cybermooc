# tests/test_3_login_route.py

def test_empty_password(client):
    # testing errors
    empty_password = client.post("/api/v1/login", json={
        'username': 'testuser', 'password': ''
    })
    assert empty_password.status_code == 422

def test_empty_username(client):
    empty_username = client.post("/api/v1/login", json={
        'username': '', 'password': 'test_user'
    })
    assert empty_username.status_code == 422

def test_correct(client):
    correct = client.post("/api/v1/login", json={
        'username': 'testuser', 'password': 'test_user'
    })
    assert correct.status_code == 200

def test_wrong_username(client):
    wrong_username = client.post("/api/v1/login", json={
        'username': 'testusernot', 'password': 'test_user'
    })
    assert wrong_username.status_code == 404

def test_wrong_password(client):
    wrong_password = client.post("/api/v1/login", json={
        'username': 'testuser', 'password': 'test_user_wrong'
    })
    assert wrong_password.status_code == 401