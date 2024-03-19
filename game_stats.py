class GameStats:
    """Tracks stats for game."""

    def __init__(self, ai_game):
        self.score = 0
        self.level = 1
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in inactive state
        self.game_active = False

        self.high_score = 0

        # Load high score
        scorefile = open("highscore.txt", "w")
        if scorefile.readable():
            self.high_score = int(scorefile.read())
        else:
            print("FAIL")
            scorefile.write("0")



    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        print("DONE")
