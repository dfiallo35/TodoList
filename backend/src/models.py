from pydantic import BaseModel
from typing import Optional


class ToDo(BaseModel):
    id_todo: int
    name: str
    description: Optional[str] = None
    checked: bool = False


class ToDoList(BaseModel):
    todos:list[ToDo] = []
    
    def append(self, elem: ToDo):
        self.todos.append(elem)
        
    def search(self, id_: int):   #delete after mocked
        for todo in self.todos:
            if todo.id_todo == id_:
                return todo
    
    def delete(self, todo: ToDo):
        self.todos.remove(todo)

 