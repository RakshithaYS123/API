from pydantic import BaseModel
from datetime import date
from typing import Optional

# Pydantic model for Item


class ItemSchema(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "item_name": "Milk",
                "quantity": 3,
                "expiry_date": "2024-12-31",
            }
        }

# Pydantic model for updating Item


class UpdateItemSchema(BaseModel):
    name: Optional[str]
    email: Optional[str]
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[date]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Jane Doe",  # Example of a potential update
                "email": "jane@example.com",
                "item_name": "Cheese",
                "quantity": 5,
                "expiry_date": "2024-11-30",
            }
        }

# Pydantic model for Clock-In Record


class ClockInSchema(BaseModel):
    email: str
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john@example.com",
                "location": "Office A",
            }
        }

# Pydantic model for updating Clock-In Record


class UpdateClockInSchema(BaseModel):
    email: Optional[str]
    location: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "jane@example.com",  # Example of a potential update
                "location": "Office B",
            }
        }
