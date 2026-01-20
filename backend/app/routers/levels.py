"""
Levels router - Endpoints for game levels.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/levels",
    tags=["levels"]
)


@router.get("/", response_model=List[schemas.LevelResponse])
def list_levels(db: Session = Depends(get_db)):
    """
    Get all game levels ordered by difficulty.
    
    Returns 10 levels from Beginner (1) to Impossible (10).
    """
    levels = crud.get_levels(db)
    return levels


@router.get("/{level_id}", response_model=schemas.LevelResponse)
def get_level(level_id: int, db: Session = Depends(get_db)):
    """
    Get a specific level by ID.
    """
    db_level = crud.get_level(db, level_id=level_id)
    if db_level is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Level not found"
        )
    return db_level


@router.get("/number/{level_number}", response_model=schemas.LevelResponse)
def get_level_by_number(level_number: int, db: Session = Depends(get_db)):
    """
    Get a level by its number (1-10).
    
    - **level_number**: Level difficulty from 1 (easiest) to 10 (hardest)
    """
    if level_number < 1 or level_number > 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Level number must be between 1 and 10"
        )
    
    db_level = crud.get_level_by_number(db, level_number=level_number)
    if db_level is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Level not found"
        )
    return db_level
