

def test_status(client):
    assert client.get('/api/status') == "status"