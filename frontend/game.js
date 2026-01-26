/**
 * Snake Game - Frontend Logic with Improvements
 * 
 * Improvements:
 * 1. Login/Register functionality
 * 2. Game starts only when arrow key is pressed
 * 3. Canvas fits on screen without scrolling
 */

// ========== Configuration ==========
const API_URL = 'http://localhost:8000';

// ========== Global State ==========
let currentPlayer = null;
let selectedLevel = null;
let currentGame = null;
let gameInterval = null;
let timerInterval = null;
let isPaused = false;
let gameStarted = false;  // NEW: Track if game has started

// Game state
let snake = [];
let food = null;
let obstacles = [];
let direction = 'RIGHT';
let nextDirection = 'RIGHT';
let score = 0;
let foodEaten = 0;
let gameTime = 0;

// Canvas configuration
let canvas = null;
let ctx = null;
let cellSize = 20;
let gridSize = 20;

// ========== Utility Functions ==========

function showLoading() {
    document.getElementById('loadingSpinner').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loadingSpinner').classList.add('hidden');
}

function showError(message) {
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

function hideError() {
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.classList.add('hidden');
}

function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.add('hidden');
    });
    document.getElementById(screenId).classList.remove('hidden');
}

// ========== API Functions ==========

/**
 * Create a new player (Register)
 */
async function createPlayer(username, email) {
    try {
        showLoading();
        
        const response = await fetch(`${API_URL}/players/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, email }),
        });
        
        hideLoading();
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to create player');
        }
        
        const player = await response.json();
        return player;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

/**
 * Login existing player by username
 */
async function loginPlayer(username) {
    try {
        showLoading();
        
        const response = await fetch(`${API_URL}/players/username/${username}`);
        
        hideLoading();
        
        if (!response.ok) {
            if (response.status === 404) {
                throw new Error('Username not found. Please register first.');
            }
            throw new Error('Failed to login');
        }
        
        const player = await response.json();
        return player;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

/**
 * Get all levels from API
 */
async function getLevels() {
    try {
        showLoading();
        
        const response = await fetch(`${API_URL}/levels/`);
        
        hideLoading();
        
        if (!response.ok) {
            throw new Error('Failed to fetch levels');
        }
        
        const levels = await response.json();
        return levels;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

/**
 * Create a new game session
 */
async function createGame(playerId, levelId) {
    try {
        showLoading();
        
        const response = await fetch(`${API_URL}/games/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ player_id: playerId, level_id: levelId }),
        });
        
        hideLoading();
        
        if (!response.ok) {
            throw new Error('Failed to create game');
        }
        
        const game = await response.json();
        return game;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

/**
 * Update game results
 */
async function updateGame(gameId, score, foodEaten, durationSeconds, completed) {
    try {
        showLoading();
        
        const response = await fetch(`${API_URL}/games/${gameId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                score,
                food_eaten: foodEaten,
                duration_seconds: durationSeconds,
                completed,
            }),
        });
        
        hideLoading();
        
        if (!response.ok) {
            throw new Error('Failed to update game');
        }
        
        const game = await response.json();
        return game;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

/**
 * Get leaderboard
 */
async function getLeaderboard(limit = 10) {
    try {
        showLoading();
        
        const response = await fetch(`${API_URL}/leaderboard/?limit=${limit}`);
        
        hideLoading();
        
        if (!response.ok) {
            throw new Error('Failed to fetch leaderboard');
        }
        
        const leaderboard = await response.json();
        return leaderboard;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

// ========== Auth Event Handlers ==========

/**
 * Tab switching between Login and Register
 */
document.getElementById('loginTab').addEventListener('click', () => {
    document.getElementById('loginTab').classList.add('active');
    document.getElementById('registerTab').classList.remove('active');
    document.getElementById('loginForm').classList.remove('hidden');
    document.getElementById('registerForm').classList.add('hidden');
    hideError();
});

document.getElementById('registerTab').addEventListener('click', () => {
    document.getElementById('registerTab').classList.add('active');
    document.getElementById('loginTab').classList.remove('active');
    document.getElementById('registerForm').classList.remove('hidden');
    document.getElementById('loginForm').classList.add('hidden');
    hideError();
});

/**
 * Login form submission
 */
document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    hideError();
    
    const username = document.getElementById('loginUsername').value.trim();
    
    try {
        const player = await loginPlayer(username);
        currentPlayer = player;
        
        // Show level selection screen
        document.getElementById('greetingName').textContent = player.username;
        await loadLevels();
        showScreen('levelScreen');
    } catch (error) {
        showError(error.message);
    }
});

/**
 * Register form submission
 */
document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    hideError();
    
    const username = document.getElementById('registerUsername').value.trim();
    const email = document.getElementById('registerEmail').value.trim();
    
    try {
        const player = await createPlayer(username, email);
        currentPlayer = player;
        
        // Show level selection screen
        document.getElementById('greetingName').textContent = player.username;
        await loadLevels();
        showScreen('levelScreen');
    } catch (error) {
        showError(error.message);
    }
});

/**
 * Logout button
 */
document.getElementById('logoutBtn').addEventListener('click', () => {
    currentPlayer = null;
    
    // Clear forms
    document.getElementById('loginUsername').value = '';
    document.getElementById('registerUsername').value = '';
    document.getElementById('registerEmail').value = '';
    
    // Reset to login tab
    document.getElementById('loginTab').click();
    
    // Show welcome screen
    showScreen('welcomeScreen');
});

// ========== Level Selection ==========

/**
 * Load and display levels
 */
async function loadLevels() {
    try {
        const levels = await getLevels();
        const levelsGrid = document.getElementById('levelsList');
        levelsGrid.innerHTML = '';
        
        levels.forEach(level => {
            const levelCard = document.createElement('div');
            levelCard.className = 'level-card';
            levelCard.innerHTML = `
                <h3>Level ${level.level_number}</h3>
                <div class="level-name">${level.name}</div>
                <div class="level-details">
                    Speed: ${level.speed}ms<br>
                    Obstacles: ${level.obstacles_count}<br>
                    Grid: ${level.grid_size}x${level.grid_size}
                </div>
            `;
            
            levelCard.addEventListener('click', () => {
                selectLevel(level);
            });
            
            levelsGrid.appendChild(levelCard);
        });
    } catch (error) {
        alert('Failed to load levels: ' + error.message);
    }
}

/**
 * Select a level and start game
 */
async function selectLevel(level) {
    try {
        selectedLevel = level;
        
        const game = await createGame(currentPlayer.id, level.id);
        currentGame = game;
        
        initGame();
        showScreen('gameScreen');
    } catch (error) {
        alert('Failed to start game: ' + error.message);
    }
}

/**
 * View leaderboard from levels screen
 */
document.getElementById('viewLeaderboardFromLevels').addEventListener('click', async () => {
    await loadLeaderboard();
    showScreen('leaderboardScreen');
});

/**
 * Back to levels from leaderboard
 */
document.getElementById('backToLevelsBtn').addEventListener('click', () => {
    showScreen('levelScreen');
});

/**
 * Load and display leaderboard
 */
async function loadLeaderboard() {
    try {
        const leaderboard = await getLeaderboard();
        const leaderboardTable = document.getElementById('leaderboardTable');
        leaderboardTable.innerHTML = '';
        
        const header = document.createElement('div');
        header.className = 'leaderboard-header';
        header.innerHTML = `
            <div>Rank</div>
            <div>Player</div>
            <div>Total Score</div>
            <div>Games Played</div>
            <div>Highest Level</div>
        `;
        leaderboardTable.appendChild(header);
        
        leaderboard.forEach(entry => {
            const entryDiv = document.createElement('div');
            entryDiv.className = `leaderboard-entry rank-${entry.rank}`;
            entryDiv.innerHTML = `
                <div class="leaderboard-rank">${entry.rank}</div>
                <div class="leaderboard-username">${entry.username}</div>
                <div class="leaderboard-stat">${entry.total_score}</div>
                <div class="leaderboard-stat">${entry.games_played}</div>
                <div class="leaderboard-stat">${entry.highest_level}</div>
            `;
            leaderboardTable.appendChild(entryDiv);
        });
    } catch (error) {
        alert('Failed to load leaderboard: ' + error.message);
    }
}

// ========== Game Logic ==========

/**
 * Initialize game
 * IMPROVEMENT: Rectangular grid that uses entire canvas area
 * Grid columns (X) and rows (Y) calculated independently
 */
function initGame() {
    canvas = document.getElementById('gameCanvas');
    ctx = canvas.getContext('2d');
    
    // Get container width (full width of container minus padding)
    const container = document.querySelector('.container');
    const containerStyle = window.getComputedStyle(container);
    const containerPadding = parseFloat(containerStyle.paddingLeft) + parseFloat(containerStyle.paddingRight);
    const containerWidth = container.clientWidth - containerPadding;
    
    // Calculate available height for canvas
    const viewportHeight = window.innerHeight;
    const reservedHeight = 350; // Space for UI elements
    const availableHeight = viewportHeight - reservedHeight;
    
    // Define desired cell size (SQUARE cells)
    const desiredCellSize = 20; // Adjust this for bigger/smaller cells
    
    // Calculate grid dimensions based on canvas area
    // Grid columns (X-axis): based on container width
    const gridCols = Math.floor(containerWidth / desiredCellSize);
    
    // Grid rows (Y-axis): based on available height
    const gridRows = Math.floor(availableHeight / desiredCellSize);
    
    // Calculate actual cell size to fit exactly
    const cellWidth = Math.floor(containerWidth / gridCols);
    const cellHeight = Math.floor(availableHeight / gridRows);
    
    // Use the smaller to keep cells SQUARE
    cellSize = Math.min(cellWidth, cellHeight);
    
    // Ensure minimum cell size
    cellSize = Math.max(cellSize, 15);
    
    // Final grid dimensions
    const finalGridCols = Math.floor(containerWidth / cellSize);
    const finalGridRows = Math.floor(availableHeight / cellSize);
    
    // Set canvas size
    const canvasWidth = finalGridCols * cellSize;
    const canvasHeight = finalGridRows * cellSize;
    
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;
    
    // Store grid dimensions globally
    window.gridCols = finalGridCols; // X-axis (horizontal)
    window.gridRows = finalGridRows; // Y-axis (vertical)
    
    // Update obstacles count based on rectangular grid
    const totalCells = finalGridCols * finalGridRows;
    const obstacleRatio = selectedLevel.obstacles_count / (selectedLevel.grid_size * selectedLevel.grid_size);
    const adjustedObstaclesCount = Math.floor(totalCells * obstacleRatio);
    
    // Log canvas info for debugging
    console.log(`Canvas: ${canvasWidth}x${canvasHeight}px`);
    console.log(`Cell: ${cellSize}x${cellSize}px (SQUARE)`);
    console.log(`Grid: ${finalGridCols} cols × ${finalGridRows} rows`);
    console.log(`Total cells: ${totalCells}`);
    console.log(`Obstacles: ${adjustedObstaclesCount}`);
    console.log(`Canvas Aspect Ratio: ${(canvasWidth/canvasHeight).toFixed(2)}:1`);
    
    // Initialize snake in the center of RECTANGULAR grid
    const centerX = Math.floor(finalGridCols / 2);
    const centerY = Math.floor(finalGridRows / 2);
    snake = [
        { x: centerX, y: centerY },
        { x: centerX - 1, y: centerY },
        { x: centerX - 2, y: centerY }
    ];
    
    direction = 'RIGHT';
    nextDirection = 'RIGHT';
    score = 0;
    foodEaten = 0;
    gameTime = 0;
    gameStarted = false;
    
    // Store adjusted obstacles count
    window.adjustedObstaclesCount = adjustedObstaclesCount;
    
    generateFood();
    generateObstacles();
    
    // Update UI
    document.getElementById('playerName').textContent = currentPlayer.username;
    document.getElementById('currentLevel').textContent = `${selectedLevel.level_number} - ${selectedLevel.name}`;
    document.getElementById('score').textContent = score;
    document.getElementById('foodCount').textContent = foodEaten;
    document.getElementById('timer').textContent = '0s';
    
    isPaused = false;
    document.getElementById('pauseBtn').classList.remove('hidden');
    document.getElementById('resumeBtn').classList.add('hidden');
    
    // Show start message
    document.getElementById('startMessage').classList.remove('hidden');
    
    // Draw initial state
    draw();
    
    // Scroll to top to ensure canvas is visible
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

/**
 * Generate food at random position
 * UPDATED: Uses rectangular grid (gridCols × gridRows)
 */
function generateFood() {
    const gridCols = window.gridCols;
    const gridRows = window.gridRows;
    
    let validPosition = false;
    
    while (!validPosition) {
        food = {
            x: Math.floor(Math.random() * gridCols),
            y: Math.floor(Math.random() * gridRows)
        };
        
        validPosition = !isPositionOccupied(food.x, food.y);
    }
}

/**
 * Check if position is occupied by snake or obstacle
 */
function isPositionOccupied(x, y) {
    for (let segment of snake) {
        if (segment.x === x && segment.y === y) {
            return true;
        }
    }
    
    for (let obstacle of obstacles) {
        if (obstacle.x === x && obstacle.y === y) {
            return true;
        }
    }
    
    return false;
}

/**
 * Generate obstacles based on level
 * UPDATED: Uses rectangular grid and adjusted count
 */
function generateObstacles() {
    obstacles = [];
    const gridCols = window.gridCols;
    const gridRows = window.gridRows;
    const count = window.adjustedObstaclesCount || selectedLevel.obstacles_count;
    
    for (let i = 0; i < count; i++) {
        let validPosition = false;
        let obstacle;
        
        while (!validPosition) {
            obstacle = {
                x: Math.floor(Math.random() * gridCols),
                y: Math.floor(Math.random() * gridRows)
            };
            
            validPosition = !isPositionOccupied(obstacle.x, obstacle.y) &&
                           (obstacle.x !== food.x || obstacle.y !== food.y);
        }
        
        obstacles.push(obstacle);
    }
}

/**
 * Start game loop
 * IMPROVEMENT: Only starts when arrow key is pressed
 */
function startGame() {
    if (gameStarted) return;
    
    gameStarted = true;
    document.getElementById('startMessage').classList.add('hidden');
    
    gameInterval = setInterval(gameLoop, selectedLevel.speed);
    
    timerInterval = setInterval(() => {
        if (!isPaused) {
            gameTime++;
            document.getElementById('timer').textContent = `${gameTime}s`;
        }
    }, 1000);
}

/**
 * Main game loop
 */
function gameLoop() {
    if (isPaused) return;
    
    direction = nextDirection;
    
    const head = { ...snake[0] };
    
    switch (direction) {
        case 'UP':
            head.y--;
            break;
        case 'DOWN':
            head.y++;
            break;
        case 'LEFT':
            head.x--;
            break;
        case 'RIGHT':
            head.x++;
            break;
    }
    
    // Check collision with walls - UPDATED for rectangular grid
    const gridCols = window.gridCols;
    const gridRows = window.gridRows;
    
    if (head.x < 0 || head.x >= gridCols || head.y < 0 || head.y >= gridRows) {
        gameOver(false);
        return;
    }
    
    // Check collision with self
    for (let segment of snake) {
        if (segment.x === head.x && segment.y === head.y) {
            gameOver(false);
            return;
        }
    }
    
    // Check collision with obstacles
    for (let obstacle of obstacles) {
        if (obstacle.x === head.x && obstacle.y === head.y) {
            gameOver(false);
            return;
        }
    }
    
    snake.unshift(head);
    
    // Check if food eaten
    if (head.x === food.x && head.y === food.y) {
        score += 10;
        foodEaten++;
        document.getElementById('score').textContent = score;
        document.getElementById('foodCount').textContent = foodEaten;
        generateFood();
    } else {
        snake.pop();
    }
    
    draw();
}

/**
 * Draw game on canvas
 * UPDATED: Draws with rectangular grid
 */
function draw() {
    const gridCols = window.gridCols;
    const gridRows = window.gridRows;
    
    // Clear canvas
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Draw grid lines (optional)
    ctx.strokeStyle = '#111';
    ctx.lineWidth = 1;
    
    // Vertical lines
    for (let x = 0; x <= gridCols; x++) {
        ctx.beginPath();
        ctx.moveTo(x * cellSize, 0);
        ctx.lineTo(x * cellSize, canvas.height);
        ctx.stroke();
    }
    
    // Horizontal lines
    for (let y = 0; y <= gridRows; y++) {
        ctx.beginPath();
        ctx.moveTo(0, y * cellSize);
        ctx.lineTo(canvas.width, y * cellSize);
        ctx.stroke();
    }
    
    // Draw snake
    snake.forEach((segment, index) => {
        if (index === 0) {
            ctx.fillStyle = '#00ff00';  // Head
        } else {
            ctx.fillStyle = '#0f0';  // Body
        }
        ctx.fillRect(
            segment.x * cellSize,
            segment.y * cellSize,
            cellSize - 2,
            cellSize - 2
        );
    });
    
    // Draw food
    ctx.fillStyle = '#ff0000';
    ctx.fillRect(
        food.x * cellSize,
        food.y * cellSize,
        cellSize - 2,
        cellSize - 2
    );
    
    // Draw obstacles
    ctx.fillStyle = '#888';
    obstacles.forEach(obstacle => {
        ctx.fillRect(
            obstacle.x * cellSize,
            obstacle.y * cellSize,
            cellSize - 2,
            cellSize - 2
        );
    });
}

// ========== Keyboard Controls ==========

/**
 * Handle keyboard input
 * IMPROVEMENT: First arrow key starts the game
 */
document.addEventListener('keydown', (e) => {
    if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '].includes(e.key)) {
        e.preventDefault();
    }
    
    // IMPROVEMENT: Start game on first arrow key press
    if (!gameStarted && ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
        startGame();
    }
    
    switch (e.key) {
        case 'ArrowUp':
            if (direction !== 'DOWN') {
                nextDirection = 'UP';
            }
            break;
        case 'ArrowDown':
            if (direction !== 'UP') {
                nextDirection = 'DOWN';
            }
            break;
        case 'ArrowLeft':
            if (direction !== 'RIGHT') {
                nextDirection = 'LEFT';
            }
            break;
        case 'ArrowRight':
            if (direction !== 'LEFT') {
                nextDirection = 'RIGHT';
            }
            break;
        case ' ':
            if (gameStarted) {
                togglePause();
            }
            break;
    }
});

/**
 * Toggle pause
 */
function togglePause() {
    isPaused = !isPaused;
    
    if (isPaused) {
        document.getElementById('pauseBtn').classList.add('hidden');
        document.getElementById('resumeBtn').classList.remove('hidden');
    } else {
        document.getElementById('pauseBtn').classList.remove('hidden');
        document.getElementById('resumeBtn').classList.add('hidden');
    }
}

document.getElementById('pauseBtn').addEventListener('click', togglePause);
document.getElementById('resumeBtn').addEventListener('click', togglePause);

/**
 * Quit button
 */
document.getElementById('quitBtn').addEventListener('click', () => {
    if (confirm('Are you sure you want to quit? Your progress will be lost.')) {
        gameOver(false);
    }
});

/**
 * Game over
 */
async function gameOver(completed) {
    clearInterval(gameInterval);
    clearInterval(timerInterval);
    
    try {
        await updateGame(currentGame.id, score, foodEaten, gameTime, completed);
    } catch (error) {
        console.error('Failed to update game:', error);
    }
    
    document.getElementById('gameOverTitle').textContent = completed ? 'Level Completed!' : 'Game Over!';
    document.getElementById('finalScore').textContent = score;
    document.getElementById('finalFood').textContent = foodEaten;
    document.getElementById('finalTime').textContent = `${gameTime}s`;
    
    const completionMsg = document.getElementById('completionMessage');
    if (completed) {
        completionMsg.textContent = '🎉 Congratulations! You completed the level!';
        completionMsg.classList.remove('hidden');
    } else {
        completionMsg.classList.add('hidden');
    }
    
    showScreen('gameOverScreen');
}

/**
 * Play again button
 */
document.getElementById('playAgainBtn').addEventListener('click', async () => {
    await selectLevel(selectedLevel);
});

/**
 * Change level button
 */
document.getElementById('changeLevelBtn').addEventListener('click', () => {
    showScreen('levelScreen');
});

/**
 * View leaderboard button
 */
document.getElementById('viewLeaderboardBtn').addEventListener('click', async () => {
    await loadLeaderboard();
    showScreen('leaderboardScreen');
});
