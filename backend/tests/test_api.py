"""
Integration tests for API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.init_levels import init_levels

# Test database
TEST_DATABASE_URL = "sqlite:///./test_api.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override database dependency for testing."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# Override dependency
app.dependency_overrides[get_db] = override_get_db

# Test client
client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    """Create fresh database for each test."""
    Base.metadata.create_all(bind=engine)
    # Initialize levels
    db = TestingSessionLocal()
    init_levels_test(db)
    db.close()
    yield
    Base.metadata.drop_all(bind=engine)


def init_levels_test(db):
    """Initialize levels for testing."""
    from app import crud, schemas
    
    levels_data = [
        {"level_number": 1, "name": "Beginner", "speed": 200, "obstacles_count": 0, "grid_size": 20},
        {"level_number": 2, "name": "Easy", "speed": 180, "obstacles_count": 2, "grid_size": 20},
    ]
    
    for level_data in levels_data:
        level_schema = schemas.LevelCreate(**level_data)
        crud.create_level(db, level_schema)


# ========== Root Endpoints Tests ==========

def test_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data


def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


# ========== Players Endpoints Tests ==========

def test_create_player():
    """Test creating a player."""
    response = client.post(
        "/players/",
        json={"username": "testuser", "email": "test@example.com"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_create_player_duplicate_username():
    """Test creating player with duplicate username."""
    client.post("/players/", json={"username": "duplicate", "email": "dup1@test.com"})
    response = client.post("/players/", json={"username": "duplicate", "email": "dup2@test.com"})
    assert response.status_code == 400
    assert "Username already registered" in response.json()["detail"]


def test_create_player_duplicate_email():
    """Test creating player with duplicate email."""
    client.post("/players/", json={"username": "user1", "email": "same@test.com"})
    response = client.post("/players/", json={"username": "user2", "email": "same@test.com"})
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]


def test_get_player():
    """Test getting a player by ID."""
    # Create player
    create_response = client.post(
        "/players/",
        json={"username": "getme", "email": "getme@test.com"}
    )
    player_id = create_response.json()["id"]
    
    # Get player
    response = client.get(f"/players/{player_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "getme"


def test_get_player_not_found():
    """Test getting non-existent player."""
    response = client.get("/players/9999")
    assert response.status_code == 404


def test_list_players():
    """Test listing all players."""
    # Create multiple players
    client.post("/players/", json={"username": "user1", "email": "user1@test.com"})
    client.post("/players/", json={"username": "user2", "email": "user2@test.com"})
    
    response = client.get("/players/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


# ========== Levels Endpoints Tests ==========

def test_list_levels():
    """Test listing all levels."""
    response = client.get("/levels/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2  # We created 2 levels in setup


def test_get_level():
    """Test getting a level by ID."""
    response = client.get("/levels/1")
    assert response.status_code == 200
    data = response.json()
    assert data["level_number"] == 1
    assert data["name"] == "Beginner"


def test_get_level_by_number():
    """Test getting level by number."""
    response = client.get("/levels/number/1")
    assert response.status_code == 200
    data = response.json()
    assert data["level_number"] == 1


def test_get_level_by_invalid_number():
    """Test getting level with invalid number."""
    response = client.get("/levels/number/99")
    assert response.status_code == 400


# ========== Games Endpoints Tests ==========

def test_create_game():
    """Test creating a game."""
    # Create player first
    player_response = client.post(
        "/players/",
        json={"username": "gamer", "email": "gamer@test.com"}
    )
    player_id = player_response.json()["id"]
    
    # Create game
    response = client.post(
        "/games/",
        json={"player_id": player_id, "level_id": 1}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["player_id"] == player_id
    assert data["level_id"] == 1
    assert data["score"] == 0


def test_create_game_invalid_player():
    """Test creating game with invalid player."""
    response = client.post(
        "/games/",
        json={"player_id": 9999, "level_id": 1}
    )
    assert response.status_code == 404


def test_update_game():
    """Test updating game results."""
    # Setup
    player_response = client.post("/players/", json={"username": "player", "email": "p@test.com"})
    player_id = player_response.json()["id"]
    game_response = client.post("/games/", json={"player_id": player_id, "level_id": 1})
    game_id = game_response.json()["id"]
    
    # Update game
    response = client.put(
        f"/games/{game_id}",
        json={
            "score": 1000,
            "food_eaten": 50,
            "duration_seconds": 180,
            "completed": True
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["score"] == 1000
    assert data["completed"] is True


def test_get_player_games():
    """Test getting player game history."""
    # Setup
    player_response = client.post("/players/", json={"username": "historian", "email": "hist@test.com"})
    player_id = player_response.json()["id"]
    client.post("/games/", json={"player_id": player_id, "level_id": 1})
    client.post("/games/", json={"player_id": player_id, "level_id": 2})
    
    # Get history
    response = client.get(f"/games/player/{player_id}/history")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


# ========== Leaderboard Endpoints Tests ==========

def test_get_leaderboard():
    """Test getting leaderboard."""
    # Create players and games
    p1 = client.post("/players/", json={"username": "top", "email": "top@test.com"}).json()
    p2 = client.post("/players/", json={"username": "mid", "email": "mid@test.com"}).json()
    
    g1 = client.post("/games/", json={"player_id": p1["id"], "level_id": 1}).json()
    client.put(f"/games/{g1['id']}", json={"score": 1000, "food_eaten": 50, "duration_seconds": 100, "completed": True})
    
    g2 = client.post("/games/", json={"player_id": p2["id"], "level_id": 1}).json()
    client.put(f"/games/{g2['id']}", json={"score": 500, "food_eaten": 25, "duration_seconds": 50, "completed": False})
    
    # Get leaderboard
    response = client.get("/leaderboard/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["username"] == "top"
    assert data[0]["total_score"] == 1000
    assert data[0]["rank"] == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
