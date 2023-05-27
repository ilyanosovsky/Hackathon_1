import pygame, controls, sys, time
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



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
            controls.game_start(screen, stats, sc) # Show game start screen
            if any(event.type == pygame.KEYDOWN for event in pygame.event.get()): # Check if any key is pressed
                stats.run_game = True # Set run_game to True
                stats.reset_stats() # Reset stats

            gun.update_gun() # Update gun position
            controls.update(bg_img, screen, stats, sc, gun, inos, bullets) # Update screen
            controls.update_bullets(screen, stats, sc, inos, bullets) # Update bullets
            controls.update_inos(stats, screen, sc, gun, inos, bullets) # Update Inos  
        else:
            controls.game_over(screen, stats, sc) # Show game over screen
            if any(event.type == pygame.KEYDOWN for event in pygame.event.get()): # Check if any key is pressed
                time.sleep(1)
                run() # Run main function 
            # else :
            #     pygame.quit()
run() # Run main function