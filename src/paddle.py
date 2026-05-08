import pygame
from src.constants import SCREEN_HEIGHT, PADDLE_HEIGHT, PADDLE_SPEED


class Paddle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 100

    def move_up(self):
        """Move paddle up by PADDLE_SPEED, clamped to screen."""
        self.y = max(0, self.y - PADDLE_SPEED)

    def move_down(self):
        """Move paddle down by PADDLE_SPEED, clamped to screen."""
        self.y = min(SCREEN_HEIGHT - PADDLE_HEIGHT, self.y + PADDLE_SPEED)

    def get_rect(self) -> pygame.Rect:
        """Return rectangle for collision detection."""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen: pygame.Surface):
        """Draw paddle on screen."""
        rect = self.get_rect()
        pygame.draw.rect(screen, (255, 255, 255), rect)
