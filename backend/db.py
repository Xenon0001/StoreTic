# Database configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Para desarrollo: SQLite
# DATABASE_URL = "sqlite:///./storetic.db"

# Para producción: PostgreSQL
DATABASE_URL = "postgresql://storetic_user:storetic123@localhost:5432/storetic"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
