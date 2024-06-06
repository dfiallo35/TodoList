from pydantic import BaseModel
from typing import Optional

   
class TodoCreateDTO(BaseModel):
    name: str
    description: Optional[str] = None

class TodoUpdateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

# class TodoResponseDTO(BaseModel):
#     id_todo: int
#     name: str
#     description: str
#     checked: bool