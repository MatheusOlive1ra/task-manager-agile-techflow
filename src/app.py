
from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json
    tasks.append(task)
    return jsonify({"message": "Tarefa criada com sucesso"}), 201

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    tasks.pop(index)
    return jsonify({"message": "Tarefa removida com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)

