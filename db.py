'''
Une tâche contient les attributs suivants :
task_id : uuid
name : string
description : string
status : string
created_at : str
updated_at : str
task_db est un index qui se présente sous la forme suivante :
{
"uuid1" : {
"task_id" : "uuid1",
"name": "Nom",
"description": "Desc",
"status": "TODO",
"created_at" : "date de création",
"updated_at" : "date de mise à jour"
}
}
'''
task_db = dict()