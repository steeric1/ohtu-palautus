from dataclasses import dataclass

@dataclass
class Player:
    name: str
    score: int = 0

    def get_score(self):
        if self.score == 0:
            return "Love"
        elif self.score == 1:
            return "Fifteen"
        elif self.score == 2:
            return "Thirty"
        elif self.score == 3:
            return "Forty"
        else:
            return "Game"

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1.score += 1
        else:
            self.player2.score += 1

    def get_score(self):
        if self.player1.score == self.player2.score:
            return self.get_tie_score()
        elif self.player1.score >= 4 or self.player2.score >= 4:
            return self.get_ads_score()
        else:
            return f"{self.player1.get_score()}-{self.player2.get_score()}"

    def get_tie_score(self):
        score = self.player1.get_score()

        if score == "Game":
            return "Deuce"
        else:
            return f"{score}-All"

    def get_ads_score(self):
        difference = self.player1.score - self.player2.score

        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"