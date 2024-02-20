# Import Feb 19, 2024. 2:34pm.
import pygame
import os
import time
import random  
pygame.init()

# Images

Main_player = pygame.image.load(os.path.join("2d Game", "Main.png"))

# Screen Window
screen = pygame.display.set_mode((600, 600))

# Player. Feb,19 ,2024. 3:27pm. 
player = pygame.Rect((300, 250 ,50 , 50))

class Main:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = 100
        self.Main_img = None
        self.Bullet_img = None
        self.Bullet = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50), 2)

# Exits
        
run = True

main = Main(600, 300)

while run:
        
    # NO traces
    screen.fill((0, 0, 0))

    # Describes the movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
       player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
       player.move_ip(0,1)

    # Exits the window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Updates the display drawings
        pygame.display.update()

pygame.quit()