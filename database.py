from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "warehouse_management"
client = AsyncIOMotorClient(MONGO_URI)

db = client[DATABASE_NAME]

# Dependency to get database
def get_database():
    return db
