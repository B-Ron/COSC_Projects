import pygame, os
from fighter import Fighter

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colors
YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255) 

#load background image
bg_image = pygame.image.load(r"C:\Users\ronwi\.vscode\COSC_Projects\2dFighter\assets\images\background\background.jpg").convert()

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

#drawing health bars
def draw_health_bar(health,x, y):
    ratio = health / 100
    pygame.draw.rect(screen,WHITE,(x  - 2, y - 2 , 404,34))
    pygame.draw.rect(screen, RED, (x,y,400,30))
    pygame.draw.rect(screen, YELLOW,(x ,y, 400 * ratio,30))

#create two instances for fighters

fighter1 = Fighter(200,310)
fighter2 = Fighter(700,310)

#game loop
run = True
while run:
    clock.tick(FPS)
    
    #draw background
    draw_bg()
    
    #show player stats
    draw_health_bar(fighter1.health, 20,20)
    draw_health_bar(fighter2.health, 580,20)
    
    #move fighters
    fighter1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter2)
    #fighter2.move()
    
    #draw fighters
    fighter1.draw(screen)
    fighter2.draw(screen)
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #update display
    pygame.display.update()
            
#quit game
pygame.quit()