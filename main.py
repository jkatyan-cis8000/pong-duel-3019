import pygame

from src.game import PongGame
from src.ui import draw_screen, handle_pygame_events


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong Duel")
    
    game = PongGame()
    ball = game.ball
    paddles = [game.paddle1, game.paddle2]
    
    clock = pygame.time.Clock()
    
    while game.is_running():
        keys = handle_pygame_events()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game._is_running = False
        
        game.handle_input(keys)
        
        old_x = game.ball.x
        game.ball.move()
        game.ball.check_collision(game.paddle1, game.paddle2)
        
        new_x = game.ball.x
        if (old_x < 400 and new_x >= 400 and game.ball.x < 0) or \
           (old_x > 400 and new_x <= 400 and game.ball.x > 800):
            scores = game.get_scores()
            if game.ball.x < 400:
                game.scoreboard.player2_score()
            else:
                game.scoreboard.player1_score()
            game.ball.reset()
        
        draw_screen(screen, game.ball, paddles, game.get_scores())
        
        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()
