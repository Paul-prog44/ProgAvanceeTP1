from flask import Flask, request
from datetime import datetime
from db import task_db
import uuid

app = Flask(__name__)

@app.get('/tasks')
def getAllTasks():
    return task_db, 200

@app.get('/tasks/<string:id>')
def getTasks(id):
    if id in task_db :
        print(id)
        return task_db[id], 200
    else: 
        print("key not found")
        return "Cette tâche n'existe pas", 404 


@app.post('/tasks')
def createTask():
    data = request.json
    if not data['name'] or not data['description'] or not data['status'] or len(data) > 3  :
        return 'Erreur dans le corps de la requête', 400
    else :
        
        newId = str(uuid.uuid4())
        task_db[newId] = {
                "task_id" : newId, 
                "name": data['name'],
                "description": data['description'],
                "status": data['status'], #« TODO », « IN_PROGRESS », « DONE ». Ces valeurs seront transmises par le front
                "created_at" : datetime.today(),
                "updated_at" : datetime.today()
        }

    return task_db[newId], 201

@app.delete('/tasks/<string:id>')
def deleteTask(id):
    task_db.pop(id)
    return "task deleted "+ str(id), 200

@app.put('/tasks/<string:id>')
def updateTask(id):
    if id in task_db :
        data = request.json
        if not data['name'] or not data['description'] or not data['status'] or len(data) > 3  :
            return 'Erreur dans le corps de la requête', 400
        else :
            task_db[id] = {
                "task_id" : id, 
                "name": data['name'],
                "description": data['description'],
                "status": data['status'],
                "created_at" : task_db[id]['created_at'],
                "updated_at" : datetime.today()
            }
        return task_db[id], 200
    else: 
        print("key not found")
        return "Cette tâche n'existe pas", 404 
    

#TODO
@app.patch('/tasks/<string:id>')
def patchTask(id):
    data = request.json
    print(data)
    return "task to be patched " + str(id)