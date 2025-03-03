import jwt
import datetime
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer
from passlib.context import CryptContext

SECRET_KEY = "your_secret_key"  # 🔹 Replace with a secure key
ALGORITHM = "HS256"

security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dummy users database (Replace this with MongoDB in production)
DUMMY_USERS = {
    "user1": {"id": "65cb123456789abcd000a001", "password": pwd_context.hash("password")},
    "user2": {"id": "65cb123456789abcd000a002", "password": pwd_context.hash("password")},
    "user3": {"id": "65cb123456789abcd000a003", "password": pwd_context.hash("password")},
    "user4": {"id": "65cb123456789abcd000a004", "password": pwd_context.hash("password")},
    "user5": {"id": "65cb123456789abcd000a005", "password": pwd_context.hash("password")},
}

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt_token(user_id: str):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    payload = {"sub": user_id, "exp": expiration}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Security(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
