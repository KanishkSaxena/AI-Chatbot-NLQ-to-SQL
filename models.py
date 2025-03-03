from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List, Dict, Optional

# Fix for PyObjectId to handle validation properly
class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

# Sector Model
class SectorModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    creator: PyObjectId
    location: str
    deleted: Optional[bool] = False

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Warehouse Model
class WarehouseModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    creator: PyObjectId
    sector: PyObjectId
    columns: List[Dict[str, str]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Log Data Model
class LogDataModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    warehouse: PyObjectId
    creator: PyObjectId
    logData: Dict[str, int]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
