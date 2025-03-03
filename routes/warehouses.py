from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from models import WarehouseModel
from bson import ObjectId
from database import get_database

router = APIRouter()

@router.get("/warehouses/{sector_id}", response_model=list[WarehouseModel])
async def get_warehouses(sector_id: str, db: AsyncIOMotorDatabase = Depends(get_database), user_id: str = "65cb123456789abcd000a001"):
    warehouses = await db.warehouses.find({"sector": ObjectId(sector_id), "creator": ObjectId(user_id)}).to_list(100)
    if not warehouses:
        raise HTTPException(status_code=404, detail="No warehouses found for this sector")
    return warehouses
