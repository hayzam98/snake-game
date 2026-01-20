"""
Unit tests for database models and CRUD operations.
"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app import models, schemas, crud


# Create in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db():
    """Create a fresh database for each test."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


def test_create_player(db):
    """Test creating a player."""
    player_data = schemas.PlayerCreate(
        username="testuser",
        email="test@example.com"
    )
    player = crud.create_player(db, player_data)
    
    assert player.id is not None
    assert player.username == "testuser"
    assert player.email == "test@example.com"
    assert player.created_at is not None


def test_get_player_by_username(db):
    """Test retrieving a player by username."""
    # Create player
    player_data = schemas.PlayerCreate(username="findme", email="findme@example.com")
    created_player = crud.create_player(db, player_data)
    
    # Find player
    found_player = crud.get_player_by_username(db, "findme")
    
    assert found_player is not None
    assert found_player.id == created_player.id
    assert found_player.username == "findme"


def test_create_level(db):
    """Test creating a level."""
    level_data = schemas.LevelCreate(
        level_number=1,
        name="Test Level",
        speed=150,
        obstacles_count=5,
        grid_size=20
    )
    level = crud.create_level(db, level_data)
    
    assert level.id is not None
    assert level.level_number == 1
    assert level.name == "Test Level"
    assert level.speed == 150
    assert level.obstacles_count == 5


def test_get_levels(db):
    """Test retrieving all levels."""
    # Create multiple levels
    for i in range(1, 4):
        level_data = schemas.LevelCreate(
            level_number=i,
            name=f"Level {i}",
            speed=200 - (i * 10),
            obstacles_count=i * 2,
            grid_size=20
        )
        crud.create_level(db, level_data)
    
    # Get all levels
    levels = crud.get_levels(db)
    
    assert len(levels) == 3
    assert levels[0].level_number == 1
    assert levels[2].level_number == 3


def test_create_game(db):
    """Test creating a game."""
    # Create player and level first
    player_data = schemas.PlayerCreate(username="gamer", email="gamer@example.com")
    player = crud.create_player(db, player_data)
    
    level_data = schemas.LevelCreate(
        level_number=1, name="Easy", speed=150, obstacles_count=2, grid_size=20
    )
    level = crud.create_level(db, level_data)
    
    # Create game
    game_data = schemas.GameCreate(player_id=player.id, level_id=level.id)
    game = crud.create_game(db, game_data)
    
    assert game.id is not None
    assert game.player_id == player.id
    assert game.level_id == level.id
    assert game.score == 0
    assert game.completed is False


def test_update_game(db):
    """Test updating game results."""
    # Setup
    player = crud.create_player(db, schemas.PlayerCreate(username="player1", email="p1@test.com"))
    level = crud.create_level(db, schemas.LevelCreate(
        level_number=1, name="Level1", speed=150, obstacles_count=0, grid_size=20
    ))
    game = crud.create_game(db, schemas.GameCreate(player_id=player.id, level_id=level.id))
    
    # Update game
    update_data = schemas.GameUpdate(
        score=500,
        food_eaten=25,
        duration_seconds=120,
        completed=True
    )
    updated_game = crud.update_game(db, game.id, update_data)
    
    assert updated_game.score == 500
    assert updated_game.food_eaten == 25
    assert updated_game.duration_seconds == 120
    assert updated_game.completed is True


def test_get_leaderboard(db):
    """Test leaderboard calculation."""
    # Create players
    player1 = crud.create_player(db, schemas.PlayerCreate(username="top_player", email="top@test.com"))
    player2 = crud.create_player(db, schemas.PlayerCreate(username="mid_player", email="mid@test.com"))
    
    # Create levels
    level1 = crud.create_level(db, schemas.LevelCreate(
        level_number=1, name="Easy", speed=150, obstacles_count=0, grid_size=20
    ))
    level2 = crud.create_level(db, schemas.LevelCreate(
        level_number=2, name="Medium", speed=120, obstacles_count=5, grid_size=22
    ))
    
    # Create games for player1 (higher score)
    game1 = crud.create_game(db, schemas.GameCreate(player_id=player1.id, level_id=level1.id))
    crud.update_game(db, game1.id, schemas.GameUpdate(score=1000, food_eaten=50, duration_seconds=180, completed=True))
    
    game2 = crud.create_game(db, schemas.GameCreate(player_id=player1.id, level_id=level2.id))
    crud.update_game(db, game2.id, schemas.GameUpdate(score=1500, food_eaten=75, duration_seconds=200, completed=True))
    
    # Create game for player2 (lower score)
    game3 = crud.create_game(db, schemas.GameCreate(player_id=player2.id, level_id=level1.id))
    crud.update_game(db, game3.id, schemas.GameUpdate(score=800, food_eaten=40, duration_seconds=150, completed=False))
    
    # Get leaderboard
    leaderboard = crud.get_leaderboard(db, limit=10)
    
    assert len(leaderboard) == 2
    assert leaderboard[0]['username'] == 'top_player'
    assert leaderboard[0]['total_score'] == 2500
    assert leaderboard[0]['games_played'] == 2
    assert leaderboard[1]['username'] == 'mid_player'
    assert leaderboard[1]['total_score'] == 800


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
