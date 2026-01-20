"""
Pydantic schemas for request/response validation.
These define the structure of data sent to/from the API.
"""
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional


# ========== Player Schemas ==========

class PlayerBase(BaseModel):
    """Base schema with common player fields."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class PlayerCreate(PlayerBase):
    """Schema for creating a new player."""
    pass


class PlayerResponse(PlayerBase):
    """Schema for player responses (includes database fields)."""
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ========== Level Schemas ==========

class LevelBase(BaseModel):
    """Base schema with common level fields."""
    level_number: int = Field(..., ge=1, le=10)
    name: str = Field(..., max_length=50)
    speed: int = Field(..., ge=50, le=500)
    obstacles_count: int = Field(default=0, ge=0)
    grid_size: int = Field(default=20, ge=15, le=40)


class LevelCreate(LevelBase):
    """Schema for creating a new level."""
    pass


class LevelResponse(LevelBase):
    """Schema for level responses."""
    id: int
    
    model_config = ConfigDict(from_attributes=True)


# ========== Game Schemas ==========

class GameBase(BaseModel):
    """Base schema with common game fields."""
    score: int = Field(default=0, ge=0)
    food_eaten: int = Field(default=0, ge=0)
    duration_seconds: int = Field(default=0, ge=0)
    completed: bool = False


class GameCreate(BaseModel):
    """Schema for creating a new game."""
    player_id: int
    level_id: int


class GameUpdate(BaseModel):
    """Schema for updating game results."""
    score: int = Field(..., ge=0)
    food_eaten: int = Field(..., ge=0)
    duration_seconds: int = Field(..., ge=0)
    completed: bool = False


class GameResponse(GameBase):
    """Schema for game responses."""
    id: int
    player_id: int
    level_id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class GameDetailResponse(GameResponse):
    """Schema for detailed game response with related data."""
    player: PlayerResponse
    level: LevelResponse
    
    model_config = ConfigDict(from_attributes=True)


# ========== Leaderboard Schema ==========

class LeaderboardEntry(BaseModel):
    """Schema for leaderboard entries."""
    rank: int
    username: str
    total_score: int
    games_played: int
    highest_level: int
    
    model_config = ConfigDict(from_attributes=True)
