# 🐍 Snake Game - Full Stack Portfolio Project

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1.svg)](https://www.mysql.com/)
[![CI/CD Pipeline](https://github.com/hayzam98/snake-game/actions/workflows/ci.yml/badge.svg)](https://github.com/hayzam98/snake-game/actions/workflows/ci.yml)

> Un juego de la serpiente clásico con 10 niveles de dificultad progresiva, sistema de autenticación, backend FastAPI, base de datos MySQL y frontend vanilla JavaScript con Canvas API.

## 📝 Descripción

Proyecto full stack completo que demuestra conocimientos profesionales en desarrollo web moderno. El juego implementa mecánicas clásicas de Snake con características avanzadas como múltiples niveles de dificultad, sistema de puntuación persistente, autenticación de usuarios y un leaderboard global competitivo.

### Habilidades Demostradas

- **Backend**: Python 3.13, FastAPI, SQLAlchemy 2.0, MySQL
- **Frontend**: HTML5, CSS3, JavaScript ES6+, Canvas API
- **Testing**: Pytest (35 tests, 100% aprobación)
- **CI/CD**: GitHub Actions
- **Git**: GitFlow con branches y pull requests
- **Database Design**: Modelado relacional, índices, consultas optimizadas

## 🎮 Características del Juego

### Funcionalidades Principales

- 🐍 **Juego Snake Clásico** con controles de teclado intuitivos
- 🔐 **Sistema de Autenticación** - Login para usuarios existentes y registro para nuevos jugadores
- 📊 **10 Niveles de Dificultad** progresiva (Beginner → Impossible)
- 🏆 **Leaderboard Global** - Top 10 jugadores con estadísticas detalladas
- 📈 **Sistema de Puntuación** - Tracking completo de score, comida consumida y tiempo de juego
- ⏸️ **Controles del Juego** - Pausa/Resume en cualquier momento
- 🎯 **Control de Inicio** - El juego espera a que presiones una tecla de dirección para comenzar
- 💾 **Persistencia de Datos** - Todas las partidas se guardan en MySQL
- 🎨 **Interfaz Moderna** - Diseño responsive con gradientes y animaciones
- 📱 **Mobile Friendly** - Canvas adaptativo que se ajusta a cualquier pantalla

### Mejoras UX Implementadas

- ✅ **Canvas Centrado y Optimizado** - Tamaño máximo (80% width, 75% height) sin necesidad de scroll
- ✅ **Mensaje de Inicio** - "Press any arrow key to start!" para mejor control del jugador
- ✅ **Tabs Login/Register** - Interfaz clara para diferenciar usuarios nuevos y existentes
- ✅ **Logout Funcional** - Permite cambiar de cuenta fácilmente
- ✅ **Validaciones** - Mensajes de error claros y útiles

## 🛠️ Stack Tecnológico

### Backend

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.13+ | Lenguaje principal |
| FastAPI | 0.115.0 | Framework web moderno |
| SQLAlchemy | 2.0.35 | ORM con Type-annotated Mapping |
| MySQL | 8.0+ | Base de datos relacional |
| Pydantic | 2.9.2 | Validación de datos y settings |
| PyMySQL | 1.1.1 | Driver MySQL para Python |
| Pytest | 8.3.3 | Framework de testing |
| pytest-cov | 4.1.0 | Cobertura de código |
| Uvicorn | 0.32.0 | Servidor ASGI de alto rendimiento |

### Frontend

- **HTML5**: Estructura semántica y Canvas API para renderizado del juego
- **CSS3**: Estilos modernos con gradientes, animaciones y diseño responsive
- **JavaScript ES6+**: 
  - Lógica del juego con game loop
  - Fetch API para comunicación con backend
  - Event handling para controles
  - Manipulación del DOM

### DevOps y Herramientas

- **Git**: Control de versiones con GitFlow methodology
- **GitHub Actions**: Pipeline CI/CD automatizado
- **VS Code**: IDE de desarrollo
- **MySQL Workbench**: Gestión de base de datos
- **PowerShell**: Scripts de automatización (Windows)

## 📊 Estructura del Proyecto
```
snake-game/
├── backend/                    # Backend FastAPI
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # Aplicación FastAPI principal
│   │   ├── config.py          # Configuración con pydantic-settings
│   │   ├── database.py        # SQLAlchemy 2.0 setup
│   │   ├── models.py          # Modelos de base de datos
│   │   ├── schemas.py         # Schemas Pydantic para validación
│   │   ├── crud.py            # Operaciones CRUD
│   │   ├── init_levels.py     # Inicialización de 10 niveles
│   │   └── routers/           # Endpoints de la API REST
│   │       ├── __init__.py
│   │       ├── players.py     # Gestión de jugadores (4 endpoints)
│   │       ├── levels.py      # Niveles de dificultad (3 endpoints)
│   │       ├── games.py       # Sesiones de juego (4 endpoints)
│   │       └── leaderboard.py # Rankings globales (1 endpoint)
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_models.py     # Tests unitarios (10 tests)
│   │   └── test_api.py        # Tests de integración (25 tests)
│   ├── requirements.txt       # Dependencias Python
│   ├── pytest.ini             # Configuración de pytest
│   ├── init_db.py             # Script de inicialización DB
│   └── .env                   # Variables de entorno (no versionado)
├── frontend/                   # Frontend web
│   ├── index.html             # Estructura HTML (5 pantallas)
│   ├── style.css              # Estilos CSS (600+ líneas)
│   └── game.js                # Lógica del juego (700+ líneas)
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD
├── .gitignore                 # Archivos ignorados por Git
├── LICENSE                    # Licencia MIT
└── README.md                  # Este archivo
```

## 🚀 Instalación y Uso

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.13 o superior** - [Descargar](https://www.python.org/downloads/)
- **MySQL 8.0 o superior** - [Descargar](https://dev.mysql.com/downloads/)
- **Git** - [Descargar](https://git-scm.com/)

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/hayzam98/snake-game.git
cd snake-game
```

### Paso 2: Configurar Backend

#### 2.1 Crear Entorno Virtual
```bash
# Navegar a backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Windows CMD:
venv\Scripts\activate.bat

# Linux/Mac:
source venv/bin/activate
```

#### 2.2 Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 3: Configurar Base de Datos MySQL

#### Opción 1: MySQL Workbench (Recomendado)

1. Abre MySQL Workbench
2. Conéctate a tu servidor local
3. Ejecuta:
```sql
CREATE DATABASE snake_game_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

#### Opción 2: Línea de Comandos
```bash
mysql -u root -p
```

Dentro de MySQL:
```sql
CREATE DATABASE snake_game_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW DATABASES;
EXIT;
```

### Paso 4: Configurar Variables de Entorno

Crea el archivo `backend/.env` con este contenido:
```env
# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_password_mysql
DB_NAME=snake_game_db

# Application Configuration
APP_NAME=Snake Game API
APP_VERSION=1.1.0
DEBUG=True

# Security
SECRET_KEY=your-secret-key-here
```

⚠️ **Importante**: Cambia `tu_password_mysql` por tu contraseña real de MySQL.

### Paso 5: Inicializar Base de Datos
```bash
# Desde backend/ con venv activado
python init_db.py
```

**Salida esperada**:
```
🗄️  Creating database tables...
✅ Tables created successfully!

🎮 Initializing 10 game levels...
  ✓ Level 1: Beginner created
  ✓ Level 2: Easy created
  ✓ Level 3: Novice created
  ✓ Level 4: Intermediate created
  ✓ Level 5: Skilled created
  ✓ Level 6: Advanced created
  ✓ Level 7: Expert created
  ✓ Level 8: Master created
  ✓ Level 9: Insane created
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

1. Abre una nueva terminal
2. Navega a la carpeta `frontend/`
3. Abre `index.html` en tu navegador preferido

O simplemente haz doble click en `frontend/index.html`.

## 🧪 Testing

### Ejecutar Todos los Tests
```bash
# Desde backend/ con venv activado
pytest tests/ -v
```

**Resultado esperado**: 35 tests pasando (10 modelos + 25 API)

### Tests Específicos
```bash
# Solo tests de modelos
pytest tests/test_models.py -v

# Solo tests de API
pytest tests/test_api.py -v

# Con reporte de cobertura
pytest tests/ --cov=app --cov-report=html

# Ver reporte HTML
# Abre: htmlcov/index.html en tu navegador
```

### Categorías de Tests

| Categoría | Cantidad | Descripción |
|-----------|----------|-------------|
| **Models** | 10 tests | CRUD operations, validaciones, relaciones |
| **API** | 25 tests | Endpoints, validaciones, errores HTTP |
| **Total** | **35 tests** | Cobertura >80% |

## 📊 API Endpoints

### Players (Jugadores)

| Método | Endpoint | Descripción | Código |
|--------|----------|-------------|--------|
| POST | `/players/` | Crear nuevo jugador | 201 |
| GET | `/players/{id}` | Obtener jugador por ID | 200 |
| GET | `/players/` | Listar jugadores (paginado) | 200 |
| GET | `/players/username/{username}` | Buscar por username (Login) | 200 |

### Levels (Niveles)

| Método | Endpoint | Descripción | Código |
|--------|----------|-------------|--------|
| GET | `/levels/` | Listar todos los niveles | 200 |
| GET | `/levels/{id}` | Obtener nivel por ID | 200 |
| GET | `/levels/number/{number}` | Obtener nivel por número (1-10) | 200 |

### Games (Partidas)

| Método | Endpoint | Descripción | Código |
|--------|----------|-------------|--------|
| POST | `/games/` | Iniciar nueva partida | 201 |
| GET | `/games/{id}` | Obtener partida con detalles | 200 |
| PUT | `/games/{id}` | Actualizar resultados | 200 |
| GET | `/games/player/{id}/history` | Historial del jugador | 200 |

### Leaderboard (Ranking)

| Método | Endpoint | Descripción | Código |
|--------|----------|-------------|--------|
| GET | `/leaderboard/` | Top 10 jugadores | 200 |

### Endpoints de Sistema

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información de la API |
| GET | `/health` | Health check |

**Total**: 14 endpoints RESTful

## 🏆 Niveles de Dificultad

| Nivel | Nombre       | Velocidad | Obstáculos | Tamaño Grid | Dificultad |
|-------|--------------|-----------|------------|-------------|------------|
| 1     | Beginner     | 200ms     | 0          | 20x20       | ⭐ |
| 2     | Easy         | 180ms     | 2          | 20x20       | ⭐⭐ |
| 3     | Novice       | 160ms     | 4          | 22x22       | ⭐⭐ |
| 4     | Intermediate | 140ms     | 6          | 22x22       | ⭐⭐⭐ |
| 5     | Skilled      | 120ms     | 8          | 25x25       | ⭐⭐⭐ |
| 6     | Advanced     | 100ms     | 10         | 25x25       | ⭐⭐⭐⭐ |
| 7     | Expert       | 90ms      | 12         | 28x28       | ⭐⭐⭐⭐ |
| 8     | Master       | 80ms      | 15         | 30x30       | ⭐⭐⭐⭐⭐ |
| 9     | Insane       | 70ms      | 18         | 32x32       | ⭐⭐⭐⭐⭐ |
| 10    | Impossible   | 60ms      | 20         | 35x35       | ⭐⭐⭐⭐⭐⭐ |

### Progresión de Dificultad

- **Velocidad**: Disminuye de 200ms a 60ms (3.3x más rápido)
- **Obstáculos**: Aumentan de 0 a 20
- **Tamaño del Grid**: Aumenta de 20x20 a 35x35 (3x más área)

## 🎮 Cómo Jugar

### 1. Autenticación

**Primera vez (Registro)**:
1. Click en pestaña **"Register"**
2. Introduce username (3-50 caracteres)
3. Introduce email válido
4. Click "Create Account"

**Usuarios existentes (Login)**:
1. Pestaña **"Login"** (por defecto)
2. Introduce tu username
3. Click "Login"

### 2. Seleccionar Nivel

- Verás 10 tarjetas con los niveles
- Cada tarjeta muestra: nombre, velocidad, obstáculos y tamaño del grid
- Click en el nivel que quieras jugar

### 3. Controles del Juego

| Tecla | Acción |
|-------|--------|
| ⬆️ | Mover arriba |
| ⬇️ | Mover abajo |
| ⬅️ | Mover izquierda |
| ➡️ | Mover derecha |
| **Espacio** | Pausar/Reanudar |

### 4. Mecánicas

- **Objetivo**: Comer la comida roja (🔴)
- **Puntuación**: +10 puntos por cada comida
- **Crecimiento**: La serpiente crece al comer
- **Evitar**: 
  - Paredes del mapa
  - Tu propio cuerpo
  - Obstáculos grises (⬛)

### 5. Inicio del Juego

- Al seleccionar un nivel, verás el mensaje: **"Press any arrow key to start!"**
- La serpiente permanece quieta
- Presiona cualquier flecha (↑, ↓, ←, →) para comenzar
- El juego empieza inmediatamente

### 6. Fin del Juego

**Game Over** cuando:
- Chocas con una pared
- Chocas con tu cuerpo
- Chocas con un obstáculo

**Opciones después del juego**:
- **Play Again**: Repetir mismo nivel
- **Change Level**: Volver a selección de niveles
- **View Leaderboard**: Ver top 10 jugadores

## 🗄️ Esquema de Base de Datos
```sql
┌─────────────────────┐
│     players         │  Almacena información de jugadores
├─────────────────────┤
│ id (PK)             │  INT AUTO_INCREMENT
│ username (UNIQUE)   │  VARCHAR(50)
│ email (UNIQUE)      │  VARCHAR(100)
│ created_at          │  DATETIME
└─────────────────────┘
          ↑
          │ 1:N (Un jugador tiene muchos juegos)
          │
┌─────────────────────┐       ┌─────────────────────┐
│      games          │   N:1 │      levels         │
├─────────────────────┤───────├─────────────────────┤
│ id (PK)             │       │ id (PK)             │
│ player_id (FK)      │       │ level_number        │ 1-10
│ level_id (FK)       │       │ name                │ VARCHAR(50)
│ score               │       │ speed               │ INT (ms)
│ food_eaten          │       │ obstacles_count     │ INT
│ duration_seconds    │       │ grid_size           │ INT
│ completed           │       └─────────────────────┘
│ created_at          │              Un nivel tiene muchos juegos
└─────────────────────┘                    N:1
```

### Relaciones

- **Player → Games**: 1:N (Un jugador puede tener múltiples partidas)
- **Level → Games**: 1:N (Un nivel puede ser jugado múltiples veces)
- **Cascade Delete**: Al eliminar un jugador, se eliminan sus partidas

### Índices

- `players.username` - UNIQUE, INDEX
- `players.email` - UNIQUE, INDEX
- `levels.level_number` - UNIQUE, INDEX
- `games.player_id` - INDEX (FK)
- `games.level_id` - INDEX (FK)

## 🔄 Proceso de Desarrollo (GitFlow)

Este proyecto siguió GitFlow methodology:
```
main (v1.0.0, v1.1.0) ← Versiones de producción
  ↑
develop ← Rama principal de desarrollo
  ↑
feature/* ← Ramas de funcionalidades
```

### Fases del Proyecto

| Fase | Branch | Descripción | Tests |
|------|--------|-------------|-------|
| 1 | `feature/project-setup` | Configuración inicial | - |
| 2 | `feature/database-models` | Modelos y CRUD | 10 |
| 3 | `feature/api-endpoints` | API REST FastAPI | 25 |
| 4 | `feature/frontend-game` | Interfaz web y juego | - |
| 5 | `feature/ci-cd-docs` | CI/CD y documentación | 35 |
| 6 | `feature/frontend-improvements` | Login/Register, UX | 35 |
| 7 | `feature/canvas-improvements-docs` | Canvas optimizado | 35 |

### Commits

- Total: **60+ commits**
- Formato: `feat:`, `fix:`, `docs:`, `test:`
- Mensajes descriptivos en inglés

### Pull Requests

- Total: **7 PRs**
- Reviews antes de merge
- Branches eliminadas después de merge

## 🚀 CI/CD Pipeline

### GitHub Actions Workflow

Cada push o PR a `develop` o `main` ejecuta:
```yaml
1. Setup MySQL 8.0 (service container)
2. Checkout code
3. Setup Python 3.13
4. Cache pip dependencies
5. Install requirements
6. Run pytest (35 tests)
7. Generate coverage report
8. Upload artifacts
```

### Estado del Pipeline

Ver estado actual: [GitHub Actions](https://github.com/hayzam98/snake-game/actions)

### Badges

- ✅ CI/CD Pipeline
- ✅ Python 3.13+
- ✅ FastAPI Version
- ✅ MySQL 8.0+
- ✅ MIT License

## 📈 Métricas del Proyecto

| Métrica | Valor |
|---------|-------|
| **Líneas de Código** | ~3,000 |
| **Archivos Python** | 15+ |
| **Archivos Frontend** | 3 |
| **Tests** | 35 (100% aprobación) |
| **Cobertura de Tests** | >80% |
| **Commits** | 60+ |
| **Pull Requests** | 7 |
| **Branches** | 8 |
| **Endpoints API** | 14 |
| **Modelos de DB** | 3 |
| **Niveles de Juego** | 10 |
| **Funciones JavaScript** | 30+ |
| **Clases CSS** | 50+ |

## 🎓 Habilidades Técnicas Demostradas

### Backend Development

✅ **Python 3.13+**
- Type hints completos
- Async/await patterns
- List comprehensions
- Exception handling
- Decorators

✅ **FastAPI**
- Routing y middleware
- Dependency injection
- Pydantic schemas
- CORS configuration
- OpenAPI/Swagger docs

✅ **SQLAlchemy 2.0**
- Type-annotated Declarative Mapping
- Relationships (1:N)
- Query optimization
- Cascade operations
- Session management

✅ **Database Design**
- Modelado relacional
- Foreign keys
- Índices estratégicos
- SQL aggregations (SUM, COUNT, MAX)
- JOIN operations

### Frontend Development

✅ **HTML5**
- Estructura semántica
- Canvas API
- Forms y validación
- Responsive meta tags

✅ **CSS3**
- Flexbox y Grid
- Gradientes y animaciones
- Media queries
- Transitions
- Custom properties

✅ **JavaScript ES6+**
- Arrow functions
- Async/await
- Fetch API
- Event listeners
- DOM manipulation
- Game loop implementation
- Collision detection
- State management

### Testing & Quality

✅ **Pytest**
- Fixtures
- Parametrización
- Mocking
- Test isolation
- Coverage reporting

✅ **Integration Testing**
- API endpoint testing
- Database testing
- Error handling verification

### DevOps & Tools

✅ **Git**
- Branching strategies
- Meaningful commits
- Pull requests
- Code reviews
- Tag management

✅ **GitHub Actions**
- Workflow automation
- Service containers
- Artifact uploading
- Environment variables

✅ **Documentation**
- Technical writing
- README structure
- Code comments
- API documentation

## 🎨 Capturas de Pantalla

### Pantalla de Bienvenida (Login/Register)
Sistema de tabs para diferenciar usuarios nuevos y existentes.

### Selección de Niveles
Grid con 10 niveles mostrando dificultad progresiva.

### Gameplay
Canvas centrado y optimizado con mensaje de inicio.

### Leaderboard
Top 10 jugadores con estadísticas detalladas.

## 🤝 Contribución

Este es un proyecto de portfolio personal. No se aceptan contribuciones externas, pero siéntete libre de:
- Hacer fork del proyecto
- Adaptarlo para tu propio portfolio
- Aprender de la estructura y código
- Reportar bugs vía Issues

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Hayzam Adan**
- GitHub: [@hayzam98](https://github.com/hayzam98)
- LinkedIn: [Hayzam Adan](https://linkedin.com/in/hayzam-adan-martinez-3765a6102/)
- Email: hayzam1998@gmail.com

## 🙏 Agradecimientos

- FastAPI por la excelente documentación
- SQLAlchemy por el poderoso ORM
- La comunidad de Python por las librerías increíbles
