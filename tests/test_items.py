import pytest
from app import create_app
from app.db import db

@pytest.fixture
def client(tmp_path, monkeypatch):
    # Use a temporary SQLite DB for tests
    db_path = tmp_path / "test.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_path}")
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_and_get_item(client):
    # Create item (no auth required for demo)
    resp = client.post("/api/v1/items/", json={"name": "test", "description": "desc"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["name"] == "test"
    item_id = data["id"]

    resp2 = client.get(f"/api/v1/items/{item_id}")
    assert resp2.status_code == 200
    assert resp2.get_json()["id"] == item_id
