import motor.motor_asyncio
from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017/API"  # Change this to your MongoDB URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.items_database

items_collection = database.get_collection("items_collection")
clockin_collection = database.get_collection("clockin_collection")

# Helper function to parse MongoDB ObjectIDs
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "item_name": item["item_name"],
        "quantity": item["quantity"],
        "expiry_date": item["expiry_date"],
        "insert_date": item["insert_date"],
    }

def clockin_helper(clockin) -> dict:
    return {
        "id": str(clockin["_id"]),
        "email": clockin["email"],
        "location": clockin["location"],
        "insert_datetime": clockin["insert_datetime"],
    }
