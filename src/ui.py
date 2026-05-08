import pygame

from src.ball import Ball
from src.constants import COLORS, SCREEN_HEIGHT, SCREEN_WIDTH
from src.paddle import Paddle
from src.scoring import ScoreBoard


def draw_screen(screen: pygame.Surface, ball: Ball, paddles: list[Paddle], scores: tuple[int, int]) -> None:
    screen.fill(COLORS["BLACK"])
    
    for paddle in paddles:
        paddle.draw(screen)
    
    pygame.draw.rect(screen, COLORS["WHITE"], (ball.x, ball.y, ball.size, ball.size))
    
    score1, score2 = scores
    font = pygame.font.Font(None, 74)
    score_text = f"{score1}   {score2}"
    text = font.render(score_text, True, COLORS["WHITE"])
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(text, text_rect)
    
    pygame.display.flip()


def handle_pygame_events() -> dict:
    keys = pygame.key.get_pressed()
    return {key: value for key, value in enumerate(keys)}
