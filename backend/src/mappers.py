from models import ToDo
from dto_models import TodoCreateDTO
from dto_models import  TodoUpdateDTO
# from dto_models import TodoResponseDTO

def todo_create_to_todo_model(todo_create_dto: TodoCreateDTO, id_new: int) -> ToDo:
    return ToDo(
        id_todo=id_new,
        name=todo_create_dto.name,
        description=todo_create_dto.description,
        id_category=todo_create_dto.id_category,
        checked=False
    )

# def to_todo_response_dto(todo_model: ToDo) -> TodoResponseDTO:
#     return TodoResponseDTO(
#         id_todo=todo_model.id_todo,
#         name=todo_model.name,
#         description=todo_model.description,
#         id_category=todo_model.id_category,
#         checked=todo_model.checked
#     )
    
def todo_update_dto_to_todo_model(todo_update_dto: TodoUpdateDTO, todo_model: ToDo) -> ToDo:    
    todo_model.name = todo_update_dto.name or todo_model.name
    todo_model.description = todo_update_dto.description or todo_model.description
    todo_model.id_category = todo_update_dto.id_category or todo_model.id_category
