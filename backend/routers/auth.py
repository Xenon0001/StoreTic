from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import hashlib
from db import SessionLocal
from models import User
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

# Clave secreta para salt (en producción usar variable de entorno)
SECRET_KEY = "storetic_secret_dev"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    message: str

def hash_password(password: str) -> str:
    """Hashear contraseña con SHA256 + salt"""
    return hashlib.sha256((password + SECRET_KEY).encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verificar contraseña contra hash"""
    return hash_password(plain_password) == hashed_password

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Autenticar usuario"""
    user = db.query(User).filter(User.username == request.username).first()
    
    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrecto")
    
    return LoginResponse(success=True, message="Autenticado")
