from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from models import LogDataModel
from bson import ObjectId
from database import get_database
from datetime import datetime

router = APIRouter()

@router.get("/logdata/start/{warehouse_id}")
async def start_logging(warehouse_id: str, db: AsyncIOMotorDatabase = Depends(get_database), user_id: str = "65cb123456789abcd000a001"):
    warehouse = await db.warehouses.find_one({"_id": ObjectId(warehouse_id), "creator": ObjectId(user_id)})
    
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found or access denied")

    columns = warehouse.get("columns", [])
    
    if not columns:
        raise HTTPException(status_code=400, detail="No inventory columns found for this warehouse")

    questions = [{"title": col["title"], "dataIndex": col["dataIndex"]} for col in columns if col["dataIndex"] != "day"]
    
    return {"message": "Please provide inventory counts for the following:", "questions": questions}

@router.post("/logdata/submit/{warehouse_id}")
async def submit_log(warehouse_id: str, logData: dict, db: AsyncIOMotorDatabase = Depends(get_database), user_id: str = "65cb123456789abcd000a001"):
    warehouse = await db.warehouses.find_one({"_id": ObjectId(warehouse_id), "creator": ObjectId(user_id)})
    
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found or access denied")

    # Ensure log data follows the warehouse structure
    columns = {col["dataIndex"]: col["title"] for col in warehouse.get("columns", [])}
    for key in logData.keys():
        if key not in columns:
            raise HTTPException(status_code=400, detail=f"Invalid dataIndex: {key}")

    log_entry = {
        "_id": ObjectId(),
        "warehouse": ObjectId(warehouse_id),
        "creator": ObjectId(user_id),
        "logData": {
            "day": datetime.utcnow().isoformat(),
            **logData
        }
    }

    await db.logdatas.insert_one(log_entry)
    
    return {"message": "Log entry added successfully", "log_entry": log_entry}
