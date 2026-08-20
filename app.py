from flask import Flask, jsonify, request

app = Flask(__name__)

class Task:
    def __init__(self, id, name, done=False):
        self.id = id
        self.name = name
        self.done = done

    def to_dict(self):
        return {"id": self.id, "name": self.name, "done": self.done}

tasks = []
next_id = 1

@app.route("/")
def home():
    return jsonify({"message": "Task Manager API is running", "status": "ok"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify([t.to_dict() for t in tasks])

@app.route("/tasks", methods=["POST"])
def add_task():
    global next_id
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "name is required"}), 400
    task = Task(next_id, name)
    tasks.append(task)
    next_id += 1
    return jsonify(task.to_dict()), 201

@app.route("/grade/<int:score>")
def grade(score):
    if score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    return jsonify({"score": score, "grade": letter})

@app.route("/stats")
def stats():
    total = len(tasks)
    completed = 0
    for t in tasks:
        if t.done:
            completed += 1
    return jsonify({"total_tasks": total, "completed": completed})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return jsonify({"message": f"Task {task_id} deleted"})