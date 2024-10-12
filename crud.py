from bson.objectid import ObjectId
from datetime import datetime
from api.database import items_collection, clockin_collection, item_helper, clockin_helper

# Create a new item
async def add_item(item_data: dict) -> dict:
    item_data["insert_date"] = datetime.utcnow().date()
    item = await items_collection.insert_one(item_data)
    new_item = await items_collection.find_one({"_id": item.inserted_id})
    return item_helper(new_item)

# Retrieve an item by ID
async def retrieve_item(id: str) -> dict:
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item_helper(item)

# Filter items
async def filter_items(email=None, expiry_date=None, insert_date=None, quantity=None):
    query = {}
    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gt": expiry_date}
    if insert_date:
        query["insert_date"] = {"$gt": insert_date}
    if quantity:
        query["quantity"] = {"$gte": quantity}
    
    items = []
    async for item in items_collection.find(query):
        items.append(item_helper(item))
    return items

# Aggregation to count items per email
async def aggregate_items_by_email():
    pipeline = [
        {"$group": {"_id": "$email", "count": {"$sum": 1}}}
    ]
    result = await items_collection.aggregate(pipeline).to_list(length=None)
    return result

# Update an item by ID
async def update_item(id: str, data: dict):
    if len(data) < 1:
        return False
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        updated_item = await items_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_item:
            return True
    return False

# Delete an item by ID
async def delete_item(id: str):
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        await items_collection.delete_one({"_id": ObjectId(id)})
        return True

# Clock-In CRUD
async def add_clockin(data: dict) -> dict:
    data["insert_datetime"] = datetime.utcnow()
    clockin = await clockin_collection.insert_one(data)
    new_clockin = await clockin_collection.find_one({"_id": clockin.inserted_id})
    return clockin_helper(new_clockin)

async def retrieve_clockin(id: str) -> dict:
    clockin = await clockin_collection.find_one({"_id": ObjectId(id)})
    if clockin:
        return clockin_helper(clockin)

# Filter Clock-In Records
async def filter_clockins(email=None, location=None, insert_datetime=None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gt": insert_datetime}
    
    clockins = []
    async for clockin in clockin_collection.find(query):
        clockins.append(clockin_helper(clockin))
    return clockins

async def update_clockin(id: str, data: dict):
    if len(data) < 1:
        return False
    clockin = await clockin_collection.find_one({"_id": ObjectId(id)})
    if clockin:
        updated_clockin = await clockin_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_clockin:
            return True
    return False

async def delete_clockin(id: str):
    clockin = await clockin_collection.find_one({"_id": ObjectId(id)})
    if clockin:
        await clockin_collection.delete_one({"_id": ObjectId(id)})
        return True
