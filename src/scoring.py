from src.constants import WINNING_SCORE


class ScoreBoard:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0

    def player1_score(self):
        """Increment player 1 score."""
        self.player1_score += 1

    def player2_score(self):
        """Increment player 2 score."""
        self.player2_score += 1

    def get_scores(self) -> tuple[int, int]:
        """Return (player1, player2) scores."""
        return (self.player1_score, self.player2_score)

    def check_winner(self) -> int | None:
        """Return 1 if player 1 won, 2 if player 2 won, or None if no winner."""
        if self.player1_score >= WINNING_SCORE:
            return 1
        elif self.player2_score >= WINNING_SCORE:
            return 2
        return None

    def reset_scores(self):
        """Reset both scores to 0."""
        self.player1_score = 0
        self.player2_score = 0
