# import pygame
# import random


# def save_data():
#     conn = psycopg2.connect(
#             database='bootcamp',
#             user='ivankozin',
#             password='2158310',
#             host='localhost',
#             port='5432'
#         )
#     cur = conn.cursor()
#     query = f"""
#         INSERT INTO dino_results (game_id, points, level)
#         VALUES ('{int(points)}', '{int(level)}')"""
#         cur.execute(query)
