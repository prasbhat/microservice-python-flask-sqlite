from flask import Flask, request, jsonify, abort
from .models import Tasks, TodoTaskComments
from datetime import datetime,date
from . import engine
import json
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
Session = sessionmaker(bind= engine)

@app.route('/todo-app/tasks/', methods=['POST'])
def create_task():
    record = json.loads(request.data)
    task = Tasks(title = record.get('title'), description = record.get('description'), status = record.get('status'), 
    dueDate = datetime.strptime(record.get('dueDate'), '%Y-%m-%d').date(), creationDate = date.today())
    
    with Session() as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        
    return __jsonResponse(task, None), 201

def __jsonResponse(task, todoTaskCommentsList):
    todoTaskCommentSet = []
    taskDict = {
        'systemTaskId' : task.systemTaskId,
        'title' : task.title,
        'description' : task.description,
        'status' : task.status,
        'dueDate' : task.dueDate,
        'creationDate' : task.creationDate,
        'todoTaskCommentSet' : todoTaskCommentSet,
        }
    
    if (todoTaskCommentsList is not None):
        for todoTaskComment in todoTaskCommentsList:
            todoTaskCommentDict = {
                'systemTodoTaskCommentsId': todoTaskComment.systemTodoTaskCommentsId,
                'taskComments': todoTaskComment.taskComments,
                'creationDate': todoTaskComment.creationDate,
                'task_systemTaskId': todoTaskComment.task_systemTaskId
            }

            taskDict["todoTaskCommentSet"].append(todoTaskCommentDict)
       
    return taskDict

@app.route('/todo-app/tasks/', methods=['GET'])
def get_all():
    with Session() as session:
        data = []
        taskList = session.query(Tasks).all()
        
        for task in taskList:
            todoTaskCommentsList = session.query(TodoTaskComments).filter(TodoTaskComments.task_systemTaskId == task.systemTaskId)
            data.append(__jsonResponse(task, todoTaskCommentsList))
        
    return data

@app.route('/todo-app/tasks/<int:id>', methods=['GET'])
def get_one_task(id):
    with Session() as session:
        task = session.query(Tasks).get(id)

    if task is None:
        abort(404)

    return jsonify(__jsonResponse(task, task.todoTaskCommentsSet))

@app.route('/todo-app/tasks/', methods=['PUT'])
def update_task():
    record = json.loads(request.data)
    print(record)
    
    with Session() as session:
        data = []
        task = session.query(Tasks).get(record.get('systemTasksId'))
        if task is None:
            abort(404)

        task.title = record.get('title')
        task.description = record.get('description')
        task.status = record.get('status')
        task.dueDate = datetime.strptime(record.get('dueDate'), '%Y-%m-%d').date()

        for taskComment in record['todoTaskCommentsSet']:
            todoTaskCommentsSet = TodoTaskComments(taskComments = taskComment['taskComments'], creationDate = date.today(), task_systemTaskId=task.systemTaskId)
            session.add(todoTaskCommentsSet)
        
        session.commit()
        session.refresh(task)

        data.append(__jsonResponse(task, task.todoTaskCommentsSet))
    return data    

@app.route("/todo-app/tasks/<int:id>", methods=["DELETE"])
def delete_one_task(id):
    with Session() as session:
        task = session.query(Tasks).get(id)
        if task is None:
            abort(404)
        
        session.delete(task)
        session.commit()
    return jsonify({'result': True})

@app.route("/todo-app/tasks/", methods=["DELETE"])
def delete_all():
    with Session() as session:
        taskList = session.query(Tasks).all()
        if taskList is None:
            abort(404)

        for task in taskList:
            session.delete(task)
            session.commit()

    return jsonify({'result': True})
