from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass  # Used when creating a new category

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True
