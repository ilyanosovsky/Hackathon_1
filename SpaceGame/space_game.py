import pygame, controls, sys, time
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
import psycopg2
from db import create_table

def run(): # Main function

    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((700, 800)) # Create screen
    pygame.display.set_caption("Space Game") # Set caption
    bg_img = pygame.image.load("SpaceGame/image/bg_stars.jpeg") # Load background image
    gun = Gun(screen) # Create gun
    bullets = Group() # Create group of bullets
    inos = Group() # Create group of Inos
    controls.create_army(screen, inos) # Create army of Inos
    stats = Stats() # Create stats
    sc = Scores(screen, stats) # Create scores

    while True: # Main loop of the game
        
        controls.events(screen, gun, bullets) # Check events of the game 
        if stats.run_game: # Check if the game is running 
            gun.update_gun() # Update gun position
            controls.update(bg_img, screen, stats, sc, gun, inos, bullets) # Update screen
            controls.update_bullets(screen, stats, sc, inos, bullets) # Update bullets
            controls.update_inos(stats, screen, sc, gun, inos, bullets) # Update Inos 
        else:
            if any(event.type == pygame.KEYDOWN for event in pygame.event.get()): # Check if any key is pressed
                stats.run_game = True # Set run_game to True
                stats.reset_stats() # Reset stats
                run() # Run main function

run() # Run the game

def manage_connection(query):
    try:
        connection = psycopg2.connect(
            host="rogue.db.elephantsql.com",
            port=5432,  
            database="wocsykfv", 
            user="wocsykfv",  
            password="rwPJlc2S6ceN1uDanxX3cS9f2w9NCDJQ"  
        )
        with connection:
            with connection.cursor() as cursor:
                if "SELECT" in query:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                else:
                    cursor.execute(query)
                    connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def get_result(points):
        query = f"""
        SELECT * FROM game_results 
        ORDER BY {points} DESC LIMIT 1
        """
        if manage_connection(query) == []:
            return None
        else:
            result = manage_connection(query)
            return result