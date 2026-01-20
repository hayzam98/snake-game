"""
Leaderboard router - Endpoints for rankings and statistics.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/leaderboard",
    tags=["leaderboard"]
)


@router.get("/", response_model=List[schemas.LeaderboardEntry])
def get_leaderboard(limit: int = 10, db: Session = Depends(get_db)):
    """
    Get the top players ranked by total score.
    
    - **limit**: Number of top players to return (default: 10, max: 100)
    
    Returns player statistics including:
    - Rank position
    - Username
    - Total score (sum of all games)
    - Number of games played
    - Highest level reached
    """
    if limit > 100:
        limit = 100
    
    leaderboard = crud.get_leaderboard(db, limit=limit)
    return leaderboard
