def test_task_creation():
    task = {
        "title": "Implementar testes",
        "status": "To Do",
        "priority": "Alta"
    }
    assert task["title"] != ""
