#All Exports Needed for the code to work. Feb, 27, 2024. 7:32pm. 
import pygame
import random 
import os
import time

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
    clock = pygame.time.Clock()

    # We won't need to pass all the things into a paramater. 
    def redraw_window():
        WIN.blit(FIRST, (0,0))

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
