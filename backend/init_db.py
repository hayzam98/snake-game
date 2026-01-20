"""
Script to initialize the database.
Creates all tables and initializes the 10 game levels.
"""
from app.database import init_db
from app.init_levels import init_levels


if __name__ == '__main__':
    print('🗄️  Creating database tables...')
    init_db()
    print('✅ Tables created successfully!')
    print('')
    init_levels()
