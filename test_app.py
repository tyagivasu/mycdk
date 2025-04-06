import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

# ✅ Stable Test
def test_index(client):
    res = client.get('/')
    assert res.status_code == 200

# ❗ Flaky due to random
def test_random_route(client):
    res = client.get('/random')
    assert res.status_code == 200

# ❗ Flaky due to timeout (simulated)
def test_slow_route(client):
    res = client.get('/slow')
    assert res.status_code == 200
