import pygame, os

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#load background image
bg_image = pygame.image.load(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\images\background\background.jpg").convert()

#game loop
run = True
while run:
    
    
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
#quit game
pygame.quit()