from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from auth import create_jwt_token, verify_password, DUMMY_USERS
from database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(user: UserLogin):
    """Authenticate user and return a JWT token"""
    db_user = DUMMY_USERS.get(user.username)

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_jwt_token(db_user["id"])
    return {"token": token}
