from flask import Flask, request
from datetime import date
from db import task_db
import uuid

app = Flask(__name__)

@app.get('/tasks')
def getAllTasks():
    return task_db

@app.get('/tasks/<uuid:id>')
def getTasks(id):
    return "Get app id: " + str(id)

@app.post('/tasks')
def createTask():
    data = request.json
    print(data)
    newId = str(uuid.uuid4())
    task_db[newId] = {
        "task_id" : newId, 
        "name": data['name'],
        "description": data['description'],
        "status": data['status'],
        "created_at" : date.today(),
        "updated_at" : date.today()
    }
    return task_db[newId] 

@app.delete('/tasks/<string:id>')
def deleteTask(id):
    task_db.pop(id)
    return "task deleted "+ id

@app.put('/tasks/<string:id>')
def updateTask(id):
    data = request.json
    task_db[id] = {
        "task_id" : id, 
        "name": data['name'],
        "description": data['description'],
        "status": data['status'],
        "updated_at" : date.today()
    }
    return task_db[id]

@app.patch('/tasks/<uuid:id>')
def patchTask(id):
    return "task to be patched " + str(id)