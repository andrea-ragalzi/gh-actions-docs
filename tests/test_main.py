from fastapi.testclient import TestClient
from src.gh_actions_docs.main import app, todos

client = TestClient(app)


def test_create_todo():
    response = client.post(
        "/todos/", json={"id": 1, "title": "Test task", "completed": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test task"
    assert data["completed"] is False


def test_get_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(todo["id"] == 1 for todo in data)


def test_update_todo():
    response = client.put(
        "/todos/1", json={"id": 1, "title": "Updated Task", "completed": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["completed"] is True


def test_update_nonexistent_todo():
    response = client.put(
        "/todos/999", json={"id": 999, "title": "Not Found", "completed": False}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}


def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted"}


def test_delete_nonexistent_todo():
    response = client.delete("/todos/999")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted"}


def test_get_todos_empty():
    todos.clear()
    response = client.get("/todos/")
    assert response.status_code == 200
    assert response.json() == []
