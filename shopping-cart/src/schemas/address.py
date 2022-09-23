import email
from typing import List
from pydantic import BaseModel, Field



class Address(BaseModel):
    street: str
    cep: str
    district: str
    city: str
    state: str
    is_delivery: bool = Field(default=True)

class UserAddress(BaseModel):
    id: str
    email: str
class AddressSchema(BaseModel):
    user: UserAddress
    address: List[Address] = []

