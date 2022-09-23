from typing import Optional
from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    name: str = Field(max_length=100)
    description: str
    price: float
    image: Optional[str]
    code: int 
