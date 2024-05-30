
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class ToDo(BaseModel):
    id_todo: int
    name: str
    description: str
    checked: bool = False
    id_category:int


todos:dict = {}


@app.get("/todos")
async def read_all_todos():
    return todos

@app.get("/todos/{todo_id}")
async def read_todo(todo_id: int):
    return todos[todo_id].__dict__

@app.post("/todos")
async def create_todo(todo_name: str, todo_description: str = "", id_category:int = 0):
    id_todo = randrange(1000)
    todo = ToDo(id_todo = id_todo, name=todo_name, description=todo_description, id_category=id_category)
    todos[id_todo] = todo
    return todo.__dict__
    
@app.patch("/todos/{todo_id}")
async def change_checked_todo(todo_id: int):
    todos[todo_id].checked = not todos[todo_id].checked
    return todos[todo_id].__dict__    

@app.patch("/todos/{todo_name}")
async def change_name_todo(todo_id: int, new_name: str):
    todos[todo_id].checked = new_name
    return todos[todo_id].__dict__    

@app.patch("/todos/{todo_description}")
async def change_description_todo(todo_id: int, new_description: str):
    todos[todo_id].checked = new_description
    return todos[todo_id].__dict__    

@app.patch("/todos/{todo_category}")
async def change_category_todo(todo_id: int, new_category: str):
    todos[todo_id].checked = new_category
    return todos[todo_id].__dict__    

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    del todos[todo_id]
    return todos  