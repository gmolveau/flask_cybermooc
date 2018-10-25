# tests/test_2_signup_route.py


def test_signup_empty_password(client):
    empty_password = client.post("/api/v1/signup", json={
        'username': 'testuser', 'password': '', 'email': 'test_user@mail.com'
    })
    assert empty_password.status_code == 422

def test_signup_empty_username(client):
    empty_username = client.post("/api/v1/signup", json={
        'username': '', 'password': 'test_user', 'email': 'test_user@mail.com'
    })
    assert empty_username.status_code == 422

def test_signup_empty_email(client):
    empty_email = client.post("/api/v1/signup", json={
        'username': 'testuser', 'password': 'test_user', 'email': ''
    })
    assert empty_email.status_code == 422

def test_signup_correct(client):
    correct = client.post("/api/v1/signup", json={
        'username': 'testuser', 'password': 'test_user', 'email': 'test_user@mail.com'
    })
    assert correct.status_code == 200

def test_signup_username_taken(client):
    username_taken = client.post("/api/v1/signup", json={
        'username': 'testuser', 'password': 'test_user', 'email': 'test_user@mail.com'
    })
    assert username_taken.status_code == 409

def test_signup_email_taken(client):
    email_taken = client.post("/api/v1/signup", json={
        'username': 'testuser', 'password': 'test_user', 'email': 'test_user@mail.com'
    })
    assert email_taken.status_code == 409