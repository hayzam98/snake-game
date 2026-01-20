# 🐍 Snake Game - Full Stack Portfolio Project

[![CI/CD Pipeline](https://github.com/hayzam98/snake-game-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/hayzam98/snake-game-portfolio/actions/workflows/ci.yml)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1.svg)](https://www.mysql.com/)
[![CI/CD Pipeline](https://github.com/hayzam98/snake-game-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/hayzam98/snake-game-portfolio/actions/workflows/ci.yml)

> Un juego de la serpiente clásico con 10 niveles de dificultad progresiva, backend FastAPI, base de datos MySQL y frontend vanilla JavaScript.

## 📝 Descripción

Proyecto full stack que demuestra conocimientos en:
- **Backend**: Python, FastAPI, SQLAlchemy 2.0, MySQL
- **Frontend**: HTML5, CSS3, JavaScript (Canvas API)
- **Testing**: Pytest (35 tests con 100% aprobación)
- **CI/CD**: GitHub Actions
- **Git**: GitFlow con branches y pull requests

## 🎮 Características del Juego

- 🐍 Juego Snake clásico con controles de teclado
- 📊 10 niveles de dificultad progresiva (Beginner → Impossible)
- 🏆 Sistema de leaderboard global (Top 10)
- 📈 Estadísticas de jugador (puntuación, partidas jugadas, nivel máximo)
- ⏸️ Pausa/Resume
- 💾 Persistencia de datos en MySQL
- 🎨 Interfaz moderna y responsive

## 🛠️ Stack Tecnológico

### Backend
| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.13+ | Lenguaje principal |
| FastAPI | 0.115.0 | Framework web |
| SQLAlchemy | 2.0.35 | ORM (Type-annotated Mapping) |
| MySQL | 8.0+ | Base de datos relacional |
| Pydantic | 2.9.2 | Validación de datos |
| Pytest | 8.3.3 | Framework de testing |
| Uvicorn | 0.32.0 | Servidor ASGI |

### Frontend
- **HTML5**: Estructura y Canvas API
- **CSS3**: Estilos modernos con gradientes y animaciones
- **JavaScript ES6+**: Lógica del juego y comunicación con API

### DevOps
- **Git**: Control de versiones con GitFlow
- **GitHub Actions**: CI/CD automatizado
- **pytest-cov**: Cobertura de tests

## 📊 Estructura del Proyecto
```
snake-game-portfolio/
├── backend/                    # Backend FastAPI
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # Aplicación FastAPI
│   │   ├── config.py          # Configuración (pydantic-settings)
│   │   ├── database.py        # SQLAlchemy setup
│   │   ├── models.py          # Modelos de base de datos
│   │   ├── schemas.py         # Schemas Pydantic
│   │   ├── crud.py            # Operaciones CRUD
│   │   └── routers/           # Endpoints de la API
│   │       ├── players.py     # Gestión de jugadores
│   │       ├── levels.py      # Niveles de dificultad
│   │       ├── games.py       # Sesiones de juego
│   │       └── leaderboard.py # Rankings
│   ├── tests/
│   │   ├── test_models.py     # Tests de modelos (10 tests)
│   │   └── test_api.py        # Tests de API (25 tests)
│   ├── requirements.txt       # Dependencias Python
│   ├── pytest.ini             # Configuración de pytest
│   └── init_db.py             # Script de inicialización
├── frontend/                   # Frontend web
│   ├── index.html             # Estructura HTML
│   ├── style.css              # Estilos CSS
│   └── game.js                # Lógica del juego
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD
├── .gitignore
└── README.md
```

## 🚀 Instalación y Uso

### Prerrequisitos

- Python 3.13 o superior
- MySQL 8.0 o superior
- Git

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/hayzam98/snake-game-portfolio.git
cd snake-game-portfolio
```

### Paso 2: Configurar Backend
```bash
# Navegar a backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 3: Configurar Base de Datos

**Opción 1: MySQL Workbench**
```sql
CREATE DATABASE snake_game_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

**Opción 2: Terminal**
```bash
mysql -u root -p
CREATE DATABASE snake_game_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### Paso 4: Configurar Variables de Entorno

Crea el archivo `backend/.env`:
```env
# Database
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=snake_game_db

# Application
APP_NAME=Snake Game API
APP_VERSION=1.0.0
DEBUG=True

# Security
SECRET_KEY=your-secret-key-here
```

### Paso 5: Inicializar Base de Datos
```bash
# Desde backend/ con venv activado
python init_db.py
```

Deberías ver:
```
🗄️  Creating database tables...
✅ Tables created successfully!

🎮 Initializing 10 game levels...
  ✓ Level 1: Beginner created
  ...
  ✓ Level 10: Impossible created
✅ All levels initialized successfully!
```

### Paso 6: Ejecutar Backend
```bash
uvicorn app.main:app --reload
```

La API estará disponible en:
- **API**: http://localhost:8000
- **Documentación Swagger**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Paso 7: Abrir Frontend

1. Navega a la carpeta `frontend/`
2. Abre `index.html` en tu navegador

## 🧪 Testing
```bash
# Ejecutar todos los tests
pytest tests/ -v

# Ejecutar con cobertura
pytest tests/ --cov=app --cov-report=html

# Ejecutar solo tests de modelos
pytest tests/test_models.py -v

# Ejecutar solo tests de API
pytest tests/test_api.py -v
```

**Resultados esperados**: 35 tests pasando (10 modelos + 25 API)

## 📊 API Endpoints

### Players
- `POST /players/` - Crear jugador
- `GET /players/{id}` - Obtener jugador por ID
- `GET /players/` - Listar jugadores
- `GET /players/username/{username}` - Buscar por username

### Levels
- `GET /levels/` - Listar todos los niveles
- `GET /levels/{id}` - Obtener nivel por ID
- `GET /levels/number/{number}` - Obtener nivel por número (1-10)

### Games
- `POST /games/` - Iniciar nueva partida
- `GET /games/{id}` - Obtener partida
- `PUT /games/{id}` - Actualizar resultados
- `GET /games/player/{id}/history` - Historial del jugador

### Leaderboard
- `GET /leaderboard/` - Top 10 jugadores

## 🏆 Niveles de Dificultad

| Nivel | Nombre       | Velocidad | Obstáculos | Tamaño Grid |
|-------|--------------|-----------|------------|-------------|
| 1     | Beginner     | 200ms     | 0          | 20x20       |
| 2     | Easy         | 180ms     | 2          | 20x20       |
| 3     | Novice       | 160ms     | 4          | 22x22       |
| 4     | Intermediate | 140ms     | 6          | 22x22       |
| 5     | Skilled      | 120ms     | 8          | 25x25       |
| 6     | Advanced     | 100ms     | 10         | 25x25       |
| 7     | Expert       | 90ms      | 12         | 28x28       |
| 8     | Master       | 80ms      | 15         | 30x30       |
| 9     | Insane       | 70ms      | 18         | 32x32       |
| 10    | Impossible   | 60ms      | 20         | 35x35       |

## 🎮 Cómo Jugar

1. **Registrarse**: Introduce username y email
2. **Seleccionar Nivel**: Elige dificultad (1-10)
3. **Controles**:
   - ⬆️⬇️⬅️➡️ **Flechas**: Mover serpiente
   - **Espacio**: Pausar/Reanudar
4. **Objetivo**: Comer comida (🔴) y evitar obstáculos (⬛)
5. **Puntuación**: +10 puntos por cada comida
6. **Game Over**: Chocar con paredes, obstáculos o tu propio cuerpo

## 🗄️ Esquema de Base de Datos
```sql
┌─────────────────────┐
│     players         │
├─────────────────────┤
│ id (PK)             │
│ username (UNIQUE)   │
│ email (UNIQUE)      │
│ created_at          │
└─────────────────────┘
          ↑
          │ 1:N
          │
┌─────────────────────┐       ┌─────────────────────┐
│      games          │   N:1 │      levels         │
├─────────────────────┤───────├─────────────────────┤
│ id (PK)             │       │ id (PK)             │
│ player_id (FK)      │       │ level_number        │
│ level_id (FK)       │       │ name                │
│ score               │       │ speed               │
│ food_eaten          │       │ obstacles_count     │
│ duration_seconds    │       │ grid_size           │
│ completed           │       └─────────────────────┘
│ created_at          │
└─────────────────────┘
```

## 🔄 Proceso de Desarrollo (GitFlow)

Este proyecto sigue GitFlow:
```
main (producción)
  ↑
develop (desarrollo)
  ↑
feature/nombre (funcionalidades)
```

### Fases del Proyecto

1. ✅ **Phase 1**: Configuración inicial
2. ✅ **Phase 2**: Modelos de base de datos
3. ✅ **Phase 3**: API endpoints
4. ✅ **Phase 4**: Frontend y juego
5. ✅ **Phase 5**: CI/CD y documentación

## 🚀 CI/CD Pipeline

GitHub Actions ejecuta automáticamente:
- ✅ Tests con pytest
- ✅ Verificación de sintaxis Python
- ✅ Cobertura de código
- ✅ MySQL en contenedor temporal

Ver estado: [Actions](https://github.com/hayzam98/snake-game-portfolio/actions)

## 📈 Métricas del Proyecto

- **Líneas de código**: ~2,500
- **Tests**: 35 (100% aprobación)
- **Cobertura**: >80%
- **Commits**: 50+
- **Pull Requests**: 5
- **Endpoints API**: 14

## 🎓 Aprendizajes Demostrados

### Python & Backend
- ✅ FastAPI con type hints
- ✅ SQLAlchemy 2.0 (Type-annotated Declarative Mapping)
- ✅ Pydantic para validación
- ✅ Async/await
- ✅ Dependency injection
- ✅ RESTful API design

### Base de Datos
- ✅ Modelado relacional
- ✅ Foreign keys y relaciones
- ✅ SQL aggregations (JOIN, GROUP BY)
- ✅ Índices para performance

### Testing
- ✅ Pytest fixtures
- ✅ Tests unitarios e integración
- ✅ Mocking y test databases
- ✅ Coverage reporting

### Frontend
- ✅ Canvas API
- ✅ Fetch API
- ✅ Event handling
- ✅ DOM manipulation
- ✅ Responsive design

### DevOps
- ✅ Git branching strategies
- ✅ GitHub Actions CI/CD
- ✅ Environment variables
- ✅ Documentation

## 🤝 Contribución

Este es un proyecto de portfolio personal. No se aceptan contribuciones externas, pero siéntete libre de hacer fork y adaptarlo.

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Tu Nombre**
- GitHub: [@hayzam98](https://github.com/hayzam98)
- LinkedIn: [Hayzam Adan](https://linkedin.com/in/hayzam-adan-martinez-3765a6102/)
- Email: hayzam1998@gmail.com

## 🙏 Agradecimientos

- FastAPI por la excelente documentación
- SQLAlchemy por el poderoso ORM
- La comunidad de Python por las librerías increíbles

---
