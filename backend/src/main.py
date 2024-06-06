from typing import Union
from random import randrange
import time

from fastapi import FastAPI
from fastapi import status
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

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

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/todos",
    responses={status.HTTP_201_CREATED: {"model": ToDoList}},
)
async def read_all_todos():
    return todos


@app.get(
    "/todos/{todo_id}", 
    responses={
        status.HTTP_201_CREATED: {"model": ToDo},
        status.HTTP_404_NOT_FOUND: {}
    }
)
async def read_todo(todo_id: int):
    to_read = todos.search(todo_id)
    if to_read:
        return to_read
    return HTTPException(status_code=404, detail="Todo not found")


@app.post(
    "/todos",          
    responses={
        status.HTTP_201_CREATED: {"model": ToDo},
        status.HTTP_404_NOT_FOUND: {}
    }
)
async def create_todo(create: TodoCreateDTO):
    id_todo = randrange(1000)
    todo = todo_create_to_todo_model(create, id_todo)
    todos.append(todo)
    return todo
 

@app.put("/todos/{todo_id}",
    responses={
        status.HTTP_201_CREATED: {"model": ToDo},
        status.HTTP_404_NOT_FOUND: {}
    }
)
async def update_todo(todo_id: int, todo_update_dto: TodoUpdateDTO):
    to_update = todos.search(todo_id)
    if to_update:
        todo_update_dto_to_todo_model(todo_update_dto, to_update)
        return to_update
    return HTTPException(status_code=404, detail="Todo not found")

  
@app.patch("/todos/{todo_id}", 
    responses={
        status.HTTP_201_CREATED: {"model": ToDo},
        status.HTTP_404_NOT_FOUND: {}
    }
)
async def change_checked_todo(todo_id: int):
    to_update = todos.search(todo_id)
    if to_update:
        to_update.checked = not to_update.checked    
        return to_update
    return HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}",
    responses={
        status.HTTP_201_CREATED: {"model": ToDo},
        status.HTTP_404_NOT_FOUND: {}
    }
)
async def delete_todo(todo_id: int):
    to_delete = todos.search(todo_id)
    if to_delete:
        todos.delete(to_delete)  
        return todos
    else:
        return HTTPException(status_code=404, detail="Todo not found")
 