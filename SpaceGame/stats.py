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

    # def save_data(points, level):
    #     try:
    #         conn = psycopg2.connect(
    #             host="rogue.db.elephantsql.com",
    #             port=5432,
    #             database="wocsykfv",
    #             user="wocsykfv",
    #             password="rwPJlc2S6ceN1uDanxX3cS9f2w9NCDJQ"
    #         )
    #         cur = conn.cursor()
    #         query = f"""
    #             INSERT INTO game_results (game_title, points, level)
    #             VALUES ('Jumping Dino', {int(points)}, {int(level)})"""
    #         cur.execute(query)
    #         conn.commit()
    #     except Exception as e:
    #         print(f'Error: {e}')
    #     finally:
    #         cur.close()
    #         conn.close()
