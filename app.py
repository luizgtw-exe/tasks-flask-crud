from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(
        id=task_id_control,
        tittle=data['title'],  # atenção: "tittle" -> talvez queira "title"
        description=data.get("description", "")
    )
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    output = {
        "tasks": [
            {
                "id": task.id,
                "tittle": task.tittle,
                "description": task.description,
                "completed": getattr(task, "completed", False)
            } for task in tasks
        ],
        "total_tasks": len(tasks)
    }
    return jsonify(output)

@app.route('/tasks/<int:id>',methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message" : "Não foi possivel encontrar a atividade"}),404

@app.route('/tasks/<int:id>',methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)        
    if task == None:
        return  jsonify({"message" : "Não foi possivel encontrar a atividade"}),404

    data = request.get_json()
    task.tittle = data['title']   
    task.description = data['description']  
    task.completed = data['completed']  
    print(task)
    return jsonify({"message": "Nova tarefa criada com sucesso"})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):

    task = None
    for t in tasks:
        if t.id == id :
            task = t
    if not task:
        return  jsonify({"message" : "Não foi possivel encontrar a atividade"}),404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})



@app.route('/user/<username>')
def show_user(username):
    print(username)
    print(type(username))
    return username  

if __name__ == "__main__":
    app.run(debug=True)
