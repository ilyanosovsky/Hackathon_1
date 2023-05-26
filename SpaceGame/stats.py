class Stats():
    # Initialize statistics
    def __init__(self):
        self.reset_stats()
        self.run_game = True


    def reset_stats(self):
    # initialize statistics that may change during the game
        self.guns_left = 2
        self.score = 0
