import random
import pygame
from src.constants import BALL_SPEED_X, BALL_SPEED_Y


class Ball:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.size = 15
        # Random initial direction (left or right, up or down)
        direction_x = random.choice([-1, 1])
        direction_y = random.choice([-1, 1])
        self.velocity_x = direction_x * BALL_SPEED_X
        self.velocity_y = direction_y * BALL_SPEED_Y

    def move(self):
        """Update position based on velocity."""
        self.x += self.velocity_x
        self.y += self.velocity_y

    def check_collision(self, paddle1, paddle2):
        """Check and handle collisions with paddles and edges."""
        # Check top and bottom walls
        if self.y <= 0 or self.y + self.size >= 600:
            self.velocity_y = -self.velocity_y

        # Check paddle collisions
        paddle1_rect = paddle1.get_rect()
        paddle2_rect = paddle2.get_rect()
        ball_rect = self.get_rect()

        # Check collision with left paddle (paddle1)
        if ball_rect.colliderect(paddle1_rect):
            self.velocity_x = abs(self.velocity_x)  # Force rightward

        # Check collision with right paddle (paddle2)
        elif ball_rect.colliderect(paddle2_rect):
            self.velocity_x = -abs(self.velocity_x)  # Force leftward

    def reset(self):
        """Reset ball to center with random x direction, reset y to 0."""
        self.x = 800 // 2 - 7
        self.y = 600 // 2 - 7
        direction_x = random.choice([-1, 1])
        direction_y = random.choice([-1, 1])
        self.velocity_x = direction_x * BALL_SPEED_X
        self.velocity_y = direction_y * BALL_SPEED_Y

    def get_rect(self) -> pygame.Rect:
        """Return ball's rectangle for collision detection."""
        return pygame.Rect(self.x, self.y, self.size, self.size)
