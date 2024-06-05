
from typing import Union
from fastapi import FastAPI
from random import randrange

from models import ToDo
from models import ToDoList

from dto_models import TodoCreateDTO
# from dto_models import TodoResponseDTO
from dto_models import TodoUpdateDTO

# from mappers import to_todo_response_dto
from mappers import todo_create_to_todo_model
from mappers import todo_update_dto_to_todo_model


app = FastAPI()
todos: ToDoList = ToDoList()

@app.get("/todos",
         response_model = ToDoList,
         )
async def read_all_todos():
    return todos


@app.get("/todos/{todo_id}", 
         response_model=ToDo,
        #  responses={status.HTTP_201_CREATED: {"model": ToDo}}
         )
async def read_todo(todo_id: int):
    to_read = todos.search(todo_id)
    if to_read:
        return to_read
    return HTTPException(status_code=404, detail="Todo not found")


@app.post("/todos", 
          response_model=ToDo,
          )
async def create_todo(create: TodoCreateDTO):
    id_todo = randrange(1000)
    todo = todo_create_to_todo_model(create, id_todo)
    todos.append(todo)
    return todo
 

@app.put("/todos/{todo_id}",
         response_model=ToDo,
         )
async def update_todo(todo_id: int, todo_update_dto: TodoUpdateDTO):
    to_update = todos.search(todo_id)
    if to_update:
        todo_update_dto_to_todo_model(todo_update_dto, to_update)
        return to_update
    return HTTPException(status_code=404, detail="Todo not found")

  
@app.patch("/todos/{todo_id}", 
           response_model=ToDo,
           )
async def change_checked_todo(todo_id: int):
    to_update = todos.search(todo_id)
    if to_update:
        to_update.checked = not to_update.checked    
        return to_update
    return HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}",
            response_model = ToDoList,
            )
async def delete_todo(todo_id: int):
    to_delete = todos.search(todo_id)
    if to_delete:
        todos.delete(to_delete)  
        return todos
    else:
        return HTTPException(status_code=404, detail="Todo not found")
 