from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from models import SectorModel
from bson import ObjectId
from database import get_database

router = APIRouter()

@router.get("/sectors", response_model=list[SectorModel])
async def get_sectors(db: AsyncIOMotorDatabase = Depends(get_database), user_id: str = "65cb123456789abcd000a001"):
    sectors = await db.sectors.find({"creator": ObjectId(user_id), "deleted": False}).to_list(100)
    if not sectors:
        raise HTTPException(status_code=404, detail="No sectors found")
    return sectors
