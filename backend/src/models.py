from pydantic import BaseModel
from typing import Optional


class ToDo(BaseModel):
    id_todo: int
    name: str
    description: Optional[str] = None
    checked: bool = False
    id_category:int = 0


class ToDoList(BaseModel):
    todos:list[ToDo] = []
    
    def append(self, elem: ToDo):
        self.todos.append(elem)
        
    def search(self, id_: int):
        for todo in self.todos:
            if todo.id_todo == id_:
                return todo
        # return filter(lambda todo: todo.id_todo == id, self.todos)
    
    def delete(self, todo: ToDo):
        self.todos.remove(todo)

class A:
    pan: int
    def __init__(self, pan):
        self.pan = pan
        
 