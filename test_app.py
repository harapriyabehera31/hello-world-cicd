from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Harmony Bakery" in response.data
    assert b"Chocolate Truffle" in response.data
