"""
Games router - Endpoints for game sessions and scores.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/games",
    tags=["games"]
)


@router.post("/", response_model=schemas.GameResponse, status_code=status.HTTP_201_CREATED)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    """
    Start a new game session.
    
    - **player_id**: ID of the player starting the game
    - **level_id**: ID of the level to play
    """
    # Verify player exists
    db_player = crud.get_player(db, player_id=game.player_id)
    if db_player is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    
    # Verify level exists
    db_level = crud.get_level(db, level_id=game.level_id)
    if db_level is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Level not found"
        )
    
    return crud.create_game(db=db, game=game)


@router.get("/{game_id}", response_model=schemas.GameDetailResponse)
def get_game(game_id: int, db: Session = Depends(get_db)):
    """
    Get a game by ID with player and level details.
    """
    db_game = crud.get_game(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )
    return db_game


@router.put("/{game_id}", response_model=schemas.GameResponse)
def update_game(game_id: int, game_update: schemas.GameUpdate, db: Session = Depends(get_db)):
    """
    Update game results after playing.
    
    - **score**: Final score achieved
    - **food_eaten**: Number of food items eaten
    - **duration_seconds**: Total game duration in seconds
    - **completed**: Whether the level was completed
    """
    db_game = crud.update_game(db, game_id=game_id, game_update=game_update)
    if db_game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )
    return db_game


@router.get("/player/{player_id}/history", response_model=List[schemas.GameDetailResponse])
def get_player_games(
    player_id: int,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """
    Get game history for a specific player.
    
    - **player_id**: ID of the player
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Maximum number of records to return (default: 50)
    """
    # Verify player exists
    db_player = crud.get_player(db, player_id=player_id)
    if db_player is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    
    games = crud.get_player_games(db, player_id=player_id, skip=skip, limit=limit)
    return games
