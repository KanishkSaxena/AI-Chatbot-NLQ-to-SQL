from fastapi import FastAPI, HTTPException
from bson import ObjectId
from database import db
from models import SectorModel, WarehouseModel, LogDataModel
import os
from huggingface_hub import login
from routes import sectors,warehouses,logs,chatbot, auth


HF_TOKEN = os.getenv("HUGGING_FACE_API_KEY")
login(token=HF_TOKEN)
app = FastAPI()
app.include_router(sectors.router)
app.include_router(warehouses.router)
app.include_router(logs.router)
app.include_router(chatbot.router)
app.include_router(auth.router)



@app.get("/")
async def root():
    return {"message": "Warehouse Management API is running"}