import pygame
from src.ball import Ball
from src.paddle import Paddle
from src.scoring import ScoreBoard
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WINNING_SCORE


class PongGame:
    def __init__(self):
        self.ball = Ball(SCREEN_WIDTH // 2 - 7, SCREEN_HEIGHT // 2 - 7)
        self.paddle1 = Paddle(20, SCREEN_HEIGHT // 2 - 50)
        self.paddle2 = Paddle(SCREEN_WIDTH - 35, SCREEN_HEIGHT // 2 - 50)
        self.scoreboard = ScoreBoard()
        self.game_running = True
        self.game_over = False

    def handle_input(self, keys):
        """Process key presses for paddle movement."""
        # Player 1 (left) controls: W (up), S (down)
        if keys[pygame.K_w]:
            self.paddle1.move_up()
        if keys[pygame.K_s]:
            self.paddle1.move_down()

        # Player 2 (right) controls: UP (up), DOWN (down)
        if keys[pygame.K_UP]:
            self.paddle2.move_up()
        if keys[pygame.K_DOWN]:
            self.paddle2.move_down()

        # Update paddle positions in game
        self.paddle1.x = self.paddle1.x  # Keep paddle1 at left
        self.paddle2.x = self.paddle2.x  # Keep paddle2 at right

    def update(self):
        """Update ball position and check collisions."""
        if not self.game_running:
            return

        self.ball.move()
        self.ball.check_collision(self.paddle1, self.paddle2)

        # Check wall collisions (left and right)
        if self.ball.x <= 0:
            self.scoreboard.player2_score()
            self.reset_ball()
        elif self.ball.x + self.ball.size >= SCREEN_WIDTH:
            self.scoreboard.player1_score()
            self.reset_ball()

        # Check win condition
        if self.check_win_condition():
            self.game_running = False
            self.game_over = True

    def check_win_condition(self) -> bool:
        """Check if someone won."""
        return self.scoreboard.check_winner() is not None

    def reset_ball(self):
        """Reset ball to center after scoring."""
        self.ball.reset()

    def is_running(self) -> bool:
        """Check if game should continue."""
        return self.game_running

    def get_scores(self) -> tuple[int, int]:
        """Get current scores."""
        return self.scoreboard.get_scores()

    def reset_game(self):
        """Reset game state."""
        self.ball.reset()
        self.paddle1 = Paddle(20, SCREEN_HEIGHT // 2 - 50)
        self.paddle2 = Paddle(SCREEN_WIDTH - 35, SCREEN_HEIGHT // 2 - 50)
        self.scoreboard.reset_scores()
        self.game_running = True
        self.game_over = False
