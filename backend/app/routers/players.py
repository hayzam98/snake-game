"""
Players router - Endpoints for player management.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/players",
    tags=["players"]
)


@router.post("/", response_model=schemas.PlayerResponse, status_code=status.HTTP_201_CREATED)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    """
    Create a new player.
    
    - **username**: Unique username (3-50 characters)
    - **email**: Valid email address
    """
    # Check if username already exists
    db_player = crud.get_player_by_username(db, username=player.username)
    if db_player:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Check if email already exists
    db_player = crud.get_player_by_email(db, email=player.email)
    if db_player:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    return crud.create_player(db=db, player=player)


@router.get("/{player_id}", response_model=schemas.PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)):
    """
    Get a player by ID.
    """
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    return db_player


@router.get("/", response_model=List[schemas.PlayerResponse])
def list_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all players with pagination.
    
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Maximum number of records to return (default: 100)
    """
    players = crud.get_players(db, skip=skip, limit=limit)
    return players


@router.get("/username/{username}", response_model=schemas.PlayerResponse)
def get_player_by_username(username: str, db: Session = Depends(get_db)):
    """
    Get a player by username.
    """
    db_player = crud.get_player_by_username(db, username=username)
    if db_player is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    return db_player
