from pydantic import BaseModel
from typing import Optional

   
class TodoCreateDTO(BaseModel):
    name: str
    description: Optional[str] = None
    id_category: int = 0

class TodoUpdateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    id_category: Optional[int] = None

# class TodoResponseDTO(BaseModel):
#     id_todo: int
#     name: str
#     description: str
#     id_category: int
#     checked: bool