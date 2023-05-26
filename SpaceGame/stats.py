class Stats():
    # Initialize statistics
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('SpaceGame/highscore.txt', 'r') as file_object:
            self.high_score = int(file_object.readline())


    def reset_stats(self):
    # initialize statistics that may change during the game
        self.guns_left = 2
        self.score = 0
