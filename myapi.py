from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

#Endpoint: domain/student/1

todoList = {
    1:{
        "task": "do WADS",
        "complete": "no"
    },
    2:{
        "task": "eat lunch",
        "complete": "yes"
    },
    3:{
        "task": "do yoga",
        "complete": "no"
    }
}

class newTodo(BaseModel):
    task: str
    complete: str

class updateTodo(BaseModel):
    task: Optional[str] = None
    complete: Optional[str] = None
    

@app.get("/")
def index():
    return {"name": "task"}

##########################

@app.get("/get-all")
def index():
    return {1:{
        "task": "do WADS",
        "complete": "no"
    },
    2:{
        "task": "eat lunch",
        "complete": "yes"
    },
    3:{
        "task": "do yoga",
        "complete": "no"
    }}

@app.get("/get-todo/{todoList_id}")
def get_todo(todoList_id: int = Path(description= "ID of the todo list")):
    return todoList[todoList_id]
#../get-todo/1
# gt = greater than 
# lt = less than
# ge = greater than or equals to 
# le less than or qeuals to 

@app.get("/get-task/{todoList_id}")
def get_task(*, task: Optional[str] = None):
    for todoList_id in todoList:
        if todoList[todoList_id]["task"] == task:
            return todoList[todoList_id]
    return {"Data": "Not found"}

@app.get("/get-complete/{todoList_id}")
def get_complete(*, complete: Optional[str] = None):
    for todoList_id in todoList:
        if todoList[todoList_id]["complete"] == complete:
            return todoList[todoList_id]
    return {"Data": "Not found"}

@app.post("/create-todo/{todoList_id}")
def create_todo(todoList_id: int, newTodo: newTodo):
    if todoList_id in todoList:
        return {"Error": "duplicate task"}
    
    todoList[todoList_id] = newTodo
    return todoList[todoList_id]

@app.put("/update-todo/{todoList_id}")
def update_todo(todoList_id: int, app: updateTodo):
    if todoList_id not in todoList:
        return{"Error": "todo doesnt exist"}
    
    if todoList.task != None:
        todoList[todoList_id].task = app.task
    
    if todoList.complete != None:
        todoList[todoList_id].complete = app.complete

    return todoList[todoList_id]

@app.delete("/delete-todo/{todoList_id}")
def delete_todo(todoList_id: int):
    if todoList_id not in todoList:
        return{"error": "database not exist"}
    del todoList[todoList_id]
    return{"action": "deleted successful"}