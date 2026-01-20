"""
Initialize the 10 game levels with predefined configurations.
Run this once to populate the levels table.
"""
from app.database import SessionLocal
from app import crud, schemas


def init_levels():
    """Create the 10 difficulty levels."""
    db = SessionLocal()
    
    # Check if levels already exist
    existing_levels = crud.get_levels(db)
    if existing_levels:
        print(f"✅ Levels already initialized ({len(existing_levels)} levels found)")
        db.close()
        return
    
    # Define 10 levels with increasing difficulty
    levels_data = [
        {"level_number": 1, "name": "Beginner", "speed": 200, "obstacles_count": 0, "grid_size": 20},
        {"level_number": 2, "name": "Easy", "speed": 180, "obstacles_count": 2, "grid_size": 20},
        {"level_number": 3, "name": "Novice", "speed": 160, "obstacles_count": 4, "grid_size": 22},
        {"level_number": 4, "name": "Intermediate", "speed": 140, "obstacles_count": 6, "grid_size": 22},
        {"level_number": 5, "name": "Skilled", "speed": 120, "obstacles_count": 8, "grid_size": 25},
        {"level_number": 6, "name": "Advanced", "speed": 100, "obstacles_count": 10, "grid_size": 25},
        {"level_number": 7, "name": "Expert", "speed": 90, "obstacles_count": 12, "grid_size": 28},
        {"level_number": 8, "name": "Master", "speed": 80, "obstacles_count": 15, "grid_size": 30},
        {"level_number": 9, "name": "Insane", "speed": 70, "obstacles_count": 18, "grid_size": 32},
        {"level_number": 10, "name": "Impossible", "speed": 60, "obstacles_count": 20, "grid_size": 35},
    ]
    
    print("🎮 Initializing 10 game levels...")
    
    for level_data in levels_data:
        level_schema = schemas.LevelCreate(**level_data)
        db_level = crud.create_level(db, level_schema)
        print(f"  ✓ Level {db_level.level_number}: {db_level.name} created")
    
    print("✅ All levels initialized successfully!")
    db.close()


if __name__ == "__main__":
    init_levels()
