# 🐍 Snake Game - Full Stack Portfolio Project

## 📝 Description
A modern Snake game built with FastAPI backend, MySQL database, and vanilla JavaScript frontend. Features 10 progressive difficulty levels, real-time score tracking, and a competitive leaderboard system.

## 🎮 Game Features
- Classic Snake gameplay with modern controls
- 10 difficulty levels (Beginner to Impossible)
- Progressive difficulty: faster speed, more obstacles, larger grids
- Real-time score tracking
- Player statistics and game history
- Global leaderboard (Top 10 players)
- Responsive web interface

## 🛠️ Technologies

### Backend
- **Python 3.13+**: Latest Python version
- **FastAPI**: Modern, fast web framework
- **SQLAlchemy 2.0**: ORM with Type-annotated Declarative Mapping
- **MySQL 8.0+**: Relational database
- **Pydantic**: Data validation
- **Pytest**: Unit and integration testing

### Frontend
- **HTML5**: Structure and Canvas API for game rendering
- **CSS3**: Modern styling with gradients and animations
- **JavaScript (ES6+)**: Game logic and API integration

### DevOps
- **Git**: Version control with GitFlow methodology
- **GitHub Actions**: CI/CD pipeline for automated testing
- **Docker**: Containerization (optional)

## 📊 Project Structure
```
snake-game-portfolio/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── main.py      # FastAPI application
│   │   ├── database.py  # Database configuration
│   │   ├── models.py    # SQLAlchemy models
│   │   ├── schemas.py   # Pydantic schemas
│   │   ├── crud.py      # Database operations
│   │   ├── config.py    # Settings management
│   │   └── routers/     # API endpoints
│   ├── tests/           # Pytest test suite
│   └── requirements.txt
├── frontend/            # Web interface
│   ├── index.html
│   ├── style.css
│   └── game.js
├── .github/
│   └── workflows/       # CI/CD configuration
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.13 or higher
- MySQL 8.0 or higher
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/snake-game-portfolio.git
cd snake-game-portfolio
```

2. **Setup backend**
```bash
cd backend
python -m venv venv

# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

3. **Configure database**
```sql
CREATE DATABASE snake_game_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

4. **Create .env file** (in backend/)
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=snake_game_db
APP_NAME=Snake Game API
APP_VERSION=1.0.0
DEBUG=True
SECRET_KEY=your-secret-key
```

5. **Initialize database**
```bash
python init_db.py
```

6. **Run the application**
```bash
uvicorn app.main:app --reload
```

7. **Open in browser**
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Game: Open `frontend/index.html` in your browser

## 🧪 Testing
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html
```

## 📈 Development Progress

- [x] Phase 1: Project setup and structure
- [x] Phase 2: Database models and CRUD operations
- [x] Phase 3: API endpoints with FastAPI
- [x] Phase 4: Frontend game interface
- [x] Phase 5: Testing and CI/CD
- [x] Phase 6: Documentation and deployment

## 🎯 API Endpoints

### Players
- `POST /players/` - Create new player
- `GET /players/{id}` - Get player by ID
- `GET /players/` - List all players

### Levels
- `GET /levels/` - List all difficulty levels
- `GET /levels/{id}` - Get specific level
- `GET /levels/number/{number}` - Get level by number (1-10)

### Games
- `POST /games/` - Start new game
- `GET /games/{id}` - Get game details
- `PUT /games/{id}` - Update game results
- `GET /games/player/{id}/history` - Get player's game history

### Leaderboard
- `GET /leaderboard/` - Get top 10 players

## 🏆 Difficulty Levels

| Level | Name         | Speed (ms) | Obstacles | Grid Size |
|-------|--------------|------------|-----------|-----------|
| 1     | Beginner     | 200        | 0         | 20x20     |
| 2     | Easy         | 180        | 2         | 20x20     |
| 3     | Novice       | 160        | 4         | 22x22     |
| 4     | Intermediate | 140        | 6         | 22x22     |
| 5     | Skilled      | 120        | 8         | 25x25     |
| 6     | Advanced     | 100        | 10        | 25x25     |
| 7     | Expert       | 90         | 12        | 28x28     |
| 8     | Master       | 80         | 15        | 30x30     |
| 9     | Insane       | 70         | 18        | 32x32     |
| 10    | Impossible   | 60         | 20        | 35x35     |

## 👤 Author

**Your Name**
- GitHub: [@hayzam98](https://github.com/hayzam98)
- LinkedIn: [Hayzam Adan](https://linkedin.com/in/hayzam-adan-martinez-3765a6102/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built as a portfolio project to demonstrate full-stack development skills
- FastAPI documentation and community
- SQLAlchemy 2.0 type-annotated mapping patterns