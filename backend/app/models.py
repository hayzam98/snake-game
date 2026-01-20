"""
SQLAlchemy database models for the Snake Game.
Models: Player, Game, Level
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Player(Base):
    """
    Player model - stores player information.
    """
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship: one player can have many games
    games = relationship("Game", back_populates="player", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Player(id={self.id}, username='{self.username}')>"


class Level(Base):
    """
    Level model - stores difficulty level configurations.
    10 levels total with increasing difficulty.
    """
    __tablename__ = "levels"
    
    id = Column(Integer, primary_key=True, index=True)
    level_number = Column(Integer, unique=True, nullable=False, index=True)
    name = Column(String(50), nullable=False)
    speed = Column(Integer, nullable=False)  # Snake speed in milliseconds
    obstacles_count = Column(Integer, default=0)  # Number of obstacles
    grid_size = Column(Integer, default=20)  # Grid size (20x20, 25x25, etc.)
    
    # Relationship: one level can have many games
    games = relationship("Game", back_populates="level")
    
    def __repr__(self):
        return f"<Level(id={self.id}, number={self.level_number}, name='{self.name}')>"


class Game(Base):
    """
    Game model - stores individual game sessions and scores.
    """
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False, index=True)
    level_id = Column(Integer, ForeignKey("levels.id"), nullable=False, index=True)
    
    score = Column(Integer, default=0)
    food_eaten = Column(Integer, default=0)  # Number of food items eaten
    duration_seconds = Column(Integer, default=0)  # Game duration
    completed = Column(Boolean, default=False)  # Did player complete the level?
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    player = relationship("Player", back_populates="games")
    level = relationship("Level", back_populates="games")
    
    def __repr__(self):
        return f"<Game(id={self.id}, player_id={self.player_id}, score={self.score})>"
