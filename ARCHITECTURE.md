# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/constants.py: Game constants (screen dimensions, colors, speeds, scores)
- src/ball.py: Ball class with movement, collision detection, and reset logic
- src/paddle.py: Paddle class with movement (up/down), boundaries, and rendering
- src/scoring.py: Score tracking system with winning threshold and reset logic
- src/game.py: Main game state, input handling, game loop, and event coordination
- src/ui.py: Pygame rendering, user input collection, and display management
- main.py: Entry point that initializes and runs the game

## Interfaces

- constants.py exposes: SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, BALL_SIZE, PADDLE_SPEED, BALL_SPEED, WINNING_SCORE, COLORS (dict)
- ball.py exposes: Ball class with __init__(x, y), move(), check_collision(paddle1, paddle2), reset(), get_rect() -> Rect
- paddle.py exposes: Paddle class with __init__(x, y), move_up(), move_down(), get_rect() -> Rect, draw(screen)
- scoring.py exposes: ScoreBoard class with __init__(), player1_score(), player2_score(), get_scores() -> (int, int), check_winner() -> int | None, reset_scores()
- game.py exposes: PongGame class with __init__(), handle_input(keys), update(), check_win_condition(), reset_ball(), is_running() -> bool, get_scores() -> (int, int)
- ui.py exposes: draw_screen(screen, ball, paddles, scores), handle_pygame_events() -> dict of key states
- main.py: main() function that creates game instance and runs the loop

## Shared Data Structures

- Position: tuple[int, int] for x, y coordinates
- Size: tuple[int, int] for width, height
- Color: tuple[int, int, int] for RGB values
- Rect: pygame.Rect object for collision detection

## External Dependencies

- pygame: For window creation, rendering, input handling, and collision detection. Chosen for its simplicity and comprehensive 2D game development features.
