"""
Database configuration using SQLAlchemy 2.0.
Sets up the engine, session factory, and base model.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import get_settings

# Get settings instance
settings = get_settings()

# Create SQLAlchemy engine
# echo=True shows SQL queries in console (useful for debugging)
engine = create_engine(
    settings.database_url,
    echo=settings.DEBUG,
    pool_pre_ping=True,  # Verify connections before using them
    pool_recycle=3600,   # Recycle connections after 1 hour
)

# Create session factory
# autocommit=False: We manually commit transactions
# autoflush=False: We manually flush changes
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()


def get_db():
    """
    Dependency function to get database session.
    Used with FastAPI's Depends().
    Ensures session is closed after request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Initialize database by creating all tables.
    Call this on application startup.
    """
    Base.metadata.create_all(bind=engine)
