from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_grade_A():
    client = app.test_client()
    response = client.get("/grade/95")
    assert response.get_json()["grade"] == "A"

def test_add_task():
    client = app.test_client()
    response = client.post("/tasks", json={"name": "Test task"})
    assert response.status_code == 201