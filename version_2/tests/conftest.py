# tests/conftest.py

import pytest

from app import create_app

@pytest.fixture(scope = 'session')
def global_data():
    return dict()

@pytest.fixture(scope="session")
def client():
    test_app = create_app()
    test_app.config['TESTING'] = True
    client = test_app.test_client()
    yield client