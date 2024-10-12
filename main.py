from fastapi import FastAPI, HTTPException
from api.crud import (
    add_item,
    retrieve_item,
    filter_items,
    update_item,
    delete_item,
    add_clockin,
    retrieve_clockin,
    filter_clockins,
    update_clockin,
    delete_clockin,
)
from api.models import ItemSchema, UpdateItemSchema, ClockInSchema, UpdateClockInSchema

app = FastAPI()


@app.get("/")
async def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the API!"}

# Items Routes


@app.post("/items", response_model=ItemSchema)
async def create_item(item: ItemSchema):
    """Create a new item."""
    new_item = await add_item(item.dict())
    return new_item


@app.get("/items/{id}", response_model=ItemSchema)
async def get_item(id: str):
    """Retrieve an item by its ID."""
    item = await retrieve_item(id)
    if item:
        return item
    raise HTTPException(status_code=404, detail=f"Item {id} not found")


@app.get("/items/filter")
async def filter_items_api(
    email: str = None,
    expiry_date: str = None,
    insert_date: str = None,
    quantity: int = None,
):
    """Filter items based on provided query parameters."""
    filtered_items = await filter_items(email, expiry_date, insert_date, quantity)
    return filtered_items


@app.put("/items/{id}", response_model=dict)
async def update_item_api(id: str, item: UpdateItemSchema):
    """Update an existing item."""
    updated = await update_item(id, item.dict(exclude_unset=True))
    if updated:
        return {"msg": "Item updated successfully"}
    raise HTTPException(status_code=404, detail=f"Item {id} not found")


@app.delete("/items/{id}", response_model=dict)
async def delete_item_api(id: str):
    """Delete an item by its ID."""
    deleted = await delete_item(id)
    if deleted:
        return {"msg": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Item {id} not found")

# Clock-In Routes


@app.post("/clock-in", response_model=ClockInSchema)
async def clockin_user(clockin: ClockInSchema):
    """Create a new clock-in record."""
    new_clockin = await add_clockin(clockin.dict())
    return new_clockin


@app.get("/clock-in/{id}", response_model=ClockInSchema)
async def get_clockin(id: str):
    """Retrieve a clock-in record by its ID."""
    clockin = await retrieve_clockin(id)
    if clockin:
        return clockin
    raise HTTPException(
        status_code=404, detail=f"Clock-In record {id} not found")


@app.get("/clock-in/filter")
async def filter_clockins_api(
    email: str = None,
    location: str = None,
    insert_datetime: str = None,
):
    """Filter clock-in records based on provided query parameters."""
    filtered_clockins = await filter_clockins(email, location, insert_datetime)
    return filtered_clockins


@app.put("/clock-in/{id}", response_model=dict)
async def update_clockin_api(id: str, clockin: UpdateClockInSchema):
    """Update an existing clock-in record."""
    updated = await update_clockin(id, clockin.dict(exclude_unset=True))
    if updated:
        return {"msg": "Clock-In updated successfully"}
    raise HTTPException(status_code=404, detail=f"Clock-In {id} not found")


@app.delete("/clock-in/{id}", response_model=dict)
async def delete_clockin_api(id: str):
    """Delete a clock-in record by its ID."""
    deleted = await delete_clockin(id)
    if deleted:
        return {"msg": "Clock-In deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Clock-In {id} not found")
