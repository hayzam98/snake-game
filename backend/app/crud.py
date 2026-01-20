"""
CRUD operations (Create, Read, Update, Delete) for database models.
These functions handle all database interactions.
"""
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from typing import List, Optional
from app import models, schemas


# ========== Player CRUD ==========

def create_player(db: Session, player: schemas.PlayerCreate) -> models.Player:
    """Create a new player in the database."""
    db_player = models.Player(
        username=player.username,
        email=player.email
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)  # Get the player with the generated ID
    return db_player


def get_player(db: Session, player_id: int) -> Optional[models.Player]:
    """Get a player by ID."""
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def get_player_by_username(db: Session, username: str) -> Optional[models.Player]:
    """Get a player by username."""
    return db.query(models.Player).filter(models.Player.username == username).first()


def get_player_by_email(db: Session, email: str) -> Optional[models.Player]:
    """Get a player by email."""
    return db.query(models.Player).filter(models.Player.email == email).first()


def get_players(db: Session, skip: int = 0, limit: int = 100) -> List[models.Player]:
    """Get all players with pagination."""
    return db.query(models.Player).offset(skip).limit(limit).all()


# ========== Level CRUD ==========

def create_level(db: Session, level: schemas.LevelCreate) -> models.Level:
    """Create a new level in the database."""
    db_level = models.Level(
        level_number=level.level_number,
        name=level.name,
        speed=level.speed,
        obstacles_count=level.obstacles_count,
        grid_size=level.grid_size
    )
    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    return db_level


def get_level(db: Session, level_id: int) -> Optional[models.Level]:
    """Get a level by ID."""
    return db.query(models.Level).filter(models.Level.id == level_id).first()


def get_level_by_number(db: Session, level_number: int) -> Optional[models.Level]:
    """Get a level by level number."""
    return db.query(models.Level).filter(models.Level.level_number == level_number).first()


def get_levels(db: Session) -> List[models.Level]:
    """Get all levels ordered by level number."""
    return db.query(models.Level).order_by(models.Level.level_number).all()


# ========== Game CRUD ==========

def create_game(db: Session, game: schemas.GameCreate) -> models.Game:
    """Create a new game session."""
    db_game = models.Game(
        player_id=game.player_id,
        level_id=game.level_id
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def update_game(db: Session, game_id: int, game_update: schemas.GameUpdate) -> Optional[models.Game]:
    """Update game results after playing."""
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if db_game:
        db_game.score = game_update.score
        db_game.food_eaten = game_update.food_eaten
        db_game.duration_seconds = game_update.duration_seconds
        db_game.completed = game_update.completed
        db.commit()
        db.refresh(db_game)
    return db_game


def get_game(db: Session, game_id: int) -> Optional[models.Game]:
    """Get a game by ID."""
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_player_games(db: Session, player_id: int, skip: int = 0, limit: int = 50) -> List[models.Game]:
    """Get all games for a specific player."""
    return (
        db.query(models.Game)
        .filter(models.Game.player_id == player_id)
        .order_by(desc(models.Game.created_at))
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_leaderboard(db: Session, limit: int = 10) -> List[dict]:
    """
    Get top players by total score.
    Returns a list of dictionaries with player stats.
    """
    results = (
        db.query(
            models.Player.username,
            func.sum(models.Game.score).label('total_score'),
            func.count(models.Game.id).label('games_played'),
            func.max(models.Level.level_number).label('highest_level')
        )
        .join(models.Game, models.Player.id == models.Game.player_id)
        .join(models.Level, models.Game.level_id == models.Level.id)
        .group_by(models.Player.id)
        .order_by(desc('total_score'))
        .limit(limit)
        .all()
    )
    
    leaderboard = []
    for rank, row in enumerate(results, start=1):
        leaderboard.append({
            'rank': rank,
            'username': row.username,
            'total_score': row.total_score,
            'games_played': row.games_played,
            'highest_level': row.highest_level
        })
    
    return leaderboard
