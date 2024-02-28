#All Exports Needed for the code to work. Feb, 27, 2024. 7:32pm. 
import pygame
import random 
import os
import time
pygame.font.init()

#Determines Height
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Window Name
pygame.display.set_caption("Not Determined")

# Imports all the Images. 
Main_Character = pygame.image.load(os.path.join("assets", "Main.png"))
FIRST = pygame.transform.scale(pygame.image.load(os.path.join("assets", "First_Dungeon.jpg")), (WIDTH, HEIGHT))

#What starts the Window 
def main():
    run = True
    FPS = 60 
    waves = 1
    lives = 6
    main_font = pygame.font.SysFont("cosmicsans", 50)

    clock = pygame.time.Clock()

    # We won't need to pass all the things into a paramater. 
    def redraw_window():
        #Draws the Background
        WIN.blit(FIRST, (0,0))
        #Draws the Text 
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 0))
        waves_label = main_font.render(f"Waves: {waves}", 1, (255, 0, 0))

        #Displays the texts 
        WIN.blit(lives_label, (WIDTH - lives_label.get_width() - 10, 10))
        WIN.blit(waves_label, (10, 10))

        #Will refresh the display
        pygame.display.update()

    while run:
        #Makes sure the Game gets' consisted FPS.
        clock.tick(FPS)
        redraw_window()

        #This runs any event that happens
        for event in pygame.event.get():
            #What makes us to quit. 
            if event.type == pygame.QUIT:
                run = False
#runs the whole thing that in def main() 
main()
