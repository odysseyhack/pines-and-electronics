import pytest
from flask_app.myapp import app

app = app

@pytest.fixture
def client():
    client = app.test_client()
    yield client