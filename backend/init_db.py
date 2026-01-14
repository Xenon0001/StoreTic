"""Script para inicializar la base de datos con usuario admin por defecto"""
from db import SessionLocal, Base, engine
from models import User
from routers.auth import hash_password

def init_db():
    """Crear tablas e insertar usuario admin si no existe"""
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Verificar si el usuario admin ya existe
    admin = db.query(User).filter(User.username == "admin").first()
    if not admin:
        # Crear usuario admin
        admin_user = User(
            username="admin",
            password_hash=hash_password("admin123")
        )
        db.add(admin_user)
        db.commit()
        print("✓ Usuario admin creado: admin / admin123")
    else:
        print("✓ Usuario admin ya existe")
    
    db.close()

if __name__ == "__main__":
    init_db()
